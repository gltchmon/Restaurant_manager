from PySide6.QtWidgets import QWidget, QDialog
from Sales.search_dialogs.ui_item_dialog import Ui_Dialog


# dialog
class ItemDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Search by item")

    def get_item(self):
        return 1