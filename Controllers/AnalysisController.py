from PyQt6 import QtGui
from PyQt6.QtWidgets import QMainWindow
from Views.Main.main_window import Ui_MainWindow_Main


class AnalysisController(QMainWindow, Ui_MainWindow_Main):
    def __init__(self, main_controller):
        super().__init__()
        self.main = main_controller

        self.main.actionTest_1.triggered.connect(self.test)

    def test(self):
        cursor = self.main.textEdit_Board.textCursor()
        cursor.movePosition(QtGui.QTextCursor.MoveOperation.End)
        cursor.insertText("Test-1")
