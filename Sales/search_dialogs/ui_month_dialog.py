# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'month_dialog.ui'
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
        Dialog.resize(381, 254)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.month_dialog_month_spinBox = QSpinBox(Dialog)
        self.month_dialog_month_spinBox.setObjectName(u"month_dialog_month_spinBox")
        self.month_dialog_month_spinBox.setMinimum(1)
        self.month_dialog_month_spinBox.setMaximum(12)

        self.horizontalLayout.addWidget(self.month_dialog_month_spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.month_dialog_year_spinBox = QSpinBox(Dialog)
        self.month_dialog_year_spinBox.setObjectName(u"month_dialog_year_spinBox")
        self.month_dialog_year_spinBox.setMinimum(2000)

        self.horizontalLayout_2.addWidget(self.month_dialog_year_spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.month_dialog_view_all_radioButton = QRadioButton(Dialog)
        self.month_dialog_display_option_group = QButtonGroup(Dialog)
        self.month_dialog_display_option_group.setObjectName(u"month_dialog_display_option_group")
        self.month_dialog_display_option_group.addButton(self.month_dialog_view_all_radioButton)
        self.month_dialog_view_all_radioButton.setObjectName(u"month_dialog_view_all_radioButton")

        self.verticalLayout.addWidget(self.month_dialog_view_all_radioButton)

        self.month_dialog_day_radioButton = QRadioButton(Dialog)
        self.month_dialog_display_option_group.addButton(self.month_dialog_day_radioButton)
        self.month_dialog_day_radioButton.setObjectName(u"month_dialog_day_radioButton")

        self.verticalLayout.addWidget(self.month_dialog_day_radioButton)

        self.month_dialog_week_radioButton = QRadioButton(Dialog)
        self.month_dialog_display_option_group.addButton(self.month_dialog_week_radioButton)
        self.month_dialog_week_radioButton.setObjectName(u"month_dialog_week_radioButton")

        self.verticalLayout.addWidget(self.month_dialog_week_radioButton)

        self.month_dialog_total_radioButton = QRadioButton(Dialog)
        self.month_dialog_display_option_group.addButton(self.month_dialog_total_radioButton)
        self.month_dialog_total_radioButton.setObjectName(u"month_dialog_total_radioButton")

        self.verticalLayout.addWidget(self.month_dialog_total_radioButton)

        self.month_dialog_ok_button = QPushButton(Dialog)
        self.month_dialog_ok_button.setObjectName(u"month_dialog_ok_button")

        self.verticalLayout.addWidget(self.month_dialog_ok_button)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Select month:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Select year:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Select display options:", None))
        self.month_dialog_view_all_radioButton.setText(QCoreApplication.translate("Dialog", u"View all sales ", None))
        self.month_dialog_day_radioButton.setText(QCoreApplication.translate("Dialog", u"View by day", None))
        self.month_dialog_week_radioButton.setText(QCoreApplication.translate("Dialog", u"View by week", None))
        self.month_dialog_total_radioButton.setText(QCoreApplication.translate("Dialog", u"View month total", None))
        self.month_dialog_ok_button.setText(QCoreApplication.translate("Dialog", u"Ok", None))
    # retranslateUi

