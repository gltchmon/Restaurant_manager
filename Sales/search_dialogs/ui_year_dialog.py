# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'year_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QDialog, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(219, 216)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.year_dialog_select_year_spinBox = QSpinBox(Dialog)
        self.year_dialog_select_year_spinBox.setObjectName(u"year_dialog_select_year_spinBox")
        self.year_dialog_select_year_spinBox.setMinimum(2000)
        self.year_dialog_select_year_spinBox.setMaximum(2026)

        self.horizontalLayout.addWidget(self.year_dialog_select_year_spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.year_dialog_monthly_radioButton = QRadioButton(Dialog)
        self.year_dialog_display_optionGroup = QButtonGroup(Dialog)
        self.year_dialog_display_optionGroup.setObjectName(u"year_dialog_display_optionGroup")
        self.year_dialog_display_optionGroup.addButton(self.year_dialog_monthly_radioButton)
        self.year_dialog_monthly_radioButton.setObjectName(u"year_dialog_monthly_radioButton")

        self.verticalLayout.addWidget(self.year_dialog_monthly_radioButton)

        self.year_dialog_daily_radioButton = QRadioButton(Dialog)
        self.year_dialog_display_optionGroup.addButton(self.year_dialog_daily_radioButton)
        self.year_dialog_daily_radioButton.setObjectName(u"year_dialog_daily_radioButton")

        self.verticalLayout.addWidget(self.year_dialog_daily_radioButton)

        self.year_dialog_weekly_radioButton = QRadioButton(Dialog)
        self.year_dialog_display_optionGroup.addButton(self.year_dialog_weekly_radioButton)
        self.year_dialog_weekly_radioButton.setObjectName(u"year_dialog_weekly_radioButton")

        self.verticalLayout.addWidget(self.year_dialog_weekly_radioButton)

        self.year_dialog_view_all_radioButton = QRadioButton(Dialog)
        self.year_dialog_display_optionGroup.addButton(self.year_dialog_view_all_radioButton)
        self.year_dialog_view_all_radioButton.setObjectName(u"year_dialog_view_all_radioButton")

        self.verticalLayout.addWidget(self.year_dialog_view_all_radioButton)

        self.year_dialog_okButton = QPushButton(Dialog)
        self.year_dialog_okButton.setObjectName(u"year_dialog_okButton")

        self.verticalLayout.addWidget(self.year_dialog_okButton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select year:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Choose how to display:", None))
        self.year_dialog_monthly_radioButton.setText(QCoreApplication.translate("Dialog", u"Monthly Sales", None))
        self.year_dialog_daily_radioButton.setText(QCoreApplication.translate("Dialog", u"Daily sales ", None))
        self.year_dialog_weekly_radioButton.setText(QCoreApplication.translate("Dialog", u"Weekly sales", None))
        self.year_dialog_view_all_radioButton.setText(QCoreApplication.translate("Dialog", u"View all sales", None))
        self.year_dialog_okButton.setText(QCoreApplication.translate("Dialog", u"Ok", None))
    # retranslateUi

