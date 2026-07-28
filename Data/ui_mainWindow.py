# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDoubleSpinBox,
    QFormLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(857, 610)
        self.actionLog_out = QAction(MainWindow)
        self.actionLog_out.setObjectName(u"actionLog_out")
        self.actionChange_details = QAction(MainWindow)
        self.actionChange_details.setObjectName(u"actionChange_details")
        self.actionChange_name = QAction(MainWindow)
        self.actionChange_name.setObjectName(u"actionChange_name")
        self.actionView_Sales = QAction(MainWindow)
        self.actionView_Sales.setObjectName(u"actionView_Sales")
        self.actionAdd_sale = QAction(MainWindow)
        self.actionAdd_sale.setObjectName(u"actionAdd_sale")
        self.actionManage_menu = QAction(MainWindow)
        self.actionManage_menu.setObjectName(u"actionManage_menu")
        self.actionAdd_expenses = QAction(MainWindow)
        self.actionAdd_expenses.setObjectName(u"actionAdd_expenses")
        self.actionView_expenses = QAction(MainWindow)
        self.actionView_expenses.setObjectName(u"actionView_expenses")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.manage_sales_page = QWidget()
        self.manage_sales_page.setObjectName(u"manage_sales_page")
        self.horizontalLayout = QHBoxLayout(self.manage_sales_page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.manage_sales_tabWidget = QTabWidget(self.manage_sales_page)
        self.manage_sales_tabWidget.setObjectName(u"manage_sales_tabWidget")
        self.view_sales_tab = QWidget()
        self.view_sales_tab.setObjectName(u"view_sales_tab")
        self.verticalLayout_2 = QVBoxLayout(self.view_sales_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.view_sales_search_button = QPushButton(self.view_sales_tab)
        self.view_sales_search_button.setObjectName(u"view_sales_search_button")

        self.horizontalLayout_2.addWidget(self.view_sales_search_button)

        self.view_sales_daily_button = QPushButton(self.view_sales_tab)
        self.view_sales_daily_button.setObjectName(u"view_sales_daily_button")

        self.horizontalLayout_2.addWidget(self.view_sales_daily_button)

        self.view_sales_monthly_button = QPushButton(self.view_sales_tab)
        self.view_sales_monthly_button.setObjectName(u"view_sales_monthly_button")

        self.horizontalLayout_2.addWidget(self.view_sales_monthly_button)

        self.view_sales_yearly_button = QPushButton(self.view_sales_tab)
        self.view_sales_yearly_button.setObjectName(u"view_sales_yearly_button")

        self.horizontalLayout_2.addWidget(self.view_sales_yearly_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.view_sales_table = QTableWidget(self.view_sales_tab)
        if (self.view_sales_table.columnCount() < 4):
            self.view_sales_table.setColumnCount(4)
        font = QFont()
        font.setPointSize(13)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font)
        self.view_sales_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font)
        self.view_sales_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font)
        self.view_sales_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font)
        self.view_sales_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.view_sales_table.setObjectName(u"view_sales_table")
        self.view_sales_table.horizontalHeader().setDefaultSectionSize(199)

        self.verticalLayout_2.addWidget(self.view_sales_table)

        self.view_sales_delete_sales_button = QPushButton(self.view_sales_tab)
        self.view_sales_delete_sales_button.setObjectName(u"view_sales_delete_sales_button")

        self.verticalLayout_2.addWidget(self.view_sales_delete_sales_button)

        self.manage_sales_tabWidget.addTab(self.view_sales_tab, "")
        self.add_sales_tab = QWidget()
        self.add_sales_tab.setObjectName(u"add_sales_tab")
        self.verticalLayout_6 = QVBoxLayout(self.add_sales_tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label = QLabel(self.add_sales_tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_17.addWidget(self.label)

        self.add_sales_date = QDateEdit(self.add_sales_tab)
        self.add_sales_date.setObjectName(u"add_sales_date")

        self.verticalLayout_17.addWidget(self.add_sales_date)


        self.horizontalLayout_4.addLayout(self.verticalLayout_17)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.add_sales_tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.add_sales_item_name_comboBox = QComboBox(self.add_sales_tab)
        self.add_sales_item_name_comboBox.setObjectName(u"add_sales_item_name_comboBox")

        self.verticalLayout_3.addWidget(self.add_sales_item_name_comboBox)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.add_sales_tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.add_sales_amount_sold_spinBox = QSpinBox(self.add_sales_tab)
        self.add_sales_amount_sold_spinBox.setObjectName(u"add_sales_amount_sold_spinBox")

        self.verticalLayout_4.addWidget(self.add_sales_amount_sold_spinBox)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.add_sales_tab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.add_sales_total_spinBox = QDoubleSpinBox(self.add_sales_tab)
        self.add_sales_total_spinBox.setObjectName(u"add_sales_total_spinBox")

        self.verticalLayout_5.addWidget(self.add_sales_total_spinBox)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.add_sales_confirm_button = QPushButton(self.add_sales_tab)
        self.add_sales_confirm_button.setObjectName(u"add_sales_confirm_button")
        self.add_sales_confirm_button.setStyleSheet(u"font-size:10pt;")

        self.horizontalLayout_4.addWidget(self.add_sales_confirm_button)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.add_sales_list = QListWidget(self.add_sales_tab)
        self.add_sales_list.setObjectName(u"add_sales_list")

        self.verticalLayout_6.addWidget(self.add_sales_list)

        self.add_sales_delete_button = QPushButton(self.add_sales_tab)
        self.add_sales_delete_button.setObjectName(u"add_sales_delete_button")

        self.verticalLayout_6.addWidget(self.add_sales_delete_button)

        self.add_sales_submit_button = QPushButton(self.add_sales_tab)
        self.add_sales_submit_button.setObjectName(u"add_sales_submit_button")

        self.verticalLayout_6.addWidget(self.add_sales_submit_button)

        self.manage_sales_tabWidget.addTab(self.add_sales_tab, "")

        self.horizontalLayout.addWidget(self.manage_sales_tabWidget)

        self.stackedWidget.addWidget(self.manage_sales_page)
        self.add_menu_page = QWidget()
        self.add_menu_page.setObjectName(u"add_menu_page")
        self.verticalLayout_9 = QVBoxLayout(self.add_menu_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.add_menu_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font-size:18pt;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.add_menu_page)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.add_menu_item_name = QComboBox(self.add_menu_page)
        self.add_menu_item_name.setObjectName(u"add_menu_item_name")
        self.add_menu_item_name.setEditable(True)

        self.verticalLayout_7.addWidget(self.add_menu_item_name)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.add_menu_page)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_8.addWidget(self.label_7)

        self.add_menu_item_price = QDoubleSpinBox(self.add_menu_page)
        self.add_menu_item_price.setObjectName(u"add_menu_item_price")

        self.verticalLayout_8.addWidget(self.add_menu_item_price)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.add_menu_item_add_button = QPushButton(self.add_menu_page)
        self.add_menu_item_add_button.setObjectName(u"add_menu_item_add_button")

        self.horizontalLayout_5.addWidget(self.add_menu_item_add_button)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.add_menu_item_list = QListWidget(self.add_menu_page)
        self.add_menu_item_list.setObjectName(u"add_menu_item_list")

        self.verticalLayout_9.addWidget(self.add_menu_item_list)

        self.add_menu_item_delete_button = QPushButton(self.add_menu_page)
        self.add_menu_item_delete_button.setObjectName(u"add_menu_item_delete_button")

        self.verticalLayout_9.addWidget(self.add_menu_item_delete_button)

        self.stackedWidget.addWidget(self.add_menu_page)
        self.manage_expenses_page = QWidget()
        self.manage_expenses_page.setObjectName(u"manage_expenses_page")
        self.verticalLayout_10 = QVBoxLayout(self.manage_expenses_page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.expenses_tabWidget = QTabWidget(self.manage_expenses_page)
        self.expenses_tabWidget.setObjectName(u"expenses_tabWidget")
        self.view_expenses_tab = QWidget()
        self.view_expenses_tab.setObjectName(u"view_expenses_tab")
        self.verticalLayout_11 = QVBoxLayout(self.view_expenses_tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.view_expenses_search_button = QPushButton(self.view_expenses_tab)
        self.view_expenses_search_button.setObjectName(u"view_expenses_search_button")

        self.horizontalLayout_6.addWidget(self.view_expenses_search_button)

        self.view_expenses_daily_button = QPushButton(self.view_expenses_tab)
        self.view_expenses_daily_button.setObjectName(u"view_expenses_daily_button")

        self.horizontalLayout_6.addWidget(self.view_expenses_daily_button)

        self.view_expenses_weekly_button = QPushButton(self.view_expenses_tab)
        self.view_expenses_weekly_button.setObjectName(u"view_expenses_weekly_button")

        self.horizontalLayout_6.addWidget(self.view_expenses_weekly_button)

        self.view_expenses_monthly_button = QPushButton(self.view_expenses_tab)
        self.view_expenses_monthly_button.setObjectName(u"view_expenses_monthly_button")

        self.horizontalLayout_6.addWidget(self.view_expenses_monthly_button)

        self.view_expenses_yearly_button = QPushButton(self.view_expenses_tab)
        self.view_expenses_yearly_button.setObjectName(u"view_expenses_yearly_button")

        self.horizontalLayout_6.addWidget(self.view_expenses_yearly_button)


        self.verticalLayout_11.addLayout(self.horizontalLayout_6)

        self.view_expenses_table = QTableWidget(self.view_expenses_tab)
        if (self.view_expenses_table.columnCount() < 3):
            self.view_expenses_table.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.view_expenses_table.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.view_expenses_table.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.view_expenses_table.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.view_expenses_table.setObjectName(u"view_expenses_table")
        self.view_expenses_table.setRowCount(0)
        self.view_expenses_table.horizontalHeader().setCascadingSectionResizes(True)
        self.view_expenses_table.horizontalHeader().setDefaultSectionSize(265)
        self.view_expenses_table.verticalHeader().setHighlightSections(True)
        self.view_expenses_table.verticalHeader().setProperty(u"showSortIndicator", False)

        self.verticalLayout_11.addWidget(self.view_expenses_table)

        self.view_expenses_delete_button = QPushButton(self.view_expenses_tab)
        self.view_expenses_delete_button.setObjectName(u"view_expenses_delete_button")

        self.verticalLayout_11.addWidget(self.view_expenses_delete_button)

        self.expenses_tabWidget.addTab(self.view_expenses_tab, "")
        self.add_expenses_tab = QWidget()
        self.add_expenses_tab.setObjectName(u"add_expenses_tab")
        self.verticalLayout_14 = QVBoxLayout(self.add_expenses_tab)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_11 = QLabel(self.add_expenses_tab)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_15.addWidget(self.label_11)

        self.add_expenses_date = QDateEdit(self.add_expenses_tab)
        self.add_expenses_date.setObjectName(u"add_expenses_date")

        self.verticalLayout_15.addWidget(self.add_expenses_date)


        self.horizontalLayout_10.addLayout(self.verticalLayout_15)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_10 = QLabel(self.add_expenses_tab)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_12.addWidget(self.label_10)

        self.add_expenses_expense_type_comboBox = QComboBox(self.add_expenses_tab)
        self.add_expenses_expense_type_comboBox.setObjectName(u"add_expenses_expense_type_comboBox")

        self.verticalLayout_12.addWidget(self.add_expenses_expense_type_comboBox)


        self.horizontalLayout_10.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_12 = QLabel(self.add_expenses_tab)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_13.addWidget(self.label_12)

        self.add_expenses_amount_spent_spinBox = QDoubleSpinBox(self.add_expenses_tab)
        self.add_expenses_amount_spent_spinBox.setObjectName(u"add_expenses_amount_spent_spinBox")

        self.verticalLayout_13.addWidget(self.add_expenses_amount_spent_spinBox)


        self.horizontalLayout_10.addLayout(self.verticalLayout_13)

        self.add_expenses_add_button = QPushButton(self.add_expenses_tab)
        self.add_expenses_add_button.setObjectName(u"add_expenses_add_button")

        self.horizontalLayout_10.addWidget(self.add_expenses_add_button)


        self.verticalLayout_14.addLayout(self.horizontalLayout_10)

        self.add_expenses_list = QListWidget(self.add_expenses_tab)
        self.add_expenses_list.setObjectName(u"add_expenses_list")

        self.verticalLayout_14.addWidget(self.add_expenses_list)

        self.add_expenses_delete_button = QPushButton(self.add_expenses_tab)
        self.add_expenses_delete_button.setObjectName(u"add_expenses_delete_button")

        self.verticalLayout_14.addWidget(self.add_expenses_delete_button)

        self.add_expenses_submit_button = QPushButton(self.add_expenses_tab)
        self.add_expenses_submit_button.setObjectName(u"add_expenses_submit_button")

        self.verticalLayout_14.addWidget(self.add_expenses_submit_button)

        self.expenses_tabWidget.addTab(self.add_expenses_tab, "")
        self.view_expenses_sales_tab = QWidget()
        self.view_expenses_sales_tab.setObjectName(u"view_expenses_sales_tab")
        self.verticalLayout_16 = QVBoxLayout(self.view_expenses_sales_tab)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.search_by_expense_sales_button = QPushButton(self.view_expenses_sales_tab)
        self.search_by_expense_sales_button.setObjectName(u"search_by_expense_sales_button")

        self.horizontalLayout_9.addWidget(self.search_by_expense_sales_button)

        self.daily_expense_sale_button = QPushButton(self.view_expenses_sales_tab)
        self.daily_expense_sale_button.setObjectName(u"daily_expense_sale_button")

        self.horizontalLayout_9.addWidget(self.daily_expense_sale_button)

        self.weekly_expense_sale_button = QPushButton(self.view_expenses_sales_tab)
        self.weekly_expense_sale_button.setObjectName(u"weekly_expense_sale_button")

        self.horizontalLayout_9.addWidget(self.weekly_expense_sale_button)

        self.yearly_expense_sale_button = QPushButton(self.view_expenses_sales_tab)
        self.yearly_expense_sale_button.setObjectName(u"yearly_expense_sale_button")

        self.horizontalLayout_9.addWidget(self.yearly_expense_sale_button)

        self.monthly_expense_sale_button = QPushButton(self.view_expenses_sales_tab)
        self.monthly_expense_sale_button.setObjectName(u"monthly_expense_sale_button")

        self.horizontalLayout_9.addWidget(self.monthly_expense_sale_button)


        self.verticalLayout_16.addLayout(self.horizontalLayout_9)

        self.expense_sales_table = QTableWidget(self.view_expenses_sales_tab)
        if (self.expense_sales_table.columnCount() < 4):
            self.expense_sales_table.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.expense_sales_table.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.expense_sales_table.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.expense_sales_table.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.expense_sales_table.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.expense_sales_table.setObjectName(u"expense_sales_table")
        self.expense_sales_table.horizontalHeader().setDefaultSectionSize(198)

        self.verticalLayout_16.addWidget(self.expense_sales_table)

        self.label_9 = QLabel(self.view_expenses_sales_tab)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_16.addWidget(self.label_9)

        self.expenses_tabWidget.addTab(self.view_expenses_sales_tab, "")

        self.verticalLayout_10.addWidget(self.expenses_tabWidget)

        self.stackedWidget.addWidget(self.manage_expenses_page)
        self.manage_account_page = QWidget()
        self.manage_account_page.setObjectName(u"manage_account_page")
        self.verticalLayout_18 = QVBoxLayout(self.manage_account_page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_8 = QLabel(self.manage_account_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font-size:18pt;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_8)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_14 = QLabel(self.manage_account_page)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_14)

        self.manage_account_change_restaurant_name_line_edit = QLineEdit(self.manage_account_page)
        self.manage_account_change_restaurant_name_line_edit.setObjectName(u"manage_account_change_restaurant_name_line_edit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.manage_account_change_restaurant_name_line_edit)

        self.label_13 = QLabel(self.manage_account_page)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.manage_account_change_password_line_edit = QLineEdit(self.manage_account_page)
        self.manage_account_change_password_line_edit.setObjectName(u"manage_account_change_password_line_edit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.manage_account_change_password_line_edit)

        self.manage_account_change_password_button = QPushButton(self.manage_account_page)
        self.manage_account_change_password_button.setObjectName(u"manage_account_change_password_button")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.manage_account_change_password_button)

        self.manage_account_change_restaurant_name_button = QPushButton(self.manage_account_page)
        self.manage_account_change_restaurant_name_button.setObjectName(u"manage_account_change_restaurant_name_button")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.manage_account_change_restaurant_name_button)


        self.verticalLayout_18.addLayout(self.formLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.verticalLayout_18.addLayout(self.horizontalLayout_7)

        self.stackedWidget.addWidget(self.manage_account_page)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 857, 33))
        self.menuView_Sales = QMenu(self.menubar)
        self.menuView_Sales.setObjectName(u"menuView_Sales")
        self.menuAdd_menu = QMenu(self.menubar)
        self.menuAdd_menu.setObjectName(u"menuAdd_menu")
        self.menuAccount = QMenu(self.menubar)
        self.menuAccount.setObjectName(u"menuAccount")
        self.menuExpenses = QMenu(self.menubar)
        self.menuExpenses.setObjectName(u"menuExpenses")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuView_Sales.menuAction())
        self.menubar.addAction(self.menuAdd_menu.menuAction())
        self.menubar.addAction(self.menuExpenses.menuAction())
        self.menubar.addAction(self.menuAccount.menuAction())
        self.menuView_Sales.addAction(self.actionView_Sales)
        self.menuView_Sales.addAction(self.actionAdd_sale)
        self.menuAdd_menu.addAction(self.actionManage_menu)
        self.menuAccount.addAction(self.actionLog_out)
        self.menuAccount.addAction(self.actionChange_details)
        self.menuExpenses.addAction(self.actionView_expenses)
        self.menuExpenses.addAction(self.actionAdd_expenses)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.manage_sales_tabWidget.setCurrentIndex(1)
        self.expenses_tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLog_out.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.actionChange_details.setText(QCoreApplication.translate("MainWindow", u"Manage account", None))
        self.actionChange_name.setText(QCoreApplication.translate("MainWindow", u"Change name", None))
        self.actionView_Sales.setText(QCoreApplication.translate("MainWindow", u"View Sales", None))
        self.actionAdd_sale.setText(QCoreApplication.translate("MainWindow", u"Add sales", None))
        self.actionManage_menu.setText(QCoreApplication.translate("MainWindow", u"Manage menu", None))
        self.actionAdd_expenses.setText(QCoreApplication.translate("MainWindow", u"Add expenses", None))
        self.actionView_expenses.setText(QCoreApplication.translate("MainWindow", u"View expenses", None))
        self.view_sales_search_button.setText(QCoreApplication.translate("MainWindow", u"Search by", None))
        self.view_sales_daily_button.setText(QCoreApplication.translate("MainWindow", u"View daily sales", None))
        self.view_sales_monthly_button.setText(QCoreApplication.translate("MainWindow", u"View monthly sales", None))
        self.view_sales_yearly_button.setText(QCoreApplication.translate("MainWindow", u"View yearly sales", None))
        ___qtablewidgetitem = self.view_sales_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        ___qtablewidgetitem1 = self.view_sales_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Item", None))
        ___qtablewidgetitem2 = self.view_sales_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        ___qtablewidgetitem3 = self.view_sales_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.view_sales_delete_sales_button.setText(QCoreApplication.translate("MainWindow", u"Delete selected sales", None))
        self.manage_sales_tabWidget.setTabText(self.manage_sales_tabWidget.indexOf(self.view_sales_tab), QCoreApplication.translate("MainWindow", u"View sales", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Item name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Amount sold:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.add_sales_confirm_button.setText(QCoreApplication.translate("MainWindow", u"Confirm entry", None))
        self.add_sales_delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete selected sales", None))
        self.add_sales_submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit sales", None))
        self.manage_sales_tabWidget.setTabText(self.manage_sales_tabWidget.indexOf(self.add_sales_tab), QCoreApplication.translate("MainWindow", u"Add sales", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Add/Remove menu Item:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Item name:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Price:", None))
        self.add_menu_item_add_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.add_menu_item_delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete selected items", None))
        self.view_expenses_search_button.setText(QCoreApplication.translate("MainWindow", u"Search by", None))
        self.view_expenses_daily_button.setText(QCoreApplication.translate("MainWindow", u"View daily expenses", None))
        self.view_expenses_weekly_button.setText(QCoreApplication.translate("MainWindow", u"View weekly expenses", None))
        self.view_expenses_monthly_button.setText(QCoreApplication.translate("MainWindow", u"View monthly expenses", None))
        self.view_expenses_yearly_button.setText(QCoreApplication.translate("MainWindow", u"View yearly expenses", None))
        ___qtablewidgetitem4 = self.view_expenses_table.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        ___qtablewidgetitem5 = self.view_expenses_table.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Expense type", None))
        ___qtablewidgetitem6 = self.view_expenses_table.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Amount spent", None))
        self.view_expenses_delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete selected expenses", None))
        self.expenses_tabWidget.setTabText(self.expenses_tabWidget.indexOf(self.view_expenses_tab), QCoreApplication.translate("MainWindow", u"View expenses", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Expense Type:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Amount spent:", None))
        self.add_expenses_add_button.setText(QCoreApplication.translate("MainWindow", u"Add expense", None))
        self.add_expenses_delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete selected expenses", None))
        self.add_expenses_submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit expenses", None))
        self.expenses_tabWidget.setTabText(self.expenses_tabWidget.indexOf(self.add_expenses_tab), QCoreApplication.translate("MainWindow", u"Add expenses", None))
        self.search_by_expense_sales_button.setText(QCoreApplication.translate("MainWindow", u"Search by", None))
        self.daily_expense_sale_button.setText(QCoreApplication.translate("MainWindow", u"Daily", None))
        self.weekly_expense_sale_button.setText(QCoreApplication.translate("MainWindow", u"Weekly", None))
        self.yearly_expense_sale_button.setText(QCoreApplication.translate("MainWindow", u"Yearly", None))
        self.monthly_expense_sale_button.setText(QCoreApplication.translate("MainWindow", u"Monthly", None))
        ___qtablewidgetitem7 = self.expense_sales_table.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        ___qtablewidgetitem8 = self.expense_sales_table.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Expense total", None))
        ___qtablewidgetitem9 = self.expense_sales_table.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Sales total", None))
        ___qtablewidgetitem10 = self.expense_sales_table.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_9.setText("")
        self.expenses_tabWidget.setTabText(self.expenses_tabWidget.indexOf(self.view_expenses_sales_tab), QCoreApplication.translate("MainWindow", u"View expenses with sales", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Manage Account", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Change restaurant name:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Change password:", None))
        self.manage_account_change_password_button.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.manage_account_change_restaurant_name_button.setText(QCoreApplication.translate("MainWindow", u"Change name", None))
        self.menuView_Sales.setTitle(QCoreApplication.translate("MainWindow", u"Sales", None))
        self.menuAdd_menu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuAccount.setTitle(QCoreApplication.translate("MainWindow", u"Account", None))
        self.menuExpenses.setTitle(QCoreApplication.translate("MainWindow", u"Expenses", None))
    # retranslateUi

