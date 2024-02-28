# Form implementation generated from reading ui file '.\about-app.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_About_App(object):
    def setupUi(self, Dialog_About_App):
        Dialog_About_App.setObjectName("Dialog_About_App")
        Dialog_About_App.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Dialog_About_App.resize(600, 650)
        Dialog_About_App.setMinimumSize(QtCore.QSize(600, 650))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog_About_App)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_Board = QtWidgets.QTextEdit(parent=Dialog_About_App)
        self.textEdit_Board.setEnabled(True)
        self.textEdit_Board.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_Board.setReadOnly(True)
        self.textEdit_Board.setObjectName("textEdit_Board")
        self.horizontalLayout.addWidget(self.textEdit_Board)

        self.retranslateUi(Dialog_About_App)
        QtCore.QMetaObject.connectSlotsByName(Dialog_About_App)

    def retranslateUi(self, Dialog_About_App):
        project_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        image_directory = os.path.join(project_directory, "images")
        image_filename = "app-icon/dex-icon-192x192.png"
        image_path = os.path.join(image_directory, image_filename)

        _translate = QtCore.QCoreApplication.translate
        Dialog_About_App.setWindowTitle(_translate("Dialog_About_App", "O programie"))
        self.textEdit_Board.setHtml(_translate("Dialog_About_App",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "hr { height: 1px; border-width: 0; }\n"
                                               "li.unchecked::marker { content: \"\\2610\"; }\n"
                                               "li.checked::marker { content: \"\\2612\"; }\n"
                                               "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    </p>\n"
                                               f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"{image_path}\" /></p>\n"
                                               "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:700; font-style:italic;\">Dex</span></p>\n"
                                               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Projekt magisterski na kierunku &quot;Analiza i przetwarzanie danych&quot; skupia się na opracowaniu aplikacji, umożliwiającej analizę danych poprzez interaktywne środowisko graficzne.</span></p>\n"
                                               "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
                                               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:700; font-style:italic;\">Autor</span></p>\n"
                                               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Oskar Lewandowski</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog_About_App = QtWidgets.QDialog()
    ui = Ui_Dialog_About_App()
    ui.setupUi(Dialog_About_App)
    Dialog_About_App.show()
    sys.exit(app.exec())
