from PyQt6 import QtGui
from PyQt6.QtCore import QTranslator
from PyQt6.QtWidgets import QApplication
from Controllers.MainController import MainController
from Controllers.AddFileController import AddFileController
from Controllers.ModifyDataController import ModifyDataController
from Controllers.SettingsController import SettingsController
from Controllers.PlotsController import PlotsController
from Controllers.AnalysisController import AnalysisController
import sys


class Main:
    def __init__(self):
        # Window Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)

        app.setWindowIcon(icon)

        # Controllers
        self.mainController = MainController()
        self.settingsController = SettingsController(app, translator)
        self.addFileController = AddFileController(self.mainController)
        self.modifyDataController = ModifyDataController()
        self.plotsController = PlotsController(self.mainController)
        self.analysisController = AnalysisController(self.mainController)

        # Connections
        self.mainController.action_Add_Data.triggered.connect(self.addFileController.createWindowAddFile)
        self.mainController.action_Modify_Data.triggered.connect(self.modifyDataController.createWindowModifyData)
        self.mainController.action_About_Application.triggered.connect(self.mainController.createAboutApp)
        self.mainController.action_Settings.triggered.connect(self.settingsController.showSettingsWindow)


translator = QTranslator()
app = QApplication(sys.argv)
window = Main()
sys.exit(app.exec())
