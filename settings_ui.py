from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(700, 450)
        self.vL_main = QtWidgets.QVBoxLayout(Settings)
        self.vL_main.setObjectName("vL_main")

        self.gr_box = QtWidgets.QGroupBox()
        self.vL_main.addWidget(self.gr_box)

        self.vL_gr_box = QtWidgets.QVBoxLayout(self.gr_box)
        self.vL_gr_box.setObjectName("vL_gr_box")

        self.radio_over = QtWidgets.QRadioButton()
        self.radio_over.setObjectName("radio_over")
        self.vL_gr_box.addWidget(self.radio_over)

        self.radio_ask = QtWidgets.QRadioButton()
        self.radio_ask.setObjectName("radio_ask")
        self.vL_gr_box.addWidget(self.radio_ask)

        self.radio_err = QtWidgets.QRadioButton()
        self.radio_err.setObjectName("radio_err")
        self.vL_gr_box.addWidget(self.radio_err)

        self.gr_box_folder = QtWidgets.QGroupBox()
        self.vL_main.addWidget(self.gr_box_folder)

        self.vL_gr_box_folder = QtWidgets.QVBoxLayout(self.gr_box_folder)
        self.vL_gr_box_folder.setObjectName("vL_gr_box_folder")

        self.radio_over_folder = QtWidgets.QRadioButton()
        self.radio_over_folder.setObjectName("radio_over_folder")
        self.vL_gr_box_folder.addWidget(self.radio_over_folder)

        self.radio_ask_folder = QtWidgets.QRadioButton()
        self.radio_ask_folder.setObjectName("radio_ask_folder")
        self.vL_gr_box_folder.addWidget(self.radio_ask_folder)

        self.radio_err_folder = QtWidgets.QRadioButton()
        self.radio_err_folder.setObjectName("radio_err_folder")
        self.vL_gr_box_folder.addWidget(self.radio_err_folder)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Save my Save"))
        self.gr_box.setTitle(_translate("Settings", "Actions when save names match"))
        self.gr_box_folder.setTitle(_translate("Settings", "Actions when folder names match"))
        self.radio_over.setText(_translate("Settings", "Overwrite"))
        self.radio_over_folder.setText(_translate("Settings", "Overwrite"))
        self.radio_ask.setText(_translate("Settings", "To ask"))
        self.radio_ask_folder.setText(_translate("Settings", "To ask"))
        self.radio_err.setText(_translate("Settings", "Issue an error"))
        self.radio_err_folder.setText(_translate("Settings", "Issue an error"))
