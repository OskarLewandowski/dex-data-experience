from PyQt6.QtWidgets import QDialog, QMainWindow, QFontComboBox, QSpinBox, QAbstractSpinBox
from PyQt6 import QtGui, QtCore
from Models.data_storage_model import DataStorageModel
from Views.Settings.settings_main_window import Ui_Dialog_settings
from Views.Main.main_window import Ui_MainWindow_Main


class MainController(QMainWindow, Ui_MainWindow_Main):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # View
        self.addFontComboBoxToolBar()
        self.addSpinBoxToolBar()

        # Connections
        self.fontComboBox_Text_Font.currentFontChanged['QFont'].connect(self.textEdit_Board.setCurrentFont)
        self.spinBox_Text_Size.valueChanged['int'].connect(self.textEdit_Board.setFontPointSize)

        self.show()

    def addFontComboBoxToolBar(self):
        self.fontComboBox_Text_Font = QFontComboBox()
        self.fontComboBox_Text_Font.setEditable(False)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.fontComboBox_Text_Font.setCurrentFont(font)
        self.toolBar.addWidget(self.fontComboBox_Text_Font)

    def addSpinBoxToolBar(self):
        self.spinBox_Text_Size = QSpinBox()
        self.spinBox_Text_Size.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_Text_Size.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBox_Text_Size.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinBox_Text_Size.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBox_Text_Size.setMinimum(8)
        self.spinBox_Text_Size.setMaximum(72)
        self.spinBox_Text_Size.setProperty("value", 12)
        self.spinBox_Text_Size.setDisplayIntegerBase(10)
        self.toolBar.addWidget(self.spinBox_Text_Size)

    def changeFont(self, font):
        self.textEdit_Board.setCurrentFont(font)

    def createWindowSettings(self):
        """
        Create the settings window
        """
        self.window_settings = QDialog()
        self.window_settings_ui = Ui_Dialog_settings()
        self.window_settings_ui.setupUi(self.window_settings)
        self.window_settings.show()

    @staticmethod
    def printDataFrames():
        """
        Display data frames in memory
        !!! For test only !!!
        """
        keys = DataStorageModel.get_all_keys()
        for i in keys:
            print(DataStorageModel.get(i))
        print(keys)
