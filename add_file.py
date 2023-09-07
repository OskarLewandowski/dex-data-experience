# Form implementation generated from reading ui file 'add-file.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import pandas as pd

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QButtonGroup
from PyQt6.QtCore import Qt


class Ui_dialog_add_file(object):

    def setupUi(self, dialog_add_file):

        # variable
        # to keep file path
        self.filePathGlobal = None

        # to kepp data frame
        self.dataFrameGlobal = None

        dialog_add_file.setObjectName("dialog_add_file")
        dialog_add_file.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        dialog_add_file.resize(800, 600)
        dialog_add_file.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        dialog_add_file.setWindowIcon(icon)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(dialog_add_file)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=dialog_add_file)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_filename = QtWidgets.QLineEdit(parent=dialog_add_file)
        self.lineEdit_filename.setReadOnly(True)
        self.lineEdit_filename.setObjectName("lineEdit_filename")
        self.verticalLayout.addWidget(self.lineEdit_filename)
        self.pushButton_choose_file = QtWidgets.QPushButton(parent=dialog_add_file)
        self.pushButton_choose_file.setObjectName("pushButton_choose_file")
        self.verticalLayout.addWidget(self.pushButton_choose_file)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(parent=dialog_add_file)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=dialog_add_file)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)

        self.radioButton1_comma = QtWidgets.QRadioButton(parent=dialog_add_file)
        self.radioButton1_comma.setObjectName("radioButton1_comma")
        self.verticalLayout_2.addWidget(self.radioButton1_comma)

        self.radioButton1_semicolon = QtWidgets.QRadioButton(parent=dialog_add_file)
        self.radioButton1_semicolon.setObjectName("radioButton1_semicolon")
        self.verticalLayout_2.addWidget(self.radioButton1_semicolon)

        self.radioButton1_tab = QtWidgets.QRadioButton(parent=dialog_add_file)
        self.radioButton1_tab.setObjectName("radioButton1_tab")
        self.verticalLayout_2.addWidget(self.radioButton1_tab)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton1_custom = QtWidgets.QRadioButton(parent=dialog_add_file)
        self.radioButton1_custom.setObjectName("radioButton1_custom")
        self.horizontalLayout.addWidget(self.radioButton1_custom)
        self.lineEdit_custom_delimiter = QtWidgets.QLineEdit(parent=dialog_add_file)
        self.lineEdit_custom_delimiter.setEnabled(False)
        self.lineEdit_custom_delimiter.setObjectName("lineEdit_custom_delimiter")
        self.lineEdit_custom_delimiter.setMaxLength(1)
        self.horizontalLayout.addWidget(self.lineEdit_custom_delimiter)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.line_2 = QtWidgets.QFrame(parent=dialog_add_file)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=dialog_add_file)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)

        self.radioButton2_comma = QtWidgets.QRadioButton(parent=dialog_add_file)
        self.radioButton2_comma.setObjectName("radioButton2_comma")
        self.verticalLayout_3.addWidget(self.radioButton2_comma)

        self.radioButton2_dot = QtWidgets.QRadioButton(parent=dialog_add_file)
        self.radioButton2_dot.setObjectName("radioButton2_dot")
        self.verticalLayout_3.addWidget(self.radioButton2_dot)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_3.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.line_3 = QtWidgets.QFrame(parent=dialog_add_file)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=dialog_add_file)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.checkBox_skip_headers = QtWidgets.QCheckBox(parent=dialog_add_file)
        self.checkBox_skip_headers.setObjectName("checkBox_skip_headers")
        self.verticalLayout_4.addWidget(self.checkBox_skip_headers)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_4.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_4.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_5.addItem(spacerItem7)
        self.tableView_data_table = QtWidgets.QTableView(parent=dialog_add_file)
        self.tableView_data_table.setObjectName("tableView_data_table")
        self.verticalLayout_5.addWidget(self.tableView_data_table)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_5.addItem(spacerItem8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_refresh = QtWidgets.QPushButton(parent=dialog_add_file)
        self.pushButton_refresh.setEnabled(False)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.horizontalLayout_2.addWidget(self.pushButton_refresh)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.pushButton_load = QtWidgets.QPushButton(parent=dialog_add_file)
        self.pushButton_load.setEnabled(False)
        self.pushButton_load.setObjectName("pushButton_load")
        self.horizontalLayout_2.addWidget(self.pushButton_load)
        self.pushButton_cancel = QtWidgets.QPushButton(parent=dialog_add_file)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_2.addWidget(self.pushButton_cancel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.retranslateUi(dialog_add_file)
        QtCore.QMetaObject.connectSlotsByName(dialog_add_file)

        # radio group
        self.delimiter_button_group = QButtonGroup(dialog_add_file)
        self.delimiter_button_group.addButton(self.radioButton1_semicolon)
        self.delimiter_button_group.addButton(self.radioButton1_comma)
        self.delimiter_button_group.addButton(self.radioButton1_tab)
        self.delimiter_button_group.addButton(self.radioButton1_custom)

        self.decimal_separator_button_group = QButtonGroup(dialog_add_file)
        self.decimal_separator_button_group.addButton(self.radioButton2_dot)
        self.decimal_separator_button_group.addButton(self.radioButton2_comma)

        self.radioButton1_comma.setChecked(True)
        self.radioButton2_comma.setChecked(True)

        # connections
        self.pushButton_cancel.clicked.connect(dialog_add_file.reject)
        self.pushButton_choose_file.clicked.connect(self.chooseFile)
        self.radioButton1_custom.toggled.connect(self.customDelimiterToggled)

        self.pushButton_refresh.clicked.connect(self.customLoadData)

    def retranslateUi(self, dialog_add_file):
        _translate = QtCore.QCoreApplication.translate
        dialog_add_file.setWindowTitle(_translate("dialog_add_file", "Dodaj plik"))
        self.label.setText(_translate("dialog_add_file", "Nazwa pliku:"))
        self.lineEdit_filename.setPlaceholderText(_translate("dialog_add_file", "brak pliku"))
        self.pushButton_choose_file.setText(_translate("dialog_add_file", "Wybierz plik"))
        self.label_2.setText(_translate("dialog_add_file", "Ogranicznik:"))
        self.radioButton1_semicolon.setText(_translate("dialog_add_file", "średnik"))
        self.radioButton1_comma.setText(_translate("dialog_add_file", "przecinek"))
        self.radioButton1_tab.setText(_translate("dialog_add_file", "tabulator"))
        self.radioButton1_custom.setText(_translate("dialog_add_file", "niestandardowy"))
        self.label_3.setText(_translate("dialog_add_file", "Seperator dziesiętny:"))
        self.radioButton2_dot.setText(_translate("dialog_add_file", "kropka"))
        self.radioButton2_comma.setText(_translate("dialog_add_file", "przecinek"))
        self.label_4.setText(_translate("dialog_add_file", "Nagłówki:"))
        self.checkBox_skip_headers.setText(_translate("dialog_add_file", "brak nagłówków"))
        self.pushButton_refresh.setText(_translate("dialog_add_file", " Zatwierdź zmiany "))
        self.pushButton_load.setText(_translate("dialog_add_file", "Załaduj"))
        self.pushButton_cancel.setText(_translate("dialog_add_file", "Anuluj"))

    def chooseFile(self):
        try:
            fileFilter = 'Pliki tekstowe (*.json; *.txt; *.csv);; Arkusz kalkulacyjny (*.xlsx; *.xls);; Pliki R (*.RData);; Wszystkie pliki (*.*)'
            fileName = QFileDialog.getOpenFileName(
                caption="Wybierz plik",
                directory=os.path.expanduser("~/Desktop"),
                filter=fileFilter,
                initialFilter='Pliki tekstowe (*.txt; *.csv)')

            if fileName[0]:
                filePath = str(fileName[0])
                self.filePathGlobal = filePath
                fileName = os.path.basename(filePath)

                self.lineEdit_filename.setText(fileName)
                self.enableLockedButton()

            if filePath.endswith(".csv"):
                try:
                    obj = pd.read_csv(filePath)
                    self.dataFrameGlobal = obj
                    self.displayDataInTableView(obj)
                except:
                    obj = pd.read_csv(filePath, encoding='iso-8859-1')
                    self.dataFrameGlobal = obj
                    self.displayDataInTableView(obj)
        except:
            self.lineEdit_filename.clear()
            self.pushButton_load.setEnabled(False)
            self.tableView_data_table.setModel(None)
            self.checkBox_skip_headers.setChecked(False)
            self.pushButton_refresh.setEnabled(False)

    def customLoadData(self):
        try:
            filePath = self.filePathGlobal

            delimiter = ","
            if self.radioButton1_semicolon.isChecked():
                delimiter = ";"
            elif self.radioButton1_comma.isChecked():
                delimiter = ","
            elif self.radioButton1_tab.isChecked():
                delimiter = "\t"
            elif self.radioButton1_custom.isChecked():
                if self.lineEdit_custom_delimiter.text() == "" or self.lineEdit_custom_delimiter.text() == " ":
                    delimiter = ","
                else:
                    delimiter = self.lineEdit_custom_delimiter.text()

            decimal_separator = "."
            if self.radioButton2_comma.isChecked():
                decimal_separator = ","

            skip_headers = self.checkBox_skip_headers.isChecked()

            if skip_headers:
                obj = pd.read_csv(filePath, delimiter=delimiter, decimal=decimal_separator, header=None)
                self.dataFrameGlobal = obj
                self.displayDataInTableView(obj, headers=False)
            else:
                obj = pd.read_csv(filePath, delimiter=delimiter, decimal=decimal_separator)
                self.dataFrameGlobal = obj
                self.displayDataInTableView(obj)

        except Exception as e:
            print("ERROR" + e)

    def displayDataInTableView(self, data_frame, headers=True):
        try:
            model = QtGui.QStandardItemModel()
            num_rows, num_cols = data_frame.shape

            if num_rows > 15:
                num_rows = 15

            model.setColumnCount(num_cols)
            model.setRowCount(num_rows)

            if headers:
                header_labels = list(data_frame.columns)
            else:
                header_labels = [str(i) for i in range(1, num_cols)]

            model.setHorizontalHeaderLabels(header_labels)

            for row in range(num_rows):
                for col in range(num_cols):
                    item = QtGui.QStandardItem(str(data_frame.iat[row, col]))
                    item.setFlags(Qt.ItemFlag.ItemIsSelectable)
                    model.setItem(row, col, item)

            self.tableView_data_table.setModel(model)
        except Exception as e:
            print("Error" + str(e))

    def enableLockedButton(self):
        if bool(self.lineEdit_filename.text()):
            self.pushButton_load.setEnabled(True)
            self.pushButton_refresh.setEnabled(True)

    def customDelimiterToggled(self, checked):
        if checked:
            self.lineEdit_custom_delimiter.setEnabled(True)
            self.lineEdit_custom_delimiter.setFocus()
        else:
            self.lineEdit_custom_delimiter.setEnabled(False)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dialog_add_file = QtWidgets.QDialog()
    ui = Ui_dialog_add_file()
    ui.setupUi(dialog_add_file)
    dialog_add_file.show()
    sys.exit(app.exec())
