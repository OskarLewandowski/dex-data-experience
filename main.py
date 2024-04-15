from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import QTranslator, Qt
from PyQt6.QtWidgets import QApplication
from Controllers.MainController import MainController
from Controllers.AddFileController import AddFileController
from Controllers.ModifyDataController import ModifyDataController
from Controllers.SettingsController import SettingsController
from Controllers.PlotsController import PlotsController
from Controllers.AnalysisController import AnalysisController
import sys
import os


class Main:
    def __init__(self):
        # Windows Icon
        icon_path = getFullPath("images/app-icon/dex-icon-512x512.png")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        app.setWindowIcon(icon)

        # Controllers
        self.mainController = MainController()
        self.settingsController = SettingsController(app, translator, self.mainController)
        self.addFileController = AddFileController(self.mainController)
        self.modifyDataController = ModifyDataController()
        self.plotsController = PlotsController(self.mainController)
        self.analysisController = AnalysisController(self.mainController)

        # Connections
        self.mainController.action_Add_Data.triggered.connect(self.addFileController.createWindowAddFile)
        self.mainController.action_Modify_Data.triggered.connect(self.modifyDataController.createWindowModifyData)
        self.mainController.action_About_Application.triggered.connect(self.mainController.createAboutApp)
        self.mainController.action_Settings.triggered.connect(self.settingsController.showSettingsWindow)


def getFullPath(relative_path):
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, relative_path)
    return full_path


translator = QTranslator()
app = QApplication(sys.argv)

splash_pix = QtGui.QPixmap(getFullPath("images/app-icon/dex_splash.png"))
splash = QtWidgets.QSplashScreen(splash_pix)

font = splash.font()
font.setPointSize(18)
font.setBold(True)
splash.setFont(font)

splash.showMessage("Aplikacja się uruchamia. Proszę czekać...",
                   Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom,
                   Qt.GlobalColor.black)
splash.show()

window = Main()

splash.finish(window.mainController)

sys.exit(app.exec())
