import sys
from PySide6 import QtWidgets
from LogIn.login_dialog import LoginDialog

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginDialog()
    window.show()
    app.exec()