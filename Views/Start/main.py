from PyQt6.QtWidgets import QApplication
from Controllers.MainController import MainController
from Controllers.AddFileController import AddFileController
import sys


class Main:
    def __init__(self):
        # Controllers
        self.mainController = MainController()
        self.addFileController = AddFileController()

        # Connections
        self.mainController.action_Add_Data.triggered.connect(self.addFileController.createWindowAddFile)
        self.mainController.action_Modify_Data.triggered.connect(self.mainController.createWindowModifyData)
        self.mainController.action_About_Application.triggered.connect(self.mainController.printDataFrames)
        self.mainController.action_Settings.triggered.connect(self.mainController.createWindowSettings)


app = QApplication(sys.argv)
window = Main()
sys.exit(app.exec())
