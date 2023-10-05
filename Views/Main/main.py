from PyQt6.QtWidgets import QMainWindow, QApplication
from Views.Main.main_window import Ui_MainWindow_Main
from Controllers.MainController import MainController
import sys


class Main(QMainWindow, Ui_MainWindow_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # Controllers
        self.mainController = MainController()

        # Connections
        self.action_Add_Data.triggered.connect(self.openAddFileWindow)
        self.action_Modify_Data.triggered.connect(self.openModifData)
        self.action_About_Application.triggered.connect(self.printData)

    def openAddFileWindow(self):
        self.mainController.createWindowAddFile()

    def openModifData(self):
        self.mainController.createWindowModifyData()

    def printData(self):
        self.mainController.printDataFrames()


app = QApplication(sys.argv)
window = Main()
sys.exit(app.exec())
