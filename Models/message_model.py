from PyQt6 import QtGui
from PyQt6.QtWidgets import QMessageBox


class MessageModel:

    @classmethod
    def error(cls, errorCode="0000", errorMessage="Coś poszło nie tak"):
        message = "Wystąpił bład: [{0}] - {1}".format(errorCode, errorMessage)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(message)
        msg.setWindowTitle('Dex')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        msg.setWindowIcon(icon)

        msg.setStandardButtons(QMessageBox.StandardButton.Close)
        msg.button(QMessageBox.StandardButton.Close).setText('Zamknij')
        reply = msg.exec()

        return reply == QMessageBox.StandardButton.Close

    @classmethod
    def statusConfirmation(cls, fileName):
        try:
            message = "Plik '{}' został pomyślnie załadowny.".format(fileName)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setText(message)
            msg.setWindowTitle('Dex')

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../../images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                           QtGui.QIcon.State.Off)
            msg.setWindowIcon(icon)

            msg.setStandardButtons(
                QMessageBox.StandardButton.Abort | QMessageBox.StandardButton.Close)
            msg.button(QMessageBox.StandardButton.Abort).setText('Dodaj kolejny plik')
            msg.button(QMessageBox.StandardButton.Close).setText('Wróc')

            reply = msg.exec()

            return reply == QMessageBox.StandardButton.Close
        except Exception as e:
            cls.error("0003", str(e))

    @classmethod
    def saveConfirmation(cls):
        try:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setText('Czy na pewno chcesz załadować dane?')
            msg.setWindowTitle('Dex')

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../../images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                           QtGui.QIcon.State.Off)
            msg.setWindowIcon(icon)

            msg.setStandardButtons(
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Abort)
            msg.button(QMessageBox.StandardButton.Yes).setText('Tak')
            msg.button(QMessageBox.StandardButton.Abort).setText('Anuluj')

            reply = msg.exec()

            return reply == QMessageBox.StandardButton.Yes
        except Exception as e:
            cls.error("0004", str(e))

    @classmethod
    def exitApp(cls):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText('Czy chcesz zapisać zmiany w pliku?')
        msg.setWindowTitle('Dex')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        msg.setWindowIcon(icon)

        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Abort)
        msg.button(QMessageBox.StandardButton.Yes).setText('Zapisz')
        msg.button(QMessageBox.StandardButton.No).setText('Nie zapisuj')
        msg.button(QMessageBox.StandardButton.Abort).setText('Anuluj')

        reply = msg.exec()

        if reply == QMessageBox.StandardButton.Yes:
            return 1
        elif reply == QMessageBox.StandardButton.No:
            return 2
        else:
            return 3

    @classmethod
    def notSavedProject(cls, func_saveChanges):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setText('Czy chcesz zapisać zmiany w obecnym projekcie?')
        msg.setWindowTitle('Dex')

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../images/app-icon/dex-icon-512x512.png"), QtGui.QIcon.Mode.Normal,
                       QtGui.QIcon.State.Off)
        msg.setWindowIcon(icon)

        msg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Abort)
        msg.button(QMessageBox.StandardButton.Yes).setText('Zapisz')
        msg.button(QMessageBox.StandardButton.No).setText('Nie zapisuj')
        msg.button(QMessageBox.StandardButton.Abort).setText('Anuluj')

        reply = msg.exec()

        if reply == QMessageBox.StandardButton.Yes:
            func_saveChanges()
            return True
        elif reply == QMessageBox.StandardButton.No:
            return True
        else:
            return False
