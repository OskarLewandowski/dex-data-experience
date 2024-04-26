from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QFileDialog
from Views.AddFile.add_file_main_window_v2 import Ui_Dialog_Add_File
from Models.data_frame_model import DataFrameModel
from Models.data_storage_model import DataStorageModel
from Models.message_model import MessageModel
import pandas as pd
import pyreadr
import os


class AddFileController(QDialog, Ui_Dialog_Add_File):
    def __init__(self, main_controller):
        super().__init__()
        self.setupUi(self)
        self.main = main_controller

        # to keep file path
        self.filePathGlobal = None

        # to keep file name
        self.fileNameGlobal = None

        # to keep data frame
        self.dataFrameGlobal = None

        # connections
        self.pushButton_Cancel.clicked.connect(self.reject)
        self.pushButton_Choose_File.clicked.connect(self.chooseFile)
        self.radioButton_A_Custom.toggled.connect(self.customDelimiterToggled)
        self.pushButton_Load.clicked.connect(self.saveData)

        self.radioButton_A_Comma.clicked.connect(self.executeLoadDataByUser)
        self.radioButton_A_Semicolon.clicked.connect(self.executeLoadDataByUser)
        self.radioButton_A_Tab.clicked.connect(self.executeLoadDataByUser)
        self.radioButton_B_Comma.clicked.connect(self.executeLoadDataByUser)
        self.radioButton_B_Dot.clicked.connect(self.executeLoadDataByUser)
        self.lineEdit_Custom_Delimiter.textEdited.connect(self.executeLoadDataByUser)
        self.radioButton_A_Custom.clicked.connect(self.executeLoadDataByUser)
        self.checkBox_Skip_Headers.clicked.connect(self.executeLoadDataByUser)
        self.checkBox_Transpose.clicked.connect(self.executeLoadDataByUser)

        self.disableGroupBoxLoadDataSettings()

    def enableGroupBoxLoadDataSettings(self):
        self.groupBox_Separator.setEnabled(True)
        self.groupBox_Decimal_Separator.setEnabled(True)
        self.groupBox_Other.setEnabled(True)

    def disableGroupBoxLoadDataSettings(self):
        self.groupBox_Separator.setEnabled(False)
        self.groupBox_Decimal_Separator.setEnabled(False)
        self.groupBox_Other.setEnabled(False)

    def createWindowAddFile(self):
        """
        Show add file window
        """
        self.clear()
        self.setWindowFlags(Qt.WindowType.WindowMinMaxButtonsHint | Qt.WindowType.WindowCloseButtonHint)
        self.show()

    def chooseFile(self):
        try:
            filePath = None
            fileFilter = ('Pliki tekstowe (*.json; *.txt; *.csv; *.tsv);;'
                          'Arkusz kalkulacyjny (*.xlsx; *.xls);;'
                          'Pliki R (*.RData);;'
                          'Wszystkie pliki (*.*)')

            excelExt = ['.xlsx', '.xls']

            fileName = QFileDialog.getOpenFileName(
                caption="Wybierz plik",
                directory=os.path.expanduser("~/Desktop"),
                filter=fileFilter,
                initialFilter='Wszystkie pliki (*.*)')

            if fileName[0]:
                filePath = str(fileName[0])
                self.filePathGlobal = filePath
                fileName = os.path.basename(filePath)

                self.fileNameGlobal = fileName

                self.lineEdit_Filename.setText(fileName)
                self.enableLockedButton()

            # first data load by default settings
            if filePath.endswith(".csv"):
                # print("CSV_1")
                self.radioButton_A_Comma.setChecked(True)
                self.radioButton_B_Comma.setChecked(True)
                self.loadDataCsvTsvTxt()
                self.enableGroupBoxLoadDataSettings()
            elif filePath.endswith(".tsv"):
                # print("TSV_1")
                self.radioButton_A_Tab.setChecked(True)
                self.radioButton_B_Comma.setChecked(True)
                self.loadDataCsvTsvTxt()
                self.enableGroupBoxLoadDataSettings()
            elif filePath.endswith(".txt"):
                # print("TXT_1")
                self.radioButton_A_Tab.setChecked(True)
                self.radioButton_B_Comma.setChecked(True)
                self.loadDataCsvTsvTxt()
                self.enableGroupBoxLoadDataSettings()
            elif filePath.endswith(".json"):
                # print("JSON_1")
                self.loadDataJson()
                self.disableGroupBoxLoadDataSettings()
            elif filePath.endswith(tuple(excelExt)):
                # print("EXCEL_1")
                self.loadDataExcel()
                self.disableGroupBoxLoadDataSettings()
            elif filePath.endswith(".RData"):
                # print("RDATA_1")
                self.loadDataRData()
                self.disableGroupBoxLoadDataSettings()
            else:
                parts = filePath.split('.')
                extension = parts[1].upper()
                MessageModel.error("0035",
                                   f"Nieprawidłowy format pliku.\nRozszerzenie {extension} nie jest obsługiwane.")
        except:
            self.clear()

    def executeLoadDataByUser(self):
        try:
            filePath = self.filePathGlobal
            excelExt = ['.xlsx', '.xls']

            if filePath.endswith(".csv"):
                # print("CSV_2")
                self.loadDataCsvTsvTxt()
            elif filePath.endswith(".tsv"):
                # print("TSV_2")
                self.loadDataCsvTsvTxt()
            elif filePath.endswith(".txt"):
                # print("TXT_2")
                self.loadDataCsvTsvTxt()
            elif filePath.endswith(".json"):
                # print("JSON_2")
                self.loadDataJson()
            elif filePath.endswith(tuple(excelExt)):
                # print("EXCEL_2")
                self.loadDataExcel()
            elif filePath.endswith(".RData"):
                # print("RDATA_2")
                self.loadDataRData()

        except Exception as e:
            MessageModel.error("0014", str(e))

    def getDecimalSeparator(self):
        if self.radioButton_B_Comma.isChecked():
            return ","
        elif self.radioButton_B_Dot.isChecked():
            return "."
        else:
            return ","

    def getDelimiter(self):
        if self.radioButton_A_Comma.isChecked():
            return ","
        elif self.radioButton_A_Semicolon.isChecked():
            return ";"
        elif self.radioButton_A_Tab.isChecked():
            return "\t"
        elif self.radioButton_A_Custom.isChecked():
            custom_delimiter = self.lineEdit_Custom_Delimiter.text()
            if custom_delimiter:
                return custom_delimiter
            else:
                return ","
        else:
            return ","

    def loadDataCsvTsvTxt(self):
        try:
            filePath = self.filePathGlobal

            if filePath:

                delimiter = self.getDelimiter()
                decimal_separator = self.getDecimalSeparator()
                skip_headers = self.checkBox_Skip_Headers.isChecked()
                transpose = self.checkBox_Transpose.isChecked()

                try:
                    if skip_headers:
                        # headers=False
                        obj = pd.read_csv(filePath,
                                          encoding='utf-8',
                                          delimiter=delimiter,
                                          decimal=decimal_separator,
                                          header=None)

                        obj.columns = [str(i) for i in range(0, len(obj.columns))]

                        if transpose:
                            obj = obj.T

                        self.displayDataInTableView(obj)
                    else:
                        obj = pd.read_csv(filePath,
                                          encoding='utf-8',
                                          delimiter=delimiter,
                                          decimal=decimal_separator)
                        if transpose:
                            obj = obj.T

                        self.displayDataInTableView(obj)
                except:
                    if skip_headers:
                        # headers=False
                        obj = pd.read_csv(filePath,
                                          encoding='iso-8859-1',
                                          delimiter=delimiter,
                                          decimal=decimal_separator,
                                          header=None)

                        obj.columns = [str(i) for i in range(0, len(obj.columns))]

                        if transpose:
                            obj = obj.T

                        self.displayDataInTableView(obj)
                    else:
                        obj = pd.read_csv(filePath,
                                          encoding='iso-8859-1',
                                          delimiter=delimiter,
                                          decimal=decimal_separator)

                        if transpose:
                            obj = obj.T

                        self.displayDataInTableView(obj)

                self.dataFrameGlobal = obj

        except Exception as e:
            MessageModel.error("0001", str(e))
            self.clear()

    def loadDataJson(self):
        try:
            filePath = self.filePathGlobal

            if filePath:
                obj = pd.read_json(filePath, orient="records")

                self.displayDataInTableView(obj)
                self.dataFrameGlobal = obj

        except Exception as e:
            MessageModel.error("0015", str(e))

    def loadDataExcel(self):
        try:
            filePath = self.filePathGlobal

            if filePath:
                obj = pd.read_excel(filePath)

                self.displayDataInTableView(obj)
                self.dataFrameGlobal = obj

        except Exception as e:
            MessageModel.error("0016", str(e))

    def loadDataRData(self):
        try:
            filePath = self.filePathGlobal

            if filePath:
                rdata = pyreadr.read_r(filePath)
                keys = rdata.keys()
                obj = pd.DataFrame()

                for key in keys:
                    df = rdata[key]

                    if df.shape[0] < df.shape[1]:
                        df = df.T

                    obj[key] = df

                obj.index = range(len(obj))

                self.displayDataInTableView(obj)
                self.dataFrameGlobal = obj

        except Exception as e:
            MessageModel.error("0017", str(e))

    def displayDataInTableView(self, data_frame):
        try:
            model = DataFrameModel(data_frame)
            self.tableView_Data_Table.setModel(model)
        except Exception as e:
            MessageModel.error("0002", str(e))
            self.clear()

    def enableLockedButton(self):
        if bool(self.lineEdit_Filename.text()):
            self.pushButton_Load.setEnabled(True)

    def customDelimiterToggled(self, checked):
        if checked:
            self.lineEdit_Custom_Delimiter.setEnabled(True)
            self.lineEdit_Custom_Delimiter.setFocus()
        else:
            self.lineEdit_Custom_Delimiter.setEnabled(False)
            self.radioButton_A_Custom.setChecked(False)

    def clear(self):
        self.lineEdit_Filename.clear()
        self.pushButton_Load.setEnabled(False)
        self.filePathGlobal = None
        self.tableView_Data_Table.setModel(None)
        if not self.radioButton_A_Custom.isChecked():
            self.lineEdit_Custom_Delimiter.setEnabled(False)
        self.disableGroupBoxLoadDataSettings()

    def saveData(self):
        try:
            nextStep = None
            confirmed = MessageModel.saveConfirmation()
            if confirmed:
                DataStorageModel.add(os.path.splitext(self.fileNameGlobal)[0], self.dataFrameGlobal)

                self.main.updateStatusBar()

                nextStep = MessageModel.statusConfirmation(self.fileNameGlobal)

            if nextStep:
                self.close()
            else:
                self.clear()

        except Exception as e:
            MessageModel.error("0005", str(e))
