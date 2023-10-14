import json
import os
import pandas as pd
from PyQt6.QtWidgets import QDialog, QMainWindow, QFontComboBox, QSpinBox, QAbstractSpinBox, QFileDialog, QMessageBox
from PyQt6 import QtGui, QtCore
from Models.data_storage_model import DataStorageModel
from Views.Settings.settings_main_window import Ui_Dialog_settings
from Views.Main.main_window import Ui_MainWindow_Main
from io import StringIO
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


class MainController(QMainWindow, Ui_MainWindow_Main):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Variable
        self.pathCurrentFileGlobal = None

        # View
        self.addFontComboBoxToolBar()
        self.addSpinBoxToolBar()

        # Connections
        self.fontComboBox_Text_Font.currentFontChanged['QFont'].connect(self.textEdit_Board.setCurrentFont)
        self.spinBox_Text_Size.valueChanged['int'].connect(self.textEdit_Board.setFontPointSize)
        self.action_Save.triggered.connect(self.saveChanges)
        self.action_Save_As_New.triggered.connect(self.saveProjectNew)
        self.action_Open_File.triggered.connect(self.openFile)
        self.action_New_File.triggered.connect(self.newProject)
        self.action_Print.triggered.connect(self.printBoard)
        self.action_Print_Preview.triggered.connect(self.printPreviewBoard)
        self.action_Exit.triggered.connect(self.close)
        self.show()

    def closeEvent(self, a0):
        result = self.exitApp()

        if result == 1:
            self.saveChanges()
            a0.accept()
        elif result == 2:
            a0.accept()
        else:
            a0.ignore()

    def exitApp(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText('Nie zapisane zmiany zostaną utracone!\n\nCzy na pewno chcesz zamknąć program?')
        msg.setWindowTitle('Zamknij program')

        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Abort)
        msg.button(QMessageBox.StandardButton.Yes).setText('Zapisz i zakończ')
        msg.button(QMessageBox.StandardButton.No).setText('Nie zapisuj i zakończ')
        msg.button(QMessageBox.StandardButton.Abort).setText('Anuluj')

        reply = msg.exec()

        if reply == QMessageBox.StandardButton.Yes:
            return 1
        elif reply == QMessageBox.StandardButton.No:
            return 2
        else:
            return 3

    def printPreviewBoard(self):
        try:
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            ui_printer = QPrintPreviewDialog(printer, self)
            ui_printer.paintRequested.connect(self.paintBoard)
            ui_printer.showMaximized()
            ui_printer.setWindowTitle("Podgląd wydruku")
            ui_printer.exec()
        except Exception as e:
            self.errorMessage("0011", str(e))

    def paintBoard(self, printer):
        self.textEdit_Board.print(printer)

    def printBoard(self):
        try:
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            ui_printer = QPrintDialog(printer)

            if ui_printer.exec() == QPrintDialog.DialogCode.Accepted:
                self.textEdit_Board.print(printer)
        except Exception as e:
            self.errorMessage("0010", str(e))

    def newProject(self):
        if self.notSavedProject():
            self.pathCurrentFileGlobal = None
            self.setWindowTitle("Dex")
            self.textEdit_Board.clear()
            DataStorageModel.clear()
        else:
            pass

    def notSavedProject(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText('Czy chcesz zapisać projekt?')
        msg.setWindowTitle('Nowy projekt')

        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Abort)
        msg.button(QMessageBox.StandardButton.Yes).setText('Zapisz')
        msg.button(QMessageBox.StandardButton.No).setText('Nie zapisuj')
        msg.button(QMessageBox.StandardButton.Abort).setText('Anuluj')

        reply = msg.exec()

        if reply == QMessageBox.StandardButton.Yes:
            self.saveChanges()
            return True
        elif reply == QMessageBox.StandardButton.No:
            return True
        else:
            return False

    def openFile(self):
        try:
            fileFilter = 'Plik Dex (*.dex)'
            fileName = QFileDialog.getOpenFileName(
                caption="Wczytaj projekt",
                directory=os.path.expanduser("~/Desktop/"),
                filter=fileFilter,
                initialFilter="Plik Dex (*.dex)"
            )

            if fileName[0]:
                text_data = ""
                data_frames = {}

                with open(fileName[0], "r") as file:
                    data = json.load(file)

                text_data = data.get("text_data", "")
                self.textEdit_Board.setHtml(text_data)

                data_frames = data.get("data_frames", {})

                for key, jsonData in data_frames.items():
                    df = pd.read_json(StringIO(jsonData), orient="split")
                    DataStorageModel.add(key, df)

                self.setSavedFilePath(fileName[0])

        except Exception as e:
            self.errorMessage("0009", str(e))

    def saveChanges(self):
        try:
            file = self.pathCurrentFileGlobal
            if file:
                self.save(self.pathCurrentFileGlobal)
            else:
                self.saveProjectNew()
        except Exception as e:
            self.errorMessage("0008", str(e))

    def saveProjectNew(self):
        try:
            fileFilter = 'Plik Dex (*.dex);;Wszystkie pliki (*.*)'

            fileName = QFileDialog.getSaveFileName(
                caption="Zapisz nowy projekt",
                directory=os.path.expanduser("~/Desktop/" + "nowy.dex"),
                filter=fileFilter,
                initialFilter="Plik Dex (*.dex)"
            )

            if fileName[0]:
                self.save(fileName[0])

        except Exception as e:
            self.errorMessage("0007", str(e))

    def save(self, filePath):
        try:
            dataFramesDictionary = DataStorageModel.copy()
            dataBoard = self.textEdit_Board.toHtml()
            dataFramesJson = {}
            dataToSave = {}

            if dataBoard:
                dataToSave["text_data"] = dataBoard

            if dataFramesDictionary:
                for key, df in dataFramesDictionary.items():
                    dataFramesJson[key] = df.to_json(index=False, orient="split")

                dataToSave["data_frames"] = dataFramesJson

            if filePath:
                with open(filePath, "w") as file:
                    json.dump(dataToSave, file)

            self.setSavedFilePath(filePath)


        except Exception as e:
            self.errorMessage("0006", str(e))

    def setSavedFilePath(self, filePath):
        newWindowTitle = "{} - Dex".format(filePath)
        self.setWindowTitle(newWindowTitle)
        self.pathCurrentFileGlobal = filePath

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

    @staticmethod
    def errorMessage(errorCode="0000", e=""):
        message = "Wystąpił bład: [{0}] - {1}".format(errorCode, e)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(message)
        msg.setWindowTitle('Błąd')

        msg.setStandardButtons(QMessageBox.StandardButton.Close)
        msg.button(QMessageBox.StandardButton.Close).setText('Zamknij')
        reply = msg.exec()

        return reply == QMessageBox.StandardButton.Close
