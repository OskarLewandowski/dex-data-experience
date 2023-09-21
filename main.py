from PyQt6 import QtWidgets, QtCore, QtGui
from main_window import Ui_MainWindow
from main_window_functions import *


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Dex")

        self.default_font_size = 26
        self.default_icon_size = QtCore.QSize(70, 70)

        # connections
        self.ui.button_exit.clicked.connect(self.exitButton)
        self.ui.button_add_file.clicked.connect(self.openAddFileDialog)
        self.ui.button_modify_data.clicked.connect(self.openModifyDataWindow)
        self.ui.button_analysis_data.clicked.connect(self.openDataAnalysis)
        self.ui.button_settings.clicked.connect(self.openSettings)

        # for test
        self.ui.button_help.clicked.connect(self.printDataFrames)

    def resizeEvent(self, event):
        handleResize(self, event)

    def exitButton(self):
        confirmed = exitConfirmationDialog()

        if confirmed:
            sys.exit()

    def closeEvent(self, event):
        confirmed = exitConfirmationDialog()

        if confirmed:
            event.accept()
        else:
            event.ignore()

    def openAddFileDialog(self):
        openAddFileDialog(self)

    def openModifyDataWindow(self):
        openModifyDataWindow(self)

    def printDataFrames(self):
        printDataFrames()

    def openDataAnalysis(self):
        openDataAnalysis(self)

    def openSettings(self):
        openSettings(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("./images/app-icon/dex-icon-512x512.png"))
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec())
