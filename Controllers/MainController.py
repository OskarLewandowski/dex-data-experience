import base64
import sys
from Views.Main.about_app import Ui_Dialog_About_App
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt6 import QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QDialog, QMainWindow, QFontComboBox, QSpinBox, QAbstractSpinBox, QFileDialog, QMessageBox, \
    QToolButton, QFontDialog, QColorDialog, QApplication, QVBoxLayout, QWidget
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Views.Main.rename_key_dataframe import Ui_Dialog_Rename_Key_Dataframe
from Models.data_storage_model import DataStorageModel
from Models.message_model import MessageModel
from io import StringIO
from Views.Main.main_window import Ui_MainWindow_Main
from Views.Main.scatter_plot_window import Ui_MainWindow_Scatter_Plot
import pandas as pd
import json
import os
import io
import seaborn as sns


class MainController(QMainWindow, Ui_MainWindow_Main):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.showMaximized()

        # Variable
        self.pathCurrentFileGlobal = None

        # View
        self.addFontComboBoxToolBar()
        self.addSpinBoxToolBar()
        self.addColorToolButtonToolBar()

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

        self.action_Scatter_Plot.triggered.connect(self.createScatterPlotWindow)

        self.action_Change_Data_Name.triggered.connect(self.createRenameKeyDataframeWindow)

        self.show()

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
                            f"Nazwa zbioru '{oldKey}' już istnieje")
                else:
                    self.window_rename_key_dataframe_ui.label_info_text.setText("Pola nie mogą być puste")

        except Exception as e:
            MessageModel.error("0020", str(e))

    def createScatterPlotWindow(self):
        self.window_scatter_plot = QMainWindow()
        self.window_scatter_plot_ui = Ui_MainWindow_Scatter_Plot()
        self.window_scatter_plot_ui.setupUi(self.window_scatter_plot)

        dataKeys = DataStorageModel.get_all_keys()
        dataAll = DataStorageModel.get_all_keys_and_columns()

        self.window_scatter_plot_ui.comboBox_Data.addItems(dataKeys)
        self.window_scatter_plot_ui.comboBox_X.addItems(dataAll)
        self.window_scatter_plot_ui.comboBox_Y.addItems(dataAll)
        self.window_scatter_plot_ui.comboBox_Hue.addItems(dataAll)
        self.window_scatter_plot_ui.comboBox_Size.addItems(dataAll)

        self.window_scatter_plot_ui.pushButton_Reset_Options.clicked.connect(self.resetScatterPlot)
        self.window_scatter_plot_ui.pushButton_Export.clicked.connect(self.exportAsPng)
        self.window_scatter_plot_ui.pushButton_Add_To_Board.clicked.connect(self.drawPlotInBoard)
        self.window_scatter_plot_ui.pushButton_Generate_Plot.clicked.connect(self.drawScatterPlot)

        self.window_scatter_plot_ui.comboBox_Data.currentIndexChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.comboBox_X.currentIndexChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.comboBox_Y.currentIndexChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.comboBox_Legend.currentIndexChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.comboBox_Style.currentIndexChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.comboBox_Hue.currentIndexChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.comboBox_Markers.currentIndexChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.comboBox_Size.currentIndexChanged.connect(self.drawScatterPlot)

        self.window_scatter_plot_ui.lineEdit_Title_Plot.textChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.lineEdit_Label_X.textChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.lineEdit_Label_Y.textChanged.connect(self.drawScatterPlot)

        self.window_scatter_plot.show()

    def exportAsPng(self):
        try:
            fileFilter = ('Plik PNG (*.png)')

            filePath = QFileDialog.getSaveFileName(
                caption="Eksportuj wykres",
                directory=os.path.expanduser("~/Desktop/wykres.png"),
                filter=fileFilter,
                initialFilter='Plik PNG (*.png)')

            filePath = str(filePath[0])

            if filePath.endswith(".png"):
                self.canvas.figure.savefig(filePath, format='png')


        except Exception as e:
            MessageModel.error("0030", str(e))

    def splitText(self, text, seperator=" : "):
        if seperator in str(text):
            textParts = str(text).split(seperator)
            return textParts
        else:
            return None

    def drawPlotInBoard(self):
        try:
            if self.figure != "":
                buf = io.BytesIO()
                self.figure.savefig(buf, format='png')
                buf.seek(0)

                data = buf.read()
                data_base64 = base64.b64encode(data).decode('utf-8')

                html = f'<img src="data:image/png;base64,{data_base64}" />'

                cursor = self.textEdit_Board.textCursor()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                cursor.insertText("\n")
                cursor.insertHtml(html)
                cursor.insertText("\n")
        except Exception as e:
            pass

    def drawScatterPlot(self):
        try:
            # This 3 lines fix the problem with freezed plot
            self.window_scatter_plot_ui.widget_Plot.deleteLater()
            self.window_scatter_plot_ui.widget_Plot = QWidget()
            self.window_scatter_plot_ui.frame.layout().addWidget(self.window_scatter_plot_ui.widget_Plot)

            self.figure, self.ax = plt.subplots()
            self.canvas = FigureCanvas(self.figure)
            self.layout = QVBoxLayout(self.window_scatter_plot_ui.widget_Plot)
            self.layout.addWidget(self.canvas)

            data = self.window_scatter_plot_ui.comboBox_Data.currentText()
            x = self.window_scatter_plot_ui.comboBox_X.currentText()
            y = self.window_scatter_plot_ui.comboBox_Y.currentText()
            hue = self.window_scatter_plot_ui.comboBox_Hue.currentText()
            size = self.window_scatter_plot_ui.comboBox_Size.currentText()
            style = self.window_scatter_plot_ui.comboBox_Style.currentText()
            markers = self.window_scatter_plot_ui.comboBox_Markers.currentText()
            legend = self.window_scatter_plot_ui.comboBox_Legend.currentText()
            title = self.window_scatter_plot_ui.lineEdit_Title_Plot.text()
            label_x = self.window_scatter_plot_ui.lineEdit_Label_X.text()
            label_y = self.window_scatter_plot_ui.lineEdit_Label_Y.text()

            # data
            data = DataStorageModel.get(data)

            # x
            result = self.splitText(x)
            x = DataStorageModel.get_data_by_key_and_column(result[0], result[1])

            # y
            result = self.splitText(y)
            y = DataStorageModel.get_data_by_key_and_column(result[0], result[1])

            # hue
            result = self.splitText(hue)
            hue = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if hue else None

            # size
            result = self.splitText(size)
            size = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if size else None

            if legend == "Brak":
                legend = "false"

            sns.scatterplot(data=data, x=x, y=y, ax=self.ax, hue=hue, size=size, palette=style if style else None,
                            legend=legend,
                            markers=markers if markers else None)

            if title:
                self.ax.set_title(title)

            if label_x:
                self.ax.set_xlabel(label_x)

            if label_y:
                self.ax.set_ylabel(label_y)

            self.canvas.draw()

            plt.close(self.figure)

        except Exception as e:
            pass

    def resetScatterPlot(self):
        self.window_scatter_plot_ui.comboBox_Data.setCurrentIndex(-1)
        self.window_scatter_plot_ui.comboBox_X.setCurrentIndex(-1)
        self.window_scatter_plot_ui.comboBox_Y.setCurrentIndex(-1)
        self.window_scatter_plot_ui.comboBox_Hue.setCurrentIndex(-1)
        self.window_scatter_plot_ui.comboBox_Size.setCurrentIndex(-1)
        self.window_scatter_plot_ui.comboBox_Legend.setCurrentIndex(-1)
        self.window_scatter_plot_ui.comboBox_Markers.setCurrentIndex(-1)
        self.window_scatter_plot_ui.comboBox_Style.setCurrentIndex(-1)
        self.window_scatter_plot_ui.lineEdit_Title_Plot.clear()
        self.window_scatter_plot_ui.lineEdit_Label_X.clear()
        self.window_scatter_plot_ui.lineEdit_Label_Y.clear()

        self.window_scatter_plot_ui.widget_Plot.deleteLater()
        self.window_scatter_plot_ui.widget_Plot = QWidget()
        self.window_scatter_plot_ui.frame.layout().addWidget(self.window_scatter_plot_ui.widget_Plot)

    def exportAsPdf(self, filePath):
        try:
            if filePath:
                printer = QPrinter(QPrinter.PrinterMode.HighResolution)
                printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
                printer.setOutputFileName(filePath)
                self.textEdit_Board.document().print(printer)
        except Exception as e:
            MessageModel.error("0013", str(e))

    def exportAs(self):
        try:
            fileFilter = ('Plik PDF (*.pdf)')

            filePath = QFileDialog.getSaveFileName(
                caption="Eksportuj plik",
                directory=os.path.expanduser("~/Desktop/raport.pdf"),
                filter=fileFilter,
                initialFilter='Plik PDF (*.pdf)')

            filePath = str(filePath[0])

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
        result = MessageModel.exitApp()

        if result == 1:
            self.saveChanges()
            a0.accept()
        elif result == 2:
            a0.accept()
        else:
            a0.ignore()

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
        else:
            pass

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
        font.setFamily("Calibri")
        font.setPointSize(12)
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
        self.spinBox_Text_Size.setProperty("value", 12)
        self.spinBox_Text_Size.setDisplayIntegerBase(10)
        self.toolBar.addWidget(self.spinBox_Text_Size)

    def createAboutApp(self):
        self.window_about_app = QDialog()
        self.window_about_app_ui = Ui_Dialog_About_App()
        self.window_about_app_ui.setupUi(self.window_about_app)
        self.window_about_app.show()
