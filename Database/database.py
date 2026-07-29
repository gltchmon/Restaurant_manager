import mysql.connector
import csv
from decimal import *
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# load environment files
db_host = os.getenv("host")
db_username= os.getenv("user")
db_pass = os.getenv("passwd")
db_database = os.getenv("database")


class Database:

    def __init__(self):
        self.db = mysql.connector.connect(
            host=db_host,
            user=db_username,
            passwd=db_pass,
            database = db_database
        )
        self.cursor = self.db.cursor()
        #print(self.get_price("Bacon egg and sausage baguette"))
        # creating tables
    def create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `restaurant` (
                        `restaurant_id` integer PRIMARY KEY AUTO_INCREMENT,
                        `restaurant_name` varchar(255) UNIQUE,
                        `code` varchar(255) UNIQUE NOT NULL,
                        `password` varchar(255) NOT NULL
                        );""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `menu_item` (
                        `item_id` integer PRIMARY KEY AUTO_INCREMENT,
                        `item_name` varchar(255) UNIQUE NOT NULL
                        );""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `restaurant_menu` (
                        `restaurant_id` integer NOT NULL,
                        `item_id` integer NOT NULL,
                        `price` decimal(10,2) NOT NULL,
                        PRIMARY KEY (`restaurant_id`, `item_id`),
                        FOREIGN KEY (restaurant_id) REFERENCES restaurant(restaurant_id),
                        FOREIGN KEY (item_id) REFERENCES menu_item(item_id));""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS `sale_made` (
                        `sale_id` integer PRIMARY KEY AUTO_INCREMENT,
                        'date' DATE NOT NULL
                        `restaurant_id` integer NOT NULL,
                        `item_id` integer NOT NULL,
                        `amount_sold` integer NOT NULL,
                        `total` decimal(10,2) NOT NULL,
                        FOREIGN KEY (restaurant_id) REFERENCES restaurant(restaurant_id),
                        FOREIGN KEY (item_id) REFERENCES menu_item(item_id)
                        );""")

    # can generalise function later
    def add_menu_items(self):
        with open("../Data/menu_items.csv", "r") as menu:
            data = csv.reader(menu)
            for i, menu_item in enumerate(data):
                if i != 0:
                    self.cursor.execute("INSERT INTO menu_item (item_name) VALUES (%s)", (menu_item[0],))
                    self.db.commit()

    # insert restaurant
    def insert_restaurant(self):
        self.cursor.execute("""INSERT INTO restaurant (restaurant_name, code ,password) VALUES (%s, %s , %s)""", ("test_restaurant","TEST22","123"))
        self.db.commit()

    def print_cur(self,cur):
        for x in cur:
            print(x)

    # connect menu to restaurant if we do add more menus in the future we can make this function take the parameter of the file
    def connect_menu(self):
        with open("../Data/menu_items.csv", "r") as menu:
            data = csv.reader(menu)
            for i, menu_item in enumerate(data):
                if i!= 0:
                    price = menu_item[1].replace("Â£", "")
                    try:
                        price = Decimal(price)
                        self.cursor.execute("SELECT item_id FROM menu_item WHERE item_name = %s ", (menu_item[0],))
                        item_id = self.cursor.fetchone()[0]
                        self.cursor.execute("INSERT INTO restaurant_menu (restaurant_id,item_id,price) VALUES (%s,%s,%s) ", (2,item_id,price))
                        self.db.commit()
                    except InvalidOperation:
                        # display error messsage that states this when user tries
                        print("could not add menu item " + menu_item[0] + "please try again")
                        continue

    # pass id to get the correct menu id
    def get_menu(self,id):
        self.cursor.execute("""SELECT item_name
                            FROM menu_item
                            INNER JOIN restaurant_menu
                            ON restaurant_menu.item_id = menu_item.item_id
                            WHERE restaurant_menu.restaurant_id = %s;
        """,(id,))
        restaurant_menu = [result[0] for result in self.cursor]
        return restaurant_menu


    def get_price(self,restaurant_id,item_name):
        self.cursor.execute("""SELECT price
                                FROM restaurant_menu
                                INNER JOIN menu_item
                                ON menu_item.item_id = restaurant_menu.item_id
                                WHERE menu_item.item_name = %s AND restaurant_menu.restaurant_id = %s ;
                            """, (item_name,restaurant_id))
        return self.cursor.fetchone()[0]

    # should just get the id
    def get_user(self,code,password):
        self.cursor.execute("""SELECT * 
                                FROM restaurant 
                                WHERE code = %s AND password = %s;""", (code,password))
        return self.cursor.fetchone()

    def query(self):
        self.cursor.execute("""SELECT * FROM sale_made""")
        self.print_cur(self.cursor)
        #return self.cursor.fetchall()

    def add_sales(self,restaurant_id, item_id ,date,quantity,total):
        self.cursor.execute("""INSERT INTO sale_made (restaurant_id,item_id,date,amount_sold,total) VALUES 
        (%s,%s,%s,%s,%s);""",(restaurant_id,item_id,date,quantity,total))
        self.db.commit()

    # get the correct item id for the passed in item name
    def get_item_id(self,item_name):
        self.cursor.execute("""SELECT item_id FROM menu_item WHERE item_name = %s""", (item_name,))
        try:
            return self.cursor.fetchone()[0]
        except TypeError:
            return -1

    def get_item_name(self,item_id):
        self.cursor.execute("""SELECT item_name from menu_item WHERE item_id = %s""", (item_id,))
        return self.cursor.fetchone()[0]

    def get_sales(self,user_id):
        self.cursor.execute("""SELECT * 
                            FROM sale_made 
                            WHERE restaurant_id = %s
                            ORDER BY date DESC""" , (user_id,))
        return self.cursor.fetchall()

    def get_daily_sales(self,restaurant_id):
        self.cursor.execute("""SELECT date, SUM(total) FROM sale_made 
                            WHERE restaurant_id = %s 
                            GROUP BY date 
                            ORDER BY date DESC""" , (restaurant_id,))
        return self.cursor.fetchall()

    def get_monthly_sales(self,restaurant_id):
        self.cursor.execute("""SELECT MONTH(date),YEAR(date), SUM(total) FROM sale_made 
                                    WHERE restaurant_id = %s 
                                    GROUP BY MONTH(date), YEAR(date) 
                                    ORDER BY YEAR(date) DESC""", (restaurant_id,))
        return self.cursor.fetchall()

    def get_weekly_Sales(self, restaurant_id):
        self.cursor.execute("""SELECT WEEK(date), MONTH(date),YEAR(date), SUM(total) FROM sale_made 
                                            WHERE restaurant_id = %s 
                                            GROUP BY WEEK(date),MONTH(date),YEAR(date)
                                            ORDER BY YEAR(date) DESC""", (restaurant_id,))
        return self.cursor.fetchall()

    def get_yearly_sales(self,restaurant_id):
        self.cursor.execute("""SELECT YEAR(date), SUM(total) FROM sale_made 
                                            WHERE restaurant_id = %s 
                                            GROUP BY YEAR(date) 
                                            ORDER BY YEAR(date) DESC""", (restaurant_id,))
        return self.cursor.fetchall()

    # function to retrieve sales made on a specific date
    def get_specific_date_record(self,restaurant_id, date ):
        self.cursor.execute("""SELECT sale_made.date, menu_item.item_name, sale_made.amount_sold,sale_made.total
                            FROM sale_made 
                            INNER JOIN menu_item
                            ON menu_item.item_id = sale_made.item_id
                            WHERE sale_made.date = %s AND sale_made.restaurant_id = %s """, (date,restaurant_id))
        return self.cursor.fetchall()

    # removing the spaces in the menu items so i can easily find the items
    def remove_leading_spaces(self):
        for item_id in range(165,247):
            self.cursor.execute("""SELECT item_name FROM menu_item WHERE item_id = %s""", (item_id,))
            item = self.cursor.fetchone()[0]
            update_query = """UPDATE menu_item SET item_name = TRIM(%s) WHERE item_id = %s;"""
            self.cursor.execute(update_query,(item,item_id,))
            self.db.commit()
            self.db.close()



trial = Database()











