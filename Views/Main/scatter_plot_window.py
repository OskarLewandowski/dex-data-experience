# Form implementation generated from reading ui file '.\scatter-plot-window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Scatter_Plot(object):
    def setupUi(self, MainWindow_Scatter_Plot):
        MainWindow_Scatter_Plot.setObjectName("MainWindow_Scatter_Plot")
        MainWindow_Scatter_Plot.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        MainWindow_Scatter_Plot.resize(1142, 805)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_Scatter_Plot)
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
        self.toolButton_Data = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Data.setObjectName("toolButton_Data")
        self.horizontalLayout_3.addWidget(self.toolButton_Data)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.comboBox_Data = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_Data.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_Data.setObjectName("comboBox_Data")
        self.verticalLayout_3.addWidget(self.comboBox_Data)
        self.verticalLayout_13.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.toolButton_X = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_X.setObjectName("toolButton_X")
        self.horizontalLayout_4.addWidget(self.toolButton_X)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.comboBox_X = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_X.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_X.setObjectName("comboBox_X")
        self.verticalLayout.addWidget(self.comboBox_X)
        self.verticalLayout_13.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.toolButton_Y = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Y.setObjectName("toolButton_Y")
        self.horizontalLayout_5.addWidget(self.toolButton_Y)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.comboBox_Y = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_Y.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_Y.setObjectName("comboBox_Y")
        self.verticalLayout_5.addWidget(self.comboBox_Y)
        self.verticalLayout_13.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.toolButton_Hue = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Hue.setObjectName("toolButton_Hue")
        self.horizontalLayout_6.addWidget(self.toolButton_Hue)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.comboBox_Hue = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_Hue.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_Hue.setObjectName("comboBox_Hue")
        self.verticalLayout_6.addWidget(self.comboBox_Hue)
        self.verticalLayout_13.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.toolButton_Size = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Size.setObjectName("toolButton_Size")
        self.horizontalLayout_7.addWidget(self.toolButton_Size)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.comboBox_Size = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_Size.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_Size.setObjectName("comboBox_Size")
        self.verticalLayout_7.addWidget(self.comboBox_Size)
        self.verticalLayout_13.addLayout(self.verticalLayout_7)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.toolButton_Style = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Style.setObjectName("toolButton_Style")
        self.horizontalLayout_8.addWidget(self.toolButton_Style)
        self.verticalLayout_15.addLayout(self.horizontalLayout_8)
        self.comboBox_Style = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_Style.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_Style.setObjectName("comboBox_Style")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.comboBox_Style.addItem("")
        self.verticalLayout_15.addWidget(self.comboBox_Style)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.toolButton_Markers = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Markers.setObjectName("toolButton_Markers")
        self.horizontalLayout_9.addWidget(self.toolButton_Markers)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.comboBox_Markers = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_Markers.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_Markers.setObjectName("comboBox_Markers")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.comboBox_Markers.addItem("")
        self.verticalLayout_8.addWidget(self.comboBox_Markers)
        self.verticalLayout_15.addLayout(self.verticalLayout_8)
        self.verticalLayout_13.addLayout(self.verticalLayout_15)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.toolButton_Legend = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Legend.setObjectName("toolButton_Legend")
        self.horizontalLayout_10.addWidget(self.toolButton_Legend)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.comboBox_Legend = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_Legend.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_Legend.setObjectName("comboBox_Legend")
        self.comboBox_Legend.addItem("")
        self.comboBox_Legend.addItem("")
        self.comboBox_Legend.addItem("")
        self.comboBox_Legend.addItem("")
        self.verticalLayout_4.addWidget(self.comboBox_Legend)
        self.verticalLayout_13.addLayout(self.verticalLayout_4)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_12.addWidget(self.label_9)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem9)
        self.toolButton_Title_Plot = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Title_Plot.setObjectName("toolButton_Title_Plot")
        self.horizontalLayout_12.addWidget(self.toolButton_Title_Plot)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.lineEdit_Title_Plot = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_Title_Plot.setObjectName("lineEdit_Title_Plot")
        self.verticalLayout_9.addWidget(self.lineEdit_Title_Plot)
        self.verticalLayout_13.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem10)
        self.toolButton_Label_X = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Label_X.setObjectName("toolButton_Label_X")
        self.horizontalLayout_13.addWidget(self.toolButton_Label_X)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.lineEdit_Label_X = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_Label_X.setObjectName("lineEdit_Label_X")
        self.verticalLayout_10.addWidget(self.lineEdit_Label_X)
        self.verticalLayout_13.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_14.addWidget(self.label_11)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem11)
        self.toolButton_Label_Y = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Label_Y.setObjectName("toolButton_Label_Y")
        self.horizontalLayout_14.addWidget(self.toolButton_Label_Y)
        self.verticalLayout_11.addLayout(self.horizontalLayout_14)
        self.lineEdit_Label_Y = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_Label_Y.setObjectName("lineEdit_Label_Y")
        self.verticalLayout_11.addWidget(self.lineEdit_Label_Y)
        self.verticalLayout_13.addLayout(self.verticalLayout_11)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem12)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.widget_Plot = QtWidgets.QWidget(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_Plot.sizePolicy().hasHeightForWidth())
        self.widget_Plot.setSizePolicy(sizePolicy)
        self.widget_Plot.setObjectName("widget_Plot")
        self.verticalLayout_14.addWidget(self.widget_Plot)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout_12.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_Reset_Options = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Reset_Options.setObjectName("pushButton_Reset_Options")
        self.horizontalLayout_11.addWidget(self.pushButton_Reset_Options)
        self.pushButton_Generate_Plot = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Generate_Plot.setObjectName("pushButton_Generate_Plot")
        self.horizontalLayout_11.addWidget(self.pushButton_Generate_Plot)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem13)
        self.pushButton_Add_To_Board = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Add_To_Board.setObjectName("pushButton_Add_To_Board")
        self.horizontalLayout_11.addWidget(self.pushButton_Add_To_Board)
        self.pushButton_Export = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Export.setObjectName("pushButton_Export")
        self.horizontalLayout_11.addWidget(self.pushButton_Export)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem14)
        self.pushButton_Close = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.horizontalLayout_11.addWidget(self.pushButton_Close)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        MainWindow_Scatter_Plot.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_Scatter_Plot)
        self.comboBox_Style.setCurrentIndex(-1)
        self.comboBox_Markers.setCurrentIndex(-1)
        self.comboBox_Legend.setCurrentIndex(-1)
        self.pushButton_Close.clicked.connect(MainWindow_Scatter_Plot.close)  # type: ignore
        self.toolButton_Data.clicked.connect(lambda: self.comboBox_Data.setCurrentIndex(-1))  # type: ignore
        self.toolButton_X.clicked.connect(lambda: self.comboBox_X.setCurrentIndex(-1))  # type: ignore
        self.toolButton_Y.clicked.connect(lambda: self.comboBox_Y.setCurrentIndex(-1))  # type: ignore
        self.toolButton_Hue.clicked.connect(lambda: self.comboBox_Hue.setCurrentIndex(-1))  # type: ignore
        self.toolButton_Title_Plot.clicked.connect(self.lineEdit_Title_Plot.clear)  # type: ignore
        self.toolButton_Style.clicked.connect(lambda: self.comboBox_Style.setCurrentIndex(-1))  # type: ignore
        self.toolButton_Size.clicked.connect(lambda: self.comboBox_Size.setCurrentIndex(-1))  # type: ignore
        self.toolButton_Markers.clicked.connect(lambda: self.comboBox_Markers.setCurrentIndex(-1))  # type: ignore
        self.toolButton_Label_X.clicked.connect(self.lineEdit_Label_X.clear)  # type: ignore
        self.toolButton_Legend.clicked.connect(lambda: self.comboBox_Legend.setCurrentIndex(-1))  # type: ignore
        self.toolButton_Label_Y.clicked.connect(self.lineEdit_Label_Y.clear)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Scatter_Plot)

    def retranslateUi(self, MainWindow_Scatter_Plot):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Scatter_Plot.setWindowTitle(_translate("MainWindow_Scatter_Plot", "Wykres punktowy"))
        self.groupBox.setTitle(_translate("MainWindow_Scatter_Plot", "Parametry:"))
        self.label.setText(_translate("MainWindow_Scatter_Plot", "Zbiór danych:"))
        self.toolButton_Data.setText(_translate("MainWindow_Scatter_Plot", "X"))
        self.comboBox_Data.setPlaceholderText(_translate("MainWindow_Scatter_Plot", "Wybierz zbiór danych..."))
        self.label_2.setText(_translate("MainWindow_Scatter_Plot", "Oś X:"))
        self.toolButton_X.setText(_translate("MainWindow_Scatter_Plot", "X"))
        self.comboBox_X.setPlaceholderText(_translate("MainWindow_Scatter_Plot", "Wybierz dane na osi x..."))
        self.label_3.setText(_translate("MainWindow_Scatter_Plot", "Oś Y:"))
        self.toolButton_Y.setText(_translate("MainWindow_Scatter_Plot", "X"))
        self.comboBox_Y.setPlaceholderText(_translate("MainWindow_Scatter_Plot", "Wybierz dane na osi y..."))
        self.label_4.setText(_translate("MainWindow_Scatter_Plot", "Grupowanie:"))
        self.toolButton_Hue.setText(_translate("MainWindow_Scatter_Plot", "X"))
        self.comboBox_Hue.setPlaceholderText(
            _translate("MainWindow_Scatter_Plot", "Wybierz dane według, których grupować..."))
        self.label_5.setText(_translate("MainWindow_Scatter_Plot", "Rozmiar punktów:"))
        self.toolButton_Size.setText(_translate("MainWindow_Scatter_Plot", "X"))
        self.comboBox_Size.setPlaceholderText(
            _translate("MainWindow_Scatter_Plot", "Wybierz dane według, których ustalić rozmiar punktów..."))
        self.label_6.setText(_translate("MainWindow_Scatter_Plot", "Styl punktów:"))
        self.toolButton_Style.setText(_translate("MainWindow_Scatter_Plot", "X"))
        self.comboBox_Style.setPlaceholderText(_translate("MainWindow_Scatter_Plot", "Wybierz styl punktów..."))
        self.comboBox_Style.setItemText(0, _translate("MainWindow_Scatter_Plot", "deep"))
        self.comboBox_Style.setItemText(1, _translate("MainWindow_Scatter_Plot", "muted"))
        self.comboBox_Style.setItemText(2, _translate("MainWindow_Scatter_Plot", "bright"))
        self.comboBox_Style.setItemText(3, _translate("MainWindow_Scatter_Plot", "pastel"))
        self.comboBox_Style.setItemText(4, _translate("MainWindow_Scatter_Plot", "dark"))
        self.comboBox_Style.setItemText(5, _translate("MainWindow_Scatter_Plot", "colorblind"))
        self.comboBox_Style.setItemText(6, _translate("MainWindow_Scatter_Plot", "Reds"))
        self.comboBox_Style.setItemText(7, _translate("MainWindow_Scatter_Plot", "Blues"))
        self.comboBox_Style.setItemText(8, _translate("MainWindow_Scatter_Plot", "Greens"))
        self.comboBox_Style.setItemText(9, _translate("MainWindow_Scatter_Plot", "Oranges"))
        self.comboBox_Style.setItemText(10, _translate("MainWindow_Scatter_Plot", "Purples"))
        self.comboBox_Style.setItemText(11, _translate("MainWindow_Scatter_Plot", "Greys"))
        self.comboBox_Style.setItemText(12, _translate("MainWindow_Scatter_Plot", "Set1"))
        self.comboBox_Style.setItemText(13, _translate("MainWindow_Scatter_Plot", "Set2"))
        self.comboBox_Style.setItemText(14, _translate("MainWindow_Scatter_Plot", "Set3"))
        self.label_7.setText(_translate("MainWindow_Scatter_Plot", "Kształt punktów:"))
        self.toolButton_Markers.setText(_translate("MainWindow_Scatter_Plot", "X"))
        self.comboBox_Markers.setPlaceholderText(_translate("MainWindow_Scatter_Plot", "Wybierz kształt punktów..."))
        self.comboBox_Markers.setItemText(0, _translate("MainWindow_Scatter_Plot", "."))
        self.comboBox_Markers.setItemText(1, _translate("MainWindow_Scatter_Plot", ","))
        self.comboBox_Markers.setItemText(2, _translate("MainWindow_Scatter_Plot", "o"))
        self.comboBox_Markers.setItemText(3, _translate("MainWindow_Scatter_Plot", "v"))
        self.comboBox_Markers.setItemText(4, _translate("MainWindow_Scatter_Plot", "^"))
        self.comboBox_Markers.setItemText(5, _translate("MainWindow_Scatter_Plot", ">"))
        self.comboBox_Markers.setItemText(6, _translate("MainWindow_Scatter_Plot", "<"))
        self.comboBox_Markers.setItemText(7, _translate("MainWindow_Scatter_Plot", "+"))
        self.comboBox_Markers.setItemText(8, _translate("MainWindow_Scatter_Plot", "x"))
        self.comboBox_Markers.setItemText(9, _translate("MainWindow_Scatter_Plot", "s"))
        self.comboBox_Markers.setItemText(10, _translate("MainWindow_Scatter_Plot", "D"))
        self.comboBox_Markers.setItemText(11, _translate("MainWindow_Scatter_Plot", "-"))
        self.comboBox_Markers.setItemText(12, _translate("MainWindow_Scatter_Plot", "--"))
        self.comboBox_Markers.setItemText(13, _translate("MainWindow_Scatter_Plot", "|"))
        self.comboBox_Markers.setItemText(14, _translate("MainWindow_Scatter_Plot", ":"))
        self.comboBox_Markers.setItemText(15, _translate("MainWindow_Scatter_Plot", "*"))
        self.comboBox_Markers.setItemText(16, _translate("MainWindow_Scatter_Plot", "H"))
        self.comboBox_Markers.setItemText(17, _translate("MainWindow_Scatter_Plot", "X"))
        self.label_8.setText(_translate("MainWindow_Scatter_Plot", "Legenda:"))
        self.toolButton_Legend.setText(_translate("MainWindow_Scatter_Plot", "X"))
        self.comboBox_Legend.setPlaceholderText(
            _translate("MainWindow_Scatter_Plot", "Wybierz opcje wyświetlania legendy..."))
        self.comboBox_Legend.setItemText(0, _translate("MainWindow_Scatter_Plot", "auto"))
        self.comboBox_Legend.setItemText(1, _translate("MainWindow_Scatter_Plot", "brief"))
        self.comboBox_Legend.setItemText(2, _translate("MainWindow_Scatter_Plot", "full"))
        self.comboBox_Legend.setItemText(3, _translate("MainWindow_Scatter_Plot", "Brak"))
        self.label_9.setText(_translate("MainWindow_Scatter_Plot", "Tytuł wykresu:"))
        self.toolButton_Title_Plot.setText(_translate("MainWindow_Scatter_Plot", "X"))
        self.label_10.setText(_translate("MainWindow_Scatter_Plot", "Etykieta osi x:"))
        self.toolButton_Label_X.setText(_translate("MainWindow_Scatter_Plot", "X"))
        self.label_11.setText(_translate("MainWindow_Scatter_Plot", "Etykieta osi y:"))
        self.toolButton_Label_Y.setText(_translate("MainWindow_Scatter_Plot", "X"))
        self.pushButton_Reset_Options.setText(_translate("MainWindow_Scatter_Plot", "Resetuj"))
        self.pushButton_Generate_Plot.setText(_translate("MainWindow_Scatter_Plot", "Generuj wykres"))
        self.pushButton_Add_To_Board.setText(_translate("MainWindow_Scatter_Plot", "Dodaj do tablicy"))
        self.pushButton_Export.setText(_translate("MainWindow_Scatter_Plot", "Eksportuj"))
        self.pushButton_Close.setText(_translate("MainWindow_Scatter_Plot", "Zamknij"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Scatter_Plot = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Scatter_Plot()
    ui.setupUi(MainWindow_Scatter_Plot)
    MainWindow_Scatter_Plot.show()
    sys.exit(app.exec())
