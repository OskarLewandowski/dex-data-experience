# Form implementation generated from reading ui file 'dialog-search.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Search(object):
    def setupUi(self, Dialog_Search):
        Dialog_Search.setObjectName("Dialog_Search")
        Dialog_Search.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        Dialog_Search.resize(500, 100)
        Dialog_Search.setMinimumSize(QtCore.QSize(500, 100))
        Dialog_Search.setMaximumSize(QtCore.QSize(500, 100))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        Dialog_Search.setWindowIcon(icon)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog_Search)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog_Search)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_Search_Text = QtWidgets.QLineEdit(parent=Dialog_Search)
        self.lineEdit_Search_Text.setObjectName("lineEdit_Search_Text")
        self.horizontalLayout.addWidget(self.lineEdit_Search_Text)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.checkBox_Case = QtWidgets.QCheckBox(parent=Dialog_Search)
        self.checkBox_Case.setObjectName("checkBox_Case")
        self.verticalLayout_2.addWidget(self.checkBox_Case)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_Search = QtWidgets.QPushButton(parent=Dialog_Search)
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.verticalLayout.addWidget(self.pushButton_Search)
        self.pushButton_Clear = QtWidgets.QPushButton(parent=Dialog_Search)
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.verticalLayout.addWidget(self.pushButton_Clear)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog_Search)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Search)

    def retranslateUi(self, Dialog_Search):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Search.setWindowTitle(_translate("Dialog_Search", "Szukaj"))
        self.label.setText(_translate("Dialog_Search", "Szukany tekst:"))
        self.checkBox_Case.setText(_translate("Dialog_Search", "Uwzględnij wielkość liter"))
        self.pushButton_Search.setText(_translate("Dialog_Search", "Znajdź"))
        self.pushButton_Clear.setText(_translate("Dialog_Search", "Anuluj"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog_Search = QtWidgets.QDialog()
    ui = Ui_Dialog_Search()
    ui.setupUi(Dialog_Search)
    Dialog_Search.show()
    sys.exit(app.exec())
