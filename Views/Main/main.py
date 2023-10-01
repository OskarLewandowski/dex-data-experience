from PyQt6.QtWidgets import QMainWindow, QApplication
from Views.Main.main_window import Ui_MainWindow_Main
import sys


class Main(QMainWindow, Ui_MainWindow_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


app = QApplication(sys.argv)
window = Main()
sys.exit(app.exec())
