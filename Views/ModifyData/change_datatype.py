# Form implementation generated from reading ui file '.\change-datatype.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Change_Datatype(object):
    def setupUi(self, Dialog_Change_Datatype):
        Dialog_Change_Datatype.setObjectName("Dialog_Change_Datatype")
        Dialog_Change_Datatype.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        Dialog_Change_Datatype.resize(400, 150)
        Dialog_Change_Datatype.setMinimumSize(QtCore.QSize(400, 150))
        Dialog_Change_Datatype.setMaximumSize(QtCore.QSize(400, 150))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        Dialog_Change_Datatype.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_Change_Datatype)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_Current_Datatype = QtWidgets.QComboBox(parent=Dialog_Change_Datatype)
        self.comboBox_Current_Datatype.setObjectName("comboBox_Current_Datatype")
        self.verticalLayout.addWidget(self.comboBox_Current_Datatype)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.comboBox_New_Datatype = QtWidgets.QComboBox(parent=Dialog_Change_Datatype)
        self.comboBox_New_Datatype.setObjectName("comboBox_New_Datatype")
        self.verticalLayout.addWidget(self.comboBox_New_Datatype)
        self.label_Info = QtWidgets.QLabel(parent=Dialog_Change_Datatype)
        self.label_Info.setText("")
        self.label_Info.setObjectName("label_Info")
        self.verticalLayout.addWidget(self.label_Info)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Apply = QtWidgets.QPushButton(parent=Dialog_Change_Datatype)
        self.pushButton_Apply.setObjectName("pushButton_Apply")
        self.horizontalLayout.addWidget(self.pushButton_Apply)
        self.pushButton_Cancel = QtWidgets.QPushButton(parent=Dialog_Change_Datatype)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.horizontalLayout.addWidget(self.pushButton_Cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog_Change_Datatype)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Change_Datatype)

    def retranslateUi(self, Dialog_Change_Datatype):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Change_Datatype.setWindowTitle(_translate("Dialog_Change_Datatype", "Zmień typ danych"))
        self.comboBox_Current_Datatype.setPlaceholderText(
            _translate("Dialog_Change_Datatype", "Wybierz kolumnę do zmiany typu danych..."))
        self.comboBox_New_Datatype.setPlaceholderText(_translate("Dialog_Change_Datatype", "Wybierz typ danych..."))
        self.pushButton_Apply.setText(_translate("Dialog_Change_Datatype", "Zastosuj"))
        self.pushButton_Cancel.setText(_translate("Dialog_Change_Datatype", "Anuluj"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog_Change_Datatype = QtWidgets.QDialog()
    ui = Ui_Dialog_Change_Datatype()
    ui.setupUi(Dialog_Change_Datatype)
    Dialog_Change_Datatype.show()
    sys.exit(app.exec())