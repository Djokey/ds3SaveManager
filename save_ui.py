from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Save(object):
    def setupUi(self, Save):
        Save.setObjectName("Save")
        Save.resize(970, 638)
        self.vL_main = QtWidgets.QVBoxLayout(Save)
        self.vL_main.setObjectName("vL_main")

        self.pushButton_save = QtWidgets.QPushButton(Save)
        self.pushButton_save.setObjectName("pushButton_save")
        self.vL_main.addWidget(self.pushButton_save)

        self.checkBox_create_new_folder = QtWidgets.QCheckBox(Save)
        self.checkBox_create_new_folder.setObjectName("checkBox_create_new_folder")
        self.vL_main.addWidget(self.checkBox_create_new_folder)

        self.label_name_folder = QtWidgets.QLabel(Save)
        self.label_name_folder.setObjectName("label_name_folder")
        self.vL_main.addWidget(self.label_name_folder)

        self.lineEdit_name_folder = QtWidgets.QLineEdit(Save)
        self.lineEdit_name_folder.setObjectName("lineEdit_name_folder")
        self.vL_main.addWidget(self.lineEdit_name_folder)

        self.label_name_saves = QtWidgets.QLabel(Save)
        self.label_name_saves.setObjectName("label_name_saves")
        self.vL_main.addWidget(self.label_name_saves)

        self.lineEdit_name_saves = QtWidgets.QLineEdit(Save)
        self.lineEdit_name_saves.setObjectName("lineEdit_name_saves")
        self.vL_main.addWidget(self.lineEdit_name_saves)

        self.label_selected_folder = QtWidgets.QLabel(Save)
        self.label_selected_folder.setObjectName("label_selected_folder")
        self.vL_main.addWidget(self.label_selected_folder)

        self.widget_for_saves = QtWidgets.QWidget(Save)
        self.widget_for_saves.setObjectName(u"widget_for_saves")
        self.hL_widget_for_saves = QtWidgets.QHBoxLayout(self.widget_for_saves)
        self.hL_widget_for_saves.setObjectName(u"hL_widget_for_saves")
        self.hL_widget_for_saves.setContentsMargins(0, 0, 0, 0)
        self.vL_main.addWidget(self.widget_for_saves)

        self.scrollArea_saves_folders = QtWidgets.QScrollArea(Save)
        self.scrollArea_saves_folders.setWidgetResizable(True)
        self.scrollArea_saves_folders.setObjectName("scrollArea_saves_folders")
        self.sAWC_folders = QtWidgets.QWidget()
        self.sAWC_folders.setGeometry(QtCore.QRect(0, 0, 950, 428))
        self.sAWC_folders.setObjectName("sAWC_folders")
        self.vL_sAWC_folders = QtWidgets.QVBoxLayout(self.sAWC_folders)
        self.vL_sAWC_folders.setObjectName("vL_sAWC_folders")
        self.scrollArea_saves_folders.setWidget(self.sAWC_folders)
        self.hL_widget_for_saves.addWidget(self.scrollArea_saves_folders)

        self.scrollArea_saves_saves = QtWidgets.QScrollArea(Save)
        self.scrollArea_saves_saves.setWidgetResizable(True)
        self.scrollArea_saves_saves.setObjectName("scrollArea_saves_saves")
        self.sAWC_saves = QtWidgets.QWidget()
        self.sAWC_saves.setGeometry(QtCore.QRect(0, 0, 950, 428))
        self.sAWC_saves.setObjectName("sAWC_saves")
        self.vL_sAWC_saves = QtWidgets.QVBoxLayout(self.sAWC_saves)
        self.vL_sAWC_saves.setObjectName("vL_sAWC_saves")
        self.scrollArea_saves_saves.setWidget(self.sAWC_saves)
        self.hL_widget_for_saves.addWidget(self.scrollArea_saves_saves)

        self.pushButton_back = QtWidgets.QPushButton(Save)
        self.pushButton_back.setObjectName("pushButton_back")
        self.vL_main.addWidget(self.pushButton_back)

        self.retranslateUi(Save)
        QtCore.QMetaObject.connectSlotsByName(Save)

    def retranslateUi(self, Save):
        _translate = QtCore.QCoreApplication.translate
        Save.setWindowTitle(_translate("Save", "Save my Save"))
        self.pushButton_save.setText(_translate("Save", "Save"))
        self.checkBox_create_new_folder.setText(_translate("Save", "Create new Saves folder"))
        self.label_name_folder.setText(_translate("Save", "Name for new folder:"))
        self.label_name_saves.setText(_translate("Save", "Name for my new Save:"))
        self.label_selected_folder.setText(_translate("Save", "Select folder for Save:"))
        self.pushButton_back.setText(_translate("Save", "Back"))
