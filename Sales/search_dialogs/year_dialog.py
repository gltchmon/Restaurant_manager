from PySide6.QtWidgets import QWidget, QDialog
from Sales.search_dialogs.ui_year_dialog import Ui_Dialog


# dialog
class YearDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Search by year")

    def get_year(self):
        return 1