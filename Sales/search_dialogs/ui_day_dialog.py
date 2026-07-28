# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(382, 112)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.day_dialog_dateEdit = QDateEdit(self.frame)
        self.day_dialog_dateEdit.setObjectName(u"day_dialog_dateEdit")

        self.horizontalLayout.addWidget(self.day_dialog_dateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.day_dialog_ok_Button = QPushButton(self.frame)
        self.day_dialog_ok_Button.setObjectName(u"day_dialog_ok_Button")

        self.verticalLayout.addWidget(self.day_dialog_ok_Button)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Filter by day:", None))
        self.day_dialog_ok_Button.setText(QCoreApplication.translate("Dialog", u"Ok", None))
    # retranslateUi

