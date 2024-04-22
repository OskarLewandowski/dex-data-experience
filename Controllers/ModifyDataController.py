from PyQt6.QtWidgets import QMainWindow, QFileDialog, QCompleter, QDialog, QMessageBox, QWidget
from PyQt6 import QtGui
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

        self.currentDataFrameGlobal = None
        self.info_dialog = None

        # Connections
        self.pushButton_Cancel.clicked.connect(self.close)
        self.action_Exit.triggered.connect(self.close)
        self.comboBox_Select_Data.currentIndexChanged.connect(self.enableLoad)
        self.action_Save_as.triggered.connect(self.saveAsAction)
        self.action_More_Info.triggered.connect(self.showInfoWidget)
        self.action_Search.triggered.connect(self.openSearchDialog)
        self.action_Change_Headers.triggered.connect(self.openChangeHeaders)
        self.pushButton_Save.clicked.connect(self.saveChanges)
        self.action_Get_Dummies.triggered.connect(self.openGetDummies)
        self.action_Delete_Nan.triggered.connect(self.openDeleteNan)
        self.action_Change_Data_Type.triggered.connect(self.openChangeDataType)
        self.action_Delete.triggered.connect(self.openDelete)
        self.action_Change.triggered.connect(self.openReplace)

    def createWindowModifyData(self):
        """
        Show add file window
        """
        self.updateDataFrameList()
        self.show()

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

    def openReplace(self):
        self.comboBox_Select_Data.setEnabled(False)

        self.window = QDialog()
        self.ui = Ui_Dialog_Replace()
        self.ui.setupUi(self.window)
        self.window.closeEvent = self.closeEventReplace
        self.ui.comboBox_Column_List_Select.currentIndexChanged.connect(self.addQCompleter)
        self.fillColumnNames()
        self.ui.pushButton_Cancel.clicked.connect(self.window.close)
        self.ui.checkBox_Replace_All.toggled.connect(self.activeReplaceAll)
        self.ui.pushButton_Apply.clicked.connect(self.applyReplace)
        self.window.show()

    def applyReplace(self):
        try:
            df = pd.DataFrame(self.currentDataFrameGlobal)

            valueToReplace = self.ui.lineEdit_Value_To_Replace.text()
            newValue = self.ui.lineEdit_New_Value.text()
            allColumnsIs = self.ui.checkBox_Replace_All.isChecked()
            columnIs = self.ui.comboBox_Column_List_Select.currentText()

            nanValueIs = self.ui.checkBox_Value_Nan.isChecked()
            nullValueIs = self.ui.checkBox_Value_Null.isChecked()

            try:
                valueToReplace = float(valueToReplace)
                newValue = float(newValue)
            except ValueError:
                pass

            if valueToReplace != "" and newValue != "" and (allColumnsIs is True or columnIs != ""):
                self.ui.label_Info.clear()
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

                self.ui.label_Info.setText("Zamiana wybranych wartości zakończona pomyślnie")
                self.displayData(df)
                self.currentDataFrameGlobal = df
            else:
                self.ui.label_Info.setText("Uzupełnij puste pola!")
        except Exception as e:
            MessageModel.error("0026", str(e))

    def closeEventReplace(self, event):
        self.window.close()
        self.comboBox_Select_Data.setEnabled(True)
        event.accept()

    def fillColumnNames(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)
        columnName = df.columns.tolist()
        self.ui.comboBox_Column_List_Select.addItems(columnName)

    def activeReplaceAll(self):
        if self.ui.checkBox_Replace_All.isChecked():
            self.ui.comboBox_Column_List_Select.setEnabled(False)
            self.addQCompleterAll()
        else:
            self.ui.comboBox_Column_List_Select.setEnabled(True)
            self.addQCompleter()

    def addQCompleterAll(self):
        try:
            if self.ui.checkBox_Replace_All.isChecked():
                df = pd.DataFrame(self.currentDataFrameGlobal)
                nameColumns = df.columns.tolist()

                suggestions = set()

                for column in nameColumns:
                    unique_values = df[column].unique()
                    if len(unique_values) > 1:
                        column_suggestions = [str(item) for item in unique_values]
                        suggestions.update(column_suggestions)

                completer = QCompleter(list(suggestions))

                self.ui.lineEdit_Value_To_Replace.setCompleter(completer)
        except Exception as e:
            MessageModel.error("0025", str(e))

    def addQCompleter(self):
        try:
            if not self.ui.checkBox_Replace_All.isChecked():
                df = pd.DataFrame(self.currentDataFrameGlobal)
                nameColumn = self.ui.comboBox_Column_List_Select.currentText()

                if nameColumn in df.columns:
                    suggestions = df[nameColumn].unique().tolist()
                    suggestions = [str(item) for item in suggestions]

                    completer = QCompleter(suggestions)
                    self.ui.lineEdit_Value_To_Replace.setCompleter(completer)
                else:
                    pass
            else:
                pass
        except Exception as e:
            MessageModel.error("0024", str(e))

    def deleteColumn(self):
        try:
            df = pd.DataFrame(self.currentDataFrameGlobal)
            columnName = self.ui.comboBox_Column_List_Select.currentText()
            df = df.drop(columnName, axis=1)
            self.currentDataFrameGlobal = df
            self.displayData(df)
            self.updateFillListDelete()
            msg = "Kolumna '{}' została usunięta".format(columnName)
            self.ui.label_Info.setText(msg)
        except Exception as e:
            MessageModel.error("0023", str(e))

    def deleteRow(self):
        try:
            df = pd.DataFrame(self.currentDataFrameGlobal)
            index = self.ui.spinBox_Row_Number_Select.value()
            df = df.drop(index)
            df = df.reset_index(drop=True)

            self.currentDataFrameGlobal = df
            self.displayData(df)
            self.updateFillListDelete()
            msg = "Wiersz '{}' został usunięty".format(index)
            self.ui.label_Info.setText(msg)
        except Exception as e:
            MessageModel.error("0022", str(e))

    def openDelete(self):
        self.comboBox_Select_Data.setEnabled(False)

        self.window = QDialog()
        self.ui = Ui_Dialog_Delete()
        self.ui.setupUi(self.window)
        self.window.closeEvent = self.closeEventDelete
        self.ui.pushButton_Cancel.clicked.connect(self.window.close)
        self.ui.pushButton_Apply_Delete_Column.clicked.connect(self.deleteColumn)
        self.ui.pushButton_Apply_Delete_Row.clicked.connect(self.deleteRow)
        self.fillListDelete()
        self.window.show()

    def fillListDelete(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)
        namesList = df.columns.tolist()
        rowCount = df.shape[0] - 1
        msg = "Wybierz numer wiersza od \'0\' do \'{}\'".format(rowCount)
        self.ui.comboBox_Column_List_Select.addItems(namesList)
        self.ui.spinBox_Row_Number_Select.setSpecialValueText(msg)
        self.ui.spinBox_Row_Number_Select.setMaximum(rowCount)
        self.ui.spinBox_Row_Number_Select.setValue(-1)

    def updateFillListDelete(self):
        self.ui.comboBox_Column_List_Select.clear()
        self.ui.spinBox_Row_Number_Select.clear()
        self.fillListDelete()

    def closeEventDelete(self, event):
        self.window.close()
        self.comboBox_Select_Data.setEnabled(True)
        event.accept()

    def openChangeDataType(self):
        self.comboBox_Select_Data.setEnabled(False)

        self.window = QDialog()
        self.ui = Ui_Dialog_Change_Datatype()
        self.ui.setupUi(self.window)
        self.listCurrentDataTypes()
        self.listNewDataTyps()
        self.window.closeEvent = self.closeEventChangeDataType
        self.ui.pushButton_Apply.clicked.connect(self.applyChangeDataType)
        self.ui.pushButton_Cancel.clicked.connect(self.window.close)
        self.window.show()

    def listCurrentDataTypes(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)
        namesList = df.columns.tolist()
        typesList = df.dtypes
        finalList = []

        for x, y in zip(namesList, typesList):
            add = "{0} : ({1})".format(x, y)
            finalList.append(add)

        self.ui.comboBox_Current_Datatype.addItems(finalList)

    def listNewDataTyps(self):
        dataTyps = ["Liczby całkowite : (int64)",
                    "Typ ogólny - tekstowy : (object)",
                    "Typ logiczny : (bool)",
                    "Liczby zmiennoprzecinkowe : (float64)",
                    "Data i czas : (datetime64)",
                    "Punkt czasowy : (timedelta64)"]

        self.ui.comboBox_New_Datatype.addItems(dataTyps)

    def applyChangeDataType(self):
        try:
            df = pd.DataFrame(self.currentDataFrameGlobal)
            namesListOrginal = df.columns.tolist()
            indexCurrentType = self.ui.comboBox_Current_Datatype.currentIndex()
            indexNewType = self.ui.comboBox_New_Datatype.currentIndex()

            dataTypes = ['int64', 'object', 'bool', 'float64', 'datetime64', 'timedelta64']

            df[namesListOrginal[indexCurrentType]] = df[namesListOrginal[indexCurrentType]].astype(
                dataTypes[indexNewType])

            self.displayData(df)
            self.currentDataFrameGlobal = df
            self.updateListCurrentDataTypes()
            msg = "Typ danych w kolumnie '{}' został pomyślnie zmieniony".format(namesListOrginal[indexCurrentType])
            self.ui.label_Info.setText(msg)
        except:
            msg = "Kolumna '{}' posiada nieodpowiednie dane".format(namesListOrginal[indexCurrentType])
            self.ui.label_Info.setText(msg)

    def updateListCurrentDataTypes(self):
        self.ui.comboBox_Current_Datatype.clear()
        self.ui.comboBox_New_Datatype.clear()

        self.listCurrentDataTypes()
        self.listNewDataTyps()

    def closeEventChangeDataType(self, event):
        self.window.close()
        self.comboBox_Select_Data.setEnabled(True)
        event.accept()

    def openDeleteNan(self):
        self.comboBox_Select_Data.setEnabled(False)

        self.window = QDialog()
        self.ui = Ui_Dialog_Delete_NaN()
        self.ui.setupUi(self.window)
        self.ui.pushButton_Cancel.clicked.connect(self.window.close)
        self.window.closeEvent = self.closeEventDeleteNan
        self.ui.pushButton_Apply.clicked.connect(self.applyDeleteNan)
        self.messageInfoDeleteNan()
        self.window.show()

    def messageInfoDeleteNan(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)
        rowCountBefore = df.shape[0] - 1
        df = df.dropna()
        rowCountAfter = df.shape[0] - 1

        rowSum = rowCountBefore - rowCountAfter

        if rowSum == 0:
            self.ui.pushButton_Apply.setEnabled(False)

        msg = ("Ilość wierszy przed usunięciem: {0}\n"
               "Ilość wierszy po usunięciu: {1}\n\n"
               "Czy chcesz usunąć {2} rekordów?").format(rowCountBefore, rowCountAfter, rowSum)
        self.ui.textEdit_Info.setText(msg)

    def applyDeleteNan(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)

        if df.isna().any().any():
            df = df.dropna()
            df = df.reset_index(drop=True)
            self.currentDataFrameGlobal = df
            self.displayData(df)
            self.messageInfoDeleteNan()

    def closeEventDeleteNan(self, event):
        self.window.close()
        self.comboBox_Select_Data.setEnabled(True)
        event.accept()

    def openGetDummies(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)
        namesList = df.columns.tolist()

        self.comboBox_Select_Data.setEnabled(False)

        self.get_dummies_window = QDialog()
        self.get_dummies_window_ui = Ui_Dialog_Get_Dummies()
        self.get_dummies_window_ui.setupUi(self.get_dummies_window)

        self.get_dummies_window_ui.comboBox_Select_Data.addItems(namesList)
        self.get_dummies_window_ui.pushButton_Apply.clicked.connect(self.applyGetDummies)
        self.get_dummies_window_ui.pushButton_Cancel.clicked.connect(self.get_dummies_window.close)

        self.get_dummies_window.closeEvent = self.closeEventGetDummies

        self.get_dummies_window.show()

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

    def closeEventGetDummies(self, event):
        self.get_dummies_window.close()
        self.comboBox_Select_Data.setEnabled(True)
        event.accept()

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

    def openChangeHeaders(self):

        df = pd.DataFrame(self.currentDataFrameGlobal)
        namesList = df.columns.tolist()

        self.comboBox_Select_Data.setEnabled(False)

        self.window = QDialog()
        self.ui = Ui_Dialog_change_headers()
        self.ui.setupUi(self.window)

        self.window.closeEvent = self.closeEventChangeHeader
        self.ui.pushButton_Cancel.clicked.connect(self.window.close)
        self.ui.pushButton_Apply.clicked.connect(self.changeHeader)
        self.ui.comboBox_headers_list.addItems(namesList)

        self.window.show()

    def changeHeader(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)
        newHeader = self.ui.lineEdit_new_header_name.text()
        currentHeader = self.ui.comboBox_headers_list.currentText()
        namesList = df.columns.tolist()

        if newHeader != "" and currentHeader != "":
            if not newHeader in namesList:
                df.rename(columns={currentHeader: newHeader}, inplace=True)
                self.currentDataFrameGlobal = df
                msg = "Nagłówek '{}' został zmieniony".format(currentHeader)
                self.ui.label_info_text.setText(msg)
                self.updateHeaderList()
                self.ui.lineEdit_new_header_name.clear()
            else:
                msg = "Nagłówek '{}' już istnieje".format(newHeader)
                self.ui.label_info_text.setText(msg)
        else:
            self.ui.label_info_text.setText("Pola nie mogą być puste")

    def updateHeaderList(self):
        df = pd.DataFrame(self.currentDataFrameGlobal)
        namesList = df.columns.tolist()
        self.ui.comboBox_headers_list.clear()
        self.ui.comboBox_headers_list.addItems(namesList)
        self.displayData(df)

    def closeEventChangeHeader(self, event):
        self.window.close()
        self.comboBox_Select_Data.setEnabled(True)
        event.accept()

    def openSearchDialog(self):
        self.comboBox_Select_Data.setEnabled(False)

        self.window = QDialog()
        self.ui = Ui_Dialog_Search()
        self.ui.setupUi(self.window)
        self.ui.pushButton_Clear.clicked.connect(self.closeActionSearchDialog)
        self.ui.pushButton_Search.clicked.connect(self.actionSearchDialog)
        self.window.closeEvent = self.closeEventSearchDialog
        self.window.show()

    def closeEventSearchDialog(self, event):
        self.window.close()
        self.displayData(self.currentDataFrameGlobal)
        self.comboBox_Select_Data.setEnabled(True)
        event.accept()

    def closeActionSearchDialog(self):
        self.window.close()

    def actionSearchDialog(self):
        try:
            search_phrase = str(self.ui.lineEdit_Search_Text.text())

            if not search_phrase:
                self.displayData(self.currentDataFrameGlobal)
            elif self.ui.checkBox_Case.isChecked():
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
        self.enableWindowFunction()
        data = DataStorageModel.get(self.comboBox_Select_Data.currentText())
        self.currentDataFrameGlobal = data
        self.displayData(self.currentDataFrameGlobal)

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

    def enableLoad(self, index):
        if index >= 0:
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

    def showInfoWidget(self):
        if self.currentDataFrameGlobal is not None and self.action_More_Info.isChecked():

            buffer = io.StringIO()
            self.currentDataFrameGlobal.info(buf=buffer)
            info_text = buffer.getvalue()

            self.window = QWidget()
            self.ui = Ui_Form_Info()
            self.ui.setupUi(self.window)

            self.ui.textEdit_info.setPlainText(info_text)
            self.ui.pushButton_Close.clicked.connect(self.closeButton)
            self.window.closeEvent = self.myCloseEvent
            self.ui.pushButton_Close.setShortcut("Ctrl+I")

            self.window.show()

        elif not self.action_More_Info.isChecked():
            self.window.close()

    def closeButton(self):
        self.action_More_Info.setChecked(False)
        self.window.close()

    def myCloseEvent(self, event):
        self.action_More_Info.setChecked(False)
        event.accept()
