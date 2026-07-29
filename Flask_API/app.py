import os
from dotenv import find_dotenv, load_dotenv
from flask import Flask, jsonify, request, g
import mysql.connector
from mysql.connector import pooling
from mysql.connector.errors import Error
from datetime import datetime
import decimal
from decimal import Decimal
import csv
import bcrypt


# get env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# load environment files
db_host = os.getenv("db_host")
db_username= os.getenv("db_username")
db_pass = os.getenv("db_pwd")
db_database = os.getenv("db_database")
db_ssl_ca = os.getenv("db_ssl_ca")

app = Flask(__name__)

db_pool =  pooling.MySQLConnectionPool(
    pool_name= "flask_api_pool",
    pool_size = 2,
    pool_reset_session = True,
    host=db_host,
    user=db_username,
    password=db_pass,
    database = db_database,
    ssl_ca = db_ssl_ca,
    ssl_verify_cert = True,
    port = 14388,
    charset = "utf8mb4"
)

# will need to connect to db when hosted online 
# database needs to close connections and only allow the flask api to communicate with it 
@app.route("/")
def home():
    return "Homepage"

@app.route("/get_tables", methods=['GET'])
def get_tables():
    con = get_db()
    cursor=con.cursor()
    cursor.execute("SHOW TABLES;")
    tables= cursor.fetchall()
    cursor.close()
    # we get a list of tuples and we iterate through list to get the first item in each
    table_names = [table[0] for table in tables]
    # return as json the status code 
    # creates dict of tables: with array of table names - tables:[menu_item, restaurant...]
    return jsonify({"tables": table_names}),200

# add sale to db
@app.route("/sales/add_sale", methods=['POST'])
def add_sale():
    data = request.get_json()
    restaurant_id = data.get("restaurant_id")
    date = datetime.strptime(data.get("date"),"%d-%m-%Y").date()
    item_id =  data.get("item_id")
    quantity = data.get("quantity")
    total = data.get("total")
    con = get_db()
    cursor = con.cursor()
    sql_query = """INSERT INTO sale_made (restaurant_id, date ,item_id, amount_sold, total) VALUES
                (%s, %s, %s, %s,%s)"""
    cursor.execute(sql_query,(restaurant_id,date,item_id,quantity,total))
    con.commit()
    return jsonify({"sale":[restaurant_id,date,item_id,quantity,total]}),200

# function to get the restaurant menu 
@app.route("/menu/get_restaurant_menu", methods =['GET'])
def get_restaurant_menu():
    con = get_db()
    data = request.get_json()
    restaurant_id = data.get("id")
    query = """SELECT item_name FROM menu_item
            INNER JOIN restaurant_menu 
            ON restaurant_menu.item_id = menu_item.item_id
            WHERE restaurant_menu.restaurant_id = %s"""
    cursor = con.cursor()
    cursor.execute(query,(restaurant_id,))
    res = cursor.fetchall()
    if res:
        menu = [menu_item[0] for menu_item in res]
        cursor.close()
        return jsonify({"menu":menu}),200
    else:
        return jsonify({"error":"restaurant does not have a menu"}),500

# route to get the item price when user is selecting the items 
@app.route("/sales/get_item_price", methods =['GET'])
def get_item_price():
    con = get_db()
    cursor = con.cursor()
    data = request.get_json()
    restaurant_id = data['restaurant_id']
    item_name = data['item_name']
    query = """SELECT price
            FROM restaurant_menu
            INNER JOIN menu_item
            ON menu_item.item_id = restaurant_menu.item_id
            WHERE menu_item.item_name = %s AND restaurant_menu.restaurant_id = %s ;"""
    values = (item_name,restaurant_id)
    cursor.execute(query,values)
    res = cursor.fetchone()
    if res:
        return jsonify({"price": res[0]}),200
    else:
         return jsonify({"Error": "Item not found"})

# removing spaces from item menu
@app.route("/menu/update_menu", methods = ['PUT'])
def update_menu():
        con = get_db()
        cursor = con.cursor()
        for item_id in range(165,247):
            cursor.execute("""SELECT item_name FROM menu_item WHERE item_id = %s""", (item_id,))
            item = cursor.fetchone()[0]
            update_query = """UPDATE menu_item SET item_name = TRIM(%s) WHERE item_id = %s;"""
            cursor.execute(update_query,(item,item_id,))
            con.commit()
        return jsonify({"message":"complete"})

# retrieve restaurant sales 
@app.route("/sales/retrieve_sales", methods = ['GET'])
def retrieve_sales():
    data = request.get_json()
    restaurant_id = data['restaurant_id']
    con = get_db()
    cursor = con.cursor()
    query = """SELECT * 
            FROM sale_made 
            WHERE restaurant_id = %s
            ORDER BY date DESC"""
    cursor.execute(query,(restaurant_id,))
    sales = [sale for sale in cursor.fetchall()]
    # if the id does not exist it will return empty
    return jsonify({"sales":sales}),200
# route to get the item name from the id
@app.route("/menu/get_item_name", methods=['GET'])
def get_item_name():
    data = request.get_json()
    item_id = data['item_id']
    con = get_db()
    cursor = con.cursor()
    cursor.execute("""SELECT item_name from menu_item WHERE item_id = %s""", (item_id,))
    item = cursor.fetchone()
    if item:
        return jsonify({"item_name": item[0]})
    else:
        return jsonify({"Error": "Item not found"})

# -- RETRIEVING SALES FOR THE SALES TAB FUNCTIONALITY --
# route to view sales by day
@app.route("/sales/retrieve_all_daily_sales", methods=['GET'])
def retrieve_all_daily_sales():
    data =  request.get_json()
    restaurant_id = data['restaurant_id']
    con = get_db()
    cursor = con.cursor()
    query = """SELECT date, SUM(total) FROM sale_made 
            WHERE restaurant_id = %s 
            GROUP BY date 
            ORDER BY date DESC"""
    cursor.execute(query, (restaurant_id,))
    daily_sales = cursor.fetchall()
    cursor.close()
    if daily_sales:
        daily_sales = [daily_sale for daily_sale in daily_sales]
        return jsonify({"daily_sales": daily_sales})
    else:
        return jsonify({"Error": "Could not find sales"})
# route to retrieve all sales by month 
@app.route("/sales/retrieve_all_monthly_sales", methods=['GET'])
def retrieve_all_monthly_sales():
    data =  request.get_json()
    restaurant_id = data['restaurant_id']
    con = get_db()
    cursor = con.cursor()
    query = """SELECT MONTH(date),YEAR(date), SUM(total) FROM sale_made 
                WHERE restaurant_id = %s 
                GROUP BY MONTH(date), YEAR(date) 
                ORDER BY YEAR(date) DESC"""
    cursor.execute(query,(restaurant_id,))
    monthly_sales = cursor.fetchall()
    cursor.close()
    monthly_sales = [monthly_sale for monthly_sale in monthly_sales]
    return jsonify({"monthly_sales": monthly_sales})

# route to retrieve all sales by year
@app.route("/sales/retrieve_all_yearly_sales", methods=['GET'])
def retrieve_all_yearly_sales():
    data =  request.get_json()
    restaurant_id = data['restaurant_id']
    con = get_db()
    cursor = con.cursor()
    query = """SELECT YEAR(date), SUM(total) FROM sale_made 
                WHERE restaurant_id = %s 
                GROUP BY YEAR(date) 
                ORDER BY YEAR(date) DESC"""
    cursor.execute(query,(restaurant_id,))
    yearly_sales = cursor.fetchall()
    cursor.close()
    yearly_sales = [yearly_sale for yearly_sale in yearly_sales]
    return jsonify({"yearly_sales": yearly_sales})

@app.route("/sales/retrieve_all_weekly_sales", methods=['GET'])
def retrieve_all_weekly_sales():
    data =  request.get_json()
    restaurant_id = data['restaurant_id']
    con = get_db()
    cursor = con.cursor()
    query = """SELECT WEEK(date), MONTH(date),YEAR(date), SUM(total) FROM sale_made 
                WHERE restaurant_id = %s 
                GROUP BY WEEK(date),MONTH(date),YEAR(date)
                ORDER BY YEAR(date) DESC"""
    cursor.execute(query,(restaurant_id,))
    weekly_sales = cursor.fetchall()
    cursor.close()
    weekly_sales = [weekly_sale for weekly_sale in weekly_sales]
    return jsonify({"weekly_sales": weekly_sales})

# -- retrieving sales for the dialogs in the sales functionality 

# get the sales from a specified date 
@app.route("/sales/dialogs/get_specified_day_sales", methods=['GET'])
def get_specified_day_sales():
    data =  request.get_json()
    restaurant_id = data['restaurant_id']
    date = datetime.strptime(data['date'],"%d/%m/%Y").date()  
    con = get_db()
    cursor = con.cursor()
    query = """SELECT sale_made.date, menu_item.item_name, sale_made.amount_sold,sale_made.total
                FROM sale_made 
                INNER JOIN menu_item
                ON menu_item.item_id = sale_made.item_id
                WHERE sale_made.date = %s AND sale_made.restaurant_id = %s"""
    cursor.execute(query,(date,restaurant_id))
    day_sales = cursor.fetchall()
    day_sales = [day_sale for day_sale in day_sales]
    cursor.close()
    return jsonify({"day_sales": day_sales})

# -- retrieving sales in the monthly dialog --
    # retrieving sales by specified month and returning by specified option
@app.route("/sales/dialogs/month/get_specified_month_<option>", methods=['GET'])
def get_specified_month(option):
    data =  request.get_json()
    restaurant_id = data['restaurant_id']
    month = data['month']
    year = data['year']
    con = get_db()
    cursor = con.cursor()
    query = """"""
    values = (restaurant_id,month,year)
    if option == "day":
        query = """SELECT date, SUM(total) FROM sale_made 
                WHERE restaurant_id = %s AND MONTH(date) = %s AND YEAR(date) = %s
                GROUP BY date 
                ORDER BY date DESC"""
    elif option == "week":
        query ="""SELECT WEEK(date), SUM(total) FROM sale_made 
                WHERE restaurant_id = %s AND MONTH(date) = %s AND YEAR(date) = %s
                GROUP BY WEEK(date) 
                ORDER BY WEEK(date) DESC"""
    else:
        query = """SELECT MONTH(date), SUM(total) FROM sale_made 
                WHERE restaurant_id = %s AND MONTH(date) = %s AND YEAR(date) = %s
                GROUP BY MONTH(date) 
                ORDER BY MONTH(date) DESC"""
    cursor.execute(query,values)
    month_sales = cursor.fetchall()
    month_sales = [month_sale for month_sale in month_sales]
    cursor.close()
    return jsonify({"month_sales": month_sales})
# -- retrieving sales in the year dialog --
@app.route("/sales/dialogs/year/get_specified_year_<option>", methods=['GET'])
def get_specified_year(option):
    data =  request.get_json()
    restaurant_id = data['restaurant_id']
    year = data['year']
    con = get_db()
    cursor = con.cursor()
    query = """"""
    values = (restaurant_id,year)
    
    if option == "day":
        query = """SELECT date, SUM(total) FROM sale_made 
                WHERE restaurant_id = %s AND YEAR(date) = %s 
                GROUP BY date 
                ORDER BY date DESC"""
    elif option == "week":
        query = """SELECT WEEK(date),YEAR(date), SUM(total) FROM sale_made 
                WHERE restaurant_id = %s AND YEAR(date) = %s 
                GROUP BY WEEK(date), YEAR(date) 
                ORDER BY WEEK(date), YEAR(date) DESC"""
    else:
        query = """SELECT sale_made.date, menu_item.item_name, sale_made.amount_sold,sale_made.total
                FROM sale_made 
                INNER JOIN menu_item
                ON menu_item.item_id = sale_made.item_id
                WHERE sale_made.restaurant_id = %s AND YEAR(date) = %s
                ORDER BY sale_made.date DESC"""
    cursor.execute(query,values)
    year_sales = cursor.fetchall()
    year_sales = [year_sale for year_sale in year_sales]
    cursor.close()
    return jsonify({"year_sales": year_sales})

# -- retrieving sales in the item dialog --
@app.route("/sales/dialogs/item/get_specified_item_<option>", methods=['GET'])
def get_specified_item_sales(option):
    data =  request.get_json()
    con = get_db()
    cursor = con.cursor()
    query = """"""
    values = ()

    if option == "day":
        query = """SELECT sale_made.date, menu_item.item_name, sale_made.amount_sold, sale_made.total FROM sale_made 
                INNER JOIN menu_item
                ON menu_item.item_id = sale_made.item_id
                WHERE menu_item.item_name = %s AND sale_made.restaurant_id = %s AND sale_made.date = %s
                ORDER BY sale_made.date DESC"""
        values = (data['item'], data['restaurant_id'], datetime.strptime(data['date'],"%d/%m/%Y").date())
    elif option == "month": # viewing sales made on that month with that item
        query = """SELECT sale_made.date, menu_item.item_name, sale_made.amount_sold, sale_made.total FROM sale_made 
                    INNER JOIN menu_item
                    ON menu_item.item_id = sale_made.item_id
                    WHERE menu_item.item_name = %s AND sale_made.restaurant_id = %s AND YEAR(date) = %s AND MONTH(date) = %s
                    ORDER BY sale_made.date DESC"""
        values = (data['item'], data['restaurant_id'], data['year'], data['month'])
    elif option == 'year': # viewing sales with that item on a specific year
        query = """SELECT sale_made.date, menu_item.item_name, sale_made.amount_sold, sale_made.total FROM sale_made 
                INNER JOIN menu_item
                ON menu_item.item_id = sale_made.item_id
                WHERE menu_item.item_name = %s AND sale_made.restaurant_id = %s AND YEAR(date) = %s
                ORDER BY sale_made.date DESC"""
        values = (data['item'], data['restaurant_id'], data['year'])
    else: # viewing all sales with that item
        query = """SELECT sale_made.date, menu_item.item_name, sale_made.amount_sold, sale_made.total 
                FROM sale_made 
                INNER JOIN menu_item
                ON menu_item.item_id = sale_made.item_id
                WHERE menu_item.item_name = %s and sale_made.restaurant_id = %s
                ORDER BY sale_made.date DESC;"""
        values = (data['item'], data['restaurant_id'])

    cursor.execute(query,values)
    item_sales = cursor.fetchall()
    item_sales = [item_sale for item_sale in item_sales]
    cursor.close()
    return jsonify({"item_sales": item_sales})

# deleting sale by sale id
@app.route("/sales/delete_sale_<sale_id>", methods=['DELETE'])
def delete_sale(sale_id):    
    con = get_db()
    cursor = con.cursor()
    query = """DELETE FROM sale_made WHERE sale_id = %s"""
    cursor.execute(query, (sale_id,))
    con.commit()
    cursor.close()
    return jsonify({"item_id deleted": sale_id})

# log users in
"""to send request: form_data = {"username":"johndoe", "password": "user@1234"}
resp = requests.post(url, data=form_data)"""
# register user and log in user then upload db 
# hash password before sending data
@app.route("/register", methods=['POST'])
def register_user():
    data =  request.get_json()
    con = get_db()
    cursor = con.cursor()
    restaurant_name = data['restaurant_name']
    code = data['code']
    # hash password before sending to API
    password = data['password']
    hashed_pass = hash_pwd(password)
    query = """INSERT INTO restaurant (restaurant_name,code,password) VALUES (%s, %s, %s)"""
    try:
        cursor.execute(query, (restaurant_name,code,hashed_pass))
        con.commit()
        cursor.close()
        return jsonify({"Registered": restaurant_name }), 200
    except mysql.connector.Error as e:
        if(e.errno == 1062):
            return jsonify({"Error": "This user already exists"})
        return jsonify({"Error": f"Could not register user due to - {e.msg}"})
    
@app.route("/login", methods=['POST'])
def login():
    data =  request.get_json()
    con = get_db()
    cursor = con.cursor()
    code = data['code']
    password = data['password']
    query =  "SELECT password,restaurant_id FROM restaurant WHERE code = %s"
    cursor.execute(query,(code,))
    user = cursor.fetchone()
    if user:
        password_match = check_pwd(password, user[0])
        if not password_match:
            return jsonify({"Error": "Incorrect password"}),200
        return jsonify({"restaurant_id": user[1]}),200
    else:
        return jsonify({"Error": "User does not exist"})

@app.route("/test", methods = ['GET'])
def test():
    return jsonify({"message": "works"})

# connect the menu from notes to the test restaurant to be able to add items to the test restaurant 
@app.route("/test/add_menu_<id>", methods = ['POST'])
def add_menu_test(id):
    
    con = get_db()
    cursor = con.cursor()
    with open("Flask_API/menu_items.csv", "r") as menu:
            data = csv.reader(menu)
            for i, menu_item in enumerate(data):
                if i!= 0:
                    price = menu_item[1].replace("Â£", "")
                    try:
                        price = Decimal(price)
                        cursor.execute("SELECT item_id FROM menu_item WHERE item_name = %s ", (menu_item[0].strip(),))
                        item_id = cursor.fetchone()[0]
                        cursor.execute("INSERT INTO restaurant_menu (restaurant_id,item_id,price) VALUES (%s,%s,%s) ", (1,item_id,price))
                        con.commit()
                    except Exception as e:
                        # display error messsage that states this when user tries
                        print(e)
                        print("could not add menu item " + menu_item[0] + "please try again")
                        continue
    cursor.close()
    return "complete"

# hash password function 
def hash_pwd(password:str, rounds=12) -> bytes:
    # hash password and generate a salt for each password 
    pwd =  bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=12))
    return pwd

# checking if hashed passwords match and returns a true value
def check_pwd(password:str, hash:bytes) -> bool:
    # compare hash and password typed 
    return bcrypt.checkpw(password.encode(),hash)

# get and close database connections
def get_db():
    if not hasattr(g,"db"):
        g.db = db_pool.get_connection()
    return g.db

# app context occurs every time the request comes in or it has been destroyed so here we are removing the db once everything is ok
@app.teardown_appcontext
def close_db(error):
    db = g.pop('db',None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run()



# TO DO 
"""
3. connect the GUI to flask api and check that the flask api can communicate well with db #IDK WHAT TO DO
4. host the flask api 
5. download and test on dads laptop

"""