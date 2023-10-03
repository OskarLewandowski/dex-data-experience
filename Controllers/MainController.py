from PyQt6 import QtWidgets
from Views.AddFile.add_file_main_window import Ui_dialog_add_file
from Models.data_storage_model import DataStorage
from Views.ModifyData.modify_data_main_window import Ui_MainWindow_modify_data
from Views.ModifyData.data_analysis import Ui_MainWindow_data_analysis
from Views.Settings.settings_main_window import Ui_Dialog_settings


class MainController:
    """
    Window for settings
    """

    def openSettings(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog_settings()
        self.ui.setupUi(self.window)
        self.window.show()

    """
    Window for data analysis
    """

    def openDataAnalysis(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_data_analysis()
        self.ui.setupUi(self.window)
        self.window.show()

    """
    For test only
    """

    def printDataFrames(self):
        keys = DataStorage.get_all_keys()
        for i in keys:
            print(DataStorage.get(i))
        print(keys)

    """
    Window to modify data frames
    """

    def openModifyDataWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_modify_data()
        self.ui.setupUi(self.window)
        self.window.show()

    """
    Manage window for import data
    """

    def openAddFileDialog(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_dialog_add_file()
        self.ui.setupUi(self.window)
        self.window.show()

    """
    Confirmation window for closing the program
    """

    def exitConfirmationDialog(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
        msg.setText('Czy na pewno chcesz zamknąć program?')
        msg.setWindowTitle('Zamknij program')

        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        msg.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Tak')
        msg.button(QtWidgets.QMessageBox.StandardButton.No).setText('Nie')

        reply = msg.exec()

        return reply == QtWidgets.QMessageBox.StandardButton.Yes
