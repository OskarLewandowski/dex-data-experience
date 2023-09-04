from PyQt6 import QtWidgets, QtCore, QtGui
from main_window import Ui_MainWindow


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Dex")

        self.resizeEvent = self.handleResize

        self.default_font_size = 26
        self.default_icon_size = QtCore.QSize(70, 70)

        self.handleResize(None)

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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec())
