# Form implementation generated from reading ui file '.\delete-nan.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Delete_NaN(object):
    def setupUi(self, Dialog_Delete_NaN):
        Dialog_Delete_NaN.setObjectName("Dialog_Delete_NaN")
        Dialog_Delete_NaN.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        Dialog_Delete_NaN.resize(400, 200)
        Dialog_Delete_NaN.setMinimumSize(QtCore.QSize(400, 200))
        Dialog_Delete_NaN.setMaximumSize(QtCore.QSize(400, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        Dialog_Delete_NaN.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_Delete_NaN)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_Info = QtWidgets.QTextEdit(parent=Dialog_Delete_NaN)
        self.textEdit_Info.setStyleSheet("QTextEdit {\n"
                                         "    font-weight: bold;\n"
                                         "    font-size: 16px;\n"
                                         "}")
        self.textEdit_Info.setReadOnly(True)
        self.textEdit_Info.setObjectName("textEdit_Info")
        self.verticalLayout.addWidget(self.textEdit_Info)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Apply = QtWidgets.QPushButton(parent=Dialog_Delete_NaN)
        self.pushButton_Apply.setObjectName("pushButton_Apply")
        self.horizontalLayout.addWidget(self.pushButton_Apply)
        self.pushButton_Cancel = QtWidgets.QPushButton(parent=Dialog_Delete_NaN)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.horizontalLayout.addWidget(self.pushButton_Cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog_Delete_NaN)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Delete_NaN)

    def retranslateUi(self, Dialog_Delete_NaN):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Delete_NaN.setWindowTitle(_translate("Dialog_Delete_NaN", "Usuń NaN"))
        self.pushButton_Apply.setText(_translate("Dialog_Delete_NaN", "Zastosuj"))
        self.pushButton_Cancel.setText(_translate("Dialog_Delete_NaN", "Anuluj"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog_Delete_NaN = QtWidgets.QDialog()
    ui = Ui_Dialog_Delete_NaN()
    ui.setupUi(Dialog_Delete_NaN)
    Dialog_Delete_NaN.show()
    sys.exit(app.exec())