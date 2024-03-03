import base64
import io

import numpy as np
import pandas as pd
from PyQt6 import QtGui
from PyQt6.QtWidgets import QMainWindow
from matplotlib import pyplot as plt
import seaborn as sns

from Models.data_storage_model import DataStorageModel
from Views.Main.main_window import Ui_MainWindow_Main
from Views.Analysis.basic_stats_window import Ui_MainWindow_Basic_Stats
from Views.Analysis.correlation_window import Ui_MainWindow_Correlation


class AnalysisController(QMainWindow, Ui_MainWindow_Main):
    def __init__(self, main_controller):
        super().__init__()
        self.main = main_controller

        self.main.action_Basic_Stats.triggered.connect(self.createBasicStatsWindow)
        self.main.action_Correlation.triggered.connect(self.createCorrelationWindow)

    def splitText(self, text, seperator=" : "):
        if seperator in str(text):
            textParts = str(text).split(seperator)
            return textParts
        else:
            return None

    def writeBasicStatsInBoard(self):
        try:
            data = self.window_basic_stats_ui.textEdit_Preview_Board.toHtml()
            if data:
                cursor = self.main.textEdit_Board.textCursor()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                cursor.insertText("\n")
                cursor.insertHtml(data)
        except Exception as e:
            pass

    def checkColumnType(self, selected_data):
        try:
            key, column = self.splitText(selected_data)
            data_frame = DataStorageModel.get(key)

            if data_frame is not None and column in data_frame.columns:
                if pd.api.types.is_numeric_dtype(data_frame[column]):
                    return 0  # ilościowe
                elif pd.api.types.is_string_dtype(data_frame[column]):
                    return 1  # jakościowe
                else:
                    return None
            else:
                return None
        except Exception as e:
            pass

    # Basic Stats
    def createBasicStatsWindow(self):
        self.window_basic_stats = QMainWindow()
        self.window_basic_stats_ui = Ui_MainWindow_Basic_Stats()
        self.window_basic_stats_ui.setupUi(self.window_basic_stats)

        dataAll = DataStorageModel.get_all_keys_and_columns()

        self.window_basic_stats_ui.comboBox_Data_Column.addItems(dataAll)

        self.window_basic_stats_ui.pushButton_Reset_Options.clicked.connect(self.resetBasicStats)
        self.window_basic_stats_ui.pushButton_Add_To_Board.clicked.connect(self.writeBasicStatsInBoard)

        self.window_basic_stats_ui.comboBox_Data_Column.currentIndexChanged.connect(self.writeBasicStats)

        self.window_basic_stats.show()

    def writeBasicStats(self):
        try:
            data = self.window_basic_stats_ui.comboBox_Data_Column.currentText()

            result = self.splitText(data)
            dataType = self.checkColumnType(data)
            selectedColumn = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if data else None

            self.window_basic_stats_ui.textEdit_Preview_Board.clear()

            if dataType == 0:
                result = (f"<b>Podstawowe statystyki</b><br>"
                          f"Zbiór: {result[0]}<br>"
                          f"Kolumna: {result[1]}<br>"
                          f"Typ danych: ilościowe<br><br>"
                          f"Średnia: <b>{round(selectedColumn.mean(), 2)}</b><br>"
                          f"Mediana: <b>{round(selectedColumn.median(), 2)}</b><br>"
                          f"Odchylenie standardowe: <b>{round(selectedColumn.std(), 2)}</b><br>"
                          f"Wariancja: <b>{round(selectedColumn.var(), 2)}</b><br>"
                          f"Minimum: <b>{round(selectedColumn.min(), 2)}</b><br>"
                          f"Maksimum: <b>{round(selectedColumn.max(), 2)}</b>")

            elif dataType == 1:
                result = (f"<b>Podstawowe statystyki</b><br>"
                          f"Zbiór: {result[0]}<br>"
                          f"Kolumna: {result[1]}<br>"
                          f"Typ danych: jakościowe<br><br>"
                          f"Liczba unikalnych wartości: <b>{selectedColumn.nunique()}</b><br>"
                          f"Najczęstsza wartość: <b>{selectedColumn.mode().iloc[0]}</b><br>"
                          f"Liczba wystąpień najczęstszej wartości: <b>{selectedColumn.value_counts().max()}</b><br>"
                          f"Entropia: <b>{round(-sum((selectedColumn.value_counts(normalize=True) * np.log2(selectedColumn.value_counts(normalize=True)))), 2)}</b>")
            else:
                result = (f"<b>Podstawowe statystyki</b><br>"
                          f"Zbiór: {result[0]}<br>"
                          f"Kolumna: {result[1]}<br>"
                          f"<u>Dane wymagają oczyszczenia<u>")

            self.window_basic_stats_ui.textEdit_Preview_Board.setText(str(result))


        except Exception as e:
            print(str(e))

    def resetBasicStats(self):
        self.window_basic_stats_ui.comboBox_Data_Column.setCurrentIndex(-1)
        self.window_basic_stats_ui.checkBox_Board_Is_Enabled.setChecked(False)
        self.window_basic_stats_ui.textEdit_Preview_Board.clear()
        self.window_basic_stats_ui.textEdit_Preview_Board.setReadOnly(True)

    # Correlation
    def createCorrelationWindow(self):
        self.window_correlation = QMainWindow()
        self.window_correlation_ui = Ui_MainWindow_Correlation()
        self.window_correlation_ui.setupUi(self.window_correlation)

        dataAll = DataStorageModel.get_all_keys()

        self.window_correlation_ui.comboBox_Data.addItems(dataAll)

        self.window_correlation_ui.pushButton_Reset_Options.clicked.connect(self.resetCorrelation)
        self.window_correlation_ui.pushButton_Add_To_Board.clicked.connect(self.writeCorrelationInBoard)

        self.window_correlation_ui.comboBox_Data.currentIndexChanged.connect(self.writeCorrelation)

        self.window_correlation.show()

    def writeCorrelation(self):
        try:
            data = self.window_correlation_ui.comboBox_Data.currentText()
            result = None
            self.window_correlation_ui.textEdit_Preview_Board.clear()

            data_frame = DataStorageModel.get(data)

            if data_frame is not None:
                correlation_matrix = data_frame.corr()
                result = correlation_matrix

            df = pd.DataFrame(result)
            html_table = df.to_html(classes='table', border=0, index=True, justify='center')
            html_table = html_table.replace('<table',
                                            '<table style="border: 1px solid black; border-collapse: collapse; padding: 10px;"')
            html_table = html_table.replace('<th>', '<th style="border: 1px solid black; padding: 5px;">')
            html_table = html_table.replace('<td>', '<td style="border: 1px solid black; padding: 5px;">')

            self.window_correlation_ui.textEdit_Preview_Board.setHtml(html_table)


        except Exception as e:
            print(str(e))

    def resetCorrelation(self):
        self.window_correlation_ui.comboBox_Data.setCurrentIndex(-1)
        self.window_correlation_ui.checkBox_Board_Is_Enabled.setChecked(False)
        self.window_correlation_ui.textEdit_Preview_Board.clear()
        self.window_correlation_ui.textEdit_Preview_Board.setReadOnly(True)

    def writeCorrelationInBoard(self):
        try:
            data = self.window_correlation_ui.textEdit_Preview_Board.toHtml()
            if data:
                cursor = self.main.textEdit_Board.textCursor()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                cursor.insertText("\n")
                cursor.insertHtml(data)
        except Exception as e:
            pass
