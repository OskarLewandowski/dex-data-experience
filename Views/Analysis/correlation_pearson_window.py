# Form implementation generated from reading ui file '.\correlation-pearson-window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Correlation_Pearson(object):
    def setupUi(self, MainWindow_Correlation_Pearson):
        MainWindow_Correlation_Pearson.setObjectName("MainWindow_Correlation_Pearson")
        MainWindow_Correlation_Pearson.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        MainWindow_Correlation_Pearson.resize(1142, 878)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_Correlation_Pearson)
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
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.toolButton_Data_Column_2 = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Data_Column_2.setObjectName("toolButton_Data_Column_2")
        self.horizontalLayout_4.addWidget(self.toolButton_Data_Column_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.comboBox_Data_Column_2 = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_Data_Column_2.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_Data_Column_2.setObjectName("comboBox_Data_Column_2")
        self.verticalLayout_5.addWidget(self.comboBox_Data_Column_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.toolButton_Alternative = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Alternative.setObjectName("toolButton_Alternative")
        self.horizontalLayout_6.addWidget(self.toolButton_Alternative)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.comboBox_Alternative = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_Alternative.setObjectName("comboBox_Alternative")
        self.comboBox_Alternative.addItem("")
        self.comboBox_Alternative.addItem("")
        self.comboBox_Alternative.addItem("")
        self.verticalLayout.addWidget(self.comboBox_Alternative)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.toolButton_Confidence_Interval_Value = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Confidence_Interval_Value.setObjectName("toolButton_Confidence_Interval_Value")
        self.horizontalLayout_7.addWidget(self.toolButton_Confidence_Interval_Value)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.spinBox_Confidence_Interval_Value = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_Confidence_Interval_Value.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinBox_Confidence_Interval_Value.setPrefix("")
        self.spinBox_Confidence_Interval_Value.setMaximum(100)
        self.spinBox_Confidence_Interval_Value.setProperty("value", 95)
        self.spinBox_Confidence_Interval_Value.setObjectName("spinBox_Confidence_Interval_Value")
        self.verticalLayout_6.addWidget(self.spinBox_Confidence_Interval_Value)
        self.verticalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
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
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem6)
        self.verticalLayout_16.addLayout(self.horizontalLayout_15)
        self.checkBox_Board_Is_Enabled = QtWidgets.QCheckBox(parent=self.groupBox)
        self.checkBox_Board_Is_Enabled.setChecked(False)
        self.checkBox_Board_Is_Enabled.setObjectName("checkBox_Board_Is_Enabled")
        self.verticalLayout_16.addWidget(self.checkBox_Board_Is_Enabled)
        self.verticalLayout_13.addLayout(self.verticalLayout_16)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
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
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.textEdit_Preview_Board.setFont(font)
        self.textEdit_Preview_Board.setStyleSheet("QTextEdit{\n"
                                                  "font-size: 14pt;\n"
                                                  "font-family: \"Segoe UI\";\n"
                                                  "}")
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
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem8)
        self.pushButton_Data_Preview = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Data_Preview.setObjectName("pushButton_Data_Preview")
        self.horizontalLayout_11.addWidget(self.pushButton_Data_Preview)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem9)
        self.pushButton_Add_To_Board = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Add_To_Board.setObjectName("pushButton_Add_To_Board")
        self.horizontalLayout_11.addWidget(self.pushButton_Add_To_Board)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.pushButton_Close = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.horizontalLayout_11.addWidget(self.pushButton_Close)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        MainWindow_Correlation_Pearson.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_Correlation_Pearson)
        self.toolButton_Data_Column.clicked.connect(
            lambda: self.comboBox_Data_Column.setCurrentIndex(-1))  # type: ignore
        self.pushButton_Close.clicked.connect(MainWindow_Correlation_Pearson.close)  # type: ignore
        self.checkBox_Board_Is_Enabled.clicked['bool'].connect(
            lambda checked: self.textEdit_Preview_Board.setReadOnly(not checked))
        self.toolButton_Data_Column_2.clicked.connect(
            lambda: self.comboBox_Data_Column_2.setCurrentIndex(-1))  # type: ignore
        self.toolButton_Alternative.clicked.connect(
            lambda: self.comboBox_Alternative.setCurrentIndex(0))  # type: ignore
        self.toolButton_Confidence_Interval_Value.clicked.connect(
            lambda: self.spinBox_Confidence_Interval_Value.setValue(95))  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Correlation_Pearson)

    def retranslateUi(self, MainWindow_Correlation_Pearson):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Correlation_Pearson.setWindowTitle(
            _translate("MainWindow_Correlation_Pearson", "Korelacja Pearsona"))
        self.groupBox.setTitle(_translate("MainWindow_Correlation_Pearson", "Parametry:"))
        self.label.setText(_translate("MainWindow_Correlation_Pearson", "Zbiór danych 1:"))
        self.toolButton_Data_Column.setText(_translate("MainWindow_Correlation_Pearson", "X"))
        self.comboBox_Data_Column.setPlaceholderText(
            _translate("MainWindow_Correlation_Pearson", "Wybierz kolumne danych..."))
        self.label_2.setText(_translate("MainWindow_Correlation_Pearson", "Zbiór danych 2:"))
        self.toolButton_Data_Column_2.setText(_translate("MainWindow_Correlation_Pearson", "X"))
        self.comboBox_Data_Column_2.setPlaceholderText(
            _translate("MainWindow_Correlation_Pearson", "Wybierz kolumne danych..."))
        self.label_4.setText(_translate("MainWindow_Correlation_Pearson", "Alternatywa:"))
        self.toolButton_Alternative.setText(_translate("MainWindow_Correlation_Pearson", "X"))
        self.comboBox_Alternative.setItemText(0, _translate("MainWindow_Correlation_Pearson", "two-sided"))
        self.comboBox_Alternative.setItemText(1, _translate("MainWindow_Correlation_Pearson", "greater"))
        self.comboBox_Alternative.setItemText(2, _translate("MainWindow_Correlation_Pearson", "less"))
        self.label_5.setText(_translate("MainWindow_Correlation_Pearson", "Przedział ufności:"))
        self.toolButton_Confidence_Interval_Value.setText(_translate("MainWindow_Correlation_Pearson", "X"))
        self.spinBox_Confidence_Interval_Value.setSuffix(_translate("MainWindow_Correlation_Pearson", "%"))
        self.label_3.setText(_translate("MainWindow_Correlation_Pearson", "Opis wyników:"))
        self.checkBox_Description_Of_Results.setText(
            _translate("MainWindow_Correlation_Pearson", "Dodaj opis do interpretacji wyników"))
        self.label_12.setText(_translate("MainWindow_Correlation_Pearson", "Edycja podglądu:"))
        self.checkBox_Board_Is_Enabled.setText(_translate("MainWindow_Correlation_Pearson", "Odblokuj edycje tablicy"))
        self.textEdit_Preview_Board.setHtml(_translate("MainWindow_Correlation_Pearson",
                                                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                       "p, li { white-space: pre-wrap; }\n"
                                                       "hr { height: 1px; border-width: 0; }\n"
                                                       "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                       "li.checked::marker { content: \"\\2612\"; }\n"
                                                       "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
                                                       "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_Reset_Options.setText(_translate("MainWindow_Correlation_Pearson", "Resetuj"))
        self.pushButton_Data_Preview.setText(_translate("MainWindow_Correlation_Pearson", "Podgląd danych"))
        self.pushButton_Add_To_Board.setText(_translate("MainWindow_Correlation_Pearson", "Dodaj do tablicy"))
        self.pushButton_Close.setText(_translate("MainWindow_Correlation_Pearson", "Zamknij"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Correlation_Pearson = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Correlation_Pearson()
    ui.setupUi(MainWindow_Correlation_Pearson)
    MainWindow_Correlation_Pearson.show()
    sys.exit(app.exec())
