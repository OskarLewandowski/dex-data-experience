import numpy as np
import pandas as pd
from scipy import stats
from PyQt6 import QtGui
from PyQt6.QtWidgets import QMainWindow
from Models.data_storage_model import DataStorageModel
from Views.Main.main_window import Ui_MainWindow_Main
from Views.Analysis.basic_stats_window import Ui_MainWindow_Basic_Stats
from Views.Analysis.correlation_window import Ui_MainWindow_Correlation
from Views.Analysis.test_shapiro_wilka_window import Ui_MainWindow_Test_Shapiro_Wilka
from Views.Analysis.test_andersona_darlinga_window import Ui_MainWindow_Test_Andersona_Darlinga
from Views.Analysis.test_kolmogorova_smirnova_window import Ui_MainWindow_Test_Kolomogorova_Smirnova


class AnalysisController(QMainWindow, Ui_MainWindow_Main):
    def __init__(self, main_controller):
        super().__init__()
        self.main = main_controller

        self.main.action_Basic_Stats.triggered.connect(self.createBasicStatsWindow)
        self.main.action_Correlation.triggered.connect(self.createCorrelationWindow)
        self.main.action_Test_Shapiro_Wilka.triggered.connect(self.createTestShapiroWilkaWindow)
        self.main.action_Test_Andersona_Darlinga.triggered.connect(self.createTestAndersonaDarlingaWindow)
        self.main.action_Test_Kolmogorova_Smirnova.triggered.connect(self.createTestKolmogorovaSmirnovaWindow)

    def splitText(self, text, seperator=" : "):
        if seperator in str(text):
            textParts = str(text).split(seperator)
            return textParts
        else:
            return None

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
                          f"Maksimum: <b>{round(selectedColumn.max(), 2)}</b><br>"
                          f"Pierwszy kwantyl: <b>{round(selectedColumn.quantile(0.25), 2)}</b><br>"
                          f"Trzeci kwantyl: <b>{round(selectedColumn.quantile(0.75), 2)}</b><br>"
                          f"Rozstęp: <b>{round(selectedColumn.max() - selectedColumn.min(), 2)}</b><br>"
                          f"Skośność: <b>{round(selectedColumn.skew(), 2)}</b><br>"
                          f"Kurtoza: <b>{round(selectedColumn.kurt(), 2)}</b>")

            elif dataType == 1:
                result = (f"<b>Podstawowe statystyki</b><br>"
                          f"Zbiór: {result[0]}<br>"
                          f"Kolumna: {result[1]}<br>"
                          f"Typ danych: jakościowe<br><br>"
                          f"Liczba unikalnych wartości: <b>{selectedColumn.nunique()}</b><br>"
                          f"Najczęstsza wartość: <b>{selectedColumn.mode().iloc[0]}</b><br>"
                          f"Liczba wystąpień najczęstszej wartości: <b>{selectedColumn.value_counts().max()}</b><br>"
                          f"Procent najczęstszej wartości: <b>{round((selectedColumn.value_counts().max() / len(selectedColumn)) * 100, 2)}%</b><br>"
                          f"Najrzadsza wartość: <b>{selectedColumn.value_counts().idxmin()}</b><br>"
                          f"Liczba wystąpień najrzadszej wartości: <b>{selectedColumn.value_counts().min()}</b><br>"
                          f"Procent najrzadszej wartości: <b>{round((selectedColumn.value_counts().min() / len(selectedColumn)) * 100, 2)}%</b><br>"
                          f"Procent wartości unikalnych: <b>{round((selectedColumn.nunique() / selectedColumn.count()) * 100, 2)}%</b><br>"
                          f"Miara różnorodności Gini-Simpson Index: <b>{round(1 - sum(selectedColumn.value_counts(normalize=True) ** 2), 2)}</b><br>"
                          f"Entropia: <b>{round(-sum((selectedColumn.value_counts(normalize=True) * np.log2(selectedColumn.value_counts(normalize=True)))), 2)}</b>")
            else:
                result = (f"<b>Podstawowe statystyki</b><br>"
                          f"Zbiór: {result[0]}<br>"
                          f"Kolumna: {result[1]}<br>"
                          f"<u>Dane wymagają oczyszczenia<u>")

            self.window_basic_stats_ui.textEdit_Preview_Board.setText(str(result))


        except Exception as e:
            print(str(e))

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
        self.window_correlation_ui.comboBox_Data.currentIndexChanged.connect(self.fillDataColumns)

        self.window_correlation_ui.listWidget_Data_Columns.itemSelectionChanged.connect(self.writeCorrelation)
        self.window_correlation_ui.checkBox_Description_Of_Results.clicked.connect(self.writeCorrelation)

        self.window_correlation.show()

    def fillDataColumns(self):
        data = self.window_correlation_ui.comboBox_Data.currentText()
        if data:
            df = pd.DataFrame(DataStorageModel.get(data))
            df = df.columns.tolist()
            self.window_correlation_ui.listWidget_Data_Columns.clear()
            self.window_correlation_ui.listWidget_Data_Columns.addItems(df)
            self.window_correlation_ui.listWidget_Data_Columns.setEnabled(True)
        else:
            self.window_correlation_ui.listWidget_Data_Columns.setEnabled(False)
            self.window_correlation_ui.listWidget_Data_Columns.clear()
            self.window_correlation_ui.textEdit_Preview_Board.clear()

    def writeCorrelation(self):
        try:
            data = self.window_correlation_ui.comboBox_Data.currentText()
            result = None
            self.window_correlation_ui.textEdit_Preview_Board.clear()

            selectedItems = self.window_correlation_ui.listWidget_Data_Columns.selectedItems()
            title = f"<b>Korelacja Pearsona - liniowa zależność między dwoma zmiennymi</b><br>"

            description = ("<br><br><b>Interpretacja wyników:</b>"
                           "<ul>"
                           "<li>Liczba w każdej komórce pokazuje siłę i kierunek korelacji.</li>"
                           "<li>Dodatnie liczby wskazują na dodatnią korelację, podczas gdy ujemne liczby wskazują na ujemną korelację.</li>"
                           "<li>Im bliżej liczby do 1 (lub -1), tym silniejsza jest korelacja.</li>"
                           "<li>Liczba 0 oznacza brak korelacji między dwoma zmiennymi.</li>"
                           "</ul>")

            if selectedItems:
                column_names = [item.text() for item in selectedItems]

                data_frame = DataStorageModel.get(data)
                data_frame = data_frame[column_names]

            else:
                data_frame = DataStorageModel.get(data)

            try:
                if data_frame is not None:
                    correlation_matrix = data_frame.corr()
                    result = correlation_matrix
            except:
                result = f"Nieprawidłowe dane w zbiorze '{data}', wymagane są dane numeryczne!<br>Wybierz kolumny zawierające dane ilościowe."
                self.window_correlation_ui.textEdit_Preview_Board.setHtml(result)

            df = pd.DataFrame(result)
            html_table = df.to_html(classes='table', border=0, index=True, justify='center')
            html_table = html_table.replace('<table',
                                            '<table style="border: 1px solid black; border-collapse: collapse; padding: 10px;"')
            html_table = html_table.replace('<th>', '<th style="border: 1px solid black; padding: 5px;">')
            html_table = html_table.replace('<td>', '<td style="border: 1px solid black; padding: 5px;">')

            if self.window_correlation_ui.checkBox_Description_Of_Results.isChecked():
                result = title + html_table + description
            else:
                result = title + html_table

            if data:
                self.window_correlation_ui.textEdit_Preview_Board.setHtml(result)

        except Exception as e:
            pass

    def resetCorrelation(self):
        self.window_correlation_ui.comboBox_Data.setCurrentIndex(-1)
        self.window_correlation_ui.checkBox_Board_Is_Enabled.setChecked(False)
        self.window_correlation_ui.textEdit_Preview_Board.clear()
        self.window_correlation_ui.textEdit_Preview_Board.setReadOnly(True)
        self.window_correlation_ui.checkBox_Description_Of_Results.setChecked(False)

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

    # Test Shapiro-Wilka
    def createTestShapiroWilkaWindow(self):
        self.window_test_shapiro_wilka = QMainWindow()
        self.window_test_shapiro_wilka_ui = Ui_MainWindow_Test_Shapiro_Wilka()
        self.window_test_shapiro_wilka_ui.setupUi(self.window_test_shapiro_wilka)

        dataAll = DataStorageModel.get_all_keys_and_columns()

        self.window_test_shapiro_wilka_ui.comboBox_Data_Column.addItems(dataAll)

        self.window_test_shapiro_wilka_ui.pushButton_Reset_Options.clicked.connect(self.resetTestShapiroWilka)
        self.window_test_shapiro_wilka_ui.pushButton_Add_To_Board.clicked.connect(self.writeTestShapiroWilkaInBoard)

        self.window_test_shapiro_wilka_ui.comboBox_Data_Column.currentIndexChanged.connect(self.writeTestShapiroWilka)

        self.window_test_shapiro_wilka_ui.checkBox_Description_Of_Results.clicked.connect(self.writeTestShapiroWilka)

        self.window_test_shapiro_wilka.show()

    def writeTestShapiroWilka(self):
        try:
            data = self.window_test_shapiro_wilka_ui.comboBox_Data_Column.currentText()
            result = None
            summary = ""

            if data:
                result = self.splitText(data)
                dataType = self.checkColumnType(data)
                selectedColumn = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if data else None
                title = f"<b>Test Shapiro Wilka - test normalności danych</b><br>"

                description = ("<br><b>Interpretacja wyników:</b><br><br>"
                               "<b>Statystyka testu:</b> Ta wartość powinna być bliska 1 dla próbki o rozkładzie normalnym. Im bardziej wartość ta odbiega od 1, tym bardziej dane odbiegają od rozkładu normalnego."
                               "<br><b>Wartość p:</b> Jest to prawdopodobieństwo, że obserwujemy dane tak ekstremalne jak te, które mamy, zakładając, że hipoteza zerowa jest prawdziwa. W kontekście testu Shapiro-Wilka, hipoteza zerowa zakłada, że dane mają rozkład normalny."
                               "<ul>"
                               "<li>Jeżeli <b>wartość p jest mniejsza</b> od wybranego poziomu istotności (np. 0.05), odrzucamy hipotezę zerową. To sugeruje, że dane nie mają rozkładu normalnego.</li>"
                               "<li>Jeżeli <b>wartość p jest większa</b> od wybranego poziomu istotności, nie ma podstaw do odrzucenia hipotezy zerowej. To sugeruje, że dane mają rozkład normalny.</li>"
                               "</ul>")

                self.window_test_shapiro_wilka_ui.textEdit_Preview_Board.clear()

                if dataType == 0:
                    statistic, p_value = stats.shapiro(selectedColumn)

                    testResult = (f"Zbiór: <b>{result[0]}</b><br>"
                                  f"Kolumna: <b>{result[1]}</b><br><br>"
                                  f"Statystyka testu: <b>{round(statistic, 2)}</b><br>"
                                  f"Wartość p: <b>{round(p_value, 2)}</b><br>")

                    summary = title + testResult

                    if self.window_test_shapiro_wilka_ui.checkBox_Description_Of_Results.isChecked():
                        summary = summary + description

                else:
                    summary = (f"Nieprawidłowe dane w kolumnie <b>'{result[1]}'</b>, wymagane są dane numeryczne!<br>"
                               f"Wybierz kolumne zawierające dane ilościowe.")

            self.window_test_shapiro_wilka_ui.textEdit_Preview_Board.setHtml(summary)

        except Exception as e:
            print(str(e))

    def resetTestShapiroWilka(self):
        self.window_test_shapiro_wilka_ui.comboBox_Data_Column.setCurrentIndex(-1)
        self.window_test_shapiro_wilka_ui.checkBox_Board_Is_Enabled.setChecked(False)
        self.window_test_shapiro_wilka_ui.textEdit_Preview_Board.clear()
        self.window_test_shapiro_wilka_ui.textEdit_Preview_Board.setReadOnly(True)
        self.window_test_shapiro_wilka_ui.checkBox_Description_Of_Results.setChecked(False)

    def writeTestShapiroWilkaInBoard(self):
        try:
            data = self.window_test_shapiro_wilka_ui.textEdit_Preview_Board.toHtml()
            if data:
                cursor = self.main.textEdit_Board.textCursor()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                cursor.insertText("\n")
                cursor.insertHtml(data)
        except Exception as e:
            pass

    # Test Andersona-Darlinga
    def createTestAndersonaDarlingaWindow(self):
        self.window_test_andersona_darlinga = QMainWindow()
        self.window_test_andersona_darlinga_ui = Ui_MainWindow_Test_Andersona_Darlinga()
        self.window_test_andersona_darlinga_ui.setupUi(self.window_test_andersona_darlinga)

        dataAll = DataStorageModel.get_all_keys_and_columns()

        self.window_test_andersona_darlinga_ui.comboBox_Data_Column.addItems(dataAll)

        self.window_test_andersona_darlinga_ui.pushButton_Reset_Options.clicked.connect(self.resetTestAndersonaDarlinga)
        self.window_test_andersona_darlinga_ui.pushButton_Add_To_Board.clicked.connect(
            self.writeTestAndersonaDarlingaInBoard)

        self.window_test_andersona_darlinga_ui.comboBox_Data_Column.currentIndexChanged.connect(
            self.writeTestAndersonaDarlinga)

        self.window_test_andersona_darlinga_ui.checkBox_Description_Of_Results.clicked.connect(
            self.writeTestAndersonaDarlinga)

        self.window_test_andersona_darlinga.show()

    def writeTestAndersonaDarlinga(self):
        try:
            data = self.window_test_andersona_darlinga_ui.comboBox_Data_Column.currentText()
            result = None
            summary = ""

            if data:
                result = self.splitText(data)
                dataType = self.checkColumnType(data)
                selectedColumn = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if data else None
                title = f"<b>Test Andersona Darlinga - test normalności danych</b><br>"

                description = ("<br><br><b>Interpretacja wyników:</b><br><br>"
                               "<b>Statystyka testowa:</b> Reprezentuje wartość testu. Im większa statystyka, tym bardziej dane różnią się od teoretycznego rozkładu."
                               "<br><b>Wartości krytyczne:</b> Są to punkty odcięcia, poza którymi statystyka testowa jest na tyle ekstremalna, że odrzucamy hipotezę zerową. Im większa wartość krytyczna, tym bardziej ekstremalna musi być statystyka testowa, aby odrzucić hipotezę zerową."
                               "<br><b>Poziomy istotności:</b> Określają poziomy ryzyka, przy których odrzucamy hipotezę zerową. Powszechnie stosowane poziomy istotności to 15%, 10%, 5%, 2.5% i 1%."
                               "<ul>"
                               "<li>Jeżeli <b>statystyka testowa jest mniejsza</b> od wartości krytycznej na danym poziomie istotności, nie ma podstaw do odrzucenia hipotezy zerowej. To sugeruje, że dane mają rozkład normalny.</li>"
                               "<li>Jeżeli <b>statystyka testowa jest większa</b> od wartości krytycznej na danym poziomie istotności, odrzucamy hipotezę zerową. To sugeruje, że dane nie mają rozkładu normalnego.</li>"
                               "</ul>"
                               )

                self.window_test_andersona_darlinga_ui.textEdit_Preview_Board.clear()

                if dataType == 0:
                    statistic, critical_values, significance_level = stats.anderson(selectedColumn)

                    testResult = (
                        f"Zbiór: <b>{result[0]}</b><br>"
                        f"Kolumna: <b>{result[1]}</b><br>"
                        "<table>"
                        f"<tr><td>Statystyka testowa:&nbsp;&nbsp;</td><td><b>{round(statistic, 2)}</b></td></tr>"
                        f"<tr><td>Wartości krytyczne:&nbsp;&nbsp;</td><td><b>{'</b></td><td><b> &nbsp;&nbsp;'.join(map(lambda x: f'{x:.2f}', critical_values))}</b></td></tr>"
                        f"<tr><td>Poziomy istotności:&nbsp;&nbsp;</td><td><b>{'</b></td><td><b> &nbsp;&nbsp;'.join(map(lambda x: f'{x:.2f}', significance_level))}</b></td></tr>"
                        "</table>"
                    )

                    summary = title + testResult

                    if self.window_test_andersona_darlinga_ui.checkBox_Description_Of_Results.isChecked():
                        summary = summary + description

                else:
                    summary = (f"Nieprawidłowe dane w kolumnie <b>'{result[1]}'</b>, wymagane są dane numeryczne!<br>"
                               f"Wybierz kolumne zawierające dane ilościowe.")

            self.window_test_andersona_darlinga_ui.textEdit_Preview_Board.setHtml(summary)

        except Exception as e:
            print(str(e))

    def resetTestAndersonaDarlinga(self):
        self.window_test_andersona_darlinga_ui.comboBox_Data_Column.setCurrentIndex(-1)
        self.window_test_andersona_darlinga_ui.checkBox_Board_Is_Enabled.setChecked(False)
        self.window_test_andersona_darlinga_ui.textEdit_Preview_Board.clear()
        self.window_test_andersona_darlinga_ui.textEdit_Preview_Board.setReadOnly(True)
        self.window_test_andersona_darlinga_ui.checkBox_Description_Of_Results.setChecked(False)

    def writeTestAndersonaDarlingaInBoard(self):
        try:
            data = self.window_test_andersona_darlinga_ui.textEdit_Preview_Board.toHtml()
            if data:
                cursor = self.main.textEdit_Board.textCursor()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                cursor.insertText("\n")
                cursor.insertHtml(data)
        except Exception as e:
            pass

    # Test Kołmogorova-Smirnova
    def createTestKolmogorovaSmirnovaWindow(self):
        self.window_test_kolmogorova_smirnova = QMainWindow()
        self.window_test_kolmogorova_smirnova_ui = Ui_MainWindow_Test_Kolomogorova_Smirnova()
        self.window_test_kolmogorova_smirnova_ui.setupUi(self.window_test_kolmogorova_smirnova)

        dataAll = DataStorageModel.get_all_keys_and_columns()

        self.window_test_kolmogorova_smirnova_ui.comboBox_Data_Column.addItems(dataAll)

        self.window_test_kolmogorova_smirnova_ui.pushButton_Reset_Options.clicked.connect(
            self.resetTestKolmogorovaSmirnova)
        self.window_test_kolmogorova_smirnova_ui.pushButton_Add_To_Board.clicked.connect(
            self.writeTestKolmogorovaSmirnovaInBoard)

        self.window_test_kolmogorova_smirnova_ui.comboBox_Data_Column.currentIndexChanged.connect(
            self.writeTestKolmogorovaSmirnova)

        self.window_test_kolmogorova_smirnova_ui.checkBox_Description_Of_Results.clicked.connect(
            self.writeTestKolmogorovaSmirnova)

        self.window_test_kolmogorova_smirnova.show()

    def writeTestKolmogorovaSmirnova(self):
        try:
            data = self.window_test_kolmogorova_smirnova_ui.comboBox_Data_Column.currentText()
            result = None
            summary = ""

            if data:
                result = self.splitText(data)
                dataType = self.checkColumnType(data)
                selectedColumn = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if data else None
                title = f"<b>Test Kołmogorova Smirnova - test normalności danych</b><br>"

                description = ("<br><b>Interpretacja wyników:</b><br><br>"
                               "<b>Statystyka testu:</b> Jest to maksymalna różnica między dystrybuantą empiryczną próbki danych a dystrybuantą teoretyczną. Im większa jest ta wartość, tym bardziej prawdopodobne jest, że próbka danych nie pochodzi z rozkładu normalnego."
                               "<br><b>Wartość p:</b> Jest to prawdopodobieństwo, że obserwujemy dane tak ekstremalne jak te, które mamy, zakładając, że hipoteza zerowa jest prawdziwa. W kontekście jednopróbkowego testu Kołmogorova-Smirnova, hipoteza zerowa zakłada, że dane mają określony rozkład normalny."
                               "<ul>"
                               "<li>Jeżeli <b>wartość p jest mniejsza</b> od wybranego poziomu istotności (np. 0.05), odrzucamy hipotezę zerową. To sugeruje, że dane nie mają rozkładu normalnego.</li>"
                               "<li>Jeżeli <b>wartość p jest większa</b> od wybranego poziomu istotności, nie ma podstaw do odrzucenia hipotezy zerowej. To sugeruje, że dane mają rozkład normalny.</li>"
                               "</ul>")

                self.window_test_kolmogorova_smirnova_ui.textEdit_Preview_Board.clear()

                if dataType == 0:
                    statistic, p_value = stats.kstest(selectedColumn, cdf='norm')

                    testResult = (f"Zbiór: <b>{result[0]}</b><br>"
                                  f"Kolumna: <b>{result[1]}</b><br><br>"
                                  f"Statystyka testu: <b>{round(statistic, 2)}</b><br>"
                                  f"Wartość p: <b>{round(p_value, 2)}</b><br>")

                    summary = title + testResult

                    if self.window_test_kolmogorova_smirnova_ui.checkBox_Description_Of_Results.isChecked():
                        summary = summary + description

                else:
                    summary = (f"Nieprawidłowe dane w kolumnie <b>'{result[1]}'</b>, wymagane są dane numeryczne!<br>"
                               f"Wybierz kolumne zawierające dane ilościowe.")

            self.window_test_kolmogorova_smirnova_ui.textEdit_Preview_Board.setHtml(summary)

        except Exception as e:
            print(str(e))

    def resetTestKolmogorovaSmirnova(self):
        self.window_test_kolmogorova_smirnova_ui.comboBox_Data_Column.setCurrentIndex(-1)
        self.window_test_kolmogorova_smirnova_ui.checkBox_Board_Is_Enabled.setChecked(False)
        self.window_test_kolmogorova_smirnova_ui.textEdit_Preview_Board.clear()
        self.window_test_kolmogorova_smirnova_ui.textEdit_Preview_Board.setReadOnly(True)
        self.window_test_kolmogorova_smirnova_ui.checkBox_Description_Of_Results.setChecked(False)

    def writeTestKolmogorovaSmirnovaInBoard(self):
        try:
            data = self.window_test_kolmogorova_smirnova_ui.textEdit_Preview_Board.toHtml()
            if data:
                cursor = self.main.textEdit_Board.textCursor()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                cursor.insertText("\n")
                cursor.insertHtml(data)
        except Exception as e:
            pass
