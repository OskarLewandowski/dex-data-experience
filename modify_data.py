# Form implementation generated from reading ui file 'modify-data.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import io
import os

import pandas as pd
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from pyreadr import pyreadr

from data_storage import DataStorage
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from data_frame_model import DataFrameModel
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, PageBreak
from widget_info import Ui_Form_Info


class Ui_MainWindow_modify_data(object):
    def setupUi(self, MainWindow_modify_data):

        self.currentDataFrameGlobal = None
        self.info_dialog = None

        MainWindow_modify_data.setObjectName("MainWindow_modify_data")
        MainWindow_modify_data.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        MainWindow_modify_data.resize(800, 600)
        MainWindow_modify_data.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        MainWindow_modify_data.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_modify_data)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_Select_Data = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_Select_Data.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.comboBox_Select_Data.setObjectName("comboBox_Select_Data")
        self.horizontalLayout.addWidget(self.comboBox_Select_Data)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Policy.Fixed,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_Load = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Load.setEnabled(False)
        self.pushButton_Load.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_Load.setObjectName("pushButton_Load")
        self.horizontalLayout.addWidget(self.pushButton_Load)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.tableView_Data_Frame = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView_Data_Frame.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tableView_Data_Frame.setObjectName("tableView_Data_Frame")
        self.verticalLayout.addWidget(self.tableView_Data_Frame)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Save = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Save.setEnabled(False)
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.horizontalLayout_2.addWidget(self.pushButton_Save)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButton_Cancel = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.horizontalLayout_2.addWidget(self.pushButton_Cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow_modify_data.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow_modify_data)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(parent=self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Edit.setEnabled(False)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Info = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Info.setEnabled(False)
        self.menu_Info.setObjectName("menu_Info")
        self.menu_Search = QtWidgets.QMenu(parent=self.menubar)
        self.menu_Search.setEnabled(False)
        self.menu_Search.setObjectName("menu_Search")
        MainWindow_modify_data.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow_modify_data)
        self.statusbar.setObjectName("statusbar")
        MainWindow_modify_data.setStatusBar(self.statusbar)
        self.action_Exit = QtGui.QAction(parent=MainWindow_modify_data)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Save_as = QtGui.QAction(parent=MainWindow_modify_data)
        self.action_Save_as.setEnabled(False)
        self.action_Save_as.setObjectName("action_Save_as")
        self.action_Change = QtGui.QAction(parent=MainWindow_modify_data)
        self.action_Change.setObjectName("action_Change")
        self.action_Delete_Nan = QtGui.QAction(parent=MainWindow_modify_data)
        self.action_Delete_Nan.setObjectName("action_Delete_Nan")
        self.action_Change_Headers = QtGui.QAction(parent=MainWindow_modify_data)
        self.action_Change_Headers.setObjectName("action_Change_Headers")
        self.action_Delete_Column = QtGui.QAction(parent=MainWindow_modify_data)
        self.action_Delete_Column.setObjectName("action_Delete_Column")
        self.action_Delete_row = QtGui.QAction(parent=MainWindow_modify_data)
        self.action_Delete_row.setObjectName("action_Delete_row")
        self.action_Change_Data_Type = QtGui.QAction(parent=MainWindow_modify_data)
        self.action_Change_Data_Type.setObjectName("action_Change_Data_Type")
        self.action_Get_Dummies = QtGui.QAction(parent=MainWindow_modify_data)
        self.action_Get_Dummies.setObjectName("action_Get_Dummies")
        self.action_More_Info = QtGui.QAction(parent=MainWindow_modify_data)
        self.action_More_Info.setCheckable(True)
        self.action_More_Info.setObjectName("action_More_Info")
        self.action_Search = QtGui.QAction(parent=MainWindow_modify_data)
        self.action_Search.setObjectName("action_Search")
        self.action_Delete = QtGui.QAction(parent=MainWindow_modify_data)
        self.action_Delete.setObjectName("action_Delete")
        self.menu_File.addAction(self.action_Save_as)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_Edit.addAction(self.action_Change_Headers)
        self.menu_Edit.addAction(self.action_Change_Data_Type)
        self.menu_Edit.addAction(self.action_Change)
        self.menu_Edit.addAction(self.action_Get_Dummies)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_Delete_Nan)
        self.menu_Edit.addAction(self.action_Delete)
        self.menu_Info.addAction(self.action_More_Info)
        self.menu_Search.addAction(self.action_Search)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Search.menuAction())
        self.menubar.addAction(self.menu_Info.menuAction())

        self.retranslateUi(MainWindow_modify_data)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_modify_data)

        # add names to combo box
        nameList = DataStorage.get_all_keys()

        if nameList:
            self.comboBox_Select_Data.addItems(nameList)

        # connections
        self.pushButton_Cancel.clicked.connect(MainWindow_modify_data.close)
        self.action_Exit.triggered.connect(MainWindow_modify_data.close)
        self.comboBox_Select_Data.currentIndexChanged.connect(self.enableLoad)
        self.pushButton_Load.clicked.connect(self.loadDataFrame)
        self.action_Save_as.triggered.connect(self.saveAsAction)
        self.action_More_Info.triggered.connect(self.showInfoWidget)

    def retranslateUi(self, MainWindow_modify_data):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_modify_data.setWindowTitle(_translate("MainWindow_modify_data", "Modyfikuj dane"))
        self.comboBox_Select_Data.setPlaceholderText(_translate("MainWindow_modify_data", "Wybierz dane do edycji..."))
        self.pushButton_Load.setText(_translate("MainWindow_modify_data", "Wczytaj"))
        self.pushButton_Save.setText(_translate("MainWindow_modify_data", "Zapisz zmiany"))
        self.pushButton_Cancel.setText(_translate("MainWindow_modify_data", "Anuluj"))
        self.menu_File.setTitle(_translate("MainWindow_modify_data", "Plik"))
        self.menu_Edit.setTitle(_translate("MainWindow_modify_data", "Edycja"))
        self.menu_Info.setTitle(_translate("MainWindow_modify_data", "Informacje"))
        self.menu_Search.setTitle(_translate("MainWindow_modify_data", "Szukaj"))
        self.action_Exit.setText(_translate("MainWindow_modify_data", "Zakończ"))
        self.action_Exit.setShortcut(_translate("MainWindow_modify_data", "Ctrl+F4"))
        self.action_Save_as.setText(_translate("MainWindow_modify_data", "Zapisz jako..."))
        self.action_Save_as.setShortcut(_translate("MainWindow_modify_data", "Ctrl+S"))
        self.action_Change.setText(_translate("MainWindow_modify_data", "Zamień "))
        self.action_Change.setShortcut(_translate("MainWindow_modify_data", "Ctrl+H"))
        self.action_Delete_Nan.setText(_translate("MainWindow_modify_data", "Usuń NaN"))
        self.action_Delete_Nan.setShortcut(_translate("MainWindow_modify_data", "Ctrl+N"))
        self.action_Change_Headers.setText(_translate("MainWindow_modify_data", "Zmień nagłówki"))
        self.action_Change_Headers.setShortcut(_translate("MainWindow_modify_data", "Ctrl+L"))
        self.action_Delete_Column.setText(_translate("MainWindow_modify_data", "Usuń"))
        self.action_Delete_Column.setShortcut(_translate("MainWindow_modify_data", "Ctrl+D"))
        self.action_Delete_row.setText(_translate("MainWindow_modify_data", "Usuń"))
        self.action_Delete_row.setShortcut(_translate("MainWindow_modify_data", "Ctrl+D"))
        self.action_Change_Data_Type.setText(_translate("MainWindow_modify_data", "Zmień typ danych"))
        self.action_Change_Data_Type.setShortcut(_translate("MainWindow_modify_data", "Ctrl+T"))
        self.action_Get_Dummies.setText(_translate("MainWindow_modify_data", "Rozdziel dane"))
        self.action_Get_Dummies.setShortcut(_translate("MainWindow_modify_data", "Ctrl+G"))
        self.action_More_Info.setText(_translate("MainWindow_modify_data", "Informacje dodatkowe"))
        self.action_More_Info.setShortcut(_translate("MainWindow_modify_data", "Ctrl+I"))
        self.action_Search.setText(_translate("MainWindow_modify_data", "Szukaj"))
        self.action_Search.setShortcut(_translate("MainWindow_modify_data", "Ctrl+F"))
        self.action_Delete.setText(_translate("MainWindow_modify_data", "Usuń"))
        self.action_Delete.setShortcut(_translate("MainWindow_modify_data", "Ctrl+D"))

    def loadDataFrame(self):
        self.enableWindowFunction()
        data = DataStorage.get(self.comboBox_Select_Data.currentText())
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

    def enableLoad(self, index):
        if index >= 0:
            self.pushButton_Load.setEnabled(True)

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

        except Exception as e:
            print("Error -", e)

    def showInfoWidget(self):
        if self.currentDataFrameGlobal is not None:
            if self.action_More_Info.isChecked():
                buffer = io.StringIO()
                self.currentDataFrameGlobal.info(buf=buffer)
                info_text = buffer.getvalue()

                if self.info_dialog is None:
                    self.info_dialog = QtWidgets.QDialog()
                    self.info_dialog.setModal(False)
                    ui_info = Ui_Form_Info()
                    ui_info.setupUi(self.info_dialog)
                    ui_info.textEdit_info.setPlainText(info_text)
                    self.info_dialog.show()
                else:
                    self.info_dialog.show()

            if not self.action_More_Info.isChecked():
                if self.info_dialog is not None:
                    self.info_dialog.close()
                    self.info_dialog = None


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow_modify_data = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_modify_data()
    ui.setupUi(MainWindow_modify_data)
    MainWindow_modify_data.show()
    sys.exit(app.exec())