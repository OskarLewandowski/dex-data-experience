# Form implementation generated from reading ui file '.\guide-window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Guide(object):
    def setupUi(self, MainWindow_Guide):
        MainWindow_Guide.setObjectName("MainWindow_Guide")
        MainWindow_Guide.setWindowModality(QtCore.Qt.WindowModality.WindowModal)
        MainWindow_Guide.resize(1500, 900)
        MainWindow_Guide.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_Guide)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget_Category_List = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget_Category_List.setMaximumSize(QtCore.QSize(160, 16777215))
        self.listWidget_Category_List.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.listWidget_Category_List.setObjectName("listWidget_Category_List")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Category_List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Category_List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Category_List.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_Category_List.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget_Category_List)
        self.stackedWidget_Content = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget_Content.setObjectName("stackedWidget_Content")
        self.Add_Data = QtWidgets.QWidget()
        self.Add_Data.setObjectName("Add_Data")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Add_Data)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit_Add_Data = QtWidgets.QTextEdit(parent=self.Add_Data)
        self.textEdit_Add_Data.setReadOnly(True)
        self.textEdit_Add_Data.setObjectName("textEdit_Add_Data")
        self.verticalLayout_2.addWidget(self.textEdit_Add_Data)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_Close_1 = QtWidgets.QPushButton(parent=self.Add_Data)
        self.pushButton_Close_1.setObjectName("pushButton_Close_1")
        self.horizontalLayout_2.addWidget(self.pushButton_Close_1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.stackedWidget_Content.addWidget(self.Add_Data)
        self.Modify_Data = QtWidgets.QWidget()
        self.Modify_Data.setObjectName("Modify_Data")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Modify_Data)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit_Modify_Data = QtWidgets.QTextEdit(parent=self.Modify_Data)
        self.textEdit_Modify_Data.setReadOnly(True)
        self.textEdit_Modify_Data.setObjectName("textEdit_Modify_Data")
        self.verticalLayout_3.addWidget(self.textEdit_Modify_Data)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_Close_2 = QtWidgets.QPushButton(parent=self.Modify_Data)
        self.pushButton_Close_2.setObjectName("pushButton_Close_2")
        self.horizontalLayout_3.addWidget(self.pushButton_Close_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.stackedWidget_Content.addWidget(self.Modify_Data)
        self.Analysis_Data = QtWidgets.QWidget()
        self.Analysis_Data.setObjectName("Analysis_Data")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Analysis_Data)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textEdit_Plots = QtWidgets.QTextEdit(parent=self.Analysis_Data)
        self.textEdit_Plots.setReadOnly(True)
        self.textEdit_Plots.setObjectName("textEdit_Plots")
        self.verticalLayout_4.addWidget(self.textEdit_Plots)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.pushButton_Close_3 = QtWidgets.QPushButton(parent=self.Analysis_Data)
        self.pushButton_Close_3.setObjectName("pushButton_Close_3")
        self.horizontalLayout_4.addWidget(self.pushButton_Close_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.stackedWidget_Content.addWidget(self.Analysis_Data)
        self.Distribution_Series = QtWidgets.QWidget()
        self.Distribution_Series.setObjectName("Distribution_Series")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Distribution_Series)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_Distribution_Series = QtWidgets.QTextEdit(parent=self.Distribution_Series)
        self.textEdit_Distribution_Series.setReadOnly(True)
        self.textEdit_Distribution_Series.setObjectName("textEdit_Distribution_Series")
        self.verticalLayout.addWidget(self.textEdit_Distribution_Series)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.pushButton_Close_4 = QtWidgets.QPushButton(parent=self.Distribution_Series)
        self.pushButton_Close_4.setObjectName("pushButton_Close_4")
        self.horizontalLayout_5.addWidget(self.pushButton_Close_4)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.stackedWidget_Content.addWidget(self.Distribution_Series)
        self.horizontalLayout.addWidget(self.stackedWidget_Content)
        MainWindow_Guide.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_Guide)
        self.stackedWidget_Content.setCurrentIndex(2)
        self.listWidget_Category_List.currentRowChanged['int'].connect(
            self.stackedWidget_Content.setCurrentIndex)  # type: ignore
        self.pushButton_Close_1.clicked.connect(MainWindow_Guide.close)  # type: ignore
        self.pushButton_Close_2.clicked.connect(MainWindow_Guide.close)  # type: ignore
        self.pushButton_Close_3.clicked.connect(MainWindow_Guide.close)  # type: ignore
        self.pushButton_Close_4.clicked.connect(MainWindow_Guide.close)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Guide)

    def retranslateUi(self, MainWindow_Guide):
        project_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        image_directory = os.path.join(project_directory, "images")
        image_filename1 = "guide/Screenshot_1.png"
        image_filename2 = "guide/Screenshot_2.png"
        image_filename3 = "guide/Screenshot_3.png"
        image_filename4 = "guide/Screenshot_4.png"
        image_filename5 = "guide/Screenshot_5.png"
        image_filename6 = "guide/Screenshot_6.png"

        image_filename1 = os.path.join(image_directory, image_filename1)
        image_filename2 = os.path.join(image_directory, image_filename2)
        image_filename3 = os.path.join(image_directory, image_filename3)
        image_filename4 = os.path.join(image_directory, image_filename4)
        image_filename5 = os.path.join(image_directory, image_filename5)
        image_filename6 = os.path.join(image_directory, image_filename6)

        _translate = QtCore.QCoreApplication.translate
        MainWindow_Guide.setWindowTitle(_translate("MainWindow_Guide", "Przewodnik"))
        __sortingEnabled = self.listWidget_Category_List.isSortingEnabled()
        self.listWidget_Category_List.setSortingEnabled(False)
        item = self.listWidget_Category_List.item(0)
        item.setText(_translate("MainWindow_Guide", "Dodawanie danych"))
        item = self.listWidget_Category_List.item(1)
        item.setText(_translate("MainWindow_Guide", "Modyfikowanie danych"))
        item = self.listWidget_Category_List.item(2)
        item.setText(_translate("MainWindow_Guide", "Analiza danych"))
        item = self.listWidget_Category_List.item(3)
        item.setText(_translate("MainWindow_Guide", "Szereg rozdzielczy"))
        self.listWidget_Category_List.setSortingEnabled(__sortingEnabled)
        self.textEdit_Add_Data.setHtml(_translate("MainWindow_Guide",
                                                  "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "hr { height: 1px; border-width: 0; }\n"
                                                  "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                  "li.checked::marker { content: \"\\2612\"; }\n"
                                                  "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:700;\">Dodawanie danych</span></p>\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\"><br />Aby dodać zbiór danych do programu, należy wybrać opcję </span><span style=\" font-size:20pt; font-weight:700; font-style:italic;\">&quot;Dane&quot;</span><span style=\" font-size:20pt;\"> z górnego paska, a następnie </span><span style=\" font-size:20pt; font-weight:700; font-style:italic;\">&quot;Dodaj dane&quot;</span><span style=\" font-size:20pt;\"> lub skorzystać z paska narzędzi.</span></p>\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                                  f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"{image_filename1}\" /></p>\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">W oknie</span><span style=\" font-size:20pt; font-weight:700; font-style:italic;\"> &quot;Dodaj dane&quot;</span><span style=\" font-size:20pt;\"> można dodać dane poprzez naciśnięcie przycisku </span><span style=\" font-size:20pt; font-weight:700; font-style:italic;\">&quot;Wybierz plik&quot;</span><span style=\" font-size:20pt;\"> w następujących rozszerzeniach:</span></p>\n"
                                                  "<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
                                                  "<li style=\" font-size:20pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pliki tekstowe: CSV, TSV, TXT, JSON</li>\n"
                                                  "<li style=\" font-size:20pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pliki Excel: XLSX, XLS</li>\n"
                                                  "<li style=\" font-size:20pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pliki R: RDATA</li></ul>\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                                  f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"{image_filename2}\" /></p>\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\"><br />W przypadku plików tekstowych możemy dostosować ogranicznik oraz separator dziesiętny. Po załadowaniu danych w oknie zobaczymy podgląd danych. Jeśli dane prezentują się w niewłaściwy sposób z powodu błędnego wyboru ogranicznika, należy to poprawić, wybierając odpowiedni ogranicznik.</span></p>\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                  f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"{image_filename3}\" /></p>\n"
                                                  "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; vertical-align:super;\">Błędny wybór ogranicznika</span></p>\n"
                                                  "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-style:italic; vertical-align:super;\"><br /></p>\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Prawidłowo wybrany ogranicznik oraz separator dziesiętny.</span></p>\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                                  f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"{image_filename4}\" /></p>\n"
                                                  "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-style:italic; vertical-align:super;\">Prawidłowy wybór ogranicznika oraz separatora.</span></p>\n"
                                                  "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-style:italic; vertical-align:super;\"><br /></p>\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Prawidłowe dodanie danych na tym etapie jest ważne dla poprawnego wykonywania analiz czy też tworzenia wykresów.</span></p>\n"
                                                  "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p></body></html>"))
        self.pushButton_Close_1.setText(_translate("MainWindow_Guide", "Zamknij"))
        self.textEdit_Modify_Data.setHtml(_translate("MainWindow_Guide",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "hr { height: 1px; border-width: 0; }\n"
                                                     "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                     "li.checked::marker { content: \"\\2612\"; }\n"
                                                     "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:700;\">Modyfikowanie danych</span></p>\n"
                                                     "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:24pt; font-weight:700;\"><br /></p>\n"
                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Aby zmodyfikować dodane zbiory danych, należy wybrać opcję </span><span style=\" font-size:20pt; font-weight:700; font-style:italic;\">&quot;Dane&quot;</span><span style=\" font-size:20pt;\"> z górnego paska, a następnie </span><span style=\" font-size:20pt; font-weight:700; font-style:italic;\">&quot;Modyfikuj dane&quot;</span><span style=\" font-size:20pt;\"> lub skorzystać z paska narzędzi.</span></p>\n"
                                                     "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                                     f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"{image_filename6}\" /></p>\n"
                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> <span style=\" font-size:20pt;\"> <br />Okno </span><span style=\" font-size:20pt; font-weight:700; font-style:italic;\">&quot;Modyfikuj dane&quot;</span><span style=\" font-size:20pt;\"> pozwala na:</span></p>\n"
                                                     "<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
                                                     "<li style=\" font-size:20pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Zmianę nagłówków kolumn w zbiorze danych.</li>\n"
                                                     "<li style=\" font-size:20pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Zmianę typu danych w kolumnie.</li>\n"
                                                     "<li style=\" font-size:20pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Zmianę danych w zbiorze.</li>\n"
                                                     "<li style=\" font-size:20pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Zastosowanie gorącego kodowania.</li>\n"
                                                     "<li style=\" font-size:20pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Usunięcie wierszy zawierających wartości NaN.</li>\n"
                                                     "<li style=\" font-size:20pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Usunięcie wybranych kolumn lub wierszy.</li>\n"
                                                     "<li style=\" font-size:20pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wyszukiwanie wartości w zbiorze.</li>\n"
                                                     "<li style=\" font-size:20pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Uzyskanie informacji o zbiorze.</li></ul>\n"
                                                     "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                                     f"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"{image_filename5}\" /></p>\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\"> </span></p>\n"
                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /><span style=\" font-size:20pt;\">Zbiory danych można wyeksportować do pliku, wybierając </span><span style=\" font-size:20pt; font-weight:700; font-style:italic;\">&quot;Plik&quot;</span><span style=\" font-size:20pt;\">, a następnie </span><span style=\" font-size:20pt; font-weight:700; font-style:italic;\">&quot;Zapisz jako&quot;</span><span style=\" font-size:20pt;\">. Dostępne opcje zapisu zbioru danych do pliku to:</span></p>\n"
                                                     "<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
                                                     "<li style=\" font-size:20pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Plik CSV</li>\n"
                                                     "<li style=\" font-size:20pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Plik TSV</li>\n"
                                                     "<li style=\" font-size:20pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Plik XLSX</li>\n"
                                                     "<li style=\" font-size:20pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Plik JSON</li>\n"
                                                     "<li style=\" font-size:20pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Plik XML</li>\n"
                                                     "<li style=\" font-size:20pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Plik PDF</li>\n"
                                                     "<li style=\" font-size:20pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Plik RDATA</li></ul>\n"
                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\"> </span></p>\n"
                                                     "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700; text-decoration: underline;\">Uwaga!</span><span style=\" font-size:20pt;\"> Aby dokonane zmiany w zbiorze zostały zachowane, należy </span><span style=\" font-size:20pt; font-weight:700;\">zapisać zmiany</span><span style=\" font-size:20pt;\">.</span></p>\n"
                                                     "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_Close_2.setText(_translate("MainWindow_Guide", "Zamknij"))
        self.textEdit_Plots.setHtml(_translate("MainWindow_Guide",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "hr { height: 1px; border-width: 0; }\n"
                                               "li.unchecked::marker { content: \"\\2610\"; }\n"
                                               "li.checked::marker { content: \"\\2612\"; }\n"
                                               "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:700;\">Analiza danych</span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\"><br />Aby przeprowadzić analizę z dodanych zbiorów danych, należy wybrać opcję </span><span style=\" font-size:20pt; font-weight:700; font-style:italic;\">„Analiza”</span><span style=\" font-size:20pt;\"> z górnego paska, a następnie wybrać interesującą nas analizę.</span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700;\">Podstawowe statystyki:</span><span style=\" font-size:20pt;\"> Dostarczają podstawowych informacji o zbiorze danych, takich jak średnia, mediana, wariancja czy odchylenie standardowe. </span></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700;\"><br />Szereg rozdzielczy:</span><span style=\" font-size:20pt;\"> Metoda prezentacji danych statystycznych, która grupuje indywidualne obserwacje w przedziały i pokazuje liczbę wystąpień w każdym z nich, umożliwiając szybką wizualizację rozkładu danych. Pozwala na zapisanie szeregu jako zbioru danych, co ułatwia tworzenie wartościowych wykresów.</span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-weight:700;\"><br /></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700;\">Testy normalności:</span><span style=\" font-size:20pt;\"> Sprawdzają, czy rozkład danych jest zgodny z rozkładem normalnym, co jest założeniem wielu innych testów statystycznych. </span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700;\">Korelacje:</span><span style=\" font-size:20pt;\"> Obejmuje różne techniki statystyczne do oceny związku między zmiennymi.</span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700;\">Testy t-Studenta:</span><span style=\" font-size:20pt;\"> Porównują średnie dwóch grup, aby stwierdzić, czy istnieją między nimi statystycznie istotne różnice. </span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700;\">Jednoczynnikowa ANOVA:</span><span style=\" font-size:20pt;\"> Umożliwia porównanie średnich wartości trzech lub więcej grup, by sprawdzić, czy przynajmniej jedna z nich różni się istotnie. </span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700;\">Test Chi-kwadrat:</span><span style=\" font-size:20pt;\"> Bada zależności między zmiennymi kategorycznymi, sprawdzając, czy rozkład obserwacji odbiega od rozkładu oczekiwanego. </span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700;\">Test Kruskala-Wallisa:</span><span style=\" font-size:20pt;\"> Jest nieparametrycznym odpowiednikiem jednoczynnikowej ANOVA, używanym, gdy dane nie spełniają założeń ANOVA. </span></p>\n"
                                               "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p>\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:700;\">Test Tukeya:</span><span style=\" font-size:20pt;\"> Wykorzystywany po jednoczynnikowej ANOVA, służy do porównania par średnich, aby ustalić, które dokładnie średnie różnią się od siebie.</span></p></body></html>"))
        self.pushButton_Close_3.setText(_translate("MainWindow_Guide", "Zamknij"))
        self.textEdit_Distribution_Series.setHtml(_translate("MainWindow_Guide",
                                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                             "p, li { white-space: pre-wrap; }\n"
                                                             "hr { height: 1px; border-width: 0; }\n"
                                                             "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                             "li.checked::marker { content: \"\\2612\"; }\n"
                                                             "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                             "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:700;\">Szereg rozdzielczy</span></p></body></html>"))
        self.pushButton_Close_4.setText(_translate("MainWindow_Guide", "Zamknij"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Guide = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Guide()
    ui.setupUi(MainWindow_Guide)
    MainWindow_Guide.show()
    sys.exit(app.exec())
