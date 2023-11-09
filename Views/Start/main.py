from PyQt6 import QtGui
from PyQt6.QtCore import QTranslator
from PyQt6.QtWidgets import QApplication
from Controllers.MainController import MainController
from Controllers.AddFileController import AddFileController
from Controllers.ModifyDataController import ModifyDataController
import sys


class Main:
    def __init__(self):
        # Window Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)

        app.setWindowIcon(icon)

        # Translations
        plQtGuiPath = "../../Translations/PL/qtbase_pl.qm"

        if translator.load(plQtGuiPath):
            app.installTranslator(translator)

        # Controllers
        self.mainController = MainController()
        self.addFileController = AddFileController()
        self.modifyDataController = ModifyDataController()

        # Connections
        self.mainController.action_Add_Data.triggered.connect(self.addFileController.createWindowAddFile)
        self.mainController.action_Modify_Data.triggered.connect(self.modifyDataController.createWindowModifyData)
        self.mainController.action_About_Application.triggered.connect(self.mainController.printDataFrames)
        self.mainController.action_Settings.triggered.connect(self.mainController.createWindowSettings)


translator = QTranslator()
app = QApplication(sys.argv)
window = Main()
sys.exit(app.exec())
