from PySide6.QtWidgets import QWidget, QDialog
from Sales.search_dialogs.ui_month_dialog import Ui_Dialog
import datetime


# dialog
class MonthDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Search by month")
        current_year = datetime.datetime.now().year
        self.month_dialog_year_spinBox.setMaximum(current_year)
        self.month_dialog_year_spinBox.setValue(current_year)


    def get_month(self):
        return 1