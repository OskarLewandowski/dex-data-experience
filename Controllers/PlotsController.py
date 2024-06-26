from PyQt6 import QtGui
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QVBoxLayout, QWidget
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from Views.Plots.box_plot_window import Ui_MainWindow_Box_Plot
from Views.Plots.line_plot_window import Ui_MainWindow_Line_Plot
from Views.Plots.pie_plot_window import Ui_MainWindow_Pie_Plot
from Views.Plots.bar_plot_window import Ui_MainWindow_Bar_Plot
from Views.Plots.hist_plot_window import Ui_MainWindow_Hist_Plot
from Models.data_storage_model import DataStorageModel
from Models.message_model import MessageModel
from Views.Main.main_window import Ui_MainWindow_Main
from Views.Plots.scatter_plot_window import Ui_MainWindow_Scatter_Plot
import seaborn as sns
import base64
import os
import io


class PlotsController(QMainWindow, Ui_MainWindow_Main):
    def __init__(self, main_controller):
        super().__init__()
        self.main = main_controller

        self.main.action_Scatter_Plot.triggered.connect(self.createScatterPlotWindow)
        self.main.action_Bar_Plot.triggered.connect(self.createBarPlotWindow)
        self.main.action_Box_Plot.triggered.connect(self.createBoxPlotWindow)
        self.main.action_Hist_Plot.triggered.connect(self.createHistPlotWindow)
        self.main.action_Line_Plot.triggered.connect(self.createLinePlotWindow)
        self.main.action_Pie_Chart.triggered.connect(self.createPiePlotWindow)

    def exportAsPng(self, window):
        try:
            dir = os.path.expanduser("~/Desktop/")

            saveFileDialog = QFileDialog()
            saveFileDialog.setWindowTitle("Eksportuj wykres")
            saveFileDialog.setNameFilter("Plik PNG (*.png)")
            saveFileDialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
            saveFileDialog.setDirectory(dir)
            saveFileDialog.selectNameFilter("Plik PNG (*.png)")
            saveFileDialog.selectFile("nowy.png")

            if saveFileDialog.exec():
                selectedFiles = saveFileDialog.selectedFiles()
                filePath = selectedFiles[0]
                filePath = self.main.adjustFilename(filePath, "png")

                if filePath.endswith(".png"):
                    self.canvas.figure.savefig(filePath, format='png')
                    MessageModel.show_toast("Wykres został zapisany jako plik png", 2000, window)

        except Exception as e:
            MessageModel.error("0030", str(e))

    def splitText(self, text, seperator=" : "):
        if seperator in str(text):
            textParts = str(text).split(seperator)
            return textParts
        else:
            return None

    def drawPlotInBoard(self, window):
        try:
            if self.figure != "":
                buf = io.BytesIO()
                self.figure.savefig(buf, format='png')
                buf.seek(0)

                data = buf.read()
                data_base64 = base64.b64encode(data).decode('utf-8')

                html = f'<img src="data:image/png;base64,{data_base64}" />'

                cursor = self.main.textEdit_Board.textCursor()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                # cursor.insertText("\n")
                cursor.insertHtml(html)
                # cursor.insertText("\n")
                MessageModel.show_toast("Wykres został dodany do tablicy", 1500, window)
        except Exception as e:
            print(str(e))

    def updateDataXY(self, window_ui):
        dataKey = window_ui.comboBox_Data.currentText()
        if dataKey:
            data = DataStorageModel.get_all_keys_and_columns_with_filter_key(dataKey)
            window_ui.comboBox_X.clear()
            window_ui.comboBox_Y.clear()

            window_ui.comboBox_X.addItems(data)
            window_ui.comboBox_Y.addItems(data)
        else:
            data = DataStorageModel.get_all_keys_and_columns()
            window_ui.comboBox_X.clear()
            window_ui.comboBox_Y.clear()

            window_ui.comboBox_X.addItems(data)
            window_ui.comboBox_Y.addItems(data)

    # Scatter Plot
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
        self.window_scatter_plot_ui.pushButton_Export.clicked.connect(
            lambda: self.exportAsPng(self.window_scatter_plot))
        self.window_scatter_plot_ui.pushButton_Add_To_Board.clicked.connect(
            lambda: self.drawPlotInBoard(self.window_scatter_plot))
        self.window_scatter_plot_ui.pushButton_Generate_Plot.clicked.connect(self.drawScatterPlot)

        self.window_scatter_plot_ui.comboBox_Data.currentIndexChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.comboBox_Data.currentIndexChanged.connect(
            lambda: self.updateDataXY(self.window_scatter_plot_ui))

        self.window_scatter_plot_ui.comboBox_X.currentIndexChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.comboBox_Y.currentIndexChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.comboBox_Legend.currentIndexChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.comboBox_Style.currentIndexChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.comboBox_Hue.currentIndexChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.comboBox_Markers.currentIndexChanged.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.comboBox_Size.currentIndexChanged.connect(self.drawScatterPlot)

        self.window_scatter_plot_ui.lineEdit_Title_Plot.editingFinished.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.lineEdit_Label_X.editingFinished.connect(self.drawScatterPlot)
        self.window_scatter_plot_ui.lineEdit_Label_Y.editingFinished.connect(self.drawScatterPlot)

        self.window_scatter_plot_ui.pushButton_Data_Preview.clicked.connect(self.main.createDataPreviewWindow)

        self.main.center(self.window_scatter_plot)

        self.window_scatter_plot.show()

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
            data = DataStorageModel.get(data) if data else None

            # x
            result = self.splitText(x)
            x = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if x else None

            # y
            result = self.splitText(y)
            y = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if y else None

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
                            marker=markers if markers else "o")

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

    # Line Plot
    def createLinePlotWindow(self):
        self.window_line_plot = QMainWindow()
        self.window_line_plot_ui = Ui_MainWindow_Line_Plot()
        self.window_line_plot_ui.setupUi(self.window_line_plot)

        dataKeys = DataStorageModel.get_all_keys()
        dataAll = DataStorageModel.get_all_keys_and_columns()

        self.window_line_plot_ui.comboBox_Data.addItems(dataKeys)
        self.window_line_plot_ui.comboBox_X.addItems(dataAll)
        self.window_line_plot_ui.comboBox_Y.addItems(dataAll)
        self.window_line_plot_ui.comboBox_Hue.addItems(dataAll)
        self.window_line_plot_ui.comboBox_Size.addItems(dataAll)

        self.window_line_plot_ui.pushButton_Reset_Options.clicked.connect(self.resetLinePlot)
        self.window_line_plot_ui.pushButton_Export.clicked.connect(lambda: self.exportAsPng(self.window_line_plot))
        self.window_line_plot_ui.pushButton_Add_To_Board.clicked.connect(
            lambda: self.drawPlotInBoard(self.window_line_plot))
        self.window_line_plot_ui.pushButton_Generate_Plot.clicked.connect(self.drawLinePlot)

        self.window_line_plot_ui.comboBox_Data.currentIndexChanged.connect(self.drawLinePlot)
        self.window_line_plot_ui.comboBox_Data.currentIndexChanged.connect(
            lambda: self.updateDataXY(self.window_line_plot_ui))

        self.window_line_plot_ui.comboBox_X.currentIndexChanged.connect(self.drawLinePlot)
        self.window_line_plot_ui.comboBox_Y.currentIndexChanged.connect(self.drawLinePlot)
        self.window_line_plot_ui.comboBox_Legend.currentIndexChanged.connect(self.drawLinePlot)
        self.window_line_plot_ui.comboBox_Style.currentIndexChanged.connect(self.drawLinePlot)
        self.window_line_plot_ui.comboBox_Hue.currentIndexChanged.connect(self.drawLinePlot)
        self.window_line_plot_ui.comboBox_Markers.currentIndexChanged.connect(self.drawLinePlot)
        self.window_line_plot_ui.comboBox_Size.currentIndexChanged.connect(self.drawLinePlot)
        self.window_line_plot_ui.spinBox_CI.valueChanged.connect(self.drawLinePlot)
        self.window_line_plot_ui.comboBox_Estimator.currentIndexChanged.connect(self.drawLinePlot)

        self.window_line_plot_ui.lineEdit_Title_Plot.editingFinished.connect(self.drawLinePlot)
        self.window_line_plot_ui.lineEdit_Label_X.editingFinished.connect(self.drawLinePlot)
        self.window_line_plot_ui.lineEdit_Label_Y.editingFinished.connect(self.drawLinePlot)

        self.window_line_plot_ui.pushButton_Data_Preview.clicked.connect(self.main.createDataPreviewWindow)

        self.main.center(self.window_line_plot)

        self.window_line_plot.show()

    def drawLinePlot(self):
        try:
            # This 3 lines fix the problem with freezed plot
            self.window_line_plot_ui.widget_Plot.deleteLater()
            self.window_line_plot_ui.widget_Plot = QWidget()
            self.window_line_plot_ui.frame.layout().addWidget(self.window_line_plot_ui.widget_Plot)

            self.figure, self.ax = plt.subplots()
            self.canvas = FigureCanvas(self.figure)
            self.layout = QVBoxLayout(self.window_line_plot_ui.widget_Plot)
            self.layout.addWidget(self.canvas)

            data = self.window_line_plot_ui.comboBox_Data.currentText()
            x = self.window_line_plot_ui.comboBox_X.currentText()
            y = self.window_line_plot_ui.comboBox_Y.currentText()
            hue = self.window_line_plot_ui.comboBox_Hue.currentText()
            size = self.window_line_plot_ui.comboBox_Size.currentText()
            style = self.window_line_plot_ui.comboBox_Style.currentText()
            markers = self.window_line_plot_ui.comboBox_Markers.currentText()
            legend = self.window_line_plot_ui.comboBox_Legend.currentText()
            title = self.window_line_plot_ui.lineEdit_Title_Plot.text()
            label_x = self.window_line_plot_ui.lineEdit_Label_X.text()
            label_y = self.window_line_plot_ui.lineEdit_Label_Y.text()
            estimator = self.window_line_plot_ui.comboBox_Estimator.currentText()
            ci = self.window_line_plot_ui.spinBox_CI.value()

            # data
            data = DataStorageModel.get(data) if data else None

            # x
            result = self.splitText(x)
            x = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if x else None

            # y
            result = self.splitText(y)
            y = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if y else None

            # hue
            result = self.splitText(hue)
            hue = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if hue else None

            # size
            result = self.splitText(size)
            size = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if size else None

            if legend == "Brak":
                legend = "false"

            if ci == -1:
                ci = None

            sns.lineplot(data=data, x=x, y=y, ax=self.ax, hue=hue, size=size, palette=style if style else None,
                         legend=legend, errorbar=('ci', ci) if ci else None, estimator=estimator,
                         marker=markers if markers else None, seed=0)

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

    def resetLinePlot(self):
        self.window_line_plot_ui.comboBox_Data.setCurrentIndex(-1)
        self.window_line_plot_ui.comboBox_X.setCurrentIndex(-1)
        self.window_line_plot_ui.comboBox_Y.setCurrentIndex(-1)
        self.window_line_plot_ui.comboBox_Hue.setCurrentIndex(-1)
        self.window_line_plot_ui.comboBox_Size.setCurrentIndex(-1)
        self.window_line_plot_ui.comboBox_Legend.setCurrentIndex(-1)
        self.window_line_plot_ui.comboBox_Markers.setCurrentIndex(-1)
        self.window_line_plot_ui.comboBox_Style.setCurrentIndex(-1)
        self.window_line_plot_ui.lineEdit_Title_Plot.clear()
        self.window_line_plot_ui.lineEdit_Label_X.clear()
        self.window_line_plot_ui.lineEdit_Label_Y.clear()
        self.window_line_plot_ui.spinBox_CI.setValue(95)
        self.window_line_plot_ui.comboBox_Estimator.setCurrentIndex(0)

        self.window_line_plot_ui.widget_Plot.deleteLater()
        self.window_line_plot_ui.widget_Plot = QWidget()
        self.window_line_plot_ui.frame.layout().addWidget(self.window_line_plot_ui.widget_Plot)

    # Bar Plot
    def createBarPlotWindow(self):
        self.window_bar_plot = QMainWindow()
        self.window_bar_plot_ui = Ui_MainWindow_Bar_Plot()
        self.window_bar_plot_ui.setupUi(self.window_bar_plot)

        dataKeys = DataStorageModel.get_all_keys()
        dataAll = DataStorageModel.get_all_keys_and_columns()

        self.window_bar_plot_ui.comboBox_Data.addItems(dataKeys)
        self.window_bar_plot_ui.comboBox_X.addItems(dataAll)
        self.window_bar_plot_ui.comboBox_Y.addItems(dataAll)
        self.window_bar_plot_ui.comboBox_Hue.addItems(dataAll)

        self.window_bar_plot_ui.pushButton_Reset_Options.clicked.connect(self.resetBarPlot)
        self.window_bar_plot_ui.pushButton_Export.clicked.connect(lambda: self.exportAsPng(self.window_bar_plot))
        self.window_bar_plot_ui.pushButton_Add_To_Board.clicked.connect(
            lambda: self.drawPlotInBoard(self.window_bar_plot))
        self.window_bar_plot_ui.pushButton_Generate_Plot.clicked.connect(self.drawBarPlot)

        self.window_bar_plot_ui.comboBox_Data.currentIndexChanged.connect(self.drawBarPlot)
        self.window_bar_plot_ui.comboBox_Data.currentIndexChanged.connect(
            lambda: self.updateDataXY(self.window_bar_plot_ui))

        self.window_bar_plot_ui.comboBox_X.currentIndexChanged.connect(self.drawBarPlot)
        self.window_bar_plot_ui.comboBox_Y.currentIndexChanged.connect(self.drawBarPlot)
        self.window_bar_plot_ui.comboBox_Legend.currentIndexChanged.connect(self.drawBarPlot)
        self.window_bar_plot_ui.comboBox_Style.currentIndexChanged.connect(self.drawBarPlot)
        self.window_bar_plot_ui.comboBox_Hue.currentIndexChanged.connect(self.drawBarPlot)
        self.window_bar_plot_ui.comboBox_Estimator.currentIndexChanged.connect(self.drawBarPlot)
        self.window_bar_plot_ui.spinBox_CI.valueChanged.connect(self.drawBarPlot)

        self.window_bar_plot_ui.lineEdit_Title_Plot.editingFinished.connect(self.drawBarPlot)
        self.window_bar_plot_ui.lineEdit_Label_X.editingFinished.connect(self.drawBarPlot)
        self.window_bar_plot_ui.lineEdit_Label_Y.editingFinished.connect(self.drawBarPlot)
        self.window_bar_plot_ui.comboBox_Orient.currentIndexChanged.connect(self.drawBarPlot)

        self.window_bar_plot_ui.pushButton_Data_Preview.clicked.connect(self.main.createDataPreviewWindow)

        self.main.center(self.window_bar_plot)

        self.window_bar_plot.show()

    def drawBarPlot(self):
        try:
            # This 3 lines fix the problem with freezed plot
            self.window_bar_plot_ui.widget_Plot.deleteLater()
            self.window_bar_plot_ui.widget_Plot = QWidget()
            self.window_bar_plot_ui.frame.layout().addWidget(self.window_bar_plot_ui.widget_Plot)

            self.figure, self.ax = plt.subplots()
            self.canvas = FigureCanvas(self.figure)
            self.layout = QVBoxLayout(self.window_bar_plot_ui.widget_Plot)
            self.layout.addWidget(self.canvas)

            data = self.window_bar_plot_ui.comboBox_Data.currentText()
            x = self.window_bar_plot_ui.comboBox_X.currentText()
            y = self.window_bar_plot_ui.comboBox_Y.currentText()
            hue = self.window_bar_plot_ui.comboBox_Hue.currentText()
            ci = self.window_bar_plot_ui.spinBox_CI.value()
            style = self.window_bar_plot_ui.comboBox_Style.currentText()
            estimator = self.window_bar_plot_ui.comboBox_Estimator.currentText()
            legend = self.window_bar_plot_ui.comboBox_Legend.currentText()
            title = self.window_bar_plot_ui.lineEdit_Title_Plot.text()
            label_x = self.window_bar_plot_ui.lineEdit_Label_X.text()
            label_y = self.window_bar_plot_ui.lineEdit_Label_Y.text()
            orient = self.window_bar_plot_ui.comboBox_Orient.currentText()

            # data
            data = DataStorageModel.get(data) if data else None

            # x
            result = self.splitText(x)
            x = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if x else None

            # y
            result = self.splitText(y)
            y = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if y else None

            # hue
            result = self.splitText(hue)
            hue = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if hue else None

            if legend == "Brak":
                legend = "false"

            if ci == -1:
                ci = None

            if orient == "wertykalna":
                orient = "v"
            elif orient == "horyzontalna":
                orient = "h"
            else:
                orient = None

            sns.barplot(data=data, x=x, y=y, ax=self.ax, hue=hue, estimator=estimator, palette=style if style else None,
                        legend=legend, seed=0, orient=orient, errorbar=('ci', ci) if ci else None)

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

    def resetBarPlot(self):
        self.window_bar_plot_ui.comboBox_Data.setCurrentIndex(-1)
        self.window_bar_plot_ui.comboBox_X.setCurrentIndex(-1)
        self.window_bar_plot_ui.comboBox_Y.setCurrentIndex(-1)
        self.window_bar_plot_ui.comboBox_Hue.setCurrentIndex(-1)
        self.window_bar_plot_ui.spinBox_CI.setValue(95)
        self.window_bar_plot_ui.comboBox_Legend.setCurrentIndex(-1)
        self.window_bar_plot_ui.comboBox_Estimator.setCurrentIndex(0)
        self.window_bar_plot_ui.comboBox_Style.setCurrentIndex(-1)
        self.window_bar_plot_ui.lineEdit_Title_Plot.clear()
        self.window_bar_plot_ui.lineEdit_Label_X.clear()
        self.window_bar_plot_ui.lineEdit_Label_Y.clear()
        self.window_bar_plot_ui.comboBox_Orient.setCurrentIndex(-1)

        self.window_bar_plot_ui.widget_Plot.deleteLater()
        self.window_bar_plot_ui.widget_Plot = QWidget()
        self.window_bar_plot_ui.frame.layout().addWidget(self.window_bar_plot_ui.widget_Plot)

    # Hist Plot
    def createHistPlotWindow(self):
        self.window_hist_plot = QMainWindow()
        self.window_hist_plot_ui = Ui_MainWindow_Hist_Plot()
        self.window_hist_plot_ui.setupUi(self.window_hist_plot)

        dataKeys = DataStorageModel.get_all_keys()
        dataAll = DataStorageModel.get_all_keys_and_columns()

        self.window_hist_plot_ui.comboBox_Data.addItems(dataKeys)
        self.window_hist_plot_ui.comboBox_X.addItems(dataAll)
        self.window_hist_plot_ui.comboBox_Y.addItems(dataAll)
        self.window_hist_plot_ui.comboBox_Hue.addItems(dataAll)

        self.window_hist_plot_ui.pushButton_Reset_Options.clicked.connect(self.resetHistPlot)
        self.window_hist_plot_ui.pushButton_Export.clicked.connect(lambda: self.exportAsPng(self.window_hist_plot))
        self.window_hist_plot_ui.pushButton_Add_To_Board.clicked.connect(
            lambda: self.drawPlotInBoard(self.window_hist_plot))
        self.window_hist_plot_ui.pushButton_Generate_Plot.clicked.connect(self.drawHistPlot)

        self.window_hist_plot_ui.comboBox_Data.currentIndexChanged.connect(self.drawHistPlot)
        self.window_hist_plot_ui.comboBox_Data.currentIndexChanged.connect(
            lambda: self.updateDataXY(self.window_hist_plot_ui))

        self.window_hist_plot_ui.comboBox_X.currentIndexChanged.connect(self.drawHistPlot)
        self.window_hist_plot_ui.comboBox_Y.currentIndexChanged.connect(self.drawHistPlot)
        self.window_hist_plot_ui.comboBox_Legend.currentIndexChanged.connect(self.drawHistPlot)
        self.window_hist_plot_ui.comboBox_Style.currentIndexChanged.connect(self.drawHistPlot)
        self.window_hist_plot_ui.comboBox_Hue.currentIndexChanged.connect(self.drawHistPlot)
        self.window_hist_plot_ui.comboBox_Stat.currentIndexChanged.connect(self.drawHistPlot)
        self.window_hist_plot_ui.comboBox_Element.currentIndexChanged.connect(self.drawHistPlot)
        self.window_hist_plot_ui.comboBox_Multiple.currentIndexChanged.connect(self.drawHistPlot)

        self.window_hist_plot_ui.lineEdit_Title_Plot.editingFinished.connect(self.drawHistPlot)
        self.window_hist_plot_ui.lineEdit_Label_X.editingFinished.connect(self.drawHistPlot)
        self.window_hist_plot_ui.lineEdit_Label_Y.editingFinished.connect(self.drawHistPlot)

        self.window_hist_plot_ui.pushButton_Data_Preview.clicked.connect(self.main.createDataPreviewWindow)

        self.main.center(self.window_hist_plot)

        self.window_hist_plot.show()

    def drawHistPlot(self):
        try:
            # This 3 lines fix the problem with freezed plot
            self.window_hist_plot_ui.widget_Plot.deleteLater()
            self.window_hist_plot_ui.widget_Plot = QWidget()
            self.window_hist_plot_ui.frame.layout().addWidget(self.window_hist_plot_ui.widget_Plot)

            self.figure, self.ax = plt.subplots()
            self.canvas = FigureCanvas(self.figure)
            self.layout = QVBoxLayout(self.window_hist_plot_ui.widget_Plot)
            self.layout.addWidget(self.canvas)

            data = self.window_hist_plot_ui.comboBox_Data.currentText()
            x = self.window_hist_plot_ui.comboBox_X.currentText()
            y = self.window_hist_plot_ui.comboBox_Y.currentText()
            hue = self.window_hist_plot_ui.comboBox_Hue.currentText()
            stat = self.window_hist_plot_ui.comboBox_Stat.currentText()
            style = self.window_hist_plot_ui.comboBox_Style.currentText()
            element = self.window_hist_plot_ui.comboBox_Element.currentText()
            multiple = self.window_hist_plot_ui.comboBox_Multiple.currentText()
            legend = self.window_hist_plot_ui.comboBox_Legend.currentText()
            title = self.window_hist_plot_ui.lineEdit_Title_Plot.text()
            label_x = self.window_hist_plot_ui.lineEdit_Label_X.text()
            label_y = self.window_hist_plot_ui.lineEdit_Label_Y.text()

            # data
            data = DataStorageModel.get(data) if data else None

            # x
            result = self.splitText(x)
            x = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if x else None

            # y
            result = self.splitText(y)
            y = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if y else None

            # hue
            result = self.splitText(hue)
            hue = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if hue else None

            if legend == "Brak":
                legend = "false"

            sns.histplot(data=data, x=x, y=y, ax=self.ax, hue=hue, palette=style if style else None,
                         legend=legend, stat=stat, multiple=multiple, element=element)

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

    def resetHistPlot(self):
        self.window_hist_plot_ui.comboBox_Data.setCurrentIndex(-1)
        self.window_hist_plot_ui.comboBox_X.setCurrentIndex(-1)
        self.window_hist_plot_ui.comboBox_Y.setCurrentIndex(-1)
        self.window_hist_plot_ui.comboBox_Hue.setCurrentIndex(-1)
        self.window_hist_plot_ui.comboBox_Stat.setCurrentIndex(0)
        self.window_hist_plot_ui.comboBox_Legend.setCurrentIndex(-1)
        self.window_hist_plot_ui.comboBox_Element.setCurrentIndex(0)
        self.window_hist_plot_ui.comboBox_Multiple.setCurrentIndex(0)
        self.window_hist_plot_ui.comboBox_Style.setCurrentIndex(-1)
        self.window_hist_plot_ui.lineEdit_Title_Plot.clear()
        self.window_hist_plot_ui.lineEdit_Label_X.clear()
        self.window_hist_plot_ui.lineEdit_Label_Y.clear()

        self.window_hist_plot_ui.widget_Plot.deleteLater()
        self.window_hist_plot_ui.widget_Plot = QWidget()
        self.window_hist_plot_ui.frame.layout().addWidget(self.window_hist_plot_ui.widget_Plot)

    # Box Plot
    def createBoxPlotWindow(self):
        self.window_box_plot = QMainWindow()
        self.window_box_plot_ui = Ui_MainWindow_Box_Plot()
        self.window_box_plot_ui.setupUi(self.window_box_plot)

        dataKeys = DataStorageModel.get_all_keys()
        dataAll = DataStorageModel.get_all_keys_and_columns()

        self.window_box_plot_ui.comboBox_Data.addItems(dataKeys)
        self.window_box_plot_ui.comboBox_X.addItems(dataAll)
        self.window_box_plot_ui.comboBox_Y.addItems(dataAll)
        self.window_box_plot_ui.comboBox_Hue.addItems(dataAll)

        self.window_box_plot_ui.pushButton_Reset_Options.clicked.connect(self.resetBoxPlot)
        self.window_box_plot_ui.pushButton_Export.clicked.connect(lambda: self.exportAsPng(self.window_box_plot))
        self.window_box_plot_ui.pushButton_Add_To_Board.clicked.connect(
            lambda: self.drawPlotInBoard(self.window_box_plot))
        self.window_box_plot_ui.pushButton_Generate_Plot.clicked.connect(self.drawBoxPlot)

        self.window_box_plot_ui.comboBox_Data.currentIndexChanged.connect(self.drawBoxPlot)
        self.window_box_plot_ui.comboBox_Data.currentIndexChanged.connect(
            lambda: self.updateDataXY(self.window_box_plot_ui))

        self.window_box_plot_ui.comboBox_X.currentIndexChanged.connect(self.drawBoxPlot)
        self.window_box_plot_ui.comboBox_Y.currentIndexChanged.connect(self.drawBoxPlot)
        self.window_box_plot_ui.comboBox_Legend.currentIndexChanged.connect(self.drawBoxPlot)
        self.window_box_plot_ui.comboBox_Style.currentIndexChanged.connect(self.drawBoxPlot)
        self.window_box_plot_ui.comboBox_Hue.currentIndexChanged.connect(self.drawBoxPlot)
        self.window_box_plot_ui.comboBox_Orient.currentIndexChanged.connect(self.drawBoxPlot)

        self.window_box_plot_ui.lineEdit_Title_Plot.editingFinished.connect(self.drawBoxPlot)
        self.window_box_plot_ui.lineEdit_Label_X.editingFinished.connect(self.drawBoxPlot)
        self.window_box_plot_ui.lineEdit_Label_Y.editingFinished.connect(self.drawBoxPlot)

        self.window_box_plot_ui.pushButton_Data_Preview.clicked.connect(self.main.createDataPreviewWindow)

        self.main.center(self.window_box_plot)

        self.window_box_plot.show()

    def drawBoxPlot(self):
        try:
            # This 3 lines fix the problem with freezed plot
            self.window_box_plot_ui.widget_Plot.deleteLater()
            self.window_box_plot_ui.widget_Plot = QWidget()
            self.window_box_plot_ui.frame.layout().addWidget(self.window_box_plot_ui.widget_Plot)

            self.figure, self.ax = plt.subplots()
            self.canvas = FigureCanvas(self.figure)
            self.layout = QVBoxLayout(self.window_box_plot_ui.widget_Plot)
            self.layout.addWidget(self.canvas)

            data = self.window_box_plot_ui.comboBox_Data.currentText()
            x = self.window_box_plot_ui.comboBox_X.currentText()
            y = self.window_box_plot_ui.comboBox_Y.currentText()
            hue = self.window_box_plot_ui.comboBox_Hue.currentText()
            style = self.window_box_plot_ui.comboBox_Style.currentText()
            orient = self.window_box_plot_ui.comboBox_Orient.currentText()
            legend = self.window_box_plot_ui.comboBox_Legend.currentText()
            title = self.window_box_plot_ui.lineEdit_Title_Plot.text()
            label_x = self.window_box_plot_ui.lineEdit_Label_X.text()
            label_y = self.window_box_plot_ui.lineEdit_Label_Y.text()

            # data
            data = DataStorageModel.get(data) if data else None

            # x
            result = self.splitText(x)
            x = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if x else None

            # y
            result = self.splitText(y)
            y = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if y else None

            # hue
            result = self.splitText(hue)
            hue = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if hue else None

            if legend == "Brak":
                legend = "false"

            if orient == "wertykalna":
                orient = "v"
            elif orient == "horyzontalna":
                orient = "h"
            else:
                orient = None

            sns.boxplot(data=data, x=x, y=y, ax=self.ax, hue=hue, palette=style if style else None,
                        legend=legend, orient=orient)

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

    def resetBoxPlot(self):
        self.window_box_plot_ui.comboBox_Data.setCurrentIndex(-1)
        self.window_box_plot_ui.comboBox_X.setCurrentIndex(-1)
        self.window_box_plot_ui.comboBox_Y.setCurrentIndex(-1)
        self.window_box_plot_ui.comboBox_Hue.setCurrentIndex(-1)
        self.window_box_plot_ui.comboBox_Orient.setCurrentIndex(-1)
        self.window_box_plot_ui.comboBox_Legend.setCurrentIndex(-1)
        self.window_box_plot_ui.comboBox_Style.setCurrentIndex(-1)
        self.window_box_plot_ui.lineEdit_Title_Plot.clear()
        self.window_box_plot_ui.lineEdit_Label_X.clear()
        self.window_box_plot_ui.lineEdit_Label_Y.clear()

        self.window_box_plot_ui.widget_Plot.deleteLater()
        self.window_box_plot_ui.widget_Plot = QWidget()
        self.window_box_plot_ui.frame.layout().addWidget(self.window_box_plot_ui.widget_Plot)

    # Pie Plot
    def createPiePlotWindow(self):
        self.window_pie_plot = QMainWindow()
        self.window_pie_plot_ui = Ui_MainWindow_Pie_Plot()
        self.window_pie_plot_ui.setupUi(self.window_pie_plot)

        dataKeys = DataStorageModel.get_all_keys()
        dataAll = DataStorageModel.get_all_keys_and_columns()

        self.window_pie_plot_ui.comboBox_Data.addItems(dataKeys)
        self.window_pie_plot_ui.comboBox_X.addItems(dataAll)
        self.window_pie_plot_ui.comboBox_Y.addItems(dataAll)

        self.window_pie_plot_ui.pushButton_Reset_Options.clicked.connect(self.resetPiePlot)
        self.window_pie_plot_ui.pushButton_Export.clicked.connect(lambda: self.exportAsPng(self.window_pie_plot))
        self.window_pie_plot_ui.pushButton_Add_To_Board.clicked.connect(
            lambda: self.drawPlotInBoard(self.window_pie_plot))
        self.window_pie_plot_ui.pushButton_Generate_Plot.clicked.connect(self.drawPiePlot)

        self.window_pie_plot_ui.comboBox_Data.currentIndexChanged.connect(
            lambda: self.updateDataXY(self.window_pie_plot_ui))

        self.window_pie_plot_ui.comboBox_X.currentIndexChanged.connect(self.drawPiePlot)
        self.window_pie_plot_ui.comboBox_Y.currentIndexChanged.connect(self.drawPiePlot)
        self.window_pie_plot_ui.comboBox_Style.currentIndexChanged.connect(self.drawPiePlot)
        self.window_pie_plot_ui.comboBox_Label_Color.currentIndexChanged.connect(self.drawPiePlot)
        self.window_pie_plot_ui.comboBox_Legend_Location.currentIndexChanged.connect(self.drawPiePlot)

        self.window_pie_plot_ui.lineEdit_Title_Plot.editingFinished.connect(self.drawPiePlot)
        self.window_pie_plot_ui.lineEdit_Label_X.editingFinished.connect(self.drawPiePlot)
        self.window_pie_plot_ui.lineEdit_Label_Y.editingFinished.connect(self.drawPiePlot)
        self.window_pie_plot_ui.lineEdit_Legend_Title.editingFinished.connect(self.drawPiePlot)

        self.window_pie_plot_ui.doubleSpinBox_Radius.valueChanged.connect(self.drawPiePlot)

        self.window_pie_plot_ui.pushButton_Data_Preview.clicked.connect(self.main.createDataPreviewWindow)

        self.main.center(self.window_pie_plot)

        self.window_pie_plot.show()

    def drawPiePlot(self):
        try:
            # This 3 lines fix the problem with freezed plot
            self.window_pie_plot_ui.widget_Plot.deleteLater()
            self.window_pie_plot_ui.widget_Plot = QWidget()
            self.window_pie_plot_ui.frame.layout().addWidget(self.window_pie_plot_ui.widget_Plot)

            self.figure, self.ax = plt.subplots()
            self.canvas = FigureCanvas(self.figure)
            self.layout = QVBoxLayout(self.window_pie_plot_ui.widget_Plot)
            self.layout.addWidget(self.canvas)

            x = self.window_pie_plot_ui.comboBox_X.currentText()
            y = self.window_pie_plot_ui.comboBox_Y.currentText()
            style = self.window_pie_plot_ui.comboBox_Style.currentText()
            title = self.window_pie_plot_ui.lineEdit_Title_Plot.text()
            label_x = self.window_pie_plot_ui.lineEdit_Label_X.text()
            label_y = self.window_pie_plot_ui.lineEdit_Label_Y.text()
            legend_title = self.window_pie_plot_ui.lineEdit_Legend_Title.text()
            radius = self.window_pie_plot_ui.doubleSpinBox_Radius.value()
            loc = self.window_pie_plot_ui.comboBox_Legend_Location.currentText()
            color = self.window_pie_plot_ui.comboBox_Label_Color.currentText()

            # x
            result = self.splitText(x)
            x = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if x else None

            # y
            result = self.splitText(y)
            y = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if y else None

            if style:
                palette_color = sns.color_palette(style)
            else:
                palette_color = sns.color_palette('bright')

            textprops = {'fontsize': 12, 'color': color}
            autopct = lambda p: '{:.1f}%'.format(p) if p > 0 else ''

            wedges, texts, autotexts = self.ax.pie(x=x, labels=y, radius=radius, colors=palette_color, autopct=autopct,
                                                   textprops=textprops)

            self.ax.legend(wedges, y,
                           title=legend_title,
                           loc=loc)

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

    def resetPiePlot(self):
        self.window_pie_plot_ui.comboBox_X.setCurrentIndex(-1)
        self.window_pie_plot_ui.comboBox_Y.setCurrentIndex(-1)
        self.window_pie_plot_ui.comboBox_Style.setCurrentIndex(2)
        self.window_pie_plot_ui.comboBox_Legend_Location.setCurrentIndex(0)
        self.window_pie_plot_ui.comboBox_Label_Color.setCurrentIndex(0)
        self.window_pie_plot_ui.comboBox_Data.setCurrentIndex(-1)

        self.window_pie_plot_ui.doubleSpinBox_Radius.setValue(1.0)

        self.window_pie_plot_ui.lineEdit_Legend_Title.clear()
        self.window_pie_plot_ui.lineEdit_Title_Plot.clear()
        self.window_pie_plot_ui.lineEdit_Label_X.clear()
        self.window_pie_plot_ui.lineEdit_Label_Y.clear()

        self.window_pie_plot_ui.widget_Plot.deleteLater()
        self.window_pie_plot_ui.widget_Plot = QWidget()
        self.window_pie_plot_ui.frame.layout().addWidget(self.window_pie_plot_ui.widget_Plot)
