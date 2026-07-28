# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)
from datetime import datetime

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(388, 204)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.item_select_item_comboBox = QComboBox(Dialog)
        self.item_select_item_comboBox.setObjectName(u"item_select_item_comboBox")

        self.horizontalLayout.addWidget(self.item_select_item_comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.item_view_all_radioButton = QRadioButton(Dialog)
        self.item_view_all_radioButton.setObjectName(u"item_view_all_radioButton")

        self.horizontalLayout_2.addWidget(self.item_view_all_radioButton)

        self.item_view_all_button = QPushButton(Dialog)
        self.item_view_all_button.setObjectName(u"item_view_all_button")

        self.horizontalLayout_2.addWidget(self.item_view_all_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.item_year_spinBox = QSpinBox(Dialog)
        self.item_year_spinBox.setMinimum(2000)
        self.item_year_spinBox.setMaximum(datetime.now().year)
        self.item_year_spinBox.setValue(datetime.now().year)
        self.item_year_spinBox.setObjectName(u"item_year_spinBox")

        self.horizontalLayout_3.addWidget(self.item_year_spinBox)

        self.item_year_button = QPushButton(Dialog)
        self.item_year_button.setObjectName(u"item_year_button")

        self.horizontalLayout_3.addWidget(self.item_year_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.item_month_spinBox = QSpinBox(Dialog)
        self.item_month_spinBox.setObjectName(u"item_month_spinBox")
        self.item_month_spinBox.setMinimum(1)
        self.item_month_spinBox.setMaximum(12)

        self.horizontalLayout_4.addWidget(self.item_month_spinBox)

        self.item_month_year_spinBox = QSpinBox(Dialog)
        self.item_month_year_spinBox.setObjectName(u"item_month_year_spinBox")
        self.item_month_year_spinBox.setMinimum(2000)
        self.item_month_year_spinBox.setMaximum(datetime.now().year)
        self.item_month_year_spinBox.setValue(datetime.now().year)

        self.horizontalLayout_4.addWidget(self.item_month_year_spinBox)

        self.item_month_button = QPushButton(Dialog)
        self.item_month_button.setObjectName(u"item_month_button")

        self.horizontalLayout_4.addWidget(self.item_month_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.item_day_dateEdit = QDateEdit(Dialog)
        self.item_day_dateEdit.setObjectName(u"item_day_dateEdit")
        self.item_day_dateEdit.setDate(QDate().currentDate())

        self.horizontalLayout_5.addWidget(self.item_day_dateEdit)

        self.item_day_button = QPushButton(Dialog)
        self.item_day_button.setObjectName(u"item_day_button")

        self.horizontalLayout_5.addWidget(self.item_day_button)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select item:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Choose display option:", None))
        self.item_view_all_radioButton.setText(QCoreApplication.translate("Dialog", u"View all sales with item", None))
        self.item_view_all_button.setText(QCoreApplication.translate("Dialog", u"View all item sales", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Select year:", None))
        self.item_year_button.setText(QCoreApplication.translate("Dialog", u"View by year", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Select month/year:", None))
        self.item_month_button.setText(QCoreApplication.translate("Dialog", u"View by month", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Select day:", None))
        self.item_day_button.setText(QCoreApplication.translate("Dialog", u"View by day", None))
    # retranslateUi

