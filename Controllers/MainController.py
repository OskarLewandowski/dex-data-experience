from Views.Main.about_app import Ui_Dialog_About_App
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt, QFile
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QDialog, QMainWindow, QFontComboBox, QSpinBox, QAbstractSpinBox, QFileDialog, QToolButton, \
    QFontDialog, QColorDialog, QLabel, QApplication
from Views.Main.rename_key_dataframe import Ui_Dialog_Rename_Key_Dataframe
from Views.Main.delete_dataframe import Ui_Dialog_Delete_Dataframe
from Models.data_storage_model import DataStorageModel
from Models.message_model import MessageModel
from Views.Main.main_window import Ui_MainWindow_Main
from Views.Main.data_preview import Ui_MainWindow_Data_Preview
from Models.data_frame_model import DataFrameModel
from Views.Main.guide_window import Ui_MainWindow_Guide
from io import StringIO
import pandas as pd
import json
import sys
import os


class MainController(QMainWindow, Ui_MainWindow_Main):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.showMaximized()

        # Variable
        self.pathCurrentFileGlobal = None
        self.selectedDataNameForDataPreviewGlobal = None

        # View
        self.addFontComboBoxToolBar()
        self.addSpinBoxToolBar()
        self.addColorToolButtonToolBar()
        self.addLabelToStatusBar()

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

        self.action_Undo.triggered.connect(self.textEdit_Board.undo)
        self.action_Redo.triggered.connect(self.textEdit_Board.redo)
        self.action_Copy.triggered.connect(self.textEdit_Board.copy)
        self.action_Cut.triggered.connect(self.textEdit_Board.cut)
        self.action_Paste.triggered.connect(self.textEdit_Board.paste)

        self.action_Bold.triggered.connect(self.toggleTextBold)
        self.action_Italic.triggered.connect(self.toggleTextItalic)
        self.action_Underline.triggered.connect(self.toggleTextUnderline)

        self.action_Right.triggered.connect(self.alignTextRight)
        self.action_Left.triggered.connect(self.alignTextLeft)
        self.action_Center.triggered.connect(self.alignTextCenter)
        self.action_Justify.triggered.connect(self.alignTextJustify)

        self.action_Font.triggered.connect(self.fontDialog)
        self.action_Color.triggered.connect(self.colorDialog)
        self.toolButtonColor.clicked.connect(self.colorDialog)
        self.textEdit_Board.cursorPositionChanged.connect(self.updateTextEdit)

        self.action_Export_As.triggered.connect(self.exportAs)
        self.action_Change_Data_Name.triggered.connect(self.createRenameKeyDataframeWindow)
        self.action_Delete_Dataframe.triggered.connect(self.createDeleteDataframeWindow)
        self.action_Data_Preview.triggered.connect(self.createDataPreviewWindow)

        self.action_Guide.triggered.connect(self.createGuideWindow)

        self.show()

    def addIconsToActions(self, color="black"):
        self.action_New_File.setIcon(self.resourceIcon(f"images/main-window-{color}/new-file.svg"))
        self.action_Open_File.setIcon(self.resourceIcon(f"images/main-window-{color}/open-file.svg"))
        self.action_Save.setIcon(self.resourceIcon(f"images/main-window-{color}/save-file.svg"))
        self.action_Print.setIcon(self.resourceIcon(f"images/main-window-{color}/print.svg"))
        self.action_Export_As.setIcon(self.resourceIcon(f"images/main-window-{color}/export-pdf.svg"))
        self.action_Exit.setIcon(self.resourceIcon(f"images/main-window-{color}/exit-red.svg"))
        self.action_Undo.setIcon(self.resourceIcon(f"images/main-window-{color}/undo-transparent.svg"))
        self.action_Redo.setIcon(self.resourceIcon(f"images/main-window-{color}/redo-transparent.svg"))
        self.action_Add_Data.setIcon(self.resourceIcon(f"images/main-window-{color}/add-data.svg"))
        self.action_Modify_Data.setIcon(self.resourceIcon(f"images/main-window-{color}/data-processing-1.svg"))
        self.action_Bold.setIcon(self.resourceIcon(f"images/main-window-{color}/bold.svg"))
        self.action_Italic.setIcon(self.resourceIcon(f"images/main-window-{color}/italic.svg"))
        self.action_Underline.setIcon(self.resourceIcon(f"images/main-window-{color}/underline.svg"))
        self.action_Left.setIcon(self.resourceIcon(f"images/main-window-{color}/text-left.svg"))
        self.action_Right.setIcon(self.resourceIcon(f"images/main-window-{color}/text-right.svg"))
        self.action_Center.setIcon(self.resourceIcon(f"images/main-window-{color}/text-center.svg"))
        self.action_Justify.setIcon(self.resourceIcon(f"images/main-window-{color}/text-justify.svg"))
        self.action_About_Application.setIcon(self.resourceIcon(f"images/main-window-{color}/mw-help.svg"))
        self.action_Settings.setIcon(self.resourceIcon(f"images/main-window-{color}/mw-settings.svg"))

    def resourceIcon(self, path):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(self.resourcePath(path)), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        return icon

    def resourcePath(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def addLabelToStatusBar(self):
        # dataframe count
        self.dataframeCount = QLabel("   Brak zbiorów danych")
        self.statusbar.setStyleSheet("QStatusBar::item { border: none; }")
        self.statusbar.addWidget(self.dataframeCount)

    def updateStatusBar(self):
        newValue = DataStorageModel.count_dataframes()

        if newValue > 0:
            self.dataframeCount.setText(f"   Liczba zbiorów danych: {newValue}")
        else:
            self.dataframeCount.setText(f"   Brak zbiorów danych")

    def createDeleteDataframeWindow(self):
        self.window_delete_dataframe = QDialog()
        self.window_delete_dataframe_ui = Ui_Dialog_Delete_Dataframe()
        self.window_delete_dataframe_ui.setupUi(self.window_delete_dataframe)

        dataKeys = DataStorageModel.get_all_keys()

        self.window_delete_dataframe_ui.comboBox_Keys_List.addItems(dataKeys)
        self.window_delete_dataframe_ui.pushButton_Apply.clicked.connect(self.deleteDataframe)

        self.window_delete_dataframe.show()

    def deleteDataframe(self):
        try:
            dfKey = self.window_delete_dataframe_ui.comboBox_Keys_List.currentText()

            if dfKey:
                DataStorageModel.remove(dfKey)
                msg = f"Zbiór danych '{dfKey}' został pomyślnie usunięty"
                self.window_delete_dataframe_ui.label_info_text_delete_dataframe.setText(msg)

                self.updateStatusBar()

            else:
                msg = f"Nie wybrano zbioru danych do usunięcia"
                self.window_delete_dataframe_ui.label_info_text_delete_dataframe.setText(msg)

            dataKeys = DataStorageModel.get_all_keys()
            self.window_delete_dataframe_ui.comboBox_Keys_List.clear()
            self.window_delete_dataframe_ui.comboBox_Keys_List.addItems(dataKeys)

        except Exception as e:
            MessageModel.error("0031", str(e))

    def createRenameKeyDataframeWindow(self):
        self.window_rename_key_dataframe = QDialog()
        self.window_rename_key_dataframe_ui = Ui_Dialog_Rename_Key_Dataframe()
        self.window_rename_key_dataframe_ui.setupUi(self.window_rename_key_dataframe)

        dataKeys = DataStorageModel.get_all_keys()

        self.window_rename_key_dataframe_ui.comboBox_Keys_List.addItems(dataKeys)
        self.window_rename_key_dataframe_ui.pushButton_Apply.clicked.connect(self.renameKeyDataframe)

        self.window_rename_key_dataframe.show()

    def updateKeysList(self):
        dataKeys = DataStorageModel.get_all_keys()
        self.window_rename_key_dataframe_ui.comboBox_Keys_List.clear()
        self.window_rename_key_dataframe_ui.comboBox_Keys_List.addItems(dataKeys)

    def renameKeyDataframe(self):
        try:
            oldKey = self.window_rename_key_dataframe_ui.comboBox_Keys_List.currentText()
            newKey = self.window_rename_key_dataframe_ui.lineEdit_New_Key_Name.text()

            if ":" in newKey:
                self.window_rename_key_dataframe_ui.label_info_text.setText("Nazwa nie może zawierać ':'")
            else:
                if oldKey != "" and newKey != "":
                    if DataStorageModel.rename_key(oldKey, newKey):
                        msg = f"Nazwa zbioru '{oldKey}' została zmienniona na '{newKey}'"
                        self.window_rename_key_dataframe_ui.label_info_text.setText(msg)

                        self.updateKeysList()
                        self.window_rename_key_dataframe_ui.lineEdit_New_Key_Name.clear()

                    else:
                        self.window_rename_key_dataframe_ui.label_info_text.setText(
                            f"Nazwa zbioru '{newKey}' już istnieje")
                else:
                    self.window_rename_key_dataframe_ui.label_info_text.setText("Pola nie mogą być puste")

        except Exception as e:
            MessageModel.error("0020", str(e))

    def exportAsPdf(self, filePath):
        try:
            if filePath:
                printer = QPrinter(QPrinter.PrinterMode.HighResolution)
                printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
                printer.setOutputFileName(filePath)
                self.textEdit_Board.document().print(printer)
                MessageModel.statusSaveAsFile(filePath)
        except Exception as e:
            MessageModel.error("0013", str(e))

    def exportAs(self):
        try:
            dir = os.path.expanduser("~/Desktop/")

            saveFileDialog = QFileDialog()
            saveFileDialog.setWindowTitle("Eksportuj plik")
            saveFileDialog.setNameFilter("Plik PDF (*.pdf)")
            saveFileDialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
            saveFileDialog.setDirectory(dir)
            saveFileDialog.selectNameFilter("Plik PDF (*.pdf)")
            saveFileDialog.selectFile("nowy.pdf")

            if saveFileDialog.exec():
                selectedFiles = saveFileDialog.selectedFiles()
                filePath = selectedFiles[0]

                filePath = self.adjustFilename(filePath, "pdf")

                if filePath.endswith(".pdf"):
                    self.exportAsPdf(filePath)

        except Exception as e:
            MessageModel.error("0012", str(e))

    def fontDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.textEdit_Board.setFont(font)
            self.updateTextEdit()

    def updateTextEdit(self):
        cursor = self.textEdit_Board.textCursor()
        selectionFormat = cursor.charFormat()
        textColor = selectionFormat.foreground().color()

        self.iconColorBox = QtGui.QIcon()
        self.pixmapColorBox = QtGui.QPixmap(32, 32)
        self.pixmapColorBox.fill(textColor)
        self.iconColorBox.addPixmap(self.pixmapColorBox)

        self.toolButtonColor.setIcon(self.iconColorBox)

        font = selectionFormat.font()
        self.fontComboBox_Text_Font.setCurrentFont(font)

        self.spinBox_Text_Size.setValue(font.pointSize())

    def colorDialog(self):
        color = QColorDialog.getColor()
        self.iconColorBox = QtGui.QIcon()
        self.pixmapColorBox = QtGui.QPixmap(32, 32)
        self.pixmapColorBox.fill(color)
        self.iconColorBox.addPixmap(self.pixmapColorBox)

        self.toolButtonColor.setIcon(self.iconColorBox)

        self.textEdit_Board.setTextColor(color)

    def addColorToolButtonToolBar(self):
        # icon
        self.iconColorBox = QtGui.QIcon()
        self.pixmapColorBox = QtGui.QPixmap(32, 32)
        self.pixmapColorBox.fill(QtGui.QColor(0, 0, 0))
        self.iconColorBox.addPixmap(self.pixmapColorBox)

        # button
        self.toolButtonColor = QToolButton()
        self.toolButtonColor.setIcon(self.iconColorBox)

        self.toolBar.addWidget(self.toolButtonColor)

    def alignTextRight(self):
        self.textEdit_Board.setAlignment(Qt.AlignmentFlag.AlignRight)

    def alignTextLeft(self):
        self.textEdit_Board.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def alignTextCenter(self):
        self.textEdit_Board.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def alignTextJustify(self):
        self.textEdit_Board.setAlignment(Qt.AlignmentFlag.AlignJustify)

    def toggleTextUnderline(self):
        cursor = self.textEdit_Board.textCursor()
        currentFormat = cursor.charFormat()

        if currentFormat.fontUnderline():
            currentFormat.setFontUnderline(False)
        else:
            currentFormat.setFontUnderline(True)

        cursor.setCharFormat(currentFormat)
        self.textEdit_Board.setTextCursor(cursor)

    def toggleTextItalic(self):
        cursor = self.textEdit_Board.textCursor()
        currentFormat = cursor.charFormat()

        if currentFormat.fontItalic():
            currentFormat.setFontItalic(False)
        else:
            currentFormat.setFontItalic(True)

        cursor.setCharFormat(currentFormat)
        self.textEdit_Board.setTextCursor(cursor)

    def toggleTextBold(self):
        cursor = self.textEdit_Board.textCursor()
        currentFormat = cursor.charFormat()

        if currentFormat.fontWeight() == QFont.Weight.Bold:
            currentFormat.setFontWeight(QFont.Weight.Normal)
        else:
            currentFormat.setFontWeight(QFont.Weight.Bold)

        cursor.setCharFormat(currentFormat)
        self.textEdit_Board.setTextCursor(cursor)

    def closeEvent(self, a0):
        if QFile.exists(self.resourcePath("settings.json")):
            with open(self.resourcePath("settings.json"), 'r') as file:
                settings = json.load(file)
                show_save_reminder_window = settings.get("show_save_reminder_window", 0)

                if show_save_reminder_window == 0:
                    result = MessageModel.exitApp()

                    if result == 1:
                        self.saveChanges()
                        self.closeChildWindows()
                        a0.accept()
                    elif result == 2:
                        self.closeChildWindows()
                        a0.accept()
                    else:
                        a0.ignore()
                elif show_save_reminder_window == 2:
                    if self.pathCurrentFileGlobal:
                        self.save(self.pathCurrentFileGlobal)

                    self.closeChildWindows()
                    a0.accept()
                else:
                    self.closeChildWindows()
                    a0.accept()
        else:
            self.saveChanges()
            self.closeChildWindows()
            a0.accept()

    def closeChildWindows(self):
        for widget in QApplication.topLevelWidgets():
            if widget != self:
                widget.close()

    def printPreviewBoard(self):
        try:
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            ui_printer = QPrintPreviewDialog(printer, self)
            ui_printer.paintRequested.connect(self.paintBoard)
            ui_printer.showMaximized()
            ui_printer.setWindowTitle("Podgląd wydruku")
            ui_printer.exec()
        except Exception as e:
            MessageModel.error("0011", str(e))

    def paintBoard(self, printer):
        self.textEdit_Board.print(printer)

    def printBoard(self):
        try:
            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            ui_printer = QPrintDialog(printer)

            if ui_printer.exec() == QPrintDialog.DialogCode.Accepted:
                self.textEdit_Board.print(printer)
        except Exception as e:
            MessageModel.error("0010", str(e))

    def newProject(self):
        if MessageModel.notSavedProject(self.saveChanges):
            self.pathCurrentFileGlobal = None
            self.setWindowTitle("Dex")
            self.textEdit_Board.clear()
            DataStorageModel.clear()
            self.updateStatusBar()
        else:
            pass

    def openFile(self):
        try:
            dir = os.path.expanduser("~/Desktop/")

            openFileDialog = QFileDialog()
            openFileDialog.setWindowTitle("Wczytaj projekt")
            openFileDialog.setNameFilter("Plik Dex (*.dex)")
            openFileDialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
            openFileDialog.setDirectory(dir)
            openFileDialog.selectNameFilter("Plik Dex (*.dex)")

            if openFileDialog.exec():
                selectedFiles = openFileDialog.selectedFiles()
                fileName = selectedFiles[0]

                if fileName.endswith(".dex"):
                    text_data = ""
                    data_frames = {}

                    with open(fileName, "r") as file:
                        data = json.load(file)

                    text_data = data.get("text_data", "")
                    self.textEdit_Board.setHtml(text_data)

                    data_frames = data.get("data_frames", {})

                    DataStorageModel.clear()

                    for key, jsonData in data_frames.items():
                        df = pd.read_json(StringIO(jsonData), orient="split")
                        df.columns = [str(col) for col in df.columns]

                        DataStorageModel.add(key, df)

                    self.setSavedFilePath(fileName)
                    self.updateStatusBar()
            else:
                MessageModel.error("1001", "Wystąpił błąd!")


        except Exception as e:
            MessageModel.error("0009", str(e))

    def saveChanges(self):
        try:
            file = self.pathCurrentFileGlobal
            if file:
                self.save(self.pathCurrentFileGlobal)
            else:
                self.saveProjectNew()
        except Exception as e:
            MessageModel.error("0008", str(e))

    def saveProjectNew(self):
        try:
            dir = os.path.expanduser("~/Desktop/")

            saveFileDialog = QFileDialog()
            saveFileDialog.setWindowTitle("Zapisz nowy projekt")
            saveFileDialog.setNameFilter("Plik Dex (*.dex)")
            saveFileDialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
            saveFileDialog.setDirectory(dir)
            saveFileDialog.selectNameFilter("Plik Dex (*.dex)")
            saveFileDialog.selectFile("nowy.dex")

            if saveFileDialog.exec():
                selectedFiles = saveFileDialog.selectedFiles()
                selectedFiles = selectedFiles[0]

                selectedFiles = self.adjustFilename(selectedFiles, "dex")

                if selectedFiles:
                    self.save(selectedFiles)

        except Exception as e:
            MessageModel.error("0007", str(e))

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
            MessageModel.error("0006", str(e))

    def setSavedFilePath(self, filePath):
        newWindowTitle = "{} - Dex".format(filePath)
        self.setWindowTitle(newWindowTitle)
        self.pathCurrentFileGlobal = filePath

    def addFontComboBoxToolBar(self):
        self.fontComboBox_Text_Font = QFontComboBox()
        self.fontComboBox_Text_Font.setEditable(False)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.fontComboBox_Text_Font.setCurrentFont(font)
        self.toolBar.addWidget(self.fontComboBox_Text_Font)

    def addSpinBoxToolBar(self):
        self.spinBox_Text_Size = QSpinBox()
        self.spinBox_Text_Size.setMinimumSize(QtCore.QSize(50, 0))
        # self.spinBox_Text_Size.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBox_Text_Size.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinBox_Text_Size.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBox_Text_Size.setMinimum(8)
        self.spinBox_Text_Size.setMaximum(72)
        self.spinBox_Text_Size.setProperty("value", 14)
        self.spinBox_Text_Size.setDisplayIntegerBase(10)
        self.toolBar.addWidget(self.spinBox_Text_Size)

    def createAboutApp(self):
        self.window_about_app = QDialog()
        self.window_about_app_ui = Ui_Dialog_About_App()
        self.window_about_app_ui.setupUi(self.window_about_app)
        self.window_about_app.show()

    def createDataPreviewWindow(self):
        self.window_data_preview = QMainWindow()
        self.window_data_preview_ui = Ui_MainWindow_Data_Preview()
        self.window_data_preview_ui.setupUi(self.window_data_preview)

        dataAll = DataStorageModel.get_all_keys()

        self.window_data_preview_ui.comboBox_Select_Data.addItems(dataAll)

        self.window_data_preview_ui.comboBox_Select_Data.currentIndexChanged.connect(self.loadDataInPreviewData)

        self.window_data_preview_ui.pushButton_Refresh.clicked.connect(self.refreshDataListPreviewData)

        if self.selectedDataNameForDataPreviewGlobal:
            self.window_data_preview_ui.comboBox_Select_Data.setCurrentText(self.selectedDataNameForDataPreviewGlobal)

        self.window_data_preview.show()

    def loadDataInPreviewData(self):
        selectedData = self.window_data_preview_ui.comboBox_Select_Data.currentText()

        if selectedData:
            self.selectedDataNameForDataPreviewGlobal = selectedData
            data = DataStorageModel.get(selectedData)
            model = DataFrameModel(data)
            self.window_data_preview_ui.tableView_Data_Frame.setModel(model)

    def refreshDataListPreviewData(self):
        dataAll = DataStorageModel.get_all_keys()
        self.window_data_preview_ui.comboBox_Select_Data.clear()
        self.window_data_preview_ui.comboBox_Select_Data.addItems(dataAll)

        if self.selectedDataNameForDataPreviewGlobal:
            self.window_data_preview_ui.comboBox_Select_Data.setCurrentText(self.selectedDataNameForDataPreviewGlobal)

    def createGuideWindow(self):
        self.window_guide = QMainWindow()
        self.window_guide_ui = Ui_MainWindow_Guide()
        self.window_guide_ui.setupUi(self.window_guide)
        self.window_guide.show()

    def adjustFilename(self, filePath, extension):
        if not extension.startswith('.'):
            extension = '.' + extension

        extensionLength = len(extension)

        if filePath[-extensionLength:] != extension:
            filePath += extension

        return filePath
