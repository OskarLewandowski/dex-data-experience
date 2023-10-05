from PyQt6.QtWidgets import QApplication
from Controllers.MainController import MainController
import sys


class Main:
    def __init__(self):
        # Controllers
        self.mainController = MainController()

        # Connections
        self.mainController.action_Add_Data.triggered.connect(self.mainController.createWindowAddFile)
        self.mainController.action_Modify_Data.triggered.connect(self.mainController.createWindowModifyData)
        self.mainController.action_About_Application.triggered.connect(self.mainController.printDataFrames)


app = QApplication(sys.argv)
window = Main()
sys.exit(app.exec())
