from PyQt6.QtWidgets import QDialog, QMainWindow
from Models.data_storage_model import DataStorageModel
from Views.Settings.settings_main_window import Ui_Dialog_settings
from Views.Main.main_window import Ui_MainWindow_Main


class MainController(QMainWindow, Ui_MainWindow_Main):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.window_settings = None
        self.window_settings_ui = None

    def createWindowSettings(self):
        """
        Create the settings window
        """
        self.window_settings = QDialog()
        self.window_settings_ui = Ui_Dialog_settings()
        self.window_settings_ui.setupUi(self.window_settings)
        self.window_settings.show()

    @staticmethod
    def printDataFrames():
        """
        Display data frames in memory
        !!! For test only !!!
        """
        keys = DataStorageModel.get_all_keys()
        for i in keys:
            print(DataStorageModel.get(i))
        print(keys)
