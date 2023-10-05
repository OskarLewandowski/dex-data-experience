# Form implementation generated from reading ui file '.\main-window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Main(object):
    def setupUi(self, MainWindow_Main):
        MainWindow_Main.setObjectName("MainWindow_Main")
        MainWindow_Main.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        MainWindow_Main.resize(800, 600)
        MainWindow_Main.setMinimumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        MainWindow_Main.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_Board = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_Board.setObjectName("textEdit_Board")
        self.verticalLayout.addWidget(self.textEdit_Board)
        MainWindow_Main.setCentralWidget(self.centralwidget)
        self.menubar_Menu = QtWidgets.QMenuBar(parent=MainWindow_Main)
        self.menubar_Menu.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar_Menu.setNativeMenuBar(True)
        self.menubar_Menu.setObjectName("menubar_Menu")
        self.menu_File = QtWidgets.QMenu(parent=self.menubar_Menu)
        self.menu_File.setObjectName("menu_File")
        self.menu_Data = QtWidgets.QMenu(parent=self.menubar_Menu)
        self.menu_Data.setObjectName("menu_Data")
        self.menu_Edit = QtWidgets.QMenu(parent=self.menubar_Menu)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Format = QtWidgets.QMenu(parent=self.menubar_Menu)
        self.menu_Format.setObjectName("menu_Format")
        self.menu_Analysis = QtWidgets.QMenu(parent=self.menubar_Menu)
        self.menu_Analysis.setObjectName("menu_Analysis")
        self.menu_Charts = QtWidgets.QMenu(parent=self.menubar_Menu)
        self.menu_Charts.setObjectName("menu_Charts")
        self.menu_Settings = QtWidgets.QMenu(parent=self.menubar_Menu)
        self.menu_Settings.setObjectName("menu_Settings")
        self.menu_Help = QtWidgets.QMenu(parent=self.menubar_Menu)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow_Main.setMenuBar(self.menubar_Menu)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow_Main)
        self.statusbar.setObjectName("statusbar")
        MainWindow_Main.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow_Main)
        self.toolBar.setObjectName("toolBar")
        MainWindow_Main.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.action_New_File = QtGui.QAction(parent=MainWindow_Main)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../images/main-window/new-file.svg"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.action_New_File.setIcon(icon1)
        self.action_New_File.setObjectName("action_New_File")
        self.action_Open_File = QtGui.QAction(parent=MainWindow_Main)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../images/main-window/open-file.svg"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.action_Open_File.setIcon(icon2)
        self.action_Open_File.setObjectName("action_Open_File")
        self.action_Save = QtGui.QAction(parent=MainWindow_Main)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../images/main-window/save-file.svg"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.action_Save.setIcon(icon3)
        self.action_Save.setObjectName("action_Save")
        self.action_Print = QtGui.QAction(parent=MainWindow_Main)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../images/main-window/print.svg"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.action_Print.setIcon(icon4)
        self.action_Print.setObjectName("action_Print")
        self.action_Export_PDF = QtGui.QAction(parent=MainWindow_Main)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../images/main-window/export-pdf.svg"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.action_Export_PDF.setIcon(icon5)
        self.action_Export_PDF.setObjectName("action_Export_PDF")
        self.action_Exit = QtGui.QAction(parent=MainWindow_Main)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../images/main-window/exit-red.svg"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.action_Exit.setIcon(icon6)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Undo = QtGui.QAction(parent=MainWindow_Main)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../../images/main-window/undo-transparent.svg"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.action_Undo.setIcon(icon7)
        self.action_Undo.setObjectName("action_Undo")
        self.action_Redo = QtGui.QAction(parent=MainWindow_Main)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../../images/main-window/redo-transparent.svg"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.action_Redo.setIcon(icon8)
        self.action_Redo.setObjectName("action_Redo")
        self.action_Cut = QtGui.QAction(parent=MainWindow_Main)
        self.action_Cut.setObjectName("action_Cut")
        self.action_Copy = QtGui.QAction(parent=MainWindow_Main)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Paste = QtGui.QAction(parent=MainWindow_Main)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Add_Data = QtGui.QAction(parent=MainWindow_Main)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../../images/main-window/add-data.svg"), QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off)
        self.action_Add_Data.setIcon(icon9)
        self.action_Add_Data.setObjectName("action_Add_Data")
        self.action_Modify_Data = QtGui.QAction(parent=MainWindow_Main)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../../images/main-window/data-processing-1.svg"), QtGui.QIcon.Mode.Normal,
                         QtGui.QIcon.State.Off)
        self.action_Modify_Data.setIcon(icon10)
        self.action_Modify_Data.setObjectName("action_Modify_Data")
        self.action_Bold = QtGui.QAction(parent=MainWindow_Main)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../../images/main-window/bold.svg"), QtGui.QIcon.Mode.Normal,
                         QtGui.QIcon.State.Off)
        self.action_Bold.setIcon(icon11)
        self.action_Bold.setObjectName("action_Bold")
        self.action_Italic = QtGui.QAction(parent=MainWindow_Main)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../../images/main-window/italic.svg"), QtGui.QIcon.Mode.Normal,
                         QtGui.QIcon.State.Off)
        self.action_Italic.setIcon(icon12)
        self.action_Italic.setObjectName("action_Italic")
        self.action_Underline = QtGui.QAction(parent=MainWindow_Main)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../../images/main-window/underline.svg"), QtGui.QIcon.Mode.Normal,
                         QtGui.QIcon.State.Off)
        self.action_Underline.setIcon(icon13)
        self.action_Underline.setObjectName("action_Underline")
        self.action_Left = QtGui.QAction(parent=MainWindow_Main)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../../images/main-window/text-left.svg"), QtGui.QIcon.Mode.Normal,
                         QtGui.QIcon.State.Off)
        self.action_Left.setIcon(icon14)
        self.action_Left.setObjectName("action_Left")
        self.action_Right = QtGui.QAction(parent=MainWindow_Main)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../../images/main-window/text-right.svg"), QtGui.QIcon.Mode.Normal,
                         QtGui.QIcon.State.Off)
        self.action_Right.setIcon(icon15)
        self.action_Right.setObjectName("action_Right")
        self.action_Center = QtGui.QAction(parent=MainWindow_Main)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("../../images/main-window/text-center.svg"), QtGui.QIcon.Mode.Normal,
                         QtGui.QIcon.State.Off)
        self.action_Center.setIcon(icon16)
        self.action_Center.setObjectName("action_Center")
        self.action_Justify = QtGui.QAction(parent=MainWindow_Main)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("../../images/main-window/text-justify.svg"), QtGui.QIcon.Mode.Normal,
                         QtGui.QIcon.State.Off)
        self.action_Justify.setIcon(icon17)
        self.action_Justify.setObjectName("action_Justify")
        self.action_About_Application = QtGui.QAction(parent=MainWindow_Main)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("../../images/main-window/mw-help.svg"), QtGui.QIcon.Mode.Normal,
                         QtGui.QIcon.State.Off)
        self.action_About_Application.setIcon(icon18)
        self.action_About_Application.setObjectName("action_About_Application")
        self.action_Settings = QtGui.QAction(parent=MainWindow_Main)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("../../images/main-window/mw-settings.svg"), QtGui.QIcon.Mode.Normal,
                         QtGui.QIcon.State.Off)
        self.action_Settings.setIcon(icon19)
        self.action_Settings.setObjectName("action_Settings")
        self.action_Color = QtGui.QAction(parent=MainWindow_Main)
        self.action_Color.setObjectName("action_Color")
        self.action_Font = QtGui.QAction(parent=MainWindow_Main)
        self.action_Font.setObjectName("action_Font")
        self.menu_File.addAction(self.action_New_File)
        self.menu_File.addAction(self.action_Open_File)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Print)
        self.menu_File.addAction(self.action_Export_PDF)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_Data.addAction(self.action_Add_Data)
        self.menu_Data.addAction(self.action_Modify_Data)
        self.menu_Edit.addAction(self.action_Undo)
        self.menu_Edit.addAction(self.action_Redo)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Format.addAction(self.action_Bold)
        self.menu_Format.addAction(self.action_Italic)
        self.menu_Format.addAction(self.action_Underline)
        self.menu_Format.addSeparator()
        self.menu_Format.addAction(self.action_Left)
        self.menu_Format.addAction(self.action_Right)
        self.menu_Format.addAction(self.action_Center)
        self.menu_Format.addAction(self.action_Justify)
        self.menu_Format.addSeparator()
        self.menu_Format.addAction(self.action_Color)
        self.menu_Format.addAction(self.action_Font)
        self.menu_Settings.addAction(self.action_Settings)
        self.menu_Help.addAction(self.action_About_Application)
        self.menubar_Menu.addAction(self.menu_File.menuAction())
        self.menubar_Menu.addAction(self.menu_Edit.menuAction())
        self.menubar_Menu.addAction(self.menu_Data.menuAction())
        self.menubar_Menu.addAction(self.menu_Format.menuAction())
        self.menubar_Menu.addAction(self.menu_Analysis.menuAction())
        self.menubar_Menu.addAction(self.menu_Charts.menuAction())
        self.menubar_Menu.addAction(self.menu_Settings.menuAction())
        self.menubar_Menu.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.action_New_File)
        self.toolBar.addAction(self.action_Open_File)
        self.toolBar.addAction(self.action_Save)
        self.toolBar.addAction(self.action_Print)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Add_Data)
        self.toolBar.addAction(self.action_Modify_Data)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Undo)
        self.toolBar.addAction(self.action_Redo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Left)
        self.toolBar.addAction(self.action_Center)
        self.toolBar.addAction(self.action_Right)
        self.toolBar.addAction(self.action_Justify)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Bold)
        self.toolBar.addAction(self.action_Italic)
        self.toolBar.addAction(self.action_Underline)

        self.retranslateUi(MainWindow_Main)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Main)

    def retranslateUi(self, MainWindow_Main):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Main.setWindowTitle(_translate("MainWindow_Main", "Dex"))
        self.menu_File.setTitle(_translate("MainWindow_Main", "Plik"))
        self.menu_Data.setTitle(_translate("MainWindow_Main", "Dane"))
        self.menu_Edit.setTitle(_translate("MainWindow_Main", "Edycja"))
        self.menu_Format.setTitle(_translate("MainWindow_Main", "Format"))
        self.menu_Analysis.setTitle(_translate("MainWindow_Main", "Analiza"))
        self.menu_Charts.setTitle(_translate("MainWindow_Main", "Wykresy"))
        self.menu_Settings.setTitle(_translate("MainWindow_Main", "Ustawienia"))
        self.menu_Help.setTitle(_translate("MainWindow_Main", "?"))
        self.toolBar.setWindowTitle(_translate("MainWindow_Main", "toolBar"))
        self.action_New_File.setText(_translate("MainWindow_Main", "Nowy"))
        self.action_New_File.setShortcut(_translate("MainWindow_Main", "Ctrl+N"))
        self.action_Open_File.setText(_translate("MainWindow_Main", "Otwórz"))
        self.action_Open_File.setShortcut(_translate("MainWindow_Main", "Ctrl+O"))
        self.action_Save.setText(_translate("MainWindow_Main", "Zapisz"))
        self.action_Save.setShortcut(_translate("MainWindow_Main", "Ctrl+S"))
        self.action_Print.setText(_translate("MainWindow_Main", "Drukuj"))
        self.action_Print.setShortcut(_translate("MainWindow_Main", "Ctrl+P"))
        self.action_Export_PDF.setText(_translate("MainWindow_Main", "Eksportuj jako PDF"))
        self.action_Exit.setText(_translate("MainWindow_Main", "Wyjście"))
        self.action_Exit.setShortcut(_translate("MainWindow_Main", "Ctrl+Alt+F4"))
        self.action_Undo.setText(_translate("MainWindow_Main", "Cofnij"))
        self.action_Undo.setShortcut(_translate("MainWindow_Main", "Ctrl+Z"))
        self.action_Redo.setText(_translate("MainWindow_Main", "Ponów"))
        self.action_Redo.setShortcut(_translate("MainWindow_Main", "Ctrl+Y"))
        self.action_Cut.setText(_translate("MainWindow_Main", "Wytnij"))
        self.action_Cut.setShortcut(_translate("MainWindow_Main", "Ctrl+X"))
        self.action_Copy.setText(_translate("MainWindow_Main", "Kopiuj"))
        self.action_Copy.setShortcut(_translate("MainWindow_Main", "Ctrl+C"))
        self.action_Paste.setText(_translate("MainWindow_Main", "Wklej"))
        self.action_Paste.setShortcut(_translate("MainWindow_Main", "Ctrl+V"))
        self.action_Add_Data.setText(_translate("MainWindow_Main", "Dodaj dane"))
        self.action_Modify_Data.setText(_translate("MainWindow_Main", "Modyfikuj dane"))
        self.action_Bold.setText(_translate("MainWindow_Main", "Pogrubienie"))
        self.action_Bold.setShortcut(_translate("MainWindow_Main", "Ctrl+B"))
        self.action_Italic.setText(_translate("MainWindow_Main", "Kursywa"))
        self.action_Italic.setShortcut(_translate("MainWindow_Main", "Ctrl+I"))
        self.action_Underline.setText(_translate("MainWindow_Main", "Podkreślenie"))
        self.action_Underline.setShortcut(_translate("MainWindow_Main", "Ctrl+U"))
        self.action_Left.setText(_translate("MainWindow_Main", "Wyrównaj do lewej"))
        self.action_Left.setShortcut(_translate("MainWindow_Main", "Ctrl+L"))
        self.action_Right.setText(_translate("MainWindow_Main", "Wyrównaj do prawej"))
        self.action_Right.setShortcut(_translate("MainWindow_Main", "Ctrl+R"))
        self.action_Center.setText(_translate("MainWindow_Main", "Wyśrodkowanie"))
        self.action_Center.setShortcut(_translate("MainWindow_Main", "Ctrl+E"))
        self.action_Justify.setText(_translate("MainWindow_Main", "Wyjustuj"))
        self.action_Justify.setShortcut(_translate("MainWindow_Main", "Ctrl+J"))
        self.action_About_Application.setText(_translate("MainWindow_Main", "O programie"))
        self.action_About_Application.setShortcut(_translate("MainWindow_Main", "Ctrl+F1"))
        self.action_Settings.setText(_translate("MainWindow_Main", "Ustawienia"))
        self.action_Color.setText(_translate("MainWindow_Main", "Kolor"))
        self.action_Font.setText(_translate("MainWindow_Main", "Czcionka"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Main = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Main()
    ui.setupUi(MainWindow_Main)
    MainWindow_Main.show()
    sys.exit(app.exec())
