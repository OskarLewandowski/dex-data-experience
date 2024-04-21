from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtWidgets import QMessageBox, QApplication, QLabel, QHBoxLayout, QWidget, QStyle


class MessageModel:

    @classmethod
    def error(cls, errorCode="0000", errorMessage="Coś poszło nie tak"):
        message = "Wystąpił bład: [{0}] - {1}".format(errorCode, errorMessage)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(message)
        msg.setWindowTitle('Dex')

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

            msg.setStandardButtons(
                QMessageBox.StandardButton.Abort | QMessageBox.StandardButton.Close)
            msg.button(QMessageBox.StandardButton.Abort).setText('Dodaj kolejny plik')
            msg.button(QMessageBox.StandardButton.Close).setText('Zamknij')

            reply = msg.exec()

            return reply == QMessageBox.StandardButton.Close
        except Exception as e:
            cls.error("0003", str(e))

    @classmethod
    def saveConfirmation(cls, text="Czy na pewno chcesz załadować dane?", bntYesText="Tak", bntAbortText="Anuluj"):
        try:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Question)
            msg.setText(text)
            msg.setWindowTitle('Dex')

            msg.setStandardButtons(
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Abort)
            msg.button(QMessageBox.StandardButton.Yes).setText(bntYesText)
            msg.button(QMessageBox.StandardButton.Abort).setText(bntAbortText)

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

    @classmethod
    def translationError(cls, language="English"):
        translations = {
            "English": {
                "message": "Please note that not all parts of the application are translated into English yet.\nPlease choose another language.",
                "title": "Dex - English is unsupported",
                "close_button": "Close"
            },
            "Español": {
                "message": "Tenga en cuenta que no todas las partes de la aplicación están traducidas al español todavía.\nPor favor, elija otro idioma.",
                "title": "Dex - Español no es compatible",
                "close_button": "Cerrar"
            },
            "Français": {
                "message": "Veuillez noter que toutes les parties de l'application ne sont pas encore traduites en français.\nVeuillez choisir une autre langue.",
                "title": "Dex - Français n'est pas pris en charge",
                "close_button": "Fermer"
            },
            "Deutsch": {
                "message": "Bitte beachten Sie, dass noch nicht alle Teile der Anwendung ins Deutsche übersetzt sind.\nBitte wählen Sie eine andere Sprache.",
                "title": "Dex - Deutsch wird nicht unterstützt",
                "close_button": "Schließen"
            },
            "Italiano": {
                "message": "Si prega di notare che non tutte le parti dell'applicazione sono ancora tradotte in italiano.\nSi prega di scegliere un'altra lingua.",
                "title": "Dex - Italiano non è supportato",
                "close_button": "Chiudi"
            },
            "Português": {
                "message": "Por favor, note que nem todas as partes da aplicação estão traduzidas para o português ainda.\nPor favor, escolha outro idioma.",
                "title": "Dex - Português não é suportado",
                "close_button": "Fechar"
            },
            "Русский": {
                "message": "Обратите внимание, что не все части приложения еще переведены на русский язык.\nПожалуйста, выберите другой язык.",
                "title": "Dex - Русский не поддерживается",
                "close_button": "Закрыть"
            },
            "中文": {
                "message": "请注意，应用程序的不是所有部分都已经翻译成中文了。\n请选择另一种语言。",
                "title": "Dex - 中文不受支持",
                "close_button": "关闭"
            },
            "日本語": {
                "message": "すべてのアプリケーションの部分がまだ日本語に翻訳されていないことに注意してください。\n別の言語を選択してください。",
                "title": "Dex - 日本語はサポートされていません",
                "close_button": "閉じる"
            }
        }
        translation = translations.get(language, translations["English"])

        message = translation["message"]
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(message)
        msg.setWindowTitle(translation['title'])

        msg.setStandardButtons(QMessageBox.StandardButton.Close)
        msg.button(QMessageBox.StandardButton.Close).setText(translation["close_button"])

        reply = msg.exec()

        return reply == QMessageBox.StandardButton.Close

    @classmethod
    def show_toast(cls, message, timeout=1000, parent=None):
        toast = QWidget(parent)
        toast_layout = QHBoxLayout(toast)
        toast_layout.setContentsMargins(15, 15, 15, 15)

        icon_label = QLabel(toast)
        icon = QApplication.style().standardIcon(QStyle.StandardPixmap.SP_DialogApplyButton)
        icon_label.setPixmap(icon.pixmap(24, 24))
        toast_layout.addWidget(icon_label)

        text_label = QLabel(message)
        toast_layout.addWidget(text_label)

        toast.setStyleSheet("""  
            QWidget {
                font-size: 24px;
                padding: 10px;
                border: 3px solid green;
            }
            
            QLabel {
                border: none;
            }
        """)
        toast.setWindowFlags(
            Qt.WindowType.SplashScreen | Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        if parent:
            parent_geometry = parent.geometry()
            toast_width = toast.sizeHint().width()
            toast.move(parent_geometry.x() + (parent_geometry.width() - toast_width) // 2, parent_geometry.y() + 40)
        else:
            screen_geometry = QApplication.primaryScreen().availableGeometry()
            toast_width = toast.sizeHint().width()
            toast.move((screen_geometry.width() - toast_width) // 2, 20)

        toast.show()

        QTimer.singleShot(timeout, toast.close)
