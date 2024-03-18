import numpy as np
import pandas as pd
from statsmodels.stats.diagnostic import lilliefors
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
from Views.Analysis.test_lillieforsa_window import Ui_MainWindow_Test_Lillieforsa
from Views.Analysis.test_jarque_bera_window import Ui_MainWindow_Test_Jarque_Bera
from Views.Analysis.test_t_studenta_window import Ui_MainWindow_Test_T_Studenta
from Views.Analysis.test_anova_window import Ui_MainWindow_Test_ANOVA
from Views.Analysis.test_chi_square_window import Ui_MainWindow_Test_Chi_Square
from Views.Analysis.test_kruskal_wallis_window import Ui_MainWindow_Test_Kruskal_Wallis


class AnalysisController(QMainWindow, Ui_MainWindow_Main):
    def __init__(self, main_controller):
        super().__init__()
        self.main = main_controller

        self.main.action_Basic_Stats.triggered.connect(self.createBasicStatsWindow)
        self.main.action_Correlation.triggered.connect(self.createCorrelationWindow)
        self.main.action_Test_Shapiro_Wilka.triggered.connect(self.createTestShapiroWilkaWindow)
        self.main.action_Test_Andersona_Darlinga.triggered.connect(self.createTestAndersonaDarlingaWindow)
        self.main.action_Test_Kolmogorova_Smirnova.triggered.connect(self.createTestKolmogorovaSmirnovaWindow)
        self.main.action_Test_Lillieforsa.triggered.connect(self.createTestLillieforsaWindow)
        self.main.action_Test_Jarque_Bera.triggered.connect(self.createTestJarqueBeraWindow)
        self.main.action_Test_t_Studenta.triggered.connect(self.createTestTStudentaWindow)
        self.main.action_Test_ANOVA.triggered.connect(self.createTestAnovaWindow)
        self.main.action_Test_Chi_Square.triggered.connect(self.createTestChiSquareWindow)
        self.main.action_Test_Kruskala_Wallisa.triggered.connect(self.createTestKruskalaWallisaWindow)

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
        self.window_correlation_ui.comboBox_Data.currentIndexChanged.connect(self.fillDataColumnsCorrelation)

        self.window_correlation_ui.listWidget_Data_Columns.itemSelectionChanged.connect(self.writeCorrelation)
        self.window_correlation_ui.checkBox_Description_Of_Results.clicked.connect(self.writeCorrelation)

        self.window_correlation.show()

    def fillDataColumnsCorrelation(self):
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
                           "</ul><br>")

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
                               "</ul><br>")

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
                               "</ul><br>"
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
                               "</ul><br>")

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

    # Test Lillieforsa
    def createTestLillieforsaWindow(self):
        self.window_test_lillieforsa = QMainWindow()
        self.window_test_lillieforsa_ui = Ui_MainWindow_Test_Lillieforsa()
        self.window_test_lillieforsa_ui.setupUi(self.window_test_lillieforsa)

        dataAll = DataStorageModel.get_all_keys_and_columns()

        self.window_test_lillieforsa_ui.comboBox_Data_Column.addItems(dataAll)

        self.window_test_lillieforsa_ui.pushButton_Reset_Options.clicked.connect(self.resetTestLillieforsa)
        self.window_test_lillieforsa_ui.pushButton_Add_To_Board.clicked.connect(self.writeTestLillieforsaInBoard)

        self.window_test_lillieforsa_ui.comboBox_Data_Column.currentIndexChanged.connect(self.writeTestLillieforsa)

        self.window_test_lillieforsa_ui.checkBox_Description_Of_Results.clicked.connect(self.writeTestLillieforsa)

        self.window_test_lillieforsa.show()

    def writeTestLillieforsa(self):
        try:
            data = self.window_test_lillieforsa_ui.comboBox_Data_Column.currentText()
            result = None
            summary = ""

            if data:
                result = self.splitText(data)
                dataType = self.checkColumnType(data)
                selectedColumn = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if data else None
                title = f"<b>Test Lillieforsa - test normalności danych</b><br>"

                description = ("<br><b>Interpretacja wyników:</b><br><br>"
                               "<b>Statystyka testu:</b> Jest to maksymalna różnica między dystrybuantą empiryczną a teoretyczną dystrybuantą rozkładu normalnego."
                               "<br><b>Wartość p:</b> Jest to prawdopodobieństwo, że obserwujemy dane tak ekstremalne jak te, które mamy, zakładając, że hipoteza zerowa jest prawdziwa. W kontekście testu Lillieforsa, hipoteza zerowa zakłada, że dane mają rozkład normalny."
                               "<ul>"
                               "<li>Jeżeli <b>wartość p jest mniejsza</b> od wybranego poziomu istotności (np. 0.05), odrzucamy hipotezę zerową. To sugeruje, że dane nie mają rozkładu normalnego.</li>"
                               "<li>Jeżeli <b>wartość p jest większa</b> od wybranego poziomu istotności, nie ma podstaw do odrzucenia hipotezy zerowej. To sugeruje, że dane mają rozkład normalny.</li>"
                               "</ul><br>")

                self.window_test_lillieforsa_ui.textEdit_Preview_Board.clear()

                if dataType == 0:
                    statistic, p_value = lilliefors(selectedColumn)

                    testResult = (f"Zbiór: <b>{result[0]}</b><br>"
                                  f"Kolumna: <b>{result[1]}</b><br><br>"
                                  f"Statystyka testu: <b>{round(statistic, 2)}</b><br>"
                                  f"Wartość p: <b>{round(p_value, 2)}</b><br>")

                    summary = title + testResult

                    if self.window_test_lillieforsa_ui.checkBox_Description_Of_Results.isChecked():
                        summary = summary + description

                else:
                    summary = (f"Nieprawidłowe dane w kolumnie <b>'{result[1]}'</b>, wymagane są dane numeryczne!<br>"
                               f"Wybierz kolumne zawierające dane ilościowe.")

            self.window_test_lillieforsa_ui.textEdit_Preview_Board.setHtml(summary)

        except Exception as e:
            print(str(e))

    def resetTestLillieforsa(self):
        self.window_test_lillieforsa_ui.comboBox_Data_Column.setCurrentIndex(-1)
        self.window_test_lillieforsa_ui.checkBox_Board_Is_Enabled.setChecked(False)
        self.window_test_lillieforsa_ui.textEdit_Preview_Board.clear()
        self.window_test_lillieforsa_ui.textEdit_Preview_Board.setReadOnly(True)
        self.window_test_lillieforsa_ui.checkBox_Description_Of_Results.setChecked(False)

    def writeTestLillieforsaInBoard(self):
        try:
            data = self.window_test_lillieforsa_ui.textEdit_Preview_Board.toHtml()
            if data:
                cursor = self.main.textEdit_Board.textCursor()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                cursor.insertText("\n")
                cursor.insertHtml(data)
        except Exception as e:
            pass

    # Test Jarque-Bera
    def createTestJarqueBeraWindow(self):
        self.window_test_jarque_bera = QMainWindow()
        self.window_test_jarque_bera_ui = Ui_MainWindow_Test_Jarque_Bera()
        self.window_test_jarque_bera_ui.setupUi(self.window_test_jarque_bera)

        dataAll = DataStorageModel.get_all_keys_and_columns()

        self.window_test_jarque_bera_ui.comboBox_Data_Column.addItems(dataAll)

        self.window_test_jarque_bera_ui.pushButton_Reset_Options.clicked.connect(self.resetTestJarqueBera)
        self.window_test_jarque_bera_ui.pushButton_Add_To_Board.clicked.connect(self.writeTestJarqueBeraInBoard)

        self.window_test_jarque_bera_ui.comboBox_Data_Column.currentIndexChanged.connect(self.writeTestJarqueBera)

        self.window_test_jarque_bera_ui.checkBox_Description_Of_Results.clicked.connect(self.writeTestJarqueBera)

        self.window_test_jarque_bera.show()

    def writeTestJarqueBera(self):
        try:
            data = self.window_test_jarque_bera_ui.comboBox_Data_Column.currentText()
            result = None
            summary = ""

            if data:
                result = self.splitText(data)
                dataType = self.checkColumnType(data)
                selectedColumn = DataStorageModel.get_data_by_key_and_column(result[0], result[1]) if data else None
                title = f"<b>Test Jarque Bera - test normalności danych</b><br>"

                description = ("<br><b>Interpretacja wyników:</b><br><br>"
                               "<br><b>Wartość p:</b> Jest to prawdopodobieństwo, że obserwujemy dane tak ekstremalne jak te, które mamy, zakładając, że hipoteza zerowa jest prawdziwa. W kontekście testu Jarque-Bera, hipoteza zerowa zakłada, że dane mają rozkład normalny."
                               "<ul>"
                               "<li>Jeżeli <b>wartość p jest mniejsza</b> od wybranego poziomu istotności (np. 0.05), odrzucamy hipotezę zerową. To sugeruje, że dane nie mają rozkładu normalnego.</li>"
                               "<li>Jeżeli <b>wartość p jest większa</b> od wybranego poziomu istotności, nie ma podstaw do odrzucenia hipotezy zerowej. To sugeruje, że dane mogą pochodzić z rozkładu normalnego. Pamiętaj jednak, że nie jest to to samo co potwierdzenie, że dane pochodzą z rozkładu normalnego.</li>"
                               "</ul><br>")

                self.window_test_jarque_bera_ui.textEdit_Preview_Board.clear()

                if dataType == 0:
                    statistic, p_value = stats.jarque_bera(selectedColumn)

                    testResult = (f"Zbiór: <b>{result[0]}</b><br>"
                                  f"Kolumna: <b>{result[1]}</b><br><br>"
                                  f"Wartość p: <b>{round(p_value, 2)}</b><br>")

                    summary = title + testResult

                    if self.window_test_jarque_bera_ui.checkBox_Description_Of_Results.isChecked():
                        summary = summary + description

                else:
                    summary = (f"Nieprawidłowe dane w kolumnie <b>'{result[1]}'</b>, wymagane są dane numeryczne!<br>"
                               f"Wybierz kolumne zawierające dane ilościowe.")

            self.window_test_jarque_bera_ui.textEdit_Preview_Board.setHtml(summary)

        except Exception as e:
            print(str(e))

    def resetTestJarqueBera(self):
        self.window_test_jarque_bera_ui.comboBox_Data_Column.setCurrentIndex(-1)
        self.window_test_jarque_bera_ui.checkBox_Board_Is_Enabled.setChecked(False)
        self.window_test_jarque_bera_ui.textEdit_Preview_Board.clear()
        self.window_test_jarque_bera_ui.textEdit_Preview_Board.setReadOnly(True)
        self.window_test_jarque_bera_ui.checkBox_Description_Of_Results.setChecked(False)

    def writeTestJarqueBeraInBoard(self):
        try:
            data = self.window_test_jarque_bera_ui.textEdit_Preview_Board.toHtml()
            if data:
                cursor = self.main.textEdit_Board.textCursor()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                cursor.insertText("\n")
                cursor.insertHtml(data)
        except Exception as e:
            pass

    # Test t-Studenta
    def createTestTStudentaWindow(self):
        self.window_test_t_studenta = QMainWindow()
        self.window_test_t_studenta_ui = Ui_MainWindow_Test_T_Studenta()
        self.window_test_t_studenta_ui.setupUi(self.window_test_t_studenta)

        dataAll = DataStorageModel.get_all_keys_and_columns()

        self.window_test_t_studenta_ui.comboBox_Data_Column.addItems(dataAll)
        self.window_test_t_studenta_ui.comboBox_Data_Column_2.addItems(dataAll)

        self.window_test_t_studenta_ui.pushButton_Reset_Options.clicked.connect(self.resetTestTStudenta)
        self.window_test_t_studenta_ui.pushButton_Add_To_Board.clicked.connect(self.writeTestTStudentaInBoard)

        self.window_test_t_studenta_ui.comboBox_Data_Column.currentIndexChanged.connect(self.writeTestTStudenta)
        self.window_test_t_studenta_ui.comboBox_Data_Column_2.currentIndexChanged.connect(self.writeTestTStudenta)

        self.window_test_t_studenta_ui.checkBox_Description_Of_Results.clicked.connect(self.writeTestTStudenta)

        self.window_test_t_studenta.show()

    def writeTestTStudenta(self):
        try:
            data1 = self.window_test_t_studenta_ui.comboBox_Data_Column.currentText()
            data2 = self.window_test_t_studenta_ui.comboBox_Data_Column_2.currentText()

            result1 = None
            result2 = None

            summary = ""

            if data1 and data2:
                result1 = self.splitText(data1)
                result2 = self.splitText(data2)

                dataType1 = self.checkColumnType(data1)
                dataType2 = self.checkColumnType(data2)

                selectedColumn1 = DataStorageModel.get_data_by_key_and_column(result1[0], result1[1]) if data1 else None
                selectedColumn2 = DataStorageModel.get_data_by_key_and_column(result2[0], result2[1]) if data2 else None

                title = f"<b>Test t-Studenta - test różnicy między średnimi dwóch grup</b><br>"

                description = ("<br><b>Interpretacja wyników:</b><br><br>"
                               "<b>Statystyka testu:</b> Ta wartość reprezentuje różnicę między średnimi dwóch grup w odniesieniu do rozproszenia danych. Większa wartość t wskazuje na większą różnicę między grupami."
                               "<br><b>Wartość p:</b> Jest to prawdopodobieństwo, że obserwujemy dane tak ekstremalne jak te, które mamy, zakładając, że hipoteza zerowa jest prawdziwa. W kontekście testu t-Studenta, hipoteza zerowa zakłada, że średnie obu grup są równe."
                               "<ul>"
                               "<li>Jeżeli <b>wartość p jest mniejsza</b> od wybranego poziomu istotności (np. 0.05), odrzucamy hipotezę zerową. To sugeruje, że średnie obu grup są różne i różnica ta jest statystycznie istotna.</li>"
                               "<li>Jeżeli <b>wartość p jest większa</b> od wybranego poziomu istotności, nie ma podstaw do odrzucenia hipotezy zerowej. To sugeruje, że nie ma statystycznie istotnej różnicy między średnimi obu grup.</li>"
                               "</ul><br>")

                self.window_test_t_studenta_ui.textEdit_Preview_Board.clear()

                if dataType1 == 0 and dataType2 == 0:
                    statistic, p_value = stats.ttest_ind(selectedColumn1, selectedColumn2)

                    testResult = (f"Grupa 1: <b>{result1[0]} : {result1[1]}</b><br>"
                                  f"Grupa 2: <b>{result2[0]} : {result2[1]}</b><br><br>"
                                  f"Statystyka testu t: <b>{round(statistic, 2)}</b><br>"
                                  f"Wartość p: <b>{round(p_value, 2)}</b><br>")

                    summary = title + testResult

                    if self.window_test_t_studenta_ui.checkBox_Description_Of_Results.isChecked():
                        summary = summary + description

                else:
                    if dataType1 == 1 and dataType2 == 0:
                        summary = (
                            f"Nieprawidłowe dane w kolumnie <b>'{result1[1]}'</b>, wymagane są dane numeryczne!<br>"
                            f"Wybierz kolumne zawierające dane ilościowe.")
                    elif dataType1 == 0 and dataType2 == 1:
                        summary = (
                            f"Nieprawidłowe dane w kolumnie <b>'{result2[1]}'</b>, wymagane są dane numeryczne!<br>"
                            f"Wybierz kolumne zawierające dane ilościowe.")
                    else:
                        summary = (
                            f"Nieprawidłowe dane w kolumnach <b>'{result1[1]}' </b> oraz <b>'{result2[1]}'</b>, wymagane są dane numeryczne!<br>"
                            f"Wybierz kolumny zawierające dane ilościowe.")
            else:
                summary = ("Wybierz obie grupy danych do przeprowadzenia testu")

            self.window_test_t_studenta_ui.textEdit_Preview_Board.setHtml(summary)

        except Exception as e:
            print(str(e))

    def resetTestTStudenta(self):
        self.window_test_t_studenta_ui.comboBox_Data_Column.setCurrentIndex(-1)
        self.window_test_t_studenta_ui.checkBox_Board_Is_Enabled.setChecked(False)
        self.window_test_t_studenta_ui.textEdit_Preview_Board.clear()
        self.window_test_t_studenta_ui.textEdit_Preview_Board.setReadOnly(True)
        self.window_test_t_studenta_ui.checkBox_Description_Of_Results.setChecked(False)
        self.window_test_t_studenta_ui.comboBox_Data_Column_2.setCurrentIndex(-1)

    def writeTestTStudentaInBoard(self):
        try:
            data = self.window_test_t_studenta_ui.textEdit_Preview_Board.toHtml()
            if data:
                cursor = self.main.textEdit_Board.textCursor()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                cursor.insertText("\n")
                cursor.insertHtml(data)
        except Exception as e:
            pass

    # Test ANOVA
    def createTestAnovaWindow(self):
        self.window_test_anova = QMainWindow()
        self.window_test_anova_ui = Ui_MainWindow_Test_ANOVA()
        self.window_test_anova_ui.setupUi(self.window_test_anova)

        dataAll = DataStorageModel.get_all_keys()

        self.window_test_anova_ui.comboBox_Data.addItems(dataAll)

        self.window_test_anova_ui.pushButton_Reset_Options.clicked.connect(self.resetTestAnova)
        self.window_test_anova_ui.pushButton_Add_To_Board.clicked.connect(self.writeTestAnovaInBoard)

        self.window_test_anova_ui.comboBox_Data.currentIndexChanged.connect(self.writeTestAnova)
        self.window_test_anova_ui.comboBox_Data.currentIndexChanged.connect(self.fillDataColumnsTestAnova)

        self.window_test_anova_ui.listWidget_Data_Columns.itemSelectionChanged.connect(self.writeTestAnova)
        self.window_test_anova_ui.checkBox_Description_Of_Results.clicked.connect(self.writeTestAnova)

        self.window_test_anova.show()

    def writeTestAnova(self):
        try:
            self.window_test_anova_ui.textEdit_Preview_Board.clear()
            data = self.window_test_anova_ui.comboBox_Data.currentText()

            result = None
            groups = None

            dataError = False
            testResult = ""
            selectedItems = self.window_test_anova_ui.listWidget_Data_Columns.selectedItems()

            title = f"<b>Test ANOVA - test różnicy między średnimi wielu grup </b><br>"

            description = ("<br><br><b>Interpretacja wyników:</b><br><br>"
                           "<b>Statystyka testu F:</b> Ta wartość reprezentuje stosunek wariancji między grupami do wariancji wewnątrz grup. Większa wartość F sugeruje, że różnice między grupami są większe niż różnice wewnątrz grup. Wysoka wartość F sugeruje, że przynajmniej jedna z grup jest statystycznie różna od innych."
                           "<br><b>Wartość p:</b> Jest to prawdopodobieństwo, że obserwujemy dane tak ekstremalne jak te, które mamy, zakładając, że hipoteza zerowa jest prawdziwa. W kontekście testu ANOVA, hipoteza zerowa zakłada, że wszystkie grupy mają takie same średnie populacji."
                           "<ul>"
                           "<li>Jeżeli <b>wartość p jest mniejsza</b> od wybranego poziomu istotności (np. 0.05), odrzucamy hipotezę zerową. To sugeruje, że przynajmniej jedna z grup ma inną średnią.</li>"
                           "<li>Jeżeli <b>wartość p jest większa</b> od wybranego poziomu istotności, nie ma podstaw do odrzucenia hipotezy zerowej. To sugeruje, że wszystkie grupy mają takie same średnie populacji.</li>"
                           "</ul><br>")

            if selectedItems:
                column_names = [item.text() for item in selectedItems]

                data_frame = DataStorageModel.get(data)
                data_frame = data_frame[column_names]
                data_frame_columns_names = data_frame.columns.tolist()
                columns_names = ', '.join(data_frame_columns_names)

                groups = [data_frame[column].values for column in data_frame.columns]

            else:
                data_frame = DataStorageModel.get(data)
                data_frame_columns_names = data_frame.columns.tolist()
                columns_names = ', '.join(data_frame_columns_names)

                groups = [data_frame[column].values for column in data_frame.columns]

            try:
                if groups and len(data_frame_columns_names) > 1:
                    statistic, p_value = stats.f_oneway(*groups)

                    testResult = (f"Zbiór: <b>{data}</b><br>"
                                  f"Wybrane kolumny: <b>{columns_names}</b><br><br>"
                                  f"Statystyka testu t: <b>{round(statistic, 2)}</b><br>"
                                  f"Wartość p: <b>{round(p_value, 2)}</b>")

            except:
                dataError = True
                testResult = f"Nieprawidłowe dane w zbiorze '{data}', wymagane są dane numeryczne!<br>Wybierz kolumny zawierające dane ilościowe."
                self.window_test_anova_ui.textEdit_Preview_Board.setHtml(testResult)

            if self.window_test_anova_ui.checkBox_Description_Of_Results.isChecked() and dataError == False:
                result = title + testResult + description
            elif dataError == False:
                result = title + testResult
            else:
                result = testResult

            if data and len(data_frame_columns_names) > 1:
                self.window_test_anova_ui.textEdit_Preview_Board.setHtml(result)
            elif len(data_frame_columns_names) < 2:
                summary = ("Wybierz co najmniej dwie grupy danych do przeprowadzenia testu")
                self.window_test_anova_ui.textEdit_Preview_Board.setHtml(summary)


        except Exception as e:
            print(str(e))

    def resetTestAnova(self):
        self.window_test_anova_ui.comboBox_Data.setCurrentIndex(-1)
        self.window_test_anova_ui.listWidget_Data_Columns.clearSelection()
        self.window_test_anova_ui.checkBox_Board_Is_Enabled.setChecked(False)
        self.window_test_anova_ui.textEdit_Preview_Board.clear()
        self.window_test_anova_ui.textEdit_Preview_Board.setReadOnly(True)
        self.window_test_anova_ui.checkBox_Description_Of_Results.setChecked(False)

    def writeTestAnovaInBoard(self):
        try:
            data = self.window_test_anova_ui.textEdit_Preview_Board.toHtml()
            if data:
                cursor = self.main.textEdit_Board.textCursor()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                cursor.insertText("\n")
                cursor.insertHtml(data)
        except Exception as e:
            pass

    def fillDataColumnsTestAnova(self):
        data = self.window_test_anova_ui.comboBox_Data.currentText()
        if data:
            df = pd.DataFrame(DataStorageModel.get(data))
            df = df.columns.tolist()
            self.window_test_anova_ui.listWidget_Data_Columns.clear()
            self.window_test_anova_ui.listWidget_Data_Columns.addItems(df)
            self.window_test_anova_ui.listWidget_Data_Columns.setEnabled(True)
        else:
            self.window_test_anova_ui.listWidget_Data_Columns.setEnabled(False)
            self.window_test_anova_ui.listWidget_Data_Columns.clear()
            self.window_test_anova_ui.textEdit_Preview_Board.clear()

    # Test Chi-square
    def createTestChiSquareWindow(self):
        self.window_test_chi_square = QMainWindow()
        self.window_test_chi_square_ui = Ui_MainWindow_Test_Chi_Square()
        self.window_test_chi_square_ui.setupUi(self.window_test_chi_square)

        dataAll = DataStorageModel.get_all_keys()

        self.window_test_chi_square_ui.comboBox_Data.addItems(dataAll)

        self.window_test_chi_square_ui.pushButton_Reset_Options.clicked.connect(self.resetTestChiSquare)
        self.window_test_chi_square_ui.pushButton_Add_To_Board.clicked.connect(self.writeTestChiSquareInBoard)

        self.window_test_chi_square_ui.comboBox_Data.currentIndexChanged.connect(self.writeTestChiSquare)
        self.window_test_chi_square_ui.comboBox_Data.currentIndexChanged.connect(self.fillDataColumnsTestChiSquare)

        self.window_test_chi_square_ui.listWidget_Data_Columns.itemSelectionChanged.connect(self.writeTestChiSquare)
        self.window_test_chi_square_ui.checkBox_Description_Of_Results.clicked.connect(self.writeTestChiSquare)

        self.window_test_chi_square.show()

    def fillDataColumnsTestChiSquare(self):
        data = self.window_test_chi_square_ui.comboBox_Data.currentText()
        if data:
            df = pd.DataFrame(DataStorageModel.get(data))
            df = df.columns.tolist()
            self.window_test_chi_square_ui.listWidget_Data_Columns.clear()
            self.window_test_chi_square_ui.listWidget_Data_Columns.addItems(df)
            self.window_test_chi_square_ui.listWidget_Data_Columns.setEnabled(True)
        else:
            self.window_test_chi_square_ui.listWidget_Data_Columns.setEnabled(False)
            self.window_test_chi_square_ui.listWidget_Data_Columns.clear()
            self.window_test_chi_square_ui.textEdit_Preview_Board.clear()

    def writeTestChiSquare(self):
        try:
            data = self.window_test_chi_square_ui.comboBox_Data.currentText()

            result = None
            testResult = None

            self.window_test_chi_square_ui.textEdit_Preview_Board.clear()

            selectedItems = self.window_test_chi_square_ui.listWidget_Data_Columns.selectedItems()
            title = "<b>Test Chi-square - test zależności między grupami</b><br>"

            description = ("<br><br><b>Interpretacja wyników:</b><br><br>"
                           "<b>Statystyka testu:</b> Wartość statystyki testu Chi-kwadrat mierzy różnicę między obserwowanymi danymi a danymi oczekiwanymi. Im większa wartość Chi-kwadrat, tym większa różnica między danymi. Statystyka ta jest obliczana na podstawie kwadratu różnicy między obserwowanymi a oczekiwanymi liczbami przypadków, podzielonym przez wartość oczekiwaną dla każdej kategorii."
                           "<br><b>Wartość p:</b> Jest to prawdopodobieństwo, że obserwujemy dane tak ekstremalne jak te, które mamy, zakładając, że hipoteza zerowa jest prawdziwa. Hipoteza zerowa sugeruje brak zależności między zmiennymi. Odrzucenie hipotezy zerowej sugeruje istnienie zależności między zmiennymi."
                           "<ul>"
                           "<li>Jeżeli <b>wartość p jest mniejsza</b> od wybranego poziomu istotności (np. 0.05), odrzucamy hipotezę zerową. To sugeruje, że istnieje zależność między zmiennymi.</li>"
                           "<li>Jeżeli <b>wartość p jest większa</b> od wybranego poziomu istotności, nie ma podstaw do odrzucenia hipotezy zerowej. To sugeruje, że nie ma dowodów na zależność między zmiennymi.</li>"
                           "</ul><br>")

            if selectedItems:
                column_names = [item.text() for item in selectedItems]

                data_frame = DataStorageModel.get(data)
                data_frame = data_frame[column_names]
                data_frame_columns_names = data_frame.columns.tolist()
                columns_names = ', '.join(data_frame_columns_names)

            else:
                data_frame = DataStorageModel.get(data)
                data_frame_columns_names = data_frame.columns.tolist()
                columns_names = ', '.join(data_frame_columns_names)

            try:
                if data_frame is not None:
                    statistic, p_value, dof, expected = stats.chi2_contingency(data_frame)

                    testResult = (f"Zbiór: <b>{data}</b><br>"
                                  f"Wybrane kolumny: <b>{columns_names}</b><br><br>"
                                  f"Statystyka testu t: <b>{round(statistic, 2)}</b><br>"
                                  f"Wartość p: <b>{round(p_value, 2)}</b>")
            except:
                result = f"Nieprawidłowe dane w zbiorze '{data}', wymagane są dane numeryczne!<br>Wybierz kolumny zawierające dane ilościowe."
                self.window_test_chi_square_ui.textEdit_Preview_Board.setHtml(result)

            if self.window_test_chi_square_ui.checkBox_Description_Of_Results.isChecked():
                result = title + testResult + description
            else:
                result = title + testResult

            if data:
                self.window_test_chi_square_ui.textEdit_Preview_Board.setHtml(result)


        except Exception as e:
            pass

    def resetTestChiSquare(self):
        self.window_test_chi_square_ui.comboBox_Data.setCurrentIndex(-1)
        self.window_test_chi_square_ui.checkBox_Board_Is_Enabled.setChecked(False)
        self.window_test_chi_square_ui.textEdit_Preview_Board.clear()
        self.window_test_chi_square_ui.textEdit_Preview_Board.setReadOnly(True)
        self.window_test_chi_square_ui.checkBox_Description_Of_Results.setChecked(False)

    def writeTestChiSquareInBoard(self):
        try:
            data = self.window_test_chi_square_ui.textEdit_Preview_Board.toHtml()
            if data:
                cursor = self.main.textEdit_Board.textCursor()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                cursor.insertText("\n")
                cursor.insertHtml(data)
        except Exception as e:
            pass

    # Test Kruskala-Wallisa
    def createTestKruskalaWallisaWindow(self):
        self.window_test_kruskala_wallisa = QMainWindow()
        self.window_test_kruskala_wallisa_ui = Ui_MainWindow_Test_Kruskal_Wallis()
        self.window_test_kruskala_wallisa_ui.setupUi(self.window_test_kruskala_wallisa)

        dataAll = DataStorageModel.get_all_keys()

        self.window_test_kruskala_wallisa_ui.comboBox_Data.addItems(dataAll)

        self.window_test_kruskala_wallisa_ui.pushButton_Reset_Options.clicked.connect(self.resetTestKruskalaWallisa)
        self.window_test_kruskala_wallisa_ui.pushButton_Add_To_Board.clicked.connect(
            self.writeTestKruskalaWallisaInBoard)

        self.window_test_kruskala_wallisa_ui.comboBox_Data.currentIndexChanged.connect(self.writeTestKruskalaWallisa)
        self.window_test_kruskala_wallisa_ui.comboBox_Data.currentIndexChanged.connect(
            self.fillDataColumnsTestKruskalaWallisa)

        self.window_test_kruskala_wallisa_ui.listWidget_Data_Columns.itemSelectionChanged.connect(
            self.writeTestKruskalaWallisa)
        self.window_test_kruskala_wallisa_ui.checkBox_Description_Of_Results.clicked.connect(
            self.writeTestKruskalaWallisa)

        self.window_test_kruskala_wallisa.show()

    def fillDataColumnsTestKruskalaWallisa(self):
        data = self.window_test_kruskala_wallisa_ui.comboBox_Data.currentText()
        if data:
            df = pd.DataFrame(DataStorageModel.get(data))
            df = df.columns.tolist()
            self.window_test_kruskala_wallisa_ui.listWidget_Data_Columns.clear()
            self.window_test_kruskala_wallisa_ui.listWidget_Data_Columns.addItems(df)
            self.window_test_kruskala_wallisa_ui.listWidget_Data_Columns.setEnabled(True)
        else:
            self.window_test_kruskala_wallisa_ui.listWidget_Data_Columns.setEnabled(False)
            self.window_test_kruskala_wallisa_ui.listWidget_Data_Columns.clear()
            self.window_test_kruskala_wallisa_ui.textEdit_Preview_Board.clear()

    def writeTestKruskalaWallisa(self):
        try:
            self.window_test_kruskala_wallisa_ui.textEdit_Preview_Board.clear()
            data = self.window_test_kruskala_wallisa_ui.comboBox_Data.currentText()

            result = None
            dataError = False
            testResult = ""

            selectedItems = self.window_test_kruskala_wallisa_ui.listWidget_Data_Columns.selectedItems()

            title = "<b>Test Kruskala-Wallisa - test różnic między niezależnymi grupami</b><br>"

            description = ("<br><br><b>Interpretacja wyników:</b><br><br>"
                           "<b>Statystyka testu:</b> Wartość statystyki testu Kruskala-Wallisa mierzy różnicę między grupami danych. Im większa wartość statystyki, tym większa różnica między grupami. Statystyka ta jest obliczana na podstawie rang przypisanych poszczególnym obserwacjom."
                           "<br><b>Wartość p:</b> Jest to prawdopodobieństwo, że obserwujemy dane tak ekstremalne jak te, które mamy, zakładając, że hipoteza zerowa jest prawdziwa. Hipoteza zerowa sugeruje brak różnic między grupami. Odrzucenie hipotezy zerowej sugeruje istnienie różnic między grupami."
                           "<ul>"
                           "<li>Jeżeli <b>wartość p jest mniejsza</b> od wybranego poziomu istotności (np. 0.05), odrzucamy hipotezę zerową. To sugeruje, że istnieją istotne różnice między grupami.</li>"
                           "<li>Jeżeli <b>wartość p jest większa</b> od wybranego poziomu istotności, nie ma podstaw do odrzucenia hipotezy zerowej. To sugeruje, że nie ma dowodów na istotne różnice między grupami.</li>"
                           "</ul><br>")

            if selectedItems:
                column_names = [item.text() for item in selectedItems]

                data_frame = DataStorageModel.get(data)
                data_frame = data_frame[column_names]
                data_frame_columns_names = data_frame.columns.tolist()
                columns_names = ', '.join(data_frame_columns_names)

                groups = [data_frame[column].values for column in data_frame.columns]
            else:
                data_frame = DataStorageModel.get(data)
                data_frame_columns_names = data_frame.columns.tolist()
                columns_names = ', '.join(data_frame_columns_names)

                groups = [data_frame[column].values for column in data_frame.columns]
            try:
                if groups and len(data_frame_columns_names) > 1:
                    statistic, p_value = stats.kruskal(*groups)

                    testResult = (f"Zbiór: <b>{data}</b><br>"
                                  f"Wybrane kolumny: <b>{columns_names}</b><br><br>"
                                  f"Statystyka testu t: <b>{round(statistic, 2)}</b><br>"
                                  f"Wartość p: <b>{round(p_value, 2)}</b>")
            except:
                dataError = True
                testResult = f"Nieprawidłowe dane w zbiorze '{data}', wymagane są dane numeryczne!<br>Wybierz kolumny zawierające dane ilościowe."
                self.window_test_kruskala_wallisa_ui.textEdit_Preview_Board.setHtml(testResult)

            if self.window_test_kruskala_wallisa_ui.checkBox_Description_Of_Results.isChecked() and dataError == False:
                result = title + testResult + description
            elif dataError == False:
                result = title + testResult
            else:
                result = testResult

            if data and len(data_frame_columns_names) > 1:
                self.window_test_kruskala_wallisa_ui.textEdit_Preview_Board.setHtml(result)
            elif len(data_frame_columns_names) < 2:
                summary = ("Wybierz co najmniej dwie grupy danych do przeprowadzenia testu")
                self.window_test_kruskala_wallisa_ui.textEdit_Preview_Board.setHtml(summary)
        except Exception as e:
            pass

    def resetTestKruskalaWallisa(self):
        self.window_test_kruskala_wallisa_ui.comboBox_Data.setCurrentIndex(-1)
        self.window_test_kruskala_wallisa_ui.checkBox_Board_Is_Enabled.setChecked(False)
        self.window_test_kruskala_wallisa_ui.textEdit_Preview_Board.clear()
        self.window_test_kruskala_wallisa_ui.textEdit_Preview_Board.setReadOnly(True)
        self.window_test_kruskala_wallisa_ui.checkBox_Description_Of_Results.setChecked(False)

    def writeTestKruskalaWallisaInBoard(self):
        try:
            data = self.window_test_kruskala_wallisa_ui.textEdit_Preview_Board.toHtml()
            if data:
                cursor = self.main.textEdit_Board.textCursor()
                cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
                cursor.insertText("\n")
                cursor.insertHtml(data)
        except Exception as e:
            pass
