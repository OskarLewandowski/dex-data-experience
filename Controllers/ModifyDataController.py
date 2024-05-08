from PyQt6.QtWidgets import QMainWindow, QFileDialog, QCompleter, QDialog, QWidget
from Views.ModifyData.widget_info import Ui_Form_Info
from Views.ModifyData.dialog_search import Ui_Dialog_Search
from Views.ModifyData.change_headers import Ui_Dialog_change_headers
from Views.ModifyData.get_dummies import Ui_Dialog_Get_Dummies
from Views.ModifyData.delete_nan import Ui_Dialog_Delete_NaN
from Views.ModifyData.change_datatype import Ui_Dialog_Change_Datatype
from Views.ModifyData.delete import Ui_Dialog_Delete
from Views.ModifyData.replace import Ui_Dialog_Replace
from Views.ModifyData.modify_data_main_window import Ui_MainWindow_modify_data
from Models.data_storage_model import DataStorageModel
from Models.data_frame_model import DataFrameModel
from Models.message_model import MessageModel
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from reportlab.lib.pagesizes import letter
from pyreadr import pyreadr
import numpy as np
import pandas as pd
import io
import os


class ModifyDataController(QMainWindow, Ui_MainWindow_modify_data):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.child_windows = []
        self.currentDataFrameGlobal = None
        self.previousDataKeyGlobal = None
        self.window_info_widget = None
        self.search_dialog_window = None
        self.get_dummies_window = None
        self.delete_nan_window = None

        # Connections
        self.pushButton_Cancel.clicked.connect(self.close)
        self.action_Exit.triggered.connect(self.close)
        self.comboBox_Select_Data.currentIndexChanged.connect(self.loadDataWithReminderAboutSaveChanges)
        self.action_Save_as.triggered.connect(self.saveAsAction)
        self.action_More_Info.triggered.connect(self.createInfoWidget)
        self.action_Search.triggered.connect(self.createSearchDialog)
        self.action_Change_Headers.triggered.connect(self.createChangeHeaders)
        self.pushButton_Save.clicked.connect(self.saveChanges)
        self.action_Get_Dummies.triggered.connect(self.createGetDummies)
        self.action_Delete_Nan.triggered.connect(self.createDeleteNan)
        self.action_Change_Data_Type.triggered.connect(self.createChangeDataType)
        self.action_Delete.triggered.connect(self.createDelete)
        self.action_Change.triggered.connect(self.createReplace)

    def createWindowModifyData(self):
        """
        Show modify file window
        """
        self.updateDataFrameList()
        self.show()

    def closeEvent(self, event):
        self.closeOpenWindow()
        self.currentDataFrameGlobal = None
        self.previousDataKeyGlobal = None
        event.accept()

    def closeOpenWindow(self):
        if self.child_windows:
            for window in self.child_windows:
                if window.isVisible():
                    window.close()

            self.child_windows.clear()

    def updateDataFrameList(self):
        nameList = DataStorageModel.get_all_keys()

        if nameList:
            self.comboBox_Select_Data.clear()
            self.comboBox_Select_Data.addItems(nameList)
            self.tableView_Data_Frame.setModel(None)
            self.disableWindowFunction()
        else:
            self.comboBox_Select_Data.clear()
            self.tableView_Data_Frame.setModel(None)
            self.disableWindowFunction()

    # Replace
    def createReplace(self):
        self.replace_window = QDialog()
        self.replace_window_ui = Ui_Dialog_Replace()
        self.replace_window_ui.setupUi(self.replace_window)
        self.replace_window_ui.comboBox_Column_List_Select.currentIndexChanged.connect(self.addQCompleter)
        self.fillColumnNames()
        self.replace_window_ui.pushButton_Cancel.clicked.connect(self.replace_window.close)
        self.replace_window_ui.checkBox_Replace_All.toggled.connect(self.activeReplaceAll)
        self.replace_window_ui.pushButton_Apply.clicked.connect(self.applyReplace)

        self.replace_window.adjustSize()

        self.replace_window.show()

        self.child_windows.append(self.replace_window)

    def applyReplace(self):
        try:
            df = pd.DataFrame(self.currentDataFrameGlobal)

            valueToReplace = self.replace_window_ui.lineEdit_Value_To_Replace.text()
            newValue = self.replace_window_ui.lineEdit_New_Value.text()
            allColumnsIs = self.replace_window_ui.checkBox_Replace_All.isChecked()
            columnIs = self.replace_window_ui.comboBox_Column_List_Select.currentText()

            nanValueIs = self.replace_window_ui.checkBox_Value_Nan.isChecked()
            nullValueIs = self.replace_window_ui.checkBox_Value_Null.isChecked()

            try:
                valueToReplace = float(valueToReplace)
                newValue = float(newValue)
            except ValueError:
                pass

            if valueToReplace != "" and newValue != "" and (allColumnsIs is True or columnIs != ""):
                self.replace_window_ui.label_Info.clear()
                replace_dict = {valueToReplace: newValue}
                if nanValueIs:
                    replace_dict[np.NaN] = newValue
                if nullValueIs:
                    replace_dict[""] = newValue

                if allColumnsIs:
                    columns = df.columns.tolist()
                else:
                    columns = [columnIs]

                for column in columns:
                    df[column] = df[column].replace(replace_dict)

                self.replace_window_ui.label_Info.setText("Zamiana wybranych wartości zakończona pomyślnie")
                self.displayData(df)
                self.currentDataFrameGlobal = df

                self.updateAddQCompleter()
            else:
                self.replace_window_ui.label_Info.setText("Uzupełnij puste pola!")
        except Exception as e:
            MessageModel.error("0026", str(e))

    def fillColumnNames(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)
        columnName = df.columns.tolist()
        self.replace_window_ui.comboBox_Column_List_Select.addItems(columnName)

    def activeReplaceAll(self):
        if self.replace_window_ui.checkBox_Replace_All.isChecked():
            self.replace_window_ui.comboBox_Column_List_Select.setEnabled(False)
            self.addQCompleterAll()
        else:
            self.replace_window_ui.comboBox_Column_List_Select.setEnabled(True)
            self.addQCompleter()

    def updateAddQCompleter(self):
        if self.replace_window_ui.checkBox_Replace_All.isChecked():
            self.addQCompleterAll()
        elif not self.replace_window_ui.checkBox_Replace_All.isChecked():
            self.addQCompleter()

    def addQCompleterAll(self):
        try:
            if self.replace_window_ui.checkBox_Replace_All.isChecked():
                df = pd.DataFrame(self.currentDataFrameGlobal)
                nameColumns = df.columns.tolist()

                suggestions = set()

                for column in nameColumns:
                    unique_values = df[column].unique()
                    if len(unique_values) > 1:
                        column_suggestions = [str(item) for item in unique_values]
                        suggestions.update(column_suggestions)

                completer = QCompleter(list(suggestions))

                self.replace_window_ui.lineEdit_Value_To_Replace.setCompleter(completer)
        except Exception as e:
            MessageModel.error("0025", str(e))

    def addQCompleter(self):
        try:
            if not self.replace_window_ui.checkBox_Replace_All.isChecked():
                df = pd.DataFrame(self.currentDataFrameGlobal)
                nameColumn = self.replace_window_ui.comboBox_Column_List_Select.currentText()

                if nameColumn in df.columns:
                    suggestions = df[nameColumn].unique().tolist()
                    suggestions = [str(item) for item in suggestions]

                    completer = QCompleter(suggestions)
                    self.replace_window_ui.lineEdit_Value_To_Replace.setCompleter(completer)
                else:
                    pass
            else:
                pass
        except Exception as e:
            MessageModel.error("0024", str(e))

    # Delete
    def createDelete(self):
        self.delete_window = QDialog()
        self.delete_window_ui = Ui_Dialog_Delete()
        self.delete_window_ui.setupUi(self.delete_window)
        self.delete_window_ui.pushButton_Cancel.clicked.connect(self.delete_window.close)
        self.delete_window_ui.pushButton_Apply_Delete_Column.clicked.connect(self.deleteColumn)
        self.delete_window_ui.pushButton_Apply_Delete_Row.clicked.connect(self.deleteRow)
        self.fillListDelete()

        self.delete_window.adjustSize()

        self.delete_window.show()

        self.child_windows.append(self.delete_window)

    def fillListDelete(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)
        namesList = df.columns.tolist()
        rowCount = df.shape[0] - 1
        msg = "Wybierz numer wiersza od \'0\' do \'{}\'".format(rowCount)
        self.delete_window_ui.comboBox_Column_List_Select.addItems(namesList)
        self.delete_window_ui.spinBox_Row_Number_Select.setSpecialValueText(msg)
        self.delete_window_ui.spinBox_Row_Number_Select.setMaximum(rowCount)
        self.delete_window_ui.spinBox_Row_Number_Select.setValue(-1)

    def updateFillListDelete(self):
        self.delete_window_ui.comboBox_Column_List_Select.clear()
        self.delete_window_ui.spinBox_Row_Number_Select.clear()
        self.fillListDelete()

    def deleteColumn(self):
        try:
            df = pd.DataFrame(self.currentDataFrameGlobal)
            columnName = self.delete_window_ui.comboBox_Column_List_Select.currentText()
            df = df.drop(columnName, axis=1)
            self.currentDataFrameGlobal = df
            self.displayData(df)
            self.updateFillListDelete()
            msg = "Kolumna '{}' została usunięta".format(columnName)
            self.delete_window_ui.label_Info.setText(msg)
        except Exception as e:
            MessageModel.error("0023", "Nieprawidłowa nazwa kolumny!")

    def deleteRow(self):
        try:
            df = pd.DataFrame(self.currentDataFrameGlobal)
            index = self.delete_window_ui.spinBox_Row_Number_Select.value()
            df = df.drop(index)
            df = df.reset_index(drop=True)

            self.currentDataFrameGlobal = df
            self.displayData(df)
            self.updateFillListDelete()
            msg = "Wiersz '{}' został usunięty".format(index)
            self.delete_window_ui.label_Info.setText(msg)
        except Exception as e:
            MessageModel.error("0022", "Nieprawidłowy numer wiersza!")

    # DataType
    def createChangeDataType(self):
        self.change_datatype_window = QDialog()
        self.change_datatype_window_ui = Ui_Dialog_Change_Datatype()
        self.change_datatype_window_ui.setupUi(self.change_datatype_window)
        self.listCurrentDataTypes()
        self.listNewDataTyps()
        self.change_datatype_window_ui.pushButton_Apply.clicked.connect(self.applyChangeDataType)
        self.change_datatype_window_ui.pushButton_Cancel.clicked.connect(self.change_datatype_window.close)
        self.change_datatype_window.show()

        self.child_windows.append(self.change_datatype_window)

    def listCurrentDataTypes(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)
        namesList = df.columns.tolist()
        typesList = df.dtypes
        finalList = []

        for x, y in zip(namesList, typesList):
            add = "{0} : ({1})".format(x, y)
            finalList.append(add)

        self.change_datatype_window_ui.comboBox_Current_Datatype.addItems(finalList)

    def listNewDataTyps(self):
        dataTyps = ["Liczby całkowite : (int64)",
                    "Typ ogólny - tekstowy : (object)",
                    "Typ logiczny : (bool)",
                    "Liczby zmiennoprzecinkowe : (float64)",
                    "Data i czas : (datetime64)",
                    "Punkt czasowy : (timedelta64)"]

        self.change_datatype_window_ui.comboBox_New_Datatype.addItems(dataTyps)

    def applyChangeDataType(self):
        try:
            df = pd.DataFrame(self.currentDataFrameGlobal)
            namesListOrginal = df.columns.tolist()
            indexCurrentType = self.change_datatype_window_ui.comboBox_Current_Datatype.currentIndex()
            indexNewType = self.change_datatype_window_ui.comboBox_New_Datatype.currentIndex()

            dataTypes = ['int64', 'object', 'bool', 'float64', 'datetime64', 'timedelta64']

            df[namesListOrginal[indexCurrentType]] = df[namesListOrginal[indexCurrentType]].astype(
                dataTypes[indexNewType])

            self.displayData(df)
            self.currentDataFrameGlobal = df
            self.updateListCurrentDataTypes()
            msg = "Typ danych w kolumnie '{}' został pomyślnie zmieniony".format(namesListOrginal[indexCurrentType])
            self.change_datatype_window_ui.label_Info.setText(msg)
        except:
            msg = "Kolumna '{}' posiada nieodpowiednie dane".format(namesListOrginal[indexCurrentType])
            self.change_datatype_window_ui.label_Info.setText(msg)

    def updateListCurrentDataTypes(self):
        self.change_datatype_window_ui.comboBox_Current_Datatype.clear()
        self.change_datatype_window_ui.comboBox_New_Datatype.clear()

        self.listCurrentDataTypes()
        self.listNewDataTyps()

    # Delete NaN
    def createDeleteNan(self):
        if self.delete_nan_window is not None and self.delete_nan_window.isVisible():
            self.delete_nan_window.raise_()
            self.delete_nan_window.activateWindow()
        else:
            self.delete_nan_window = QDialog()
            self.delete_nan_window_ui = Ui_Dialog_Delete_NaN()
            self.delete_nan_window_ui.setupUi(self.delete_nan_window)

            self.delete_nan_window_ui.pushButton_Cancel.clicked.connect(self.delete_nan_window.close)
            self.delete_nan_window_ui.pushButton_Apply.clicked.connect(self.applyDeleteNan)
            self.messageInfoDeleteNan()

            self.delete_nan_window.adjustSize()
            self.delete_nan_window.show()

            self.child_windows.append(self.delete_nan_window)

    def messageInfoDeleteNan(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)
        rowCountBefore = df.shape[0] - 1
        df = df.dropna()
        rowCountAfter = df.shape[0] - 1

        rowSum = rowCountBefore - rowCountAfter

        if rowSum == 0:
            self.delete_nan_window_ui.pushButton_Apply.setEnabled(False)

        msg = ("Ilość wierszy przed usunięciem: {0}\n"
               "Ilość wierszy po usunięciu: {1}\n\n"
               "Czy chcesz usunąć {2} rekordów?").format(rowCountBefore, rowCountAfter, rowSum)
        self.delete_nan_window_ui.textEdit_Info.setText(msg)

    def applyDeleteNan(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)

        if df.isna().any().any():
            df = df.dropna()
            df = df.reset_index(drop=True)
            self.currentDataFrameGlobal = df
            self.displayData(df)
            self.messageInfoDeleteNan()

    # Get Dummies
    def createGetDummies(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)
        namesList = df.columns.tolist()

        if self.get_dummies_window is not None and self.get_dummies_window.isVisible():
            self.get_dummies_window_ui.comboBox_Select_Data.clear()
            self.get_dummies_window_ui.comboBox_Select_Data.addItems(namesList)

            self.get_dummies_window.raise_()
            self.get_dummies_window.activateWindow()
        else:
            self.get_dummies_window = QDialog()
            self.get_dummies_window_ui = Ui_Dialog_Get_Dummies()
            self.get_dummies_window_ui.setupUi(self.get_dummies_window)

            self.get_dummies_window_ui.comboBox_Select_Data.addItems(namesList)
            self.get_dummies_window_ui.pushButton_Apply.clicked.connect(self.applyGetDummies)
            self.get_dummies_window_ui.pushButton_Cancel.clicked.connect(self.get_dummies_window.close)

            self.get_dummies_window.show()

            self.child_windows.append(self.get_dummies_window)

    def applyGetDummies(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)
        nameColumn = self.get_dummies_window_ui.comboBox_Select_Data.currentText()

        if nameColumn:
            if self.get_dummies_window_ui.checkBox_Keep_Data.isChecked():
                dummies = pd.get_dummies(df[nameColumn], prefix=nameColumn)
                df = pd.concat([df, dummies], axis=1)
            else:
                df = pd.get_dummies(df, columns=[nameColumn])

            self.get_dummies_window_ui.label_Info.setText("Operacja wykonana pomyślnie!")
        else:
            self.get_dummies_window_ui.label_Info.setText("Wybierz kolumnę!")

        self.currentDataFrameGlobal = df
        self.updateGetDummiesList()

    def updateGetDummiesList(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)
        namesList = df.columns.tolist()
        self.get_dummies_window_ui.comboBox_Select_Data.clear()
        self.get_dummies_window_ui.comboBox_Select_Data.addItems(namesList)
        self.displayData(df)

    def saveChanges(self):
        try:
            confirmed = MessageModel.saveConfirmation(text="Czy na pewno chcesz zapisać zmiany?", bntYesText="Zapisz")
            if confirmed:
                df = pd.DataFrame(self.currentDataFrameGlobal)
                name = self.comboBox_Select_Data.currentText()
                DataStorageModel.update(name, df)
        except Exception as e:
            MessageModel.error("0021", str(e))

    def createChangeHeaders(self):
        try:
            namesList = self.currentDataFrameGlobal.columns.tolist()

            self.change_headers_window = QDialog()
            self.change_headers_window_ui = Ui_Dialog_change_headers()
            self.change_headers_window_ui.setupUi(self.change_headers_window)

            self.change_headers_window_ui.pushButton_Apply.clicked.connect(self.changeHeader)
            self.change_headers_window_ui.comboBox_headers_list.addItems(namesList)

            self.change_headers_window.show()

            self.child_windows.append(self.change_headers_window)
        except Exception as e:
            MessageModel.error("0036", str(e))

    def changeHeader(self):
        newHeader = self.change_headers_window_ui.lineEdit_new_header_name.text()
        currentHeader = self.change_headers_window_ui.comboBox_headers_list.currentText()
        namesList = self.currentDataFrameGlobal.columns.tolist()

        if newHeader != "" and currentHeader != "":
            if not newHeader in namesList:
                self.currentDataFrameGlobal.rename(columns={currentHeader: newHeader}, inplace=True)
                msg = "Nagłówek '{}' został zmieniony".format(currentHeader)
                self.change_headers_window_ui.label_info_text.setText(msg)
                self.updateHeaderList()
                self.change_headers_window_ui.lineEdit_new_header_name.clear()
            else:
                msg = "Nagłówek '{}' już istnieje".format(newHeader)
                self.change_headers_window_ui.label_info_text.setText(msg)
        else:
            self.change_headers_window_ui.label_info_text.setText("Pola nie mogą być puste")

    def updateHeaderList(self):
        namesList = self.currentDataFrameGlobal.columns.tolist()
        self.change_headers_window_ui.comboBox_headers_list.clear()
        self.change_headers_window_ui.comboBox_headers_list.addItems(namesList)
        self.displayData(self.currentDataFrameGlobal)

    # Search Dialog
    def createSearchDialog(self):
        if self.search_dialog_window is not None and self.search_dialog_window.isVisible():
            self.search_dialog_window.raise_()
            self.search_dialog_window.activateWindow()
        else:
            self.search_dialog_window = QDialog()
            self.search_dialog_window_ui = Ui_Dialog_Search()
            self.search_dialog_window_ui.setupUi(self.search_dialog_window)
            self.search_dialog_window_ui.pushButton_Clear.clicked.connect(self.closeActionSearchDialog)
            self.search_dialog_window_ui.pushButton_Search.clicked.connect(self.actionSearchDialog)
            self.search_dialog_window.closeEvent = self.closeEventSearchDialog
            self.search_dialog_window.show()

            self.child_windows.append(self.search_dialog_window)

    def closeEventSearchDialog(self, event):
        self.displayData(self.currentDataFrameGlobal)
        event.accept()

    def closeActionSearchDialog(self):
        self.search_dialog_window.close()

    def actionSearchDialog(self):
        try:
            search_phrase = str(self.search_dialog_window_ui.lineEdit_Search_Text.text())

            if not search_phrase:
                self.displayData(self.currentDataFrameGlobal)
            elif self.search_dialog_window_ui.checkBox_Case.isChecked():
                mask = self.currentDataFrameGlobal.astype(str).apply(
                    lambda row: row.str.contains(search_phrase, case=True).any(), axis=1)
            else:
                mask = self.currentDataFrameGlobal.astype(str).apply(
                    lambda row: row.str.contains(search_phrase, case=False).any(), axis=1)

            if search_phrase:
                filtered_data = self.currentDataFrameGlobal[mask]
                self.displayData(filtered_data)

        except Exception as e:
            MessageModel.error("0019", str(e))

    def loadDataFrame(self):
        try:
            dataKey = self.comboBox_Select_Data.currentText()

            if dataKey:
                self.enableWindowFunction()
                data = DataStorageModel.copy_by_key(dataKey)
                self.currentDataFrameGlobal = data
                self.previousDataKeyGlobal = dataKey
                self.displayData(data)
        except Exception as e:
            MessageModel.error("0034", str(e))

    def displayData(self, data):
        model = DataFrameModel(data)
        self.tableView_Data_Frame.setModel(model)

    def enableWindowFunction(self):
        self.menu_Edit.setEnabled(True)
        self.menu_Search.setEnabled(True)
        self.menu_Info.setEnabled(True)
        self.pushButton_Save.setEnabled(True)
        self.action_Save_as.setEnabled(True)

    def disableWindowFunction(self):
        self.menu_Edit.setEnabled(False)
        self.menu_Search.setEnabled(False)
        self.menu_Info.setEnabled(False)
        self.pushButton_Save.setEnabled(False)
        self.action_Save_as.setEnabled(False)

    def loadDataWithReminderAboutSaveChanges(self):
        try:
            dataKey = self.comboBox_Select_Data.currentText()
            previousDataKey = self.previousDataKeyGlobal

            if dataKey and self.currentDataFrameGlobal is None and previousDataKey is None:
                self.loadDataFrame()
            elif dataKey and previousDataKey:
                if dataKey != previousDataKey:
                    storageDataFrame = DataStorageModel.get(previousDataKey)

                    if not storageDataFrame.equals(self.currentDataFrameGlobal):
                        confirmed = MessageModel.saveConfirmation(
                            text=f"Czy chcesz zapisać zmiany w zbiorze '{previousDataKey}'?",
                            bntYesText="Zapisz zmiany",
                            bntAbortText="Nie zapisuj zmian")

                        if confirmed:
                            df = pd.DataFrame(self.currentDataFrameGlobal)
                            DataStorageModel.update(previousDataKey, df)

                        self.closeOpenWindow()
                        self.loadDataFrame()
                    else:
                        self.closeOpenWindow()
                        self.loadDataFrame()

                else:
                    self.closeOpenWindow()
                    self.loadDataFrame()

            else:
                self.closeOpenWindow()
                self.loadDataFrame()

        except:
            self.closeOpenWindow()
            self.loadDataFrame()

    def saveAsAction(self):
        try:
            fileFilter = ("CSV (rozdzielany przecinkami) (*.csv);;"
                          "TSV (rozdzielany tabulatorem) (*.tsv);;"
                          "Skoroszyt programu Excel (*.xlsx);;"
                          "Plik JSON (*.json);;"
                          "Plik XML (*.xml);;"
                          "Plik PDF (*.pdf);;"
                          "Plik R (*.RData)")

            currentDataName = self.comboBox_Select_Data.currentText()
            fileName = "{}.csv".format(currentDataName)

            saveFileName = QFileDialog.getSaveFileName(
                caption="Zapisz jako",
                directory=os.path.expanduser("~/Desktop/" + fileName),
                filter=fileFilter,
                initialFilter="CSV (rozdzielany przecinkami) (*.csv)"
            )

            if saveFileName[0]:
                df = pd.DataFrame(self.currentDataFrameGlobal)

                # Save to CSV
                if saveFileName[1] == "CSV (rozdzielany przecinkami) (*.csv)":
                    df.to_csv(saveFileName[0], index=False)
                elif saveFileName[1] == "TSV (rozdzielany tabulatorem) (*.tsv)":
                    df.to_csv(saveFileName[0], sep='\t', index=False)
                elif saveFileName[1] == "Skoroszyt programu Excel (*.xlsx)":
                    df.to_excel(saveFileName[0], index=False)
                elif saveFileName[1] == "Plik JSON (*.json)":
                    df.to_json(saveFileName[0], orient="records", index=False)
                elif saveFileName[1] == "Plik XML (*.xml)":
                    df.to_xml(saveFileName[0], index=False)
                elif saveFileName[1] == "Plik PDF (*.pdf)":
                    doc = SimpleDocTemplate(saveFileName[0], pagesize=letter)

                    elements = []
                    chunk_size = 1000

                    for i in range(0, len(df), chunk_size):
                        chunk = df.iloc[i:i + chunk_size]
                        table_data = [chunk.columns.tolist()] + chunk.values.tolist()
                        table = Table(table_data)

                        style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)),
                                            ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),
                                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                            ('BACKGROUND', (0, 1), (-1, -1), (0.85, 0.85, 0.85)),
                                            ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
                                            ])
                        table.setStyle(style)

                        elements.append(table)
                        elements.append(PageBreak())

                    doc.build(elements)
                elif saveFileName[1] == "Plik R (*.RData)":
                    pyreadr.write_rdata(saveFileName[0], df)

                MessageModel.statusSaveAsFile(saveFileName[0])

        except Exception as e:
            MessageModel.error("0018", str(e))

    # Info Widget
    def createInfoWidget(self):
        if self.window_info_widget is not None and self.window_info_widget.isVisible():
            self.window_info_widget.raise_()
            self.window_info_widget.activateWindow()
        else:
            self.window_info_widget = QWidget()
            self.window_info_widget_ui = Ui_Form_Info()
            self.window_info_widget_ui.setupUi(self.window_info_widget)
            self.window_info_widget.show()

            self.child_windows.append(self.window_info_widget)
            self.addDataToInfoWidgetWindow()

    def addDataToInfoWidgetWindow(self):
        if self.currentDataFrameGlobal is not None:
            buffer = io.StringIO()
            self.currentDataFrameGlobal.info(buf=buffer)
            info_text = buffer.getvalue()
            self.window_info_widget_ui.textEdit_info.setPlainText(info_text)
        else:
            self.window_info_widget_ui.textEdit_info.setPlainText("Wystąpił błąd: Brak danych")
