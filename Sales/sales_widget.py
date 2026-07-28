import PySide6
import mysql.connector
from PySide6.QtWidgets import QMessageBox,QWidget
from Sales.ui_sales_widget import Ui_manage_sales_widget as Ui_sales_widget
from datetime import date
from datetime import datetime
from Database import database
from Sales.search_dialogs.day_dialog import DayDialog
from Sales.search_dialogs.year_dialog import YearDialog
from Sales.search_dialogs.month_dialog import MonthDialog
from Sales.search_dialogs.item_dialog import ItemDialog
import calendar
import requests

# widget for managing the restaurant sales
class SalesWidget(QWidget, Ui_sales_widget):
    def __init__(self,restaurant_id):
        super().__init__()
        self.flask_url = "http://127.0.0.1:5000/"
        self.restaurant_id = restaurant_id
        self.setupUi(self)
        self.setWindowTitle("Manage sales")
        self.db = database.Database()
        self.manage_sales_tabWidget.setCurrentIndex(0)
        # initialise dialogs
        self.day_dialog = DayDialog()
        self.day_dialog.day_dialog_ok_Button.clicked.connect(self.display_specified_day_sales)
        # year dialog
        self.year_dialog = YearDialog()
        self.year_dialog.year_dialog_select_year_spinBox.setMaximum(datetime.now().year)
        self.year_dialog.year_dialog_select_year_spinBox.setValue(datetime.now().year)
        self.year_dialog.year_dialog_okButton.clicked.connect(self.get_year_dialog_results)
        # month dialog
        self.month_dialog = MonthDialog()
        self.month_dialog.month_dialog_ok_button.clicked.connect(self.display_specified_month_sales)
        # item dialog - connecting buttons
        self.item_dialog = ItemDialog()
        self.item_dialog.item_view_all_button.clicked.connect(self.get_item_dialog_results)
        self.item_dialog.item_year_button.clicked.connect(self.get_item_dialog_results)
        self.item_dialog.item_month_button.clicked.connect(self.get_item_dialog_results)
        self.item_dialog.item_day_button.clicked.connect(self.get_item_dialog_results)

        # -- ADDING SALES FUNCTIONALITY --
        self.add_sales_listWidget.setStyleSheet("font-size:15pt;")

        # design functionality
        # set up date to automatically show up as today
        self.add_sales_date.setDate(date.today())

        # add menu items to combo box
        self.add_sales_item_name_comboBox.setEditable(True)
        self.add_sales_amount_sold_spinBox.setMinimum(1)
        # get restaurant menu items - pass id once logged in
        # add menu items to select item dialog and add item combo boxees
        self.get_menu_items(restaurant_id)
        # change prices based on what has been selected
        self.change_price()

        # --CANNOT DO MULTIPLE SELECTION--

        # every time you change amount and selection change the total
        self.add_sales_item_name_comboBox.currentTextChanged.connect(self.change_price)
        self.add_sales_amount_sold_spinBox.valueChanged.connect(self.change_price)

        # pressing confirm adds sale to the list
        self.add_sales_confirm_button.clicked.connect(self.add_sale_to_list)

        # delete items in list
        self.add_sales_delete_button.clicked.connect(self.add_sales_delete_sale)

        #submit sales
        self.add_sales_submit_button.clicked.connect(self.submit_sales)

        #--MAKING VIEW SALES TAB INTERACTIVE--

        # retrieve and display all sales made by current user
        self.retrieve_sales()
        # add functionality to buttons
        # view daily sales button
        self.view_sales_daily_button.clicked.connect(self.view_daily_sales)
        # view weekly sales button
        self.view_sales_weekly_button.clicked.connect(self.view_weekly_sales)
        # view monthly sales button
        self.view_sales_monthly_button.clicked.connect(self.view_monthly_sales)
        # view yearly sales button
        self.view_sales_yearly_sales.clicked.connect(self.view_yearly_sales)
        # view all button
        self.view_sales_view_all_button.clicked.connect(self.retrieve_sales)
        # search by comboBox
            # adding items
        self.view_sales_search_comboBox.addItem("Day")
        self.view_sales_search_comboBox.addItem("Month")
        self.view_sales_search_comboBox.addItem("Year")
        self.view_sales_search_comboBox.addItem("Item")
        self.view_sales_search_comboBox.addItem("-")
        # dialogs to filter table
            # display dialog when user selects search filter
        self.view_sales_search_comboBox.currentTextChanged.connect(self.open_search_dialog)
        # adding functionality to delete button
        #self.view_sales_delete_button.clicked.connect(self.delete_items)

    # --ADD SALES TAB--

    # getting the items of the menu that belongs to the restaurant. to place into comboboxes
    def get_menu_items(self, user):
        menu = self.db.get_menu(user)
        for i in range(len(menu)):
            self.add_sales_item_name_comboBox.addItem(f"{menu[i]}")
            self.item_dialog.item_select_item_comboBox.addItem(f"{menu[i]}")

    # remember to make id be passed in
    # change price of item based on what item is being selected at the moment and the amount
    def change_price(self):
        try:
            price = self.db.get_price(self.restaurant_id,self.add_sales_item_name_comboBox.currentText())
            amount = self.add_sales_amount_sold_spinBox.value()
            self.add_sales_total_spinBox.setValue(float(price * amount))
        except TypeError:
            return

    # confirming a single sales entry
    def add_sale_to_list(self):
        date = self.add_sales_date.date().toString("dd-MM-yyyy")
        item_name = self.add_sales_item_name_comboBox.currentText()
        items = [self.add_sales_item_name_comboBox.itemText(i) for i in range(self.add_sales_item_name_comboBox.count())]
        amount_sold = self.add_sales_amount_sold_spinBox.value()
        total = self.add_sales_total_spinBox.value()
        # error checking to see if the item actually exists in menu before submission
        if item_name not in items:
            error_message = QMessageBox.critical(None, "Could not add sale", f"{item_name} does not exist in your menu. Add this item to your menu and try again.",
                                                 QMessageBox.StandardButton.Ok)
            return
        else:
            # avoid adding duplicates by checking if its already in the list
            items = [self.add_sales_listWidget.item(x).text() for x in range(self.add_sales_listWidget.count())]
            sale_str = f"{date} | {item_name} | {amount_sold} | {total}"
            if sale_str in items:
                error_message = QMessageBox.warning(None, "Could not add sale",
                                                     f"{item_name} is already in your sales made list.",
                                                     QMessageBox.StandardButton.Ok)
                return
            else:
                self.add_sales_listWidget.addItem(sale_str)

    # delete selected sale from list before submitting
    def add_sales_delete_sale(self):
        items = self.add_sales_listWidget.selectedItems()
        for item in items:
            self.add_sales_listWidget.takeItem(self.add_sales_listWidget.row(item))

    # submit entire sales list and place into the sale made table of the correct restaurant
    def submit_sales(self):
        items = [self.add_sales_listWidget.item(x).text() for x in range(self.add_sales_listWidget.count())]
        for item in items:
            # format the sales
            data = item.split(" | ")
            date_sold = datetime.strptime(data[0],"%d-%m-%Y").date()
            item_id = self.db.get_item_id(data[1])
            quantity = data[2]
            total = data[3]
            try:
                self.db.add_sales(self.restaurant_id,item_id,date_sold,quantity,total)
            # check for any errors
            except mysql.connector.Error:
                error_message = QMessageBox.critical(None, "Could not commit sales",
                                                     f"Your sales cannot be added. There may be a problem in how the sales were inserted. Please try again",
                                                     QMessageBox.StandardButton.Ok)
        self.db.query()
        self.add_sales_listWidget.clear()

    # -- VIEW SALES TAB METHODS--
    # function to retrieve and display all sales using the restaurant id
    def retrieve_sales(self):
        self.view_sales_tableWidget.clear()
        try:
            sales_li = self.db.get_sales(self.restaurant_id)
            self.view_sales_tableWidget.setRowCount(len(sales_li))
            if self.view_sales_tableWidget.columnCount() != 4:
                self.view_sales_tableWidget.setColumnCount(4)
            self.view_sales_tableWidget.setHorizontalHeaderItem(0, PySide6.QtWidgets.QTableWidgetItem("Date"))
            self.view_sales_tableWidget.setHorizontalHeaderItem(1, PySide6.QtWidgets.QTableWidgetItem("Item"))
            self.view_sales_tableWidget.setHorizontalHeaderItem(2, PySide6.QtWidgets.QTableWidgetItem("Quantity"))
            self.view_sales_tableWidget.setHorizontalHeaderItem(3, PySide6.QtWidgets.QTableWidgetItem("Total"))
            self.view_sales_tableWidget.setStyleSheet("font-size: 15pt;")
            counter = 0
            for sale in sales_li:
                current_row =  self.manage_sales_tabWidget.count()
                item_name = self.db.get_item_name(sale[2])
                quantity = sale[3]
                total = sale[4]
                date_sold = sale[5].strftime("%d-%m-%Y")
                self.view_sales_tableWidget.setItem(counter,0,PySide6.QtWidgets.QTableWidgetItem(date_sold))
                self.view_sales_tableWidget.setItem(counter, 1, PySide6.QtWidgets.QTableWidgetItem(item_name))
                self.view_sales_tableWidget.setItem(counter, 2, PySide6.QtWidgets.QTableWidgetItem(f"{quantity}"))
                self.view_sales_tableWidget.setItem(counter, 3, PySide6.QtWidgets.QTableWidgetItem(f"£{total}"))
                counter+=1
        except mysql.connector.Error:
            print("could not find user")
            return
    # function to display the daily sales on the table
    def view_daily_sales(self):
        self.view_sales_tableWidget.clear()
        # pass id here
        daily_sales = self.db.get_daily_sales(2)
        self.view_sales_tableWidget.setRowCount(len(daily_sales))
        if self.view_sales_tableWidget.columnCount() != 2:
            self.view_sales_tableWidget.setColumnCount(2)
        self.view_sales_tableWidget.setHorizontalHeaderItem(0, PySide6.QtWidgets.QTableWidgetItem("Date"))
        self.view_sales_tableWidget.setHorizontalHeaderItem(1, PySide6.QtWidgets.QTableWidgetItem("Day total"))
        for row_count, sale in enumerate(daily_sales):
            self.view_sales_tableWidget.setItem(row_count, 0,
                                                    PySide6.QtWidgets.QTableWidgetItem(sale[0].strftime("%d-%m-%Y")))
            self.view_sales_tableWidget.setItem(row_count, 1, PySide6.QtWidgets.QTableWidgetItem(f"£{sale[1]}"))

    # function to retrieve and display sales made by week
    def view_weekly_sales(self):
        self.view_sales_tableWidget.clear()
        # pass id here
        weekly_sales = self.db.get_weekly_Sales(self.restaurant_id)
        self.view_sales_tableWidget.setRowCount(len(weekly_sales))
        if self.view_sales_tableWidget.columnCount() != 4:
            self.view_sales_tableWidget.setColumnCount(4)
        self.view_sales_tableWidget.setHorizontalHeaderItem(0, PySide6.QtWidgets.QTableWidgetItem("Week Number"))
        self.view_sales_tableWidget.setHorizontalHeaderItem(1, PySide6.QtWidgets.QTableWidgetItem("Month"))
        self.view_sales_tableWidget.setHorizontalHeaderItem(2, PySide6.QtWidgets.QTableWidgetItem("Year"))
        self.view_sales_tableWidget.setHorizontalHeaderItem(3, PySide6.QtWidgets.QTableWidgetItem("Total"))
        for row_count, sale in enumerate(weekly_sales):
            self.view_sales_tableWidget.setItem(row_count, 0,
                                                PySide6.QtWidgets.QTableWidgetItem(f"{sale[0]}"))
            self.view_sales_tableWidget.setItem(row_count, 1, PySide6.QtWidgets.QTableWidgetItem(f"{calendar.month_abbr[sale[1]]}"))
            self.view_sales_tableWidget.setItem(row_count, 2, PySide6.QtWidgets.QTableWidgetItem(f"{sale[2]}"))
            self.view_sales_tableWidget.setItem(row_count, 3, PySide6.QtWidgets.QTableWidgetItem(f"£{sale[3]}"))

    # function to retrieve and display sales made by month
    def view_monthly_sales(self):
        self.view_sales_tableWidget.clear()
        # pass id here
        monthly_sales = self.db.get_monthly_sales(self.restaurant_id)
        self.view_sales_tableWidget.setRowCount(len(monthly_sales))
        if self.view_sales_tableWidget.columnCount() != 2:
            self.view_sales_tableWidget.setColumnCount(2)
        self.view_sales_tableWidget.setHorizontalHeaderItem(0, PySide6.QtWidgets.QTableWidgetItem("Month"))
        self.view_sales_tableWidget.setHorizontalHeaderItem(1, PySide6.QtWidgets.QTableWidgetItem("Monthly total"))
        for row_count, sale in enumerate(monthly_sales):
            self.view_sales_tableWidget.setItem(row_count, 0,
                                                    PySide6.QtWidgets.QTableWidgetItem(f"{calendar.month_abbr[sale[0]]}-{sale[1]}"))
            self.view_sales_tableWidget.setItem(row_count, 1, PySide6.QtWidgets.QTableWidgetItem(f"£{sale[2]}"))

    # function to retrieve and display sales by year
    def view_yearly_sales(self):
        self.view_sales_tableWidget.clear()
        # pass id here
        yearly_sales = self.db.get_yearly_sales(self.restaurant_id)
        self.view_sales_tableWidget.setRowCount(len(yearly_sales))
        if self.view_sales_tableWidget.columnCount() != 2:
            self.view_sales_tableWidget.setColumnCount(2)
        self.view_sales_tableWidget.setHorizontalHeaderItem(0, PySide6.QtWidgets.QTableWidgetItem("Year"))
        self.view_sales_tableWidget.setHorizontalHeaderItem(1, PySide6.QtWidgets.QTableWidgetItem("Yearly total"))
        for row_count, sale in enumerate(yearly_sales):
            self.view_sales_tableWidget.setItem(row_count, 0,
                                                    PySide6.QtWidgets.QTableWidgetItem(f"{sale[0]}"))
            self.view_sales_tableWidget.setItem(row_count, 1, PySide6.QtWidgets.QTableWidgetItem(f"£{sale[1]}"))

    # open the corresponding dialogs to search for specific filter
    def open_search_dialog(self,text):
        match text:
            case "Day":
                self.day_dialog.show()
            case "Year":
                self.year_dialog.show()
            case "Month":
                self.month_dialog.show()
            case "Item":
                self.item_dialog.show()
        self.view_sales_search_comboBox.setCurrentIndex(4)

    # display results in table once user has pressed okay on selecting the day
    def display_specified_day_sales(self):
        date_edit_date = self.day_dialog.day_dialog_dateEdit.date()
        date = datetime(date_edit_date.year(), date_edit_date.month(), date_edit_date.day())

        sales = self.db.get_specific_date_record(self.restaurant_id, date)
        self.view_sales_tableWidget.clear()
        self.view_sales_tableWidget.setRowCount(len(sales))

        if self.view_sales_tableWidget.columnCount() != 4:
            self.view_sales_tableWidget.setColumnCount(4)
        self.view_sales_tableWidget.setHorizontalHeaderItem(0, PySide6.QtWidgets.QTableWidgetItem("Date"))
        self.view_sales_tableWidget.setHorizontalHeaderItem(1, PySide6.QtWidgets.QTableWidgetItem("Item"))
        self.view_sales_tableWidget.setHorizontalHeaderItem(2, PySide6.QtWidgets.QTableWidgetItem("Quantity"))
        self.view_sales_tableWidget.setHorizontalHeaderItem(3, PySide6.QtWidgets.QTableWidgetItem("Total"))
        for row_count, sale in enumerate(sales):
            self.view_sales_tableWidget.setItem(row_count, 0,PySide6.QtWidgets.QTableWidgetItem(sale[0].strftime("%d-%m-%Y")))
            self.view_sales_tableWidget.setItem(row_count, 1,
                                                PySide6.QtWidgets.QTableWidgetItem(f"{sale[1]}"))
            self.view_sales_tableWidget.setItem(row_count, 2,
                                                PySide6.QtWidgets.QTableWidgetItem(f"{sale[2]}"))
            self.view_sales_tableWidget.setItem(row_count, 3, PySide6.QtWidgets.QTableWidgetItem(f"£{sale[3]}"))
        self.view_sales_search_comboBox.setCurrentIndex(4)
        self.day_dialog.close()

    # helper function to display the results in table according to display option selected
    def display_month_dialog_results(self, sales ,col_name1, col_name2 ):
        self.view_sales_tableWidget.setRowCount(len(sales))
        if self.view_sales_tableWidget.columnCount() != 2:
            self.view_sales_tableWidget.setColumnCount(2)
        self.view_sales_tableWidget.setHorizontalHeaderItem(0, PySide6.QtWidgets.QTableWidgetItem(f"{col_name1}"))
        self.view_sales_tableWidget.setHorizontalHeaderItem(1, PySide6.QtWidgets.QTableWidgetItem(f"{col_name2}"))
        for row_count, sale in enumerate(sales):
            if col_name1 == "Date":
                self.view_sales_tableWidget.setItem(row_count, 0,
                                                    PySide6.QtWidgets.QTableWidgetItem(
                                                        sale[0].strftime("%d-%m-%Y")))
            elif col_name1 == "Week no":
                self.view_sales_tableWidget.setItem(row_count, 0,
                                                    PySide6.QtWidgets.QTableWidgetItem(
                                                        f"{sale[0]}"))
            elif col_name1 == "Month":
                self.view_sales_tableWidget.setItem(row_count, 0,
                                                    PySide6.QtWidgets.QTableWidgetItem(
                                                        f"{calendar.month_abbr[sale[0]]}"))
            self.view_sales_tableWidget.setItem(row_count, 1,
                                                PySide6.QtWidgets.QTableWidgetItem(f"£{sale[1]}"))

    # displays records once the user has selected specific month in the month dialog
    def display_specified_month_sales(self):
        checked_button = self.month_dialog.month_dialog_display_option_group.checkedButton().text() if self.month_dialog.month_dialog_display_option_group.checkedButton() else None
        if checked_button:
            year = self.month_dialog.month_dialog_year_spinBox.text()
            sales = None
            # get sales depending on what was checked
            match checked_button:
                # check how much was made every day for that month
                case "View by day":
                    self.db.cursor.execute("""SELECT date, SUM(total) FROM sale_made 
                                WHERE restaurant_id = %s AND MONTH(date) = %s AND YEAR(date) = %s
                                GROUP BY date 
                                ORDER BY date DESC""",(self.restaurant_id,int(self.month_dialog.month_dialog_month_spinBox.text()), int(year)))
                    sales = self.db.cursor.fetchall()
                    self.view_sales_tableWidget.clear()
                    # display results
                    self.display_month_dialog_results(sales,"Date", "Total")
                    # check how much was made weekly for that month
                case "View by week":
                    self.db.cursor.execute("""SELECT WEEK(date), SUM(total) FROM sale_made 
                                            WHERE restaurant_id = %s AND MONTH(date) = %s AND YEAR(date) = %s
                                            GROUP BY WEEK(date) 
                                            ORDER BY WEEK(date) DESC""",
                                   (self.restaurant_id, int(self.month_dialog.month_dialog_month_spinBox.text()), int(year)))
                    sales = self.db.cursor.fetchall()
                    self.view_sales_tableWidget.clear()
                    self.display_month_dialog_results(sales,"Week no", "Total")
                    # check how much was made that month in total
                case "View month total":
                    self.db.cursor.execute("""SELECT MONTH(date), SUM(total) FROM sale_made 
                                                       WHERE restaurant_id = %s AND MONTH(date) = %s AND YEAR(date) = %s
                                                       GROUP BY MONTH(date) 
                                                       ORDER BY MONTH(date) DESC""",
                                   (self.restaurant_id, int(self.month_dialog.month_dialog_month_spinBox.text()), int(year)))
                    sales = self.db.cursor.fetchall()
                    self.view_sales_tableWidget.clear()
                    self.display_month_dialog_results(sales, "Month", "Total")
                case _:
                    self.db.cursor.execute("""SELECT sale_made.date, menu_item.item_name, sale_made.amount_sold,sale_made.total
                                                    FROM sale_made 
                                                    INNER JOIN menu_item
                                                    ON menu_item.item_id = sale_made.item_id
                                                    WHERE sale_made.restaurant_id = %s AND MONTH(date) = %s AND YEAR(date) = %s
                                                    ORDER BY sale_made.date DESC""",
                                           (self.restaurant_id, int(self.month_dialog.month_dialog_month_spinBox.text()), int(year)))
                    sales = self.db.cursor.fetchall()
                    self.view_sales_tableWidget.clear()
                    self.view_sales_tableWidget.setRowCount(len(sales))
                    if self.view_sales_tableWidget.columnCount() != 4:
                        self.view_sales_tableWidget.setColumnCount(4)
                    self.view_sales_tableWidget.setHorizontalHeaderItem(0, PySide6.QtWidgets.QTableWidgetItem(f"Date"))
                    self.view_sales_tableWidget.setHorizontalHeaderItem(1, PySide6.QtWidgets.QTableWidgetItem(f"Item"))
                    self.view_sales_tableWidget.setHorizontalHeaderItem(2, PySide6.QtWidgets.QTableWidgetItem(f"Quantity"))
                    self.view_sales_tableWidget.setHorizontalHeaderItem(3, PySide6.QtWidgets.QTableWidgetItem(f"Total"))
                    for row_count, sale in enumerate(sales):
                        self.view_sales_tableWidget.setItem(row_count, 0,
                                                                PySide6.QtWidgets.QTableWidgetItem(
                                                                    sale[0].strftime("%d-%m-%Y")))
                        self.view_sales_tableWidget.setItem(row_count, 1,
                                                            PySide6.QtWidgets.QTableWidgetItem(f"{sale[1]}"))
                        self.view_sales_tableWidget.setItem(row_count, 2,
                                                            PySide6.QtWidgets.QTableWidgetItem(f"{sale[2]}"))
                        self.view_sales_tableWidget.setItem(row_count, 3,
                                                            PySide6.QtWidgets.QTableWidgetItem(f"£{sale[3]}"))
            self.month_dialog.close()
        else:
            error_message = QMessageBox.critical(None, "Choose a display option",
                                                 f"You must check one of the display options to view sales on specified month. Please try again",
                                                 QMessageBox.StandardButton.Ok)

    # function to display records from year dialog
    # pass id here
    def get_year_dialog_results(self):
        checked_button = self.year_dialog.year_dialog_display_optionGroup.checkedButton().text().strip() if self.year_dialog.year_dialog_display_optionGroup.checkedButton() else None
        year = self.year_dialog.year_dialog_select_year_spinBox.value()
        if checked_button:
                match checked_button:
                    case "Monthly Sales":
                        self.db.cursor.execute("""SELECT MONTH(date),YEAR(date), SUM(total) FROM sale_made 
                                                           WHERE restaurant_id = %s AND YEAR(date) = %s 
                                                           GROUP BY MONTH(date), YEAR(date) 
                                                           ORDER BY YEAR(date) DESC""",
                                              (self.restaurant_id, year))
                        sales = self.db.cursor.fetchall()
                        self.display_year_dialog_results(sales, "Month", "Month", "Total")
                    case "Daily sales":
                        self.db.cursor.execute("""SELECT date, SUM(total) FROM sale_made 
                                              WHERE restaurant_id = %s AND YEAR(date) = %s 
                                              GROUP BY date 
                                              ORDER BY date DESC""",
                                              (self.restaurant_id, year))
                        sales = self.db.cursor.fetchall()
                        self.display_year_dialog_results(sales, "Daily", "Date", "Total")
                    case "Weekly sales":
                        self.db.cursor.execute("""SELECT WEEK(date),YEAR(date), SUM(total) FROM sale_made 
                                              WHERE restaurant_id = %s AND YEAR(date) = %s 
                                              GROUP BY WEEK(date), YEAR(date) 
                                              ORDER BY WEEK(date), YEAR(date) DESC""",
                                               (self.restaurant_id, year))
                        sales = self.db.cursor.fetchall()
                        self.display_year_dialog_results(sales, "Week", "Week number-Year", "Total")
                    case "View all sales":
                        self.db.cursor.execute("""SELECT sale_made.date, menu_item.item_name, sale_made.amount_sold,sale_made.total
                                                FROM sale_made 
                                                INNER JOIN menu_item
                                                ON menu_item.item_id = sale_made.item_id
                                                WHERE sale_made.restaurant_id = %s AND YEAR(date) = %s
                                                ORDER BY sale_made.date DESC""",(self.restaurant_id,year))

                        sales = self.db.cursor.fetchall()
                        self.display_year_dialog_results(sales, "View all", "View all", "Total")
        else:
            QMessageBox.critical(None, "Choose a display option",
                                 f"You must check one of the display options to view the sales on the specified year. Please try again",
                                 QMessageBox.StandardButton.Ok)

    # need to display results using this function
    def display_year_dialog_results(self,sales,option,col1,col2):
        self.view_sales_tableWidget.clear()
        self.view_sales_tableWidget.setRowCount(len(sales))
        if option != "View all":
            if self.view_sales_tableWidget.columnCount() != 2:
                self.view_sales_tableWidget.setColumnCount(2)
            self.view_sales_tableWidget.setHorizontalHeaderItem(0,
                                                                PySide6.QtWidgets.QTableWidgetItem(f"{col1}"))
            self.view_sales_tableWidget.setHorizontalHeaderItem(1,
                                                                PySide6.QtWidgets.QTableWidgetItem(f"{col2}"))
            for row_count, sale in enumerate(sales):
                if option == "Daily":
                    self.view_sales_tableWidget.setItem(row_count, 0,
                                                        PySide6.QtWidgets.QTableWidgetItem(
                                                            sale[0].strftime("%d-%m-%Y")))
                elif option == "Week":
                    self.view_sales_tableWidget.setItem(row_count, 0,
                                                        PySide6.QtWidgets.QTableWidgetItem(
                                                            f"{sale[0]}-{sale[1]}"))
                elif option == "Month":
                    self.view_sales_tableWidget.setItem(row_count, 0,
                                                        PySide6.QtWidgets.QTableWidgetItem(
                                                            f"{calendar.month_abbr[sale[0]]}-{sale[1]}"))
                if option == "Week" or option == "Month":
                    self.view_sales_tableWidget.setItem(row_count, 1,
                                                        PySide6.QtWidgets.QTableWidgetItem(f"£{sale[2]}"))
                else:
                    self.view_sales_tableWidget.setItem(row_count, 1,
                                                        PySide6.QtWidgets.QTableWidgetItem(f"£{sale[1]}"))
        else:
            if self.view_sales_tableWidget.columnCount() != 4:
                self.view_sales_tableWidget.setColumnCount(4)
            self.view_sales_tableWidget.setHorizontalHeaderItem(0, PySide6.QtWidgets.QTableWidgetItem(f"Date"))
            self.view_sales_tableWidget.setHorizontalHeaderItem(1, PySide6.QtWidgets.QTableWidgetItem(f"Item"))
            self.view_sales_tableWidget.setHorizontalHeaderItem(2, PySide6.QtWidgets.QTableWidgetItem(f"Quantity"))
            self.view_sales_tableWidget.setHorizontalHeaderItem(3, PySide6.QtWidgets.QTableWidgetItem(f"Total"))
            for row_count, sale in enumerate(sales):
                self.view_sales_tableWidget.setItem(row_count, 0,
                                                    PySide6.QtWidgets.QTableWidgetItem(
                                                        sale[0].strftime("%d-%m-%Y")))
                self.view_sales_tableWidget.setItem(row_count, 1,
                                                    PySide6.QtWidgets.QTableWidgetItem(f"{sale[1]}"))
                self.view_sales_tableWidget.setItem(row_count, 2,
                                                    PySide6.QtWidgets.QTableWidgetItem(f"{sale[2]}"))
                self.view_sales_tableWidget.setItem(row_count, 3,
                                                    PySide6.QtWidgets.QTableWidgetItem(f"£{sale[3]}"))
        self.year_dialog.close()

    # function to get results from the selected item in item dialog to search for
    def get_item_dialog_results(self):
        dialog = self.item_dialog
        button_clicked =  self.sender().text().strip()
        sales = None
        # pass id here
        item = dialog.item_select_item_comboBox.currentText()
        if button_clicked == "View all item sales" and  dialog.item_view_all_radioButton.isChecked():
            query = """SELECT sale_made.date, menu_item.item_name, sale_made.amount_sold, sale_made.total FROM sale_made 
                    INNER JOIN menu_item
                    ON menu_item.item_id = sale_made.item_id
                    WHERE menu_item.item_name = %s and sale_made.restaurant_id = %s
                    ORDER BY sale_made.date DESC"""
            self.db.cursor.execute(query,(item,self.restaurant_id))
            sales = self.db.cursor.fetchall()
        elif button_clicked == "View by year":
            year = self.item_dialog.item_year_spinBox.value()
            query = """SELECT sale_made.date, menu_item.item_name, sale_made.amount_sold, sale_made.total FROM sale_made 
                                INNER JOIN menu_item
                                ON menu_item.item_id = sale_made.item_id
                                WHERE menu_item.item_name = %s AND sale_made.restaurant_id = %s AND YEAR(date) = %s
                                ORDER BY sale_made.date DESC"""
            self.db.cursor.execute(query, (item, self.restaurant_id,year))
            sales = self.db.cursor.fetchall()
        elif button_clicked == "View by month":
            year = self.item_dialog.item_month_year_spinBox.value()
            month = self.item_dialog.item_month_spinBox.value()
            query = """SELECT sale_made.date, menu_item.item_name, sale_made.amount_sold, sale_made.total FROM sale_made 
                    INNER JOIN menu_item
                    ON menu_item.item_id = sale_made.item_id
                    WHERE menu_item.item_name = %s AND sale_made.restaurant_id = %s AND YEAR(date) = %s AND MONTH(date) = %s
                    ORDER BY sale_made.date DESC"""
            self.db.cursor.execute(query, (item, self.restaurant_id, year, month))
        elif button_clicked == "View by day":
            cur_date = datetime(self.item_dialog.item_day_dateEdit.date().year(), self.item_dialog.item_day_dateEdit.date().month(), self.item_dialog.item_day_dateEdit.date().day())
            query = """SELECT sale_made.date, menu_item.item_name, sale_made.amount_sold, sale_made.total FROM sale_made 
                                INNER JOIN menu_item
                                ON menu_item.item_id = sale_made.item_id
                                WHERE menu_item.item_name = %s AND sale_made.restaurant_id = %s AND sale_made.date = %s
                                ORDER BY sale_made.date DESC"""
            self.db.cursor.execute(query, (item, self.restaurant_id,cur_date))
            sales = self.db.cursor.fetchall()
        self.display_item_dialog_results(sales,button_clicked)
        self.item_dialog.close()

# function to display the results after retrieving the data from the item dialog
    def display_item_dialog_results(self, sales,option):
        self.view_sales_tableWidget.clear()
        self.view_sales_tableWidget.setRowCount(len(sales))
        if self.view_sales_tableWidget.columnCount() != 4:
            self.view_sales_tableWidget.setColumnCount(4)
        self.view_sales_tableWidget.setHorizontalHeaderItem(0,
                                                            PySide6.QtWidgets.QTableWidgetItem(f"Date"))
        self.view_sales_tableWidget.setHorizontalHeaderItem(1,
                                                            PySide6.QtWidgets.QTableWidgetItem(f"Item name"))
        self.view_sales_tableWidget.setHorizontalHeaderItem(2,
                                                            PySide6.QtWidgets.QTableWidgetItem(f"Amount sold"))
        self.view_sales_tableWidget.setHorizontalHeaderItem(3,
                                                            PySide6.QtWidgets.QTableWidgetItem(f"Total"))
        for row_count, sale in enumerate(sales):
            self.view_sales_tableWidget.setItem(row_count, 0,
                                                PySide6.QtWidgets.QTableWidgetItem(
                                                    sale[0].strftime("%d-%m-%Y")))
            self.view_sales_tableWidget.setItem(row_count, 1,
                                                PySide6.QtWidgets.QTableWidgetItem(f"{sale[1]}"))
            self.view_sales_tableWidget.setItem(row_count, 2,
                                                PySide6.QtWidgets.QTableWidgetItem(f"{sale[2]}"))
            self.view_sales_tableWidget.setItem(row_count, 3,
                                                PySide6.QtWidgets.QTableWidgetItem(f"£{sale[3]}"))





    def view_sales_delete_items(self):
       sales = self.view_sales_tableWidget.selectedItems()
       for sale in sales:
           print(sale.text())