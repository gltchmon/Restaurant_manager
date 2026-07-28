from ui_search_dialog import Ui_search_dialog
from PySide6.QtWidgets import QDialog

class SearchDialog(QDialog, Ui_search_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Search by")