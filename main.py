import datetime
import shutil
import configparser as cp
import os
import sys
import res
from PyQt5.QtWidgets import QMessageBox
from mainwin_ui import *
from save_ui import *
from settings_ui import *
from save_over_ui import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ask_over_save_status = False
        self.try_save_load = 0
        self.finished_count = 1
        self.disk_dir = os.getenv("SystemDrive")
        self.user = os.environ.get("USERNAME")
        self.conf_path = "config.ini"
        self.account = get_option(self.conf_path,
                                  "Settings",
                                  "account")
        self.how_to_save = get_option(self.conf_path, "Settings", "how_to_save")
        self.how_to_save_folder = get_option(self.conf_path, "Settings", "how_to_save_folder")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget = QtWidgets.QTabWidget(self.ui.centralwidget)
        self.ui.tabWidget.setObjectName("tabWidget")
        self._translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(self._translate("MainWindow", "ds3SaveManager " + version))
        self.ui_save_loader(self.ui.tabWidget)
        self.ui.tabWidgetForFrame = QtWidgets.QWidget(self.ui.centralwidget)
        self.ui.vL_centralwidget.addWidget(self.ui.tabWidgetForFrame)
        self.ui_save = Ui_Save()
        self.ui_save.setupUi(self.ui.tabWidgetForFrame)
        self.ui_save.label_name_folder.setEnabled(0)
        self.ui_save.lineEdit_name_folder.setEnabled(0)
        self.resize(800, 500)
        self.loader_for_start()
        self.but_func_inst()
        self.clear_for_start()

        set_option(conf_path, "Settings", "first_run", "0")

    def loader_for_start(self):
        self.ui.icon = QtGui.QIcon()
        self.ui.icon.addPixmap(QtGui.QPixmap(":/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(self.ui.icon)
        self.ui.label_current_save.setText("Current Save: " +
                                           get_option(self.conf_path, self.account, "current_save").split("||||")[0] +
                                           "\\" +
                                           get_option(self.conf_path, self.account, "current_save").split("||||")[1])

    def clear_for_start(self):
        self.ui.tabWidgetForFrame.hide()
        if self.try_save_load == 1:
            self.ui.tabWidget.hide()
            self.ui.widget_for_btn.hide()
            self.ui.label_current_save.hide()

    def ui_save_loader(self, tab_widget):
        self.tab_loader(tab_widget)
        self.ui.vL_centralwidget.addWidget(tab_widget)

    def tab_loader(self, tab_parent):
        for i in tab_parent.findChild(QtWidgets.QWidget).children():
            if 'tab_' in i.objectName():
                i.setAttribute(55, 1)
                i.close()

        path = r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups".format(self.disk_dir,
                                                                             self.user,
                                                                             self.account)
        if os.path.exists(path):
            listdir = os.listdir(path)
            for collect_build in listdir:
                tab = QtWidgets.QWidget()
                tab.setObjectName('tab_' + collect_build)
                vL_tab = QtWidgets.QVBoxLayout(tab)
                vL_tab.setObjectName("vL_tab_" + collect_build)
                vL_tab.setContentsMargins(0, 0, 0, 0)
                tab_parent.addTab(tab, "")
                tab_parent.setTabText(tab_parent.indexOf(tab), self._translate("MainWindow", collect_build))

                scrollA_tab = QtWidgets.QScrollArea(tab)
                scrollA_tab.setAutoFillBackground(False)
                scrollA_tab.setWidgetResizable(True)
                scrollA_tab.setObjectName("scrollA_tab_" + collect_build)
                sAWContent_tab = QtWidgets.QWidget()
                sAWContent_tab.setGeometry(QtCore.QRect(0, 0, 466, 484))
                sAWContent_tab.setObjectName("sAWContent_tab" + collect_build)
                vL_sAWContent_tab = QtWidgets.QVBoxLayout(sAWContent_tab)
                vL_sAWContent_tab.setObjectName("vL_sAWContent_tab" + collect_build)
                scrollA_tab.setWidget(sAWContent_tab)
                vL_tab.addWidget(scrollA_tab)

                self.clb_loader(collect_build, scrollA_tab, vL_sAWContent_tab)
        else:
            def select_acc():
                for _clb in self.ui.sAWC_folders.children():
                    if _clb.objectName().startswith("clb_"):
                        if _clb.isChecked():
                            set_option(self.conf_path, "Settings", "account", _clb.objectName()[4:])
                            self.account = _clb.objectName()[4:]
                            if os.path.exists(
                                    r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups".format(self.disk_dir,
                                                                                                  self.user,
                                                                                                  self.account)):
                                pass
                            else:
                                os.mkdir(r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups".format(self.disk_dir,
                                                                                                       self.user,
                                                                                                       self.account))
                self.ui.select_acc_widget.hide()
                self.ui.tabWidget.show()
                self.ui.widget_for_btn.show()
                self.ui.label_current_save.show()
                self.tab_loader(self.ui.tabWidget)

            accounts = search_game_saves_folders()
            self.ui.select_acc_widget = QtWidgets.QWidget(self.ui.centralwidget)
            self.ui.vL_centralwidget.addWidget(self.ui.select_acc_widget)
            self.ui.verticalLayout_select_acc_widget = QtWidgets.QVBoxLayout(self.ui.select_acc_widget)
            self.ui.verticalLayout_select_acc_widget.setObjectName("verticalLayout")
            self.ui.Label_select_acc = QtWidgets.QLabel(self.ui.select_acc_widget)
            self.ui.Label_select_acc.setObjectName("Label_select_acc")
            self.ui.verticalLayout_select_acc_widget.addWidget(self.ui.Label_select_acc)
            self.ui.Label_select_acc.setText(self._translate("MainWindow", "Select an Account"))
            self.ui.scrollArea_folders = QtWidgets.QScrollArea(self.ui.select_acc_widget)
            self.ui.scrollArea_folders.setWidgetResizable(True)
            self.ui.scrollArea_folders.setObjectName("scrollArea_saves")
            self.ui.sAWC_folders = QtWidgets.QWidget()
            self.ui.sAWC_folders.setGeometry(QtCore.QRect(0, 0, 950, 428))
            self.ui.sAWC_folders.setObjectName("sAWC")
            self.ui.vL_sAWC = \
                QtWidgets.QVBoxLayout(self.ui.sAWC_folders)
            self.ui.vL_sAWC.setObjectName("vL_sAWC")
            self.ui.scrollArea_folders.setWidget(self.ui.sAWC_folders)
            self.ui.verticalLayout_select_acc_widget.addWidget(self.ui.scrollArea_folders)
            if len(accounts) > 1:
                for _account in accounts:
                    clb = QtWidgets.QCommandLinkButton(self.ui.scrollArea_folders)
                    clb.setCheckable(True)
                    clb.setAutoExclusive(True)
                    clb.setObjectName("clb_" + _account)
                    self.ui.vL_sAWC.addWidget(clb)
                    clb.setText(self._translate("MainWindow", _account))
                    clb.clicked.connect(lambda: select_acc())
                self.try_save_load = 1
            else:
                set_option(self.conf_path, "Settings", "account", accounts[0])
                self.account = accounts[0]
                if not os.path.exists(r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups".format(self.disk_dir,
                                                                                                    self.user,
                                                                                                    self.account)):
                    os.mkdir(r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups".format(self.disk_dir,
                                                                                           self.user,
                                                                                           self.account))
                self.ui.select_acc_widget.hide()
                self.ui.tabWidget.show()
                self.ui.widget_for_btn.show()
                self.ui.label_current_save.show()
                self.tab_loader(self.ui.tabWidget)

    def clb_loader(self, collect, parent, layout_parent):
        listdir = os.listdir(r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups/".format(self.disk_dir,
                                                                                            self.user,
                                                                                            self.account) + collect)
        if collect == 'backups':
            listdir.reverse()
        for build in listdir:
            clb = QtWidgets.QCommandLinkButton(parent)
            clb.setCheckable(True)
            clb.setAutoExclusive(True)
            clb.setObjectName("clb_" + build[:-4])
            layout_parent.addWidget(clb)
            clb.setText(self._translate("MainWindow", build[:-4]))

    def but_func_inst(self):
        def load_save_ui():
            def saves_loader():
                def save_name_load():
                    for i in self.ui_save.sAWC_saves.children():
                        if i.objectName().startswith("clb_") and i.isChecked():
                            self.ui_save.lineEdit_name_saves.setText(i.objectName().replace("clb_", ""))
                for clb in self.ui_save.sAWC_folders.children():
                    if clb.objectName().startswith("clb_") and clb.isChecked():
                        listdir = os.listdir(
                            r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups/{}/".format(
                                self.disk_dir,
                                self.user,
                                self.account,
                                clb.objectName().split("_")[-1]))

                        for clb_del in self.ui_save.sAWC_saves.children():
                            if clb_del.objectName().startswith("clb_"):
                                clb_del.setAttribute(55, 1)
                                clb_del.close()

                        for saves in listdir:
                            save_name = saves.replace(".sl2", "")
                            s_clb = QtWidgets.QCommandLinkButton(self.ui_save.sAWC_saves)
                            s_clb.setCheckable(True)
                            s_clb.setAutoExclusive(True)
                            s_clb.setObjectName("clb_" + save_name)
                            self.ui_save.vL_sAWC_saves.addWidget(s_clb)
                            s_clb.setText(self._translate("MainWindow", save_name))
                            s_clb.clicked.connect(lambda: save_name_load())

                        break

            def folder_loader_for_load_save_ui():
                for clb in self.ui_save.sAWC_folders.children():
                    if clb.objectName().startswith("clb_"):
                        clb.setAttribute(55, 1)
                        clb.close()
                listdir = os.listdir(r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups/".format(self.disk_dir,
                                                                                                    self.user,
                                                                                                    self.account))
                for folder in listdir:
                    clb = QtWidgets.QCommandLinkButton(self.ui_save.sAWC_folders)
                    clb.setCheckable(True)
                    clb.setAutoExclusive(True)
                    clb.setObjectName("clb_" + folder)
                    self.ui_save.vL_sAWC_folders.addWidget(clb)
                    clb.setText(self._translate("MainWindow", folder))
                    clb.clicked.connect(lambda: saves_loader())

            self.ui.tabWidget.hide()
            self.ui.widget_for_btn.hide()
            self.ui.label_current_save.hide()
            folder_loader_for_load_save_ui()
            self.ui.tabWidgetForFrame.show()

        def unload_save_ui():
            self.ui.tabWidgetForFrame.hide()
            self.ui.tabWidget.show()
            self.ui.widget_for_btn.show()
            self.ui.label_current_save.show()

        def check_box_change():
            if self.ui_save.checkBox_create_new_folder.isChecked():
                self.ui_save.label_selected_folder.setEnabled(0)
                self.ui_save.scrollArea_saves_folders.setEnabled(0)
                self.ui_save.label_name_folder.setEnabled(1)
                self.ui_save.lineEdit_name_folder.setEnabled(1)
            else:
                self.ui_save.label_name_folder.setEnabled(0)
                self.ui_save.lineEdit_name_folder.setEnabled(0)
                self.ui_save.label_selected_folder.setEnabled(1)
                self.ui_save.scrollArea_saves_folders.setEnabled(1)

        def save_my_save():
            def check_save_this(status_folder_match, folder):
                def save_this(_folder, _over=False):
                    if os.path.exists(r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups/{}".format(self.disk_dir,
                                                                                                       self.user,
                                                                                                       self.account,
                                                                                                       _folder)):
                        pass
                    else:
                        os.mkdir(
                            r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups/{}".format(self.disk_dir,
                                                                                             self.user,
                                                                                             self.account,
                                                                                             _folder))
                    set_option(self.conf_path,
                               self.account,
                               "current_save",
                               _folder + r'||||' + self.ui_save.lineEdit_name_saves.text())
                    self.ui.label_current_save.setText("Current Save: " + _folder + '\\' + self.ui_save.lineEdit_name_saves.text())
                    if os.path.exists(
                            r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\DS30000.sl2".format(self.disk_dir,
                                                                                              self.user,
                                                                                              self.account)):
                        if _over:
                            if os.path.exists(
                                    r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups/backups".format(self.disk_dir,
                                                                                                          self.user,
                                                                                                          self.account,
                                                                                                          )):
                                pass
                            else:
                                os.mkdir(
                                    r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups/backups".format(self.disk_dir,
                                                                                                          self.user,
                                                                                                          self.account,
                                                                                                          ))
                            shutil.copy2(
                                r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups\{}\{}.sl2".format(
                                    self.disk_dir,
                                    self.user,
                                    self.account,
                                    _folder,
                                    self.ui_save.lineEdit_name_saves.text()),
                                r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups\backups\{}.sl2".format(
                                    self.disk_dir,
                                    self.user,
                                    self.account,
                                    datetime.datetime.today().strftime(
                                        "%Y_%m_%d_%H_%M_%S_") +
                                    'over_' +
                                    self.ui_save.lineEdit_name_saves.text()))
                        shutil.copy2(
                            r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\DS30000.sl2".format(self.disk_dir,
                                                                                              self.user,
                                                                                              self.account),
                            r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups\{}\{}.sl2".format(
                                self.disk_dir,
                                self.user,
                                self.account,
                                _folder,
                                self.ui_save.lineEdit_name_saves.text()))
                        unload_save_ui()
                        self.tab_loader(self.ui.tabWidget)
                        self.finished_count += 1
                        self.ui.statusbar.showMessage('Finished ({}). Saved.'.format(self.finished_count), 5000)

                if self.ui_save.lineEdit_name_saves.text() == '':
                    set_doc_warning("Error",
                                    "Enter the Save name!")
                elif os.path.exists(
                        r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups/{}/{}.sl2".format(self.disk_dir,
                                                                                                self.user,
                                                                                                self.account,
                                                                                                folder,
                                                                                                self.ui_save.lineEdit_name_saves.text())):
                    if self.how_to_save == "0":
                        set_doc_warning("Error",
                                        "This save name is already taken!")
                    elif self.how_to_save == "1":
                        if status_folder_match:
                            self.save_over_window("Save over folder and save?")
                            if self.ask_over_save_status:
                                save_this(folder, True)
                                self.ask_over_save_status = False
                        else:
                            self.save_over_window("Save over a save with the same name?")
                            if self.ask_over_save_status:
                                save_this(folder, True)
                                self.ask_over_save_status = False
                    elif self.how_to_save == "2":
                        if status_folder_match:
                            self.save_over_window("Save in a folder with the same name?")
                            if self.ask_over_save_status:
                                save_this(folder)
                                self.ask_over_save_status = False
                        else:
                            save_this(folder)
                            self.ask_over_save_status = False
                else:
                    if status_folder_match:
                        self.save_over_window("Save in a folder with the same name?")
                        if self.ask_over_save_status:
                            save_this(folder)
                            self.ask_over_save_status = False
                    else:
                        save_this(folder)
                        self.ask_over_save_status = False

            if self.ui_save.checkBox_create_new_folder.isChecked():
                if self.ui_save.lineEdit_name_folder.text() == '':
                    set_doc_warning("Error",
                                    'Enter the Folder name!')
                elif os.path.exists(r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups/{}".format(self.disk_dir,
                                                                                                     self.user,
                                                                                                     self.account,
                                                                                                     self.ui_save.lineEdit_name_folder.text())):
                    if self.how_to_save_folder == "0":
                        set_doc_warning("Error",
                                        "This folder name is already taken!")
                    elif self.how_to_save_folder == "1":
                        check_save_this(True, self.ui_save.lineEdit_name_folder.text())
                    elif self.how_to_save_folder == "2":
                        check_save_this(False, self.ui_save.lineEdit_name_folder.text())
                else:
                    check_save_this(False, self.ui_save.lineEdit_name_folder.text())

            else:
                checked_folder = ''
                for i in self.ui_save.sAWC_folders.children():
                    if 'clb_' in i.objectName() and i.isChecked():
                        checked_folder = i.objectName()
                if self.ui_save.lineEdit_name_saves.text() == '':
                    set_doc_warning("Error",
                                    "Enter the Save name!")
                elif checked_folder == '':
                    set_doc_warning("Error",
                                    'Select the Folder!')
                else:
                    check_save_this(False, checked_folder[4:])

        def delete_selected_save():
            save_del = ''
            if os.path.exists(
                    r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups\backups".format(self.disk_dir,
                                                                                          self.user,
                                                                                          self.account)):
                pass
            else:
                os.mkdir(
                    r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups\backups".format(self.disk_dir,
                                                                                          self.user,
                                                                                          self.account))
            for i in self.ui.tabWidget.currentWidget().children():
                if 'clb_' in i.objectName() and i.isChecked():
                    if self.ui.tabWidget.currentWidget().objectName() == 'tab_backups':
                        save_del = i.objectName()[4:]
                        os.remove(r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups/{}/{}.sl2".format(self.disk_dir,
                                                                                                          self.user,
                                                                                                          self.account,
                                                                                                          self.ui.tabWidget.currentWidget().objectName()[
                                                                                                          4:],
                                                                                                          i.objectName()[
                                                                                                          4:]))
                        self.tab_loader(self.ui.tabWidget)
                        self.finished_count += 1
                        self.ui.statusbar.showMessage(
                            'Finished ({}). The Save({}) was deleted.'.format(self.finished_count,
                                                                              save_del),
                            5000)
                    else:
                        save_del = i.objectName()[4:]
                        shutil.copy2(
                            r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups/{}/{}.sl2".format(self.disk_dir,
                                                                                                    self.user,
                                                                                                    self.account,
                                                                                                    self.ui.tabWidget.currentWidget().objectName()[
                                                                                                    4:],
                                                                                                    i.objectName()[
                                                                                                    4:]),
                            r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups/backups/{}.sl2".format(self.disk_dir,
                                                                                                         self.user,
                                                                                                         self.account,
                                                                                                         datetime.datetime.today().strftime(
                                                                                                             "%Y_%m_%d_%H_%M_%S_") +
                                                                                                         'deleted_' +
                                                                                                         i.objectName()[
                                                                                                         4:]))
                        os.remove(r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups/{}/{}.sl2".format(self.disk_dir,
                                                                                                          self.user,
                                                                                                          self.account,
                                                                                                          self.ui.tabWidget.currentWidget().objectName()[
                                                                                                          4:],
                                                                                                          i.objectName()[
                                                                                                          4:]))
                        self.tab_loader(self.ui.tabWidget)
                        self.finished_count += 1
                        self.ui.statusbar.showMessage(
                            'Finished ({}). The Save({}) was deleted.'.format(self.finished_count,
                                                                              save_del),
                            5000)
            if save_del == '':
                set_doc_warning("Error",
                                "Select the Save!")

        def delete_selected_folder():
            if isinstance(self.ui.tabWidget.currentWidget(), QtWidgets.QWidget):
                fold = self.ui.tabWidget.currentWidget().objectName()[4:]
                shutil.rmtree(r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups\{}".format(self.disk_dir,
                                                                                               self.user,
                                                                                               self.account,
                                                                                               self.ui.tabWidget.currentWidget().objectName()[
                                                                                               4:], ))
                self.ui.tabWidget.removeTab(self.ui.tabWidget.currentIndex())
                self.tab_loader(self.ui.tabWidget)
                self.finished_count += 1
                self.ui.statusbar.showMessage('Finished ({}). The Folder({}) was deleted.'.format(self.finished_count,
                                                                                                  fold),
                                              5000)
            else:
                set_doc_warning("Error",
                                "Nothing to delete!")

        def select_account():
            def select_acc():
                for _clb in self.ui.sAWC_folders.children():
                    if _clb.objectName().startswith("clb_"):
                        if _clb.isChecked():
                            set_option(self.conf_path, "Settings", "account", _clb.objectName()[4:])
                            self.account = _clb.objectName()[4:]
                            if os.path.exists(
                                    r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups".format(self.disk_dir,
                                                                                                  self.user,
                                                                                                  self.account)):
                                pass
                            else:
                                os.mkdir(r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups".format(self.disk_dir,
                                                                                                       self.user,
                                                                                                       self.account))
                self.ui.select_acc_widget.hide()
                self.ui.tabWidget.show()
                self.ui.widget_for_btn.show()
                self.ui.label_current_save.show()
                self.tab_loader(self.ui.tabWidget)
                self.finished_count += 1
                self.ui.statusbar.showMessage('Finished ({}). The Account({}) was selected.'.format(self.finished_count,
                                                                                                    self.account),
                                              5000)

            accounts = search_game_saves_folders()
            self.ui.select_acc_widget = QtWidgets.QWidget(self.ui.centralwidget)
            self.ui.vL_centralwidget.addWidget(self.ui.select_acc_widget)
            self.ui.verticalLayout_select_acc_widget = QtWidgets.QVBoxLayout(self.ui.select_acc_widget)
            self.ui.verticalLayout_select_acc_widget.setObjectName("verticalLayout")
            self.ui.Label_select_acc = QtWidgets.QLabel(self.ui.select_acc_widget)
            self.ui.Label_select_acc.setObjectName("Label_select_acc")
            self.ui.verticalLayout_select_acc_widget.addWidget(self.ui.Label_select_acc)
            self.ui.Label_select_acc.setText(self._translate("MainWindow", "Select an Account"))
            self.ui.scrollArea_folders = QtWidgets.QScrollArea(self.ui.select_acc_widget)
            self.ui.scrollArea_folders.setWidgetResizable(True)
            self.ui.scrollArea_folders.setObjectName("scrollArea_saves")
            self.ui.sAWC_folders = QtWidgets.QWidget()
            self.ui.sAWC_folders.setGeometry(QtCore.QRect(0, 0, 950, 428))
            self.ui.sAWC_folders.setObjectName("sAWC")
            self.ui.vL_sAWC = \
                QtWidgets.QVBoxLayout(self.ui.sAWC_folders)
            self.ui.vL_sAWC.setObjectName("vL_sAWC")
            self.ui.scrollArea_folders.setWidget(self.ui.sAWC_folders)
            self.ui.verticalLayout_select_acc_widget.addWidget(self.ui.scrollArea_folders)
            if len(accounts) > 1:
                for _account in accounts:
                    clb = QtWidgets.QCommandLinkButton(self.ui.scrollArea_folders)
                    clb.setCheckable(True)
                    clb.setAutoExclusive(True)
                    clb.setObjectName("clb_" + _account)
                    self.ui.vL_sAWC.addWidget(clb)
                    clb.setText(self._translate("MainWindow", _account))
                    clb.clicked.connect(lambda: select_acc())
                self.ui.widget_for_btn.hide()
                self.ui.label_current_save.hide()
                self.ui.tabWidget.hide()
            else:
                set_option(self.conf_path, "Settings", "account", accounts[0])
                self.account = accounts[0]
                if os.path.exists(
                        r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups".format(self.disk_dir,
                                                                                      self.user,
                                                                                      self.account)):
                    pass
                else:
                    os.mkdir(r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups".format(self.disk_dir,
                                                                                           self.user,
                                                                                           self.account))
                self.ui.select_acc_widget.hide()
                self.ui.tabWidget.show()
                self.ui.widget_for_btn.show()
                self.ui.label_current_save.show()
                self.tab_loader(self.ui.tabWidget)
                set_doc_warning("Error",
                                "You have one account!")
            self.try_save_load = 1

        def load_save():
            status_save_checked = 0
            if isinstance(self.ui.tabWidget.currentWidget(), QtWidgets.QWidget):
                for i in self.ui.tabWidget.currentWidget().findChild(
                        QtWidgets.QWidget, "sAWContent_tab" + self.ui.tabWidget.currentWidget().objectName().replace("tab_", "")
                ).children():
                    if 'clb_' in i.objectName() and i.isChecked():
                        status_save_checked = 1
                        if os.path.exists(
                                r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups\backups".format(self.disk_dir,
                                                                                                      self.user,
                                                                                                      self.account)):
                            shutil.copy2(
                                r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\DS30000.sl2".format(self.disk_dir,
                                                                                                  self.user,
                                                                                                  self.account),
                                r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups\backups\{}.sl2".format(
                                    self.disk_dir,
                                    self.user,
                                    self.account,
                                    datetime.datetime.today().strftime(
                                        "%Y_%m_%d_%H_%M_%S_") +
                                    'before_' +
                                    get_option(self.conf_path,
                                               self.account,
                                               'current_save').split(
                                        r"||||")[1]))
                        else:
                            os.mkdir(
                                r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups\backups".format(self.disk_dir,
                                                                                                      self.user,
                                                                                                      self.account))
                            shutil.copy2(
                                r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\DS30000.sl2".format(self.disk_dir,
                                                                                                  self.user,
                                                                                                  self.account),
                                r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups\backups\{}.sl2".format(
                                    self.disk_dir,
                                    self.user,
                                    self.account,
                                    datetime.datetime.today().strftime(
                                        "%Y_%m_%d_%H_%M_%S_") +
                                    'before_' +
                                    get_option(self.conf_path,
                                               self.account,
                                               'current_save').split(
                                        r"||||")[1]))
                        os.remove(r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\DS30000.sl2".format(self.disk_dir,
                                                                                                    self.user,
                                                                                                    self.account))
                        shutil.copy2(
                            r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\backups/{}/{}.sl2".format(self.disk_dir,
                                                                                                    self.user,
                                                                                                    self.account,
                                                                                                    self.ui.tabWidget.currentWidget().objectName()[
                                                                                                    4:],
                                                                                                    i.objectName()[4:]),
                            r"{}\Users\{}\AppData\Roaming\DarkSoulsIII\{}\DS30000.sl2".format(self.disk_dir,
                                                                                              self.user,
                                                                                              self.account))
                        set_option(self.conf_path,
                                   self.account,
                                   "current_save",
                                   self.ui.tabWidget.currentWidget().objectName()[4:] + r'||||' + i.objectName()[4:])
                        self.ui.label_current_save.setText("Current Save: " + self.ui.tabWidget.currentWidget().objectName()[4:] + '\\' + i.objectName()[4:])
                        self.finished_count += 1
                        self.ui.statusbar.showMessage('Finished ({}). The Save({}) loaded.'.format(self.finished_count,
                                                                                                   i.objectName()[4:]),
                                                      5000)
                        self.tab_loader(self.ui.tabWidget)
            else:
                set_doc_warning("Error",
                                "Nothing to Load!")
                status_save_checked = 1
            if status_save_checked == 0:
                set_doc_warning("Error",
                                "Select the Save!")

        self.ui.pushButton_save_my_save.clicked.connect(lambda: load_save_ui())
        self.ui_save.pushButton_back.clicked.connect(lambda: unload_save_ui())
        self.ui_save.checkBox_create_new_folder.clicked.connect(lambda: check_box_change())
        self.ui_save.pushButton_save.clicked.connect(lambda: save_my_save())
        self.ui.pushButton_delete_selected_save.clicked.connect(lambda: delete_selected_save())
        self.ui.pushButton_delete_selected_folder.clicked.connect(lambda: delete_selected_folder())
        self.ui.pushButton_select_account.clicked.connect(lambda: select_account())
        self.ui.pushButton_select_save.clicked.connect(lambda: load_save())
        self.ui.settings.triggered.connect(lambda: self.settings_window())

    def settings_window(self, war_icon=":/ico.ico"):
        def set_how_to_save(setting):
            set_option(self.conf_path, "Settings", "how_to_save", setting)
            self.how_to_save = setting

        def set_how_to_save_folder(setting):
            set_option(self.conf_path, "Settings", "how_to_save_folder", setting)
            self.how_to_save_folder = setting

        set_win = QtWidgets.QDialog(self)
        settings_win = Ui_Settings()
        settings_win.setupUi(set_win)
        set_win.setWindowTitle('Settings')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(war_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        set_win.setWindowIcon(icon)

        settings_win.radio_err.clicked.connect(lambda: set_how_to_save("0"))
        settings_win.radio_ask.clicked.connect(lambda: set_how_to_save("1"))
        settings_win.radio_over.clicked.connect(lambda: set_how_to_save("2"))
        settings_win.radio_err_folder.clicked.connect(lambda: set_how_to_save_folder("0"))
        settings_win.radio_ask_folder.clicked.connect(lambda: set_how_to_save_folder("1"))
        settings_win.radio_over_folder.clicked.connect(lambda: set_how_to_save_folder("2"))

        if self.how_to_save == "0":
            settings_win.radio_err.setChecked(True)
        elif self.how_to_save == "1":
            settings_win.radio_ask.setChecked(True)
        elif self.how_to_save == "2":
            settings_win.radio_over.setChecked(True)

        if self.how_to_save_folder == "0":
            settings_win.radio_err_folder.setChecked(True)
        elif self.how_to_save_folder == "1":
            settings_win.radio_ask_folder.setChecked(True)
        elif self.how_to_save_folder == "2":
            settings_win.radio_over_folder.setChecked(True)

        set_win.exec_()

    def save_over_window(self, question, war_icon=":/ico.ico"):
        def func_set_ask():
            self.ask_over_save_status = True
            set_win.close()

        set_win = QtWidgets.QDialog(self)
        settings_win = Ui_Save_over()
        settings_win.setupUi(set_win)
        set_win.setWindowTitle('Overwrite or note')
        settings_win.main_quest.setText(question)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(war_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        set_win.setWindowIcon(icon)
        settings_win.overwrite.clicked.connect(lambda: func_set_ask())
        settings_win.cancel.clicked.connect(lambda: set_win.close())
        set_win.exec_()


def set_doc_warning(war_name, war_text, war_icon=":/ico.ico"):
    _set_doc_warning = QMessageBox()
    _set_doc_warning.setWindowTitle(war_name)
    _set_doc_warning.setText(war_text)
    _set_doc_warning.setIcon(QMessageBox.Warning)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(war_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    _set_doc_warning.setWindowIcon(icon)
    _set_doc_warning.exec_()


def get_option(path, section, option):
    if not os.path.exists(path):
        create_new_config(path)
    else:
        config = cp.ConfigParser()
        config.read(path)
        if config.has_option(section, option):
            ret = config.get(section, option)
        else:
            ret = 'None||||None'
        return ret


def set_option(path, section, option, setting):
    if not os.path.exists(path):
        create_new_config(path)
    else:
        config = cp.ConfigParser()
        config.read(path)
        if config.has_section(section):
            config.set(section, option, setting)
        else:
            _add_section(path, section)
            config = cp.ConfigParser()
            config.read(path)
            config.set(section, option, setting)
        with open(path, "w") as config_file:
            config.write(config_file)


def _add_section(path, section):
    if os.path.exists(path):
        config = cp.ConfigParser()
        config.read(path)
        if config.has_section(section):
            # Section has already been added
            ret = "0"
        else:
            # Section add
            config.add_section(section)
            with open(path, "w") as config_file:
                config.write(config_file)
                config_file.close()
            ret = "1"
    else:
        # Config not found, create new config.ini
        ret = '2'
        create_new_config(path)
    return ret


def create_new_config(path):
    config = cp.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "account", r"None")
    config.set("Settings", "how_to_save", r"1")
    config.set("Settings", "how_to_save_folder", r"1")
    config.set("Settings", "version", version)
    config.set("Settings", "first_run", '1')
    with open(path, "w") as config_file:
        config.write(config_file)


def remove_option(path, section, option):
    config = cp.ConfigParser()
    config.read(path)
    config.remove_option(section, option)
    with open(path, "w") as config_file:
        config.write(config_file)


def search_game_saves_folders():
    ret_list = []
    disk_dir = os.getenv("SystemDrive")
    user = os.environ.get("USERNAME")
    listdir = os.listdir(r"{}\Users\{}\AppData\Roaming\DarkSoulsIII".format(disk_dir, user))
    for i in listdir:
        if '0110000' in i and len(i) == 16:
            ret_list.append(i)
    return ret_list


def version_controller(path="config.ini"):
    up_1_0_4(path)
    up_1_1_0()
    up_1_1_115()


def up_1_0_4(path):
    if os.path.exists(path):
        with open(conf_path) as config_file:
            config = config_file.read()
            config_file.close()

        config = config.replace(r'|/\|', '||||')
        config = config.replace('\nsave = ', '\ncurrent_save = ')
        config = config.replace('\nacc = ', '\naccount = ')

        with open(conf_path, 'w') as config_file:
            config_file.write(config)
            config_file.close()

        if get_option(path, "Settings", "version") == "None||||None":
            set_option(path, "Settings", "how_to_save", r"1")
            set_option(path, "Settings", "how_to_save_folder", r"1")
            set_option(path, "Settings", "version", version)
            set_option(path, "Settings", "first_run", '1')


def up_1_1_0():
    pass


def up_1_1_115():
    pass


def main_win_start():
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())


def main():
    main_win_start()


if __name__ == "__main__":
    conf_path = "config.ini"
    version = "1.3.0"
    version_controller(conf_path)
    if not os.path.exists(conf_path):
        create_new_config(conf_path)
    main()
