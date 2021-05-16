from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Save_over(object):
    def setupUi(self, Save_over):
        Save_over.setObjectName("Save_over")
        Save_over.resize(400, 250)
        self.vL_main = QtWidgets.QVBoxLayout(Save_over)
        self.vL_main.setObjectName("vL_main")

        self.main_quest = QtWidgets.QLabel(Save_over)
        self.vL_main.addWidget(self.main_quest)

        self.butt_box = QtWidgets.QWidget()
        self.vL_main.addWidget(self.butt_box)

        self.vL_butt_box = QtWidgets.QVBoxLayout(self.butt_box)
        self.vL_butt_box.setObjectName("vL_gr_box")

        self.overwrite = QtWidgets.QPushButton(self.butt_box)
        self.overwrite.setObjectName("overwrite")
        self.vL_butt_box.addWidget(self.overwrite)

        self.cancel = QtWidgets.QPushButton(self.butt_box)
        self.cancel.setObjectName("cancel")
        self.vL_butt_box.addWidget(self.cancel)

        self.retranslateUi(Save_over)
        QtCore.QMetaObject.connectSlotsByName(Save_over)

    def retranslateUi(self, Save_over):
        _translate = QtCore.QCoreApplication.translate
        Save_over.setWindowTitle(_translate("Save_over", "Save my Save"))
        self.main_quest.setText(_translate("Save_over", "Save over?"))
        self.overwrite.setText(_translate("Save_over", "Overwrite"))
        self.cancel.setText(_translate("Save_over", "Cancel"))
