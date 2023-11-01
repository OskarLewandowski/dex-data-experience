from PyQt6.QtWidgets import QDialog, QMessageBox, QFileDialog
from Views.AddFile.add_file_main_window import Ui_Dialog_Add_File
from Models.data_frame_model import DataFrameModel
from Models.data_storage_model import DataStorageModel
import pandas as pd
import os
from PyQt6 import QtGui


class AddFileController(QDialog, Ui_Dialog_Add_File):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        self.show()

    def chooseFile(self):
        try:
            filePath = None
            fileFilter = ('Pliki tekstowe (*.json; *.txt; *.csv; *.tsv);;'
                          'Arkusz kalkulacyjny (*.xlsx; *.xls);;'
                          'Pliki R (*.RData);;'
                          'Wszystkie pliki (*.*)')

            fileName = QFileDialog.getOpenFileName(
                caption="Wybierz plik",
                directory=os.path.expanduser("~/Desktop"),
                filter=fileFilter,
                initialFilter='Pliki tekstowe (*.json; *.txt; *.csv; *.tsv)')

            if fileName[0]:
                filePath = str(fileName[0])
                self.filePathGlobal = filePath
                fileName = os.path.basename(filePath)

                self.fileNameGlobal = fileName

                self.lineEdit_Filename.setText(fileName)
                self.enableLockedButton()

            # first data load by default settings
            if filePath.endswith(".csv"):
                print("CSV_1")
                self.radioButton_A_Comma.setChecked(True)
                self.radioButton_B_Comma.setChecked(True)
                self.loadDataCsvTsvTxt()
                self.enableGroupBoxLoadDataSettings()
            elif filePath.endswith(".tsv"):
                print("TSV_1")
                self.radioButton_A_Tab.setChecked(True)
                self.radioButton_B_Comma.setChecked(True)
                self.loadDataCsvTsvTxt()
                self.enableGroupBoxLoadDataSettings()
            elif filePath.endswith(".txt"):
                print("TXT_1")
                self.radioButton_A_Tab.setChecked(True)
                self.radioButton_B_Comma.setChecked(True)
                self.loadDataCsvTsvTxt()
                self.enableGroupBoxLoadDataSettings()
            elif filePath.endswith(".json"):
                print("JSON_1")
                self.loadDataJson()
                pass
        except:
            self.clear()

    def executeLoadDataByUser(self):
        try:
            filePath = self.filePathGlobal

            if filePath.endswith(".csv"):
                print("CSV_2")
                self.loadDataCsvTsvTxt()
            elif filePath.endswith(".tsv"):
                print("TSV_2")
                self.loadDataCsvTsvTxt()
            elif filePath.endswith(".txt"):
                print("TXT_2")
                self.loadDataCsvTsvTxt()
            elif filePath.endswith(".json"):
                print("JSON_2")
                self.loadDataJson()
                pass

        except Exception as e:
            self.errorMessage("0014", str(e))

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
            self.errorMessage("0001", str(e))
            self.clear()

    def loadDataJson(self):
        try:
            filePath = self.filePathGlobal

            if filePath:
                obj = pd.read_json(filePath, orient="records")

                self.displayDataInTableView(obj)
                self.dataFrameGlobal = obj

        except Exception as e:
            print(str(e))

    def displayDataInTableView(self, data_frame):
        try:
            data = data_frame.head(15)
            model = DataFrameModel(data)
            self.tableView_Data_Table.setModel(model)
        except Exception as e:
            self.errorMessage("0002", str(e))
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
            confirmed = self.saveConfirmationDialog()
            if confirmed:
                DataStorageModel.add(os.path.splitext(self.fileNameGlobal)[0], self.dataFrameGlobal)
                nextStep = self.statusConfirmationDialog()

            if nextStep:
                self.close()
            else:
                self.clear()
        except Exception as e:
            self.errorMessage("0005", str(e))

    def saveConfirmationDialog(self):
        try:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setText('Czy na pewno chcesz załadować dane?')
            msg.setWindowTitle('Dex')

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../../images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                           QtGui.QIcon.State.Off)
            msg.setWindowIcon(icon)

            msg.setStandardButtons(
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Abort)
            msg.button(QMessageBox.StandardButton.Yes).setText('Tak')
            msg.button(QMessageBox.StandardButton.Abort).setText('Anuluj')

            reply = msg.exec()

            return reply == QMessageBox.StandardButton.Yes
        except Exception as e:
            self.errorMessage("0004", str(e))

    def statusConfirmationDialog(self):
        try:
            message = "Plik '{}' został pomyślnie załadowny.".format(self.fileNameGlobal)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setText(message)
            msg.setWindowTitle('Dex')

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../../images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                           QtGui.QIcon.State.Off)
            msg.setWindowIcon(icon)

            msg.setStandardButtons(
                QMessageBox.StandardButton.Abort | QMessageBox.StandardButton.Close)
            msg.button(QMessageBox.StandardButton.Abort).setText('Dodaj kolejny plik')
            msg.button(QMessageBox.StandardButton.Close).setText('Wróc')

            reply = msg.exec()

            return reply == QMessageBox.StandardButton.Close
        except Exception as e:
            self.errorMessage("0003", str(e))

    @staticmethod
    def errorMessage(errorCode="0000", e=""):
        message = "Wystąpił bład: [{0}] - {1}".format(errorCode, e)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(message)
        msg.setWindowTitle('Dex')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        msg.setWindowIcon(icon)

        msg.setStandardButtons(QMessageBox.StandardButton.Close)
        msg.button(QMessageBox.StandardButton.Close).setText('Zamknij')
        reply = msg.exec()

        return reply == QMessageBox.StandardButton.Close
