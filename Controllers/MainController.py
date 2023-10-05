from PyQt6.QtWidgets import QDialog, QMainWindow
from Views.AddFile.add_file_main_window import Ui_dialog_add_file
from Models.data_storage_model import DataStorageModel
from Views.ModifyData.modify_data_main_window import Ui_MainWindow_modify_data
from Views.Settings.settings_main_window import Ui_Dialog_settings


class MainController:

    def __init__(self):
        self.window_add_file = None
        self.window_add_file_ui = None

        self.window_modify_data = None
        self.window_modify_data_ui = None

        self.window_settings = None
        self.window_settings_ui = None

    def createWindowAddFile(self):
        """
        Create the add file window, to import data
        """
        self.window_add_file = QDialog()
        self.window_add_file_ui = Ui_dialog_add_file()
        self.window_add_file_ui.setupUi(self.window_add_file)
        self.window_add_file.show()

    def createWindowModifyData(self):
        """
        Window to modify data frames
        """
        self.window_modify_data = QMainWindow()
        self.window_modify_data_ui = Ui_MainWindow_modify_data()
        self.window_modify_data_ui.setupUi(self.window_modify_data)
        self.window_modify_data.show()

    def createWindowSettings(self):
        """
        Create the settings window
        """
        self.window_settings = QDialog()
        self.window_settings_ui = Ui_Dialog_settings()
        self.window_settings_ui.setupUi(self.window_settings)
        self.window_settings.show()

    def printDataFrames(self):
        """
        Display data frames in memory
        !!! For test only !!!
        """
        keys = DataStorageModel.get_all_keys()
        for i in keys:
            print(DataStorageModel.get(i))
        print(keys)
