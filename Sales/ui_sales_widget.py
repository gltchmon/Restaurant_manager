# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sales_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDoubleSpinBox,
    QHBoxLayout, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpinBox,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_manage_sales_widget(object):
    def setupUi(self, manage_sales_widget):
        if not manage_sales_widget.objectName():
            manage_sales_widget.setObjectName(u"manage_sales_widget")
        manage_sales_widget.resize(620, 428)
        self.verticalLayout = QVBoxLayout(manage_sales_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.manage_sales_tabWidget = QTabWidget(manage_sales_widget)
        self.manage_sales_tabWidget.setObjectName(u"manage_sales_tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.view_sales_search_comboBox = QComboBox(self.tab)
        self.view_sales_search_comboBox.setObjectName(u"view_sales_search_comboBox")

        self.horizontalLayout.addWidget(self.view_sales_search_comboBox)


        self.view_sales_view_all_button = QPushButton(self.tab)
        self.view_sales_view_all_button.setObjectName(u"view_sales_view_all_button")

        self.horizontalLayout.addWidget(self.view_sales_view_all_button)

        self.view_sales_daily_button = QPushButton(self.tab)
        self.view_sales_daily_button.setObjectName(u"view_sales_daily_button")

        self.horizontalLayout.addWidget(self.view_sales_daily_button)

        self.view_sales_weekly_button = QPushButton(self.tab)
        self.view_sales_weekly_button.setObjectName(u"view_sales_weekly_button")

        self.horizontalLayout.addWidget(self.view_sales_weekly_button)

        self.view_sales_monthly_button = QPushButton(self.tab)
        self.view_sales_monthly_button.setObjectName(u"view_sales_monthly_button")

        self.horizontalLayout.addWidget(self.view_sales_monthly_button)

        self.view_sales_yearly_sales = QPushButton(self.tab)
        self.view_sales_yearly_sales.setObjectName(u"view_sales_yearly_sales")

        self.horizontalLayout.addWidget(self.view_sales_yearly_sales)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.view_sales_tableWidget = QTableWidget(self.tab)
        if (self.view_sales_tableWidget.columnCount() < 4):
            self.view_sales_tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.view_sales_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.view_sales_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.view_sales_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.view_sales_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.view_sales_tableWidget.setObjectName(u"view_sales_tableWidget")
        self.view_sales_tableWidget.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_2.addWidget(self.view_sales_tableWidget)

        self.view_sales_delete_button = QPushButton(self.tab)
        self.view_sales_delete_button.setObjectName(u"view_sales_delete_button")

        self.verticalLayout_2.addWidget(self.view_sales_delete_button)

        self.manage_sales_tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_7 = QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.add_sales_date = QDateEdit(self.tab_2)
        self.add_sales_date.setObjectName(u"add_sales_date")

        self.verticalLayout_3.addWidget(self.add_sales_date)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.add_sales_item_name_comboBox = QComboBox(self.tab_2)
        self.add_sales_item_name_comboBox.setObjectName(u"add_sales_item_name_comboBox")

        self.verticalLayout_4.addWidget(self.add_sales_item_name_comboBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.add_sales_amount_sold_spinBox = QSpinBox(self.tab_2)
        self.add_sales_amount_sold_spinBox.setObjectName(u"add_sales_amount_sold_spinBox")

        self.verticalLayout_5.addWidget(self.add_sales_amount_sold_spinBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.add_sales_total_spinBox = QDoubleSpinBox(self.tab_2)
        self.add_sales_total_spinBox.setObjectName(u"add_sales_total_spinBox")

        self.verticalLayout_6.addWidget(self.add_sales_total_spinBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.add_sales_confirm_button = QPushButton(self.tab_2)
        self.add_sales_confirm_button.setObjectName(u"add_sales_confirm_button")
        self.add_sales_confirm_button.setStyleSheet(u"height:50px;")

        self.horizontalLayout_2.addWidget(self.add_sales_confirm_button)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.add_sales_listWidget = QListWidget(self.tab_2)
        self.add_sales_listWidget.setObjectName(u"add_sales_listWidget")

        self.verticalLayout_7.addWidget(self.add_sales_listWidget)

        self.add_sales_delete_button = QPushButton(self.tab_2)
        self.add_sales_delete_button.setObjectName(u"add_sales_delete_button")

        self.verticalLayout_7.addWidget(self.add_sales_delete_button)

        self.add_sales_submit_button = QPushButton(self.tab_2)
        self.add_sales_submit_button.setObjectName(u"add_sales_submit_button")

        self.verticalLayout_7.addWidget(self.add_sales_submit_button)

        self.manage_sales_tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.manage_sales_tabWidget)


        self.retranslateUi(manage_sales_widget)

        self.manage_sales_tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(manage_sales_widget)
    # setupUi

    def retranslateUi(self, manage_sales_widget):
        manage_sales_widget.setWindowTitle(QCoreApplication.translate("manage_sales_widget", u"Form", None))
        self.view_sales_search_comboBox.setPlaceholderText(QCoreApplication.translate("manage_sales_widget", u"Search by ", None))
        self.view_sales_view_all_button.setText(QCoreApplication.translate("manage_sales_widget", u"View all sales ", None))
        self.view_sales_daily_button.setText(QCoreApplication.translate("manage_sales_widget", u"View daily sales", None))
        self.view_sales_weekly_button.setText(QCoreApplication.translate("manage_sales_widget", u"View weekly sales", None))
        self.view_sales_monthly_button.setText(QCoreApplication.translate("manage_sales_widget", u"View monthly sales", None))
        self.view_sales_yearly_sales.setText(QCoreApplication.translate("manage_sales_widget", u"View yearly sales", None))
        ___qtablewidgetitem = self.view_sales_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("manage_sales_widget", u"Date", None))
        ___qtablewidgetitem1 = self.view_sales_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("manage_sales_widget", u"Item", None))
        ___qtablewidgetitem2 = self.view_sales_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("manage_sales_widget", u"Quantity", None))
        ___qtablewidgetitem3 = self.view_sales_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("manage_sales_widget", u"Total", None))
        self.view_sales_delete_button.setText(QCoreApplication.translate("manage_sales_widget", u"Delete selected sales ", None))
        self.manage_sales_tabWidget.setTabText(self.manage_sales_tabWidget.indexOf(self.tab), QCoreApplication.translate("manage_sales_widget", u"View sales", None))
        self.label.setText(QCoreApplication.translate("manage_sales_widget", u"Date:", None))
        self.label_2.setText(QCoreApplication.translate("manage_sales_widget", u"Item name:", None))
        self.label_3.setText(QCoreApplication.translate("manage_sales_widget", u"Quantity:", None))
        self.label_4.setText(QCoreApplication.translate("manage_sales_widget", u"Total:", None))
        self.add_sales_confirm_button.setText(QCoreApplication.translate("manage_sales_widget", u"Confirm entry", None))
        self.add_sales_delete_button.setText(QCoreApplication.translate("manage_sales_widget", u"Delete selected sales", None))
        self.add_sales_submit_button.setText(QCoreApplication.translate("manage_sales_widget", u"Submit sales", None))
        self.manage_sales_tabWidget.setTabText(self.manage_sales_tabWidget.indexOf(self.tab_2), QCoreApplication.translate("manage_sales_widget", u"Add sales", None))
    # retranslateUi

