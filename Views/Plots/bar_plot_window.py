# Form implementation generated from reading ui file '.\bar-plot-window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Bar_Plot(object):
    def setupUi(self, MainWindow_Bar_Plot):
        MainWindow_Bar_Plot.setObjectName("MainWindow_Bar_Plot")
        MainWindow_Bar_Plot.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        MainWindow_Bar_Plot.resize(1200, 850)
        MainWindow_Bar_Plot.setMinimumSize(QtCore.QSize(1200, 850))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_Bar_Plot)
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
                                           QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(400, 0))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 383, 768))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.groupBox = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
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
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
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
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.toolButton_Estimator = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Estimator.setObjectName("toolButton_Estimator")
        self.horizontalLayout_9.addWidget(self.toolButton_Estimator)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.comboBox_Estimator = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_Estimator.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_Estimator.setObjectName("comboBox_Estimator")
        self.comboBox_Estimator.addItem("")
        self.comboBox_Estimator.addItem("")
        self.comboBox_Estimator.addItem("")
        self.comboBox_Estimator.addItem("")
        self.comboBox_Estimator.addItem("")
        self.comboBox_Estimator.addItem("")
        self.comboBox_Estimator.addItem("")
        self.verticalLayout_8.addWidget(self.comboBox_Estimator)
        self.verticalLayout_15.addLayout(self.verticalLayout_8)
        self.verticalLayout_13.addLayout(self.verticalLayout_15)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.toolButton_CI = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_CI.setObjectName("toolButton_CI")
        self.horizontalLayout_7.addWidget(self.toolButton_CI)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.spinBox_CI = QtWidgets.QSpinBox(parent=self.groupBox)
        self.spinBox_CI.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.spinBox_CI.setPrefix("")
        self.spinBox_CI.setMinimum(-1)
        self.spinBox_CI.setMaximum(100)
        self.spinBox_CI.setProperty("value", 95)
        self.spinBox_CI.setObjectName("spinBox_CI")
        self.verticalLayout_7.addWidget(self.spinBox_CI)
        self.verticalLayout_13.addLayout(self.verticalLayout_7)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_15.addWidget(self.label_12)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem8)
        self.toolButton_Orient = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Orient.setObjectName("toolButton_Orient")
        self.horizontalLayout_15.addWidget(self.toolButton_Orient)
        self.verticalLayout_17.addLayout(self.horizontalLayout_15)
        self.comboBox_Orient = QtWidgets.QComboBox(parent=self.groupBox)
        self.comboBox_Orient.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_Orient.setObjectName("comboBox_Orient")
        self.comboBox_Orient.addItem("")
        self.comboBox_Orient.addItem("")
        self.verticalLayout_17.addWidget(self.comboBox_Orient)
        self.verticalLayout_13.addLayout(self.verticalLayout_17)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
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
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem10)
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
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem11)
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
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem12)
        self.toolButton_Label_Y = QtWidgets.QToolButton(parent=self.groupBox)
        self.toolButton_Label_Y.setObjectName("toolButton_Label_Y")
        self.horizontalLayout_14.addWidget(self.toolButton_Label_Y)
        self.verticalLayout_11.addLayout(self.horizontalLayout_14)
        self.lineEdit_Label_Y = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit_Label_Y.setObjectName("lineEdit_Label_Y")
        self.verticalLayout_11.addWidget(self.lineEdit_Label_Y)
        self.verticalLayout_13.addLayout(self.verticalLayout_11)
        self.verticalLayout_16.addWidget(self.groupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                             QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_2.addItem(spacerItem13)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.widget_Plot = QtWidgets.QWidget(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
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
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem14)
        self.pushButton_Data_Preview = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Data_Preview.setObjectName("pushButton_Data_Preview")
        self.horizontalLayout_11.addWidget(self.pushButton_Data_Preview)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem15)
        self.pushButton_Add_To_Board = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Add_To_Board.setObjectName("pushButton_Add_To_Board")
        self.horizontalLayout_11.addWidget(self.pushButton_Add_To_Board)
        self.pushButton_Export = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Export.setObjectName("pushButton_Export")
        self.horizontalLayout_11.addWidget(self.pushButton_Export)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed,
                                             QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem16)
        self.pushButton_Close = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.horizontalLayout_11.addWidget(self.pushButton_Close)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        MainWindow_Bar_Plot.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_Bar_Plot)
        self.comboBox_Style.setCurrentIndex(-1)
        self.comboBox_Orient.setCurrentIndex(-1)
        self.comboBox_Estimator.setCurrentIndex(0)
        self.comboBox_Legend.setCurrentIndex(-1)
        self.pushButton_Close.clicked.connect(MainWindow_Bar_Plot.close)  # type: ignore
        self.toolButton_Data.clicked.connect(lambda: self.comboBox_Data.setCurrentIndex(-1))  # type: ignore
        self.toolButton_X.clicked.connect(lambda: self.comboBox_X.setCurrentIndex(-1))  # type: ignore
        self.toolButton_Y.clicked.connect(lambda: self.comboBox_Y.setCurrentIndex(-1))  # type: ignore
        self.toolButton_Hue.clicked.connect(lambda: self.comboBox_Hue.setCurrentIndex(-1))  # type: ignore
        self.toolButton_Title_Plot.clicked.connect(self.lineEdit_Title_Plot.clear)  # type: ignore
        self.toolButton_Style.clicked.connect(lambda: self.comboBox_Style.setCurrentIndex(-1))  # type: ignore
        self.toolButton_Label_X.clicked.connect(self.lineEdit_Label_X.clear)  # type: ignore
        self.toolButton_Legend.clicked.connect(lambda: self.comboBox_Legend.setCurrentIndex(-1))  # type: ignore
        self.toolButton_Label_Y.clicked.connect(self.lineEdit_Label_Y.clear)  # type: ignore
        self.toolButton_Estimator.clicked.connect(lambda: self.comboBox_Estimator.setCurrentIndex(0))  # type: ignore
        self.toolButton_CI.clicked.connect(lambda: self.spinBox_CI.setValue(95))  # type: ignore
        self.toolButton_Orient.clicked.connect(lambda: self.comboBox_Orient.setCurrentIndex(-1))  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Bar_Plot)

    def retranslateUi(self, MainWindow_Bar_Plot):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Bar_Plot.setWindowTitle(_translate("MainWindow_Bar_Plot", "Wykres słupkowy"))
        self.groupBox.setTitle(_translate("MainWindow_Bar_Plot", "Parametry:"))
        self.label.setText(_translate("MainWindow_Bar_Plot", "Zbiór danych:"))
        self.toolButton_Data.setText(_translate("MainWindow_Bar_Plot", "X"))
        self.comboBox_Data.setPlaceholderText(_translate("MainWindow_Bar_Plot", "Wybierz zbiór danych..."))
        self.label_2.setText(_translate("MainWindow_Bar_Plot", "Oś X:"))
        self.toolButton_X.setText(_translate("MainWindow_Bar_Plot", "X"))
        self.comboBox_X.setPlaceholderText(_translate("MainWindow_Bar_Plot", "Wybierz dane na osi x..."))
        self.label_3.setText(_translate("MainWindow_Bar_Plot", "Oś Y:"))
        self.toolButton_Y.setText(_translate("MainWindow_Bar_Plot", "X"))
        self.comboBox_Y.setPlaceholderText(_translate("MainWindow_Bar_Plot", "Wybierz dane na osi y..."))
        self.label_4.setText(_translate("MainWindow_Bar_Plot", "Grupowanie:"))
        self.toolButton_Hue.setText(_translate("MainWindow_Bar_Plot", "X"))
        self.comboBox_Hue.setPlaceholderText(
            _translate("MainWindow_Bar_Plot", "Wybierz dane według, których grupować..."))
        self.label_6.setText(_translate("MainWindow_Bar_Plot", "Odcień słupków:"))
        self.toolButton_Style.setText(_translate("MainWindow_Bar_Plot", "X"))
        self.comboBox_Style.setPlaceholderText(_translate("MainWindow_Bar_Plot", "Wybierz odcień słupków..."))
        self.comboBox_Style.setItemText(0, _translate("MainWindow_Bar_Plot", "deep"))
        self.comboBox_Style.setItemText(1, _translate("MainWindow_Bar_Plot", "muted"))
        self.comboBox_Style.setItemText(2, _translate("MainWindow_Bar_Plot", "bright"))
        self.comboBox_Style.setItemText(3, _translate("MainWindow_Bar_Plot", "pastel"))
        self.comboBox_Style.setItemText(4, _translate("MainWindow_Bar_Plot", "dark"))
        self.comboBox_Style.setItemText(5, _translate("MainWindow_Bar_Plot", "colorblind"))
        self.comboBox_Style.setItemText(6, _translate("MainWindow_Bar_Plot", "Reds"))
        self.comboBox_Style.setItemText(7, _translate("MainWindow_Bar_Plot", "Blues"))
        self.comboBox_Style.setItemText(8, _translate("MainWindow_Bar_Plot", "Greens"))
        self.comboBox_Style.setItemText(9, _translate("MainWindow_Bar_Plot", "Oranges"))
        self.comboBox_Style.setItemText(10, _translate("MainWindow_Bar_Plot", "Purples"))
        self.comboBox_Style.setItemText(11, _translate("MainWindow_Bar_Plot", "Greys"))
        self.comboBox_Style.setItemText(12, _translate("MainWindow_Bar_Plot", "Set1"))
        self.comboBox_Style.setItemText(13, _translate("MainWindow_Bar_Plot", "Set2"))
        self.comboBox_Style.setItemText(14, _translate("MainWindow_Bar_Plot", "Set3"))
        self.label_7.setText(_translate("MainWindow_Bar_Plot", "Estymator:"))
        self.toolButton_Estimator.setText(_translate("MainWindow_Bar_Plot", "X"))
        self.comboBox_Estimator.setPlaceholderText(_translate("MainWindow_Bar_Plot", "Wybierz estymator..."))
        self.comboBox_Estimator.setItemText(0, _translate("MainWindow_Bar_Plot", "mean"))
        self.comboBox_Estimator.setItemText(1, _translate("MainWindow_Bar_Plot", "sum"))
        self.comboBox_Estimator.setItemText(2, _translate("MainWindow_Bar_Plot", "median"))
        self.comboBox_Estimator.setItemText(3, _translate("MainWindow_Bar_Plot", "std"))
        self.comboBox_Estimator.setItemText(4, _translate("MainWindow_Bar_Plot", "min"))
        self.comboBox_Estimator.setItemText(5, _translate("MainWindow_Bar_Plot", "max"))
        self.comboBox_Estimator.setItemText(6, _translate("MainWindow_Bar_Plot", "var"))
        self.label_5.setText(_translate("MainWindow_Bar_Plot", "Przedział ufności:"))
        self.toolButton_CI.setText(_translate("MainWindow_Bar_Plot", "X"))
        self.spinBox_CI.setSuffix(_translate("MainWindow_Bar_Plot", " %"))
        self.label_12.setText(_translate("MainWindow_Bar_Plot", "Orientacja:"))
        self.toolButton_Orient.setText(_translate("MainWindow_Bar_Plot", "X"))
        self.comboBox_Orient.setPlaceholderText(_translate("MainWindow_Bar_Plot", "Wybierz orientacje słupków..."))
        self.comboBox_Orient.setItemText(0, _translate("MainWindow_Bar_Plot", "wertykalna"))
        self.comboBox_Orient.setItemText(1, _translate("MainWindow_Bar_Plot", "horyzontalna"))
        self.label_8.setText(_translate("MainWindow_Bar_Plot", "Legenda:"))
        self.toolButton_Legend.setText(_translate("MainWindow_Bar_Plot", "X"))
        self.comboBox_Legend.setPlaceholderText(
            _translate("MainWindow_Bar_Plot", "Wybierz opcje wyświetlania legendy..."))
        self.comboBox_Legend.setItemText(0, _translate("MainWindow_Bar_Plot", "auto"))
        self.comboBox_Legend.setItemText(1, _translate("MainWindow_Bar_Plot", "brief"))
        self.comboBox_Legend.setItemText(2, _translate("MainWindow_Bar_Plot", "full"))
        self.comboBox_Legend.setItemText(3, _translate("MainWindow_Bar_Plot", "Brak"))
        self.label_9.setText(_translate("MainWindow_Bar_Plot", "Tytuł wykresu:"))
        self.toolButton_Title_Plot.setText(_translate("MainWindow_Bar_Plot", "X"))
        self.label_10.setText(_translate("MainWindow_Bar_Plot", "Etykieta osi x:"))
        self.toolButton_Label_X.setText(_translate("MainWindow_Bar_Plot", "X"))
        self.label_11.setText(_translate("MainWindow_Bar_Plot", "Etykieta osi y:"))
        self.toolButton_Label_Y.setText(_translate("MainWindow_Bar_Plot", "X"))
        self.pushButton_Reset_Options.setText(_translate("MainWindow_Bar_Plot", "Resetuj"))
        self.pushButton_Generate_Plot.setText(_translate("MainWindow_Bar_Plot", "Generuj wykres"))
        self.pushButton_Data_Preview.setText(_translate("MainWindow_Bar_Plot", "Podgląd danych"))
        self.pushButton_Add_To_Board.setText(_translate("MainWindow_Bar_Plot", "Dodaj do tablicy"))
        self.pushButton_Export.setText(_translate("MainWindow_Bar_Plot", "Eksportuj"))
        self.pushButton_Close.setText(_translate("MainWindow_Bar_Plot", "Zamknij"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Bar_Plot = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Bar_Plot()
    ui.setupUi(MainWindow_Bar_Plot)
    MainWindow_Bar_Plot.show()
    sys.exit(app.exec())
