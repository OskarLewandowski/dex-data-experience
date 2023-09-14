from PyQt6 import QtWidgets, QtCore, QtGui
from add_file import Ui_dialog_add_file
from data_storage import DataStorage
from modify_data import Ui_MainWindow_modify_data

"""
For test only
"""


def printDataFrames():
    keys = DataStorage.get_all_keys()
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
    dialog = QtWidgets.QDialog()
    add_file_ui = Ui_dialog_add_file()
    add_file_ui.setupUi(dialog)

    result = dialog.exec()
    if result == QtWidgets.QDialog.DialogCode.Accepted:
        pass


"""
Confirmation window for closing the program
"""


def exitConfirmationDialog():
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Icon.Question)
    msg.setText('Czy na pewno chcesz zamknąć program?')
    msg.setWindowTitle('Zamknij program')

    msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
    msg.button(QtWidgets.QMessageBox.StandardButton.Yes).setText('Tak')
    msg.button(QtWidgets.QMessageBox.StandardButton.No).setText('Nie')

    reply = msg.exec()

    return reply == QtWidgets.QMessageBox.StandardButton.Yes


"""
Automatic resizing of icons and text in the main window
"""


def handleResize(self, event):
    if event:
        width = self.width()
        height = self.height()

        font_size = int(self.default_font_size * ((width + height) / (800 + 400)) / 2)
        icon_size_width = int(self.default_icon_size.width() * (width / 800))
        icon_size_height = int(self.default_icon_size.height() * (height / 600))
    else:
        font_size = self.default_font_size
        icon_size_width = self.default_icon_size.width()
        icon_size_height = self.default_icon_size.height()

    font = QtGui.QFont()
    font.setPointSize(font_size)

    self.ui.button_add_file.setFont(font)
    self.ui.button_modify_data.setFont(font)
    self.ui.button_analysis_data.setFont(font)
    self.ui.button_settings.setFont(font)
    self.ui.button_help.setFont(font)
    self.ui.button_exit.setFont(font)

    icon_size = QtCore.QSize(icon_size_width, icon_size_height)

    self.ui.button_add_file.setIconSize(icon_size)
    self.ui.button_modify_data.setIconSize(icon_size)
    self.ui.button_analysis_data.setIconSize(icon_size)
    self.ui.button_settings.setIconSize(icon_size)
    self.ui.button_help.setIconSize(icon_size)
    self.ui.button_exit.setIconSize(icon_size)
