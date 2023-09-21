# Form implementation generated from reading ui file 'data-analysis.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_data_analysis(object):
    def setupUi(self, MainWindow_data_analysis):
        MainWindow_data_analysis.setObjectName("MainWindow_data_analysis")
        MainWindow_data_analysis.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        MainWindow_data_analysis.resize(800, 600)
        MainWindow_data_analysis.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        MainWindow_data_analysis.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_data_analysis)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.South)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow_data_analysis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow_data_analysis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuPlik = QtWidgets.QMenu(parent=self.menubar)
        self.menuPlik.setObjectName("menuPlik")
        self.menuEdycja = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdycja.setObjectName("menuEdycja")
        self.menuAnaliza_statystyczna = QtWidgets.QMenu(parent=self.menubar)
        self.menuAnaliza_statystyczna.setObjectName("menuAnaliza_statystyczna")
        self.menuAnaliza = QtWidgets.QMenu(parent=self.menubar)
        self.menuAnaliza.setObjectName("menuAnaliza")
        self.menuWykres = QtWidgets.QMenu(parent=self.menubar)
        self.menuWykres.setObjectName("menuWykres")
        MainWindow_data_analysis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow_data_analysis)
        self.statusbar.setObjectName("statusbar")
        MainWindow_data_analysis.setStatusBar(self.statusbar)
        self.actionWyjd = QtGui.QAction(parent=MainWindow_data_analysis)
        self.actionWyjd.setObjectName("actionWyjd")
        self.actionZapisz = QtGui.QAction(parent=MainWindow_data_analysis)
        self.actionZapisz.setObjectName("actionZapisz")
        self.actionCofnij = QtGui.QAction(parent=MainWindow_data_analysis)
        self.actionCofnij.setObjectName("actionCofnij")
        self.actionPon_w = QtGui.QAction(parent=MainWindow_data_analysis)
        self.actionPon_w.setObjectName("actionPon_w")
        self.menuPlik.addAction(self.actionZapisz)
        self.menuPlik.addSeparator()
        self.menuPlik.addAction(self.actionWyjd)
        self.menuEdycja.addAction(self.actionCofnij)
        self.menuEdycja.addAction(self.actionPon_w)
        self.menubar.addAction(self.menuPlik.menuAction())
        self.menubar.addAction(self.menuEdycja.menuAction())
        self.menubar.addAction(self.menuAnaliza_statystyczna.menuAction())
        self.menubar.addAction(self.menuAnaliza.menuAction())
        self.menubar.addAction(self.menuWykres.menuAction())

        self.retranslateUi(MainWindow_data_analysis)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_data_analysis)

    def retranslateUi(self, MainWindow_data_analysis):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_data_analysis.setWindowTitle(_translate("MainWindow_data_analysis", "Analizuj dane"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow_data_analysis", "Strona 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  _translate("MainWindow_data_analysis", "Strona 2"))
        self.menuPlik.setTitle(_translate("MainWindow_data_analysis", "Plik"))
        self.menuEdycja.setTitle(_translate("MainWindow_data_analysis", "Edycja"))
        self.menuAnaliza_statystyczna.setTitle(_translate("MainWindow_data_analysis", "Statystyka"))
        self.menuAnaliza.setTitle(_translate("MainWindow_data_analysis", "Analiza"))
        self.menuWykres.setTitle(_translate("MainWindow_data_analysis", "Wykresy"))
        self.actionWyjd.setText(_translate("MainWindow_data_analysis", "Zakończ"))
        self.actionZapisz.setText(_translate("MainWindow_data_analysis", "Zapisz"))
        self.actionCofnij.setText(_translate("MainWindow_data_analysis", "Cofnij"))
        self.actionPon_w.setText(_translate("MainWindow_data_analysis", "Ponów"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow_data_analysis = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_data_analysis()
    ui.setupUi(MainWindow_data_analysis)
    MainWindow_data_analysis.show()
    sys.exit(app.exec())