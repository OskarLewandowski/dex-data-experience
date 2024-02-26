from PyQt6 import QtGui
from PyQt6.QtWidgets import QMainWindow
from Views.Main.main_window import Ui_MainWindow_Main


class AnalysisController(QMainWindow, Ui_MainWindow_Main):
    def __init__(self, main_controller):
        super().__init__()
        self.main = main_controller
