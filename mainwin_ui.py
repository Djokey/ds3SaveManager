from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(954, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vL_centralwidget = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vL_centralwidget.setObjectName(u"vL_centralwidget")
        self.widget_for_btn = QtWidgets.QWidget(self.centralwidget)
        self.widget_for_btn.setObjectName(u"widget_for_btn")
        self.hL_widget_for_btn = QtWidgets.QHBoxLayout(self.widget_for_btn)
        self.hL_widget_for_btn.setObjectName(u"hL_widget_for_btn")
        self.pushButton_save_my_save = QtWidgets.QPushButton(self.widget_for_btn)
        self.pushButton_save_my_save.setObjectName(u"pushButton_save_my_save")
        self.pushButton_select_account = QtWidgets.QPushButton(self.widget_for_btn)
        self.pushButton_select_account.setObjectName(u"pushButton_select_account")
        self.pushButton_select_save = QtWidgets.QPushButton(self.widget_for_btn)
        self.pushButton_select_save.setObjectName(u"pushButton_select_save")
        self.pushButton_delete_selected_save = QtWidgets.QPushButton(self.widget_for_btn)
        self.pushButton_delete_selected_save.setObjectName(u"pushButton_delete_selected_save")
        self.pushButton_delete_selected_folder = QtWidgets.QPushButton(self.widget_for_btn)
        self.pushButton_delete_selected_folder.setObjectName(u"pushButton_delete_selected_folder")

        self.label_current_save = QtWidgets.QLabel(self.centralwidget)
        self.label_current_save.setObjectName(u"label_current_save")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_current_save.setFont(font)

        self.hL_widget_for_btn.addWidget(self.pushButton_select_save)
        self.hL_widget_for_btn.addWidget(self.pushButton_save_my_save)
        self.hL_widget_for_btn.addWidget(self.pushButton_select_account)
        self.hL_widget_for_btn.addWidget(self.pushButton_delete_selected_save)
        self.hL_widget_for_btn.addWidget(self.pushButton_delete_selected_folder)
        self.vL_centralwidget.addWidget(self.widget_for_btn)
        self.vL_centralwidget.addWidget(self.label_current_save)

        MainWindow.setCentralWidget(self.centralwidget)

        # Menu Bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QtCore.QRect(0, 0, 963, 21))
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        # Settings
        self.settings = QtWidgets.QAction(MainWindow)
        self.settings.setObjectName("settings")
        self.menu.addAction(self.settings)
        self.menubar.addAction(self.menu.menuAction())

        # Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.statusbar.setFont(font)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ds3SaveManager"))
        self.pushButton_save_my_save.setText(QtCore.QCoreApplication.translate("MainWindow", u"Save my Save", None))
        self.pushButton_select_save.setText(QtCore.QCoreApplication.translate("MainWindow", u"Load selected Save", None))
        self.pushButton_delete_selected_save.setText(QtCore.QCoreApplication.translate("MainWindow", u"Delete selected Save", None))
        self.pushButton_delete_selected_folder.setText(QtCore.QCoreApplication.translate("MainWindow", u"Delete selected Folder", None))
        self.pushButton_select_account.setText(QtCore.QCoreApplication.translate("MainWindow", u"Select Account", None))
        self.label_current_save.setText(QtCore.QCoreApplication.translate("MainWindow", u"Current Save: ", None))

        self.menu.setTitle(_translate("MainWindow", "Menu"))
        self.settings.setText(_translate("MainWindow", "Settings"))
