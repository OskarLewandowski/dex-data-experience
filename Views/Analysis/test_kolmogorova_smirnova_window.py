# Form implementation generated from reading ui file '.\test-kolmogorova-smirnova-window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Test_Kolomogorova_Smirnova(object):
    def setupUi(self, MainWindow_Test_Kolomogorova_Smirnova):
        MainWindow_Test_Kolomogorova_Smirnova.setObjectName("MainWindow_Test_Kolomogorova_Smirnova")
        MainWindow_Test_Kolomogorova_Smirnova.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        MainWindow_Test_Kolomogorova_Smirnova.resize(1142, 878)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_Test_Kolomogorova_Smirnova)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.toolButton_Data_Column = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Data_Column.setObjectName("toolButton_Data_Column")
        self.horizontalLayout_3.addWidget(self.toolButton_Data_Column)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.comboBox_Data_Column = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_Data_Column.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_Data_Column.setObjectName("comboBox_Data_Column")
        self.verticalLayout_3.addWidget(self.comboBox_Data_Column)
        self.verticalLayout_13.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.checkBox_Description_Of_Results = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox_Description_Of_Results.setObjectName("checkBox_Description_Of_Results")
        self.verticalLayout_4.addWidget(self.checkBox_Description_Of_Results)
        self.verticalLayout_13.addLayout(self.verticalLayout_4)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_15.addWidget(self.label_12)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem3)
        self.verticalLayout_16.addLayout(self.horizontalLayout_15)
        self.checkBox_Board_Is_Enabled = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox_Board_Is_Enabled.setChecked(False)
        self.checkBox_Board_Is_Enabled.setObjectName("checkBox_Board_Is_Enabled")
        self.verticalLayout_16.addWidget(self.checkBox_Board_Is_Enabled)
        self.verticalLayout_13.addLayout(self.verticalLayout_16)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.textEdit_Preview_Board = QtWidgets.QTextEdit(parent=self.frame)
        self.textEdit_Preview_Board.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_Preview_Board.sizePolicy().hasHeightForWidth())
        self.textEdit_Preview_Board.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_Preview_Board.setFont(font)
        self.textEdit_Preview_Board.setReadOnly(True)
        self.textEdit_Preview_Board.setObjectName("textEdit_Preview_Board")
        self.verticalLayout_14.addWidget(self.textEdit_Preview_Board)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout_12.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_Reset_Options = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Reset_Options.setObjectName("pushButton_Reset_Options")
        self.horizontalLayout_11.addWidget(self.pushButton_Reset_Options)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem5)
        self.pushButton_Add_To_Board = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Add_To_Board.setObjectName("pushButton_Add_To_Board")
        self.horizontalLayout_11.addWidget(self.pushButton_Add_To_Board)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.pushButton_Close = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.horizontalLayout_11.addWidget(self.pushButton_Close)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        MainWindow_Test_Kolomogorova_Smirnova.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_Test_Kolomogorova_Smirnova)
        self.toolButton_Data_Column.clicked.connect(
            lambda: self.comboBox_Data_Column.setCurrentIndex(-1))  # type: ignore
        self.pushButton_Close.clicked.connect(MainWindow_Test_Kolomogorova_Smirnova.close)  # type: ignore
        self.checkBox_Board_Is_Enabled.clicked['bool'].connect(
            lambda checked: self.textEdit_Preview_Board.setReadOnly(not checked))
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Test_Kolomogorova_Smirnova)

    def retranslateUi(self, MainWindow_Test_Kolomogorova_Smirnova):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Test_Kolomogorova_Smirnova.setWindowTitle(
            _translate("MainWindow_Test_Kolomogorova_Smirnova", "Test Kołomogorova-Smirnova"))
        self.groupBox.setTitle(_translate("MainWindow_Test_Kolomogorova_Smirnova", "Parametry:"))
        self.label.setText(_translate("MainWindow_Test_Kolomogorova_Smirnova", "Zbiór danych:"))
        self.toolButton_Data_Column.setText(_translate("MainWindow_Test_Kolomogorova_Smirnova", "X"))
        self.comboBox_Data_Column.setPlaceholderText(
            _translate("MainWindow_Test_Kolomogorova_Smirnova", "Wybierz kolumne danych..."))
        self.label_3.setText(_translate("MainWindow_Test_Kolomogorova_Smirnova", "Opis wyników:"))
        self.checkBox_Description_Of_Results.setText(
            _translate("MainWindow_Test_Kolomogorova_Smirnova", "Dodaj opis do interpretacji wyników"))
        self.label_12.setText(_translate("MainWindow_Test_Kolomogorova_Smirnova", "Edycja podglądu:"))
        self.checkBox_Board_Is_Enabled.setText(
            _translate("MainWindow_Test_Kolomogorova_Smirnova", "Odblokuj edycje tablicy"))
        self.textEdit_Preview_Board.setHtml(_translate("MainWindow_Test_Kolomogorova_Smirnova",
                                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "hr { height: 1px; border-width: 0; }\n"
                                                       "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                       "li.checked::marker { content: \"\\2612\"; }\n"
                                                       "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_Reset_Options.setText(_translate("MainWindow_Test_Kolomogorova_Smirnova", "Resetuj"))
        self.pushButton_Add_To_Board.setText(_translate("MainWindow_Test_Kolomogorova_Smirnova", "Dodaj do tablicy"))
        self.pushButton_Close.setText(_translate("MainWindow_Test_Kolomogorova_Smirnova", "Zamknij"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Test_Kolomogorova_Smirnova = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Test_Kolomogorova_Smirnova()
    ui.setupUi(MainWindow_Test_Kolomogorova_Smirnova)
    MainWindow_Test_Kolomogorova_Smirnova.show()
    sys.exit(app.exec())
