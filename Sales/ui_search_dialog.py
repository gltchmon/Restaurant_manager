# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_dialog.ui'
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
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_search_dialog(object):
    def setupUi(self, search_dialog):
        if not search_dialog.objectName():
            search_dialog.setObjectName(u"search_dialog")
        search_dialog.resize(440, 488)
        self.verticalLayout_5 = QVBoxLayout(search_dialog)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame = QFrame(search_dialog)
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

        self.search_by_day_filter_spinbox = QDateEdit(self.frame)
        self.search_by_day_filter_spinbox.setObjectName(u"search_by_day_filter_spinbox")

        self.horizontalLayout.addWidget(self.search_by_day_filter_spinbox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.search_by_day_filter_ok_button = QPushButton(self.frame)
        self.search_by_day_filter_ok_button.setObjectName(u"search_by_day_filter_ok_button")

        self.verticalLayout.addWidget(self.search_by_day_filter_ok_button)


        self.horizontalLayout_5.addWidget(self.frame)

        self.frame_3 = QFrame(search_dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.search_by_month_spinBox = QSpinBox(self.frame_3)
        self.search_by_month_spinBox.setObjectName(u"search_by_month_spinBox")
        self.search_by_month_spinBox.setMinimum(1)

        self.horizontalLayout_3.addWidget(self.search_by_month_spinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.search_by_month_year_spinBox = QSpinBox(self.frame_3)
        self.search_by_month_year_spinBox.setObjectName(u"search_by_month_year_spinBox")
        self.search_by_month_year_spinBox.setMinimum(2000)

        self.horizontalLayout_4.addWidget(self.search_by_month_year_spinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.search_by_month_ok_button = QPushButton(self.frame_3)
        self.search_by_month_ok_button.setObjectName(u"search_by_month_ok_button")

        self.verticalLayout_3.addWidget(self.search_by_month_ok_button)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.frame_2 = QFrame(search_dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.search_by_year_spinBox = QSpinBox(self.frame_2)
        self.search_by_year_spinBox.setObjectName(u"search_by_year_spinBox")
        self.search_by_year_spinBox.setMinimum(2000)

        self.horizontalLayout_2.addWidget(self.search_by_year_spinBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.search_by_year_weekly_radioButton = QRadioButton(self.frame_2)
        self.search_by_year_weekly_radioButton.setObjectName(u"search_by_year_weekly_radioButton")

        self.horizontalLayout_6.addWidget(self.search_by_year_weekly_radioButton)

        self.search_by_year_monthly_radioButton = QRadioButton(self.frame_2)
        self.search_by_year_monthly_radioButton.setObjectName(u"search_by_year_monthly_radioButton")

        self.horizontalLayout_6.addWidget(self.search_by_year_monthly_radioButton)

        self.search_by_year_daily_radioButton = QRadioButton(self.frame_2)
        self.search_by_year_daily_radioButton.setObjectName(u"search_by_year_daily_radioButton")

        self.horizontalLayout_6.addWidget(self.search_by_year_daily_radioButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.search_by_year_ok_button = QPushButton(self.frame_2)
        self.search_by_year_ok_button.setObjectName(u"search_by_year_ok_button")

        self.verticalLayout_2.addWidget(self.search_by_year_ok_button)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame_4 = QFrame(search_dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.search_by_item_comboBox = QComboBox(self.frame_4)
        self.search_by_item_comboBox.setObjectName(u"search_by_item_comboBox")

        self.horizontalLayout_7.addWidget(self.search_by_item_comboBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.search_by_item_view_all_radioButton = QRadioButton(self.frame_4)
        self.search_by_item_view_all_radioButton.setObjectName(u"search_by_item_view_all_radioButton")

        self.horizontalLayout_8.addWidget(self.search_by_item_view_all_radioButton)

        self.search_by_item_view_all_ok_button = QPushButton(self.frame_4)
        self.search_by_item_view_all_ok_button.setObjectName(u"search_by_item_view_all_ok_button")

        self.horizontalLayout_8.addWidget(self.search_by_item_view_all_ok_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.search_by_item_year_comboBox = QSpinBox(self.frame_4)
        self.search_by_item_year_comboBox.setObjectName(u"search_by_item_year_comboBox")
        self.search_by_item_year_comboBox.setMinimum(2000)

        self.horizontalLayout_9.addWidget(self.search_by_item_year_comboBox)

        self.search_by_item_year_ok_button = QPushButton(self.frame_4)
        self.search_by_item_year_ok_button.setObjectName(u"search_by_item_year_ok_button")

        self.horizontalLayout_9.addWidget(self.search_by_item_year_ok_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.search_by_item_month_spinBox = QSpinBox(self.frame_4)
        self.search_by_item_month_spinBox.setObjectName(u"search_by_item_month_spinBox")
        self.search_by_item_month_spinBox.setMinimum(1)
        self.search_by_item_month_spinBox.setMaximum(12)

        self.horizontalLayout_10.addWidget(self.search_by_item_month_spinBox)

        self.search_by_item_month_year_spinBox = QSpinBox(self.frame_4)
        self.search_by_item_month_year_spinBox.setObjectName(u"search_by_item_month_year_spinBox")
        self.search_by_item_month_year_spinBox.setMinimum(2000)

        self.horizontalLayout_10.addWidget(self.search_by_item_month_year_spinBox)

        self.search_by_item_month_ok_button = QPushButton(self.frame_4)
        self.search_by_item_month_ok_button.setObjectName(u"search_by_item_month_ok_button")

        self.horizontalLayout_10.addWidget(self.search_by_item_month_ok_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.search_by_item_day_spinBox = QDateEdit(self.frame_4)
        self.search_by_item_day_spinBox.setObjectName(u"search_by_item_day_spinBox")

        self.horizontalLayout_11.addWidget(self.search_by_item_day_spinBox)

        self.search_by_item_day_ok_button = QPushButton(self.frame_4)
        self.search_by_item_day_ok_button.setObjectName(u"search_by_item_day_ok_button")

        self.horizontalLayout_11.addWidget(self.search_by_item_day_ok_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)


        self.verticalLayout_5.addWidget(self.frame_4)


        self.retranslateUi(search_dialog)

        QMetaObject.connectSlotsByName(search_dialog)
    # setupUi

    def retranslateUi(self, search_dialog):
        search_dialog.setWindowTitle(QCoreApplication.translate("search_dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("search_dialog", u"Filter by day", None))
        self.search_by_day_filter_ok_button.setText(QCoreApplication.translate("search_dialog", u"Ok", None))
        self.label_4.setText(QCoreApplication.translate("search_dialog", u"Filter by month:", None))
        self.label_5.setText(QCoreApplication.translate("search_dialog", u"Select year:", None))
        self.search_by_month_ok_button.setText(QCoreApplication.translate("search_dialog", u"Ok", None))
        self.label_2.setText(QCoreApplication.translate("search_dialog", u"Filter by year:", None))
        self.label_3.setText(QCoreApplication.translate("search_dialog", u"Show:", None))
        self.search_by_year_weekly_radioButton.setText(QCoreApplication.translate("search_dialog", u"Weekly sales", None))
        self.search_by_year_monthly_radioButton.setText(QCoreApplication.translate("search_dialog", u"Monthly sales", None))
        self.search_by_year_daily_radioButton.setText(QCoreApplication.translate("search_dialog", u"Daily sales", None))
        self.search_by_year_ok_button.setText(QCoreApplication.translate("search_dialog", u"Ok", None))
        self.label_6.setText(QCoreApplication.translate("search_dialog", u"Search by item:", None))
        self.search_by_item_view_all_radioButton.setText(QCoreApplication.translate("search_dialog", u"View all sales", None))
        self.search_by_item_view_all_ok_button.setText(QCoreApplication.translate("search_dialog", u"Ok", None))
        self.label_7.setText(QCoreApplication.translate("search_dialog", u"Select year", None))
        self.search_by_item_year_ok_button.setText(QCoreApplication.translate("search_dialog", u"Ok", None))
        self.label_8.setText(QCoreApplication.translate("search_dialog", u"Select month:", None))
        self.search_by_item_month_ok_button.setText(QCoreApplication.translate("search_dialog", u"Ok", None))
        self.label_9.setText(QCoreApplication.translate("search_dialog", u"Select day", None))
        self.search_by_item_day_ok_button.setText(QCoreApplication.translate("search_dialog", u"Ok", None))
    # retranslateUi

