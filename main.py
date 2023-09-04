from PyQt6 import QtWidgets, QtCore, QtGui
from main_window import Ui_MainWindow
from main_window_functions import exit_confirmation_dialog, handleResize


class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Dex")

        self.default_font_size = 26
        self.default_icon_size = QtCore.QSize(70, 70)

        # connections
        self.ui.button_exit.clicked.connect(self.exitButton)

    def resizeEvent(self, event):
        handleResize(self, event)

    def exitButton(self):
        confirmed = exit_confirmation_dialog()

        if confirmed:
            sys.exit()

    def closeEvent(self, event):
        confirmed = exit_confirmation_dialog()

        if confirmed:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("./images/app-icon/dex-icon-512x512.png"))
    MainWindow = MyMainWindow()
    MainWindow.show()
    sys.exit(app.exec())
