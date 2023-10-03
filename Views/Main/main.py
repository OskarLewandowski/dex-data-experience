from PyQt6.QtWidgets import QMainWindow, QApplication
from Views.Main.main_window import Ui_MainWindow_Main
from Controllers.MainController import MainController
import sys


class Main(QMainWindow, Ui_MainWindow_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Connections
        self.action_Add_Data.triggered.connect(self.openAddFileWindow)
        self.action_Modify_Data.triggered.connect(self.openModifData)
        self.action_About_Application.triggered.connect(self.printData)

    def openAddFileWindow(self):
        MainController.openAddFileDialog(self)

    def openModifData(self):
        MainController.openModifyDataWindow(self)

    def printData(self):
        MainController.printDataFrames(self)


app = QApplication(sys.argv)
window = Main()
sys.exit(app.exec())
