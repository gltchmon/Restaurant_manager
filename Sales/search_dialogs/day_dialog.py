
from PySide6.QtWidgets import QWidget, QDialog
from Sales.search_dialogs.ui_day_dialog import Ui_Dialog
import datetime
from Database.database import Database


# widget for managing the restaurant sales
class DayDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        date = datetime.datetime.now().date()
        self.setWindowTitle("Search by day")
        self.day_dialog_dateEdit.setMaximumDate(date)
        self.day_dialog_dateEdit.setDate(date)
        self.db = Database()

