from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QDialog, QPushButton, QApplication, QGridLayout, QLabel, QLineEdit, QMessageBox)
from Database.database import Database
from Sales.sales_widget import SalesWidget
import requests



class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        # create grid layout for log in form
        layout = QGridLayout()
        self.setLayout(layout)
        self.db = Database()
        self.sales_widget = None

        title = QLabel("Login or Register")
        title.setStyleSheet("font-size:14pt;")
        # title in middle
        layout.addWidget(title,0,0,1,3, Qt.AlignmentFlag.AlignCenter)

        # create username and password labels
        restaurant_code_label = QLabel("Restaurant code:")
        layout.addWidget(restaurant_code_label ,1,0)
        password_label =  QLabel("Password:")
        layout.addWidget(password_label,2,0)

        # create username and password line edits
        self.line_edits = {}
        self.line_edits["restaurant_code_line_edit"] = QLineEdit()
        layout.addWidget(self.line_edits["restaurant_code_line_edit"],1,1,1,2)
        self.line_edits["password_line_edit"] = QLineEdit()
        layout.addWidget(self.line_edits["password_line_edit"], 2, 1,1,2)

        self.log_in_button = QPushButton("Log in")
        layout.addWidget(self.log_in_button,3,1)
        self.create_account_button = QPushButton("Create account")
        layout.addWidget(self.create_account_button, 3, 2)

        self.log_in_button.clicked.connect(self.log_in_user)

    def log_in_user(self):
        flask_url = self.get_api_url("/login")
        restaurant_code = self.line_edits["restaurant_code_line_edit"].text()
        password = self.line_edits["password_line_edit"].text()
        data = {
            "code": restaurant_code,
            "password" : password
        }
        print(requests.get(flask_url,data))

        """
        # get password
        query = SELECT restaurant_id FROM restaurant
                WHERE code = %s AND password = %s
        self.db.cursor.execute(query,(restaurant_code,password))
        restaurant_id = self.db.cursor.fetchone()
        if restaurant_id:
            self.sales_widget = SalesWidget(restaurant_id[0])
            self.sales_widget.show()
            self.close()
        else:
            QMessageBox.critical(None, "Error logging in",
                                 f"This user does not exist.\nYour credentials may be wrong or you may need to create a new account.",
                                 QMessageBox.StandardButton.Ok)
        """
    def get_api_url(self,route):
        return f"http://127.0.0.1:5000/{route}"