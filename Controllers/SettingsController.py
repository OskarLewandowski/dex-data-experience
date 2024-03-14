import os
import sys

import qdarktheme
from PyQt6.QtWidgets import QMainWindow, QColorDialog, QPushButton
from PyQt6.QtCore import Qt, QDir, QFile, QCoreApplication
from qt_material import QtStyleTools
from xml.etree import ElementTree as ET
from Views.Settings.settings_window import Ui_MainWindow_Settings
import json


class SettingsController(QMainWindow, Ui_MainWindow_Settings, QtStyleTools):
    SETTINGS_FILE = "settings.json"
    CUSTOM_THEM_FILE = "Themes/my_custom.xml"

    def __init__(self, app, translator, main):
        super().__init__()
        self.app = app
        self.translator = translator
        self.main = main
        self.setWindowFlags(
            Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowCloseButtonHint)

        self.setupUi(self)

        self.populateLanguage()
        self.populateThemes()
        self.loadSettings()
        self.loadAndApplyCustomStylesheet()
        self.loadLanguage()

        # Connections
        self.comboBox_Theme.currentIndexChanged.connect(self.loadThem)
        self.comboBox_Theme.currentIndexChanged.connect(self.saveSettings)
        self.comboBox_Language.currentIndexChanged.connect(self.saveSettings)
        self.checkBox_Use_Custom_Theme.clicked.connect(self.loadThem)
        self.checkBox_Use_Secondary_Colors.clicked.connect(self.loadThem)
        self.comboBox_Language.currentIndexChanged.connect(self.loadLanguage)
        self.checkBox_Use_Custom_Theme.clicked.connect(self.saveSettings)
        self.checkBox_Use_Secondary_Colors.clicked.connect(self.saveSettings)
        self.comboBox_Icon_Color.currentIndexChanged.connect(self.loadThem)
        self.comboBox_Icon_Color.currentIndexChanged.connect(self.saveSettings)
        self.comboBox_Window_Reminding_To_Save.currentIndexChanged.connect(self.saveSettings)

        self.pushButton_Primary_Color.clicked.connect(
            lambda: self.changeColor('primaryColor', 'pushButton_Primary_Color'))
        self.pushButton_Primary_Light_Color.clicked.connect(
            lambda: self.changeColor('primaryLightColor', 'pushButton_Primary_Light_Color'))
        self.pushButton_Secondary_Color.clicked.connect(
            lambda: self.changeColor('secondaryColor', 'pushButton_Secondary_Color'))
        self.pushButton_Secondary_Light_Color.clicked.connect(
            lambda: self.changeColor('secondaryLightColor', 'pushButton_Secondary_Light_Color'))
        self.pushButton_Secondary_Dark_Color.clicked.connect(
            lambda: self.changeColor('secondaryDarkColor', 'pushButton_Secondary_Dark_Color'))
        self.pushButton_Primary_Text_Color.clicked.connect(
            lambda: self.changeColor('primaryTextColor', 'pushButton_Primary_Text_Color'))
        self.pushButton_Secondary_Text_Color.clicked.connect(
            lambda: self.changeColor('secondaryTextColor', 'pushButton_Secondary_Text_Color'))

    def loadLanguage(self):
        language_files = {
            0: self.main.resourcePath("Translations/PL/qtbase_pl.qm"),
            1: self.main.resourcePath("Translations/EN/qtbase_en.qm"),
        }

        selected_language = self.comboBox_Language.currentIndex()

        selected_language_file = language_files.get(selected_language)
        if selected_language_file:
            if self.translator.load(selected_language_file):
                self.app.installTranslator(self.translator)
        else:
            default_language_file = self.main.resourcePath("Translations/EN/qtbase_en.qm")
            if self.translator.load(default_language_file):
                self.app.installTranslator(self.translator)

    def changeColor(self, field_name, button_name):
        try:
            button = self.findChild(QPushButton, button_name)

            if button:
                current_style = button.styleSheet()

                color = QColorDialog.getColor(options=QColorDialog.ColorDialogOption.ShowAlphaChannel)

                if color.isValid():
                    button.setStyleSheet(f"{current_style}background-color: {color.name()};")

                    custom_colors = self.loadCustomColors(self.main.resourcePath(SettingsController.CUSTOM_THEM_FILE))
                    custom_colors[field_name] = color.name()

                    self.saveCustomColors(custom_colors, self.main.resourcePath(SettingsController.CUSTOM_THEM_FILE))
                    self.loadThem()
                else:
                    button.setStyleSheet(current_style)

        except Exception as e:
            print(f"Error changing color: {e}")

    def saveCustomColors(self, colors, file_path):
        try:
            root = ET.Element("resources")

            for color_name, color_value in colors.items():
                color_elem = ET.SubElement(root, "color", name=color_name)
                color_elem.text = color_value

            tree = ET.ElementTree(root)

            with open(file_path, 'wb') as file:
                tree.write(file, encoding="utf-8", xml_declaration=True)

        except Exception as e:
            print(f"Error saving custom colors: {e}")

    def loadCustomColors(self, file_path):
        colors = {}
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            for color_elem in root.findall(".//color"):
                color_name = color_elem.get("name")
                color_value = color_elem.text
                colors[color_name] = color_value
        except Exception as e:
            print(f"Error loading custom colors: {e}")
        return colors

    def applyCustomStylesheet(self, custom_stylesheet):
        self.pushButton_Primary_Color.setStyleSheet(
            f"background-color: {custom_stylesheet.get('primaryColor', '#ffffff')};")
        self.pushButton_Primary_Light_Color.setStyleSheet(
            f"background-color: {custom_stylesheet.get('primaryLightColor', '#ffffff')};")
        self.pushButton_Secondary_Color.setStyleSheet(
            f"background-color: {custom_stylesheet.get('secondaryColor', '#ffffff')};")
        self.pushButton_Secondary_Light_Color.setStyleSheet(
            f"background-color: {custom_stylesheet.get('secondaryLightColor', '#ffffff')};")
        self.pushButton_Secondary_Dark_Color.setStyleSheet(
            f"background-color: {custom_stylesheet.get('secondaryDarkColor', '#ffffff')};")
        self.pushButton_Primary_Text_Color.setStyleSheet(
            f"background-color: {custom_stylesheet.get('primaryTextColor', '#ffffff')};")
        self.pushButton_Secondary_Text_Color.setStyleSheet(
            f"background-color: {custom_stylesheet.get('secondaryTextColor', '#ffffff')};")

    def loadAndApplyCustomStylesheet(self):
        file_path = self.main.resourcePath(SettingsController.CUSTOM_THEM_FILE)
        custom_colors = self.loadCustomColors(file_path)
        self.applyCustomStylesheet(custom_colors)

    def showSettingsWindow(self):
        self.show()

    def populateLanguage(self):
        languages = ["Polski", "English"]

        self.comboBox_Language.clear()
        self.comboBox_Language.addItems(languages)

    def populateThemes(self):
        themes_path = self.main.resourcePath("Themes")
        themes = [entry.replace(".xml", "") for entry in QDir(themes_path).entryList(['*.xml'])]
        if "my_custom" in themes:
            themes.remove("my_custom")

        self.comboBox_Theme.clear()
        self.comboBox_Theme.addItems(themes)

    def customThemIconColor(self, colorIconIndex=0):
        if colorIconIndex == 0:
            self.main.addIconsToActions("black")
        elif colorIconIndex == 1:
            self.main.addIconsToActions("white")
        else:
            self.main.addIconsToActions("black")

    def loadThem(self):
        if self.checkBox_Use_Custom_Theme.isChecked():
            colorIconIndex = self.comboBox_Icon_Color.currentIndex()
            if self.checkBox_Use_Secondary_Colors.isChecked():
                self.apply_stylesheet(self.app, self.main.resourcePath(SettingsController.CUSTOM_THEM_FILE),
                                      invert_secondary=True)
                self.customThemIconColor(colorIconIndex)

            else:
                self.apply_stylesheet(self.app, self.main.resourcePath(SettingsController.CUSTOM_THEM_FILE))
                self.customThemIconColor(colorIconIndex)

        else:
            themes_path = self.main.resourcePath("Themes/")
            extension = ".xml"
            them_name = self.comboBox_Theme.currentText()
            filename = themes_path + them_name + extension

            if them_name == "Basic_light":
                qdarktheme.setup_theme("light")
                self.main.addIconsToActions("black")
            elif them_name == "Basic_dark":
                qdarktheme.setup_theme("dark")
                self.main.addIconsToActions("white")
            elif them_name == "Basic_default":
                self.app = QCoreApplication.instance()
                self.main.addIconsToActions("black")
                self.app.setStyleSheet(""" * {
                                                color: black;
                                             }
                                       """)
            else:
                if 'dark' in filename:
                    self.main.addIconsToActions("white")
                elif 'light' in filename:
                    self.main.addIconsToActions("black")
                else:
                    self.main.addIconsToActions("black")

                self.apply_stylesheet(self.app, filename)

    def loadSettings(self):
        if QFile.exists(self.main.resourcePath(SettingsController.SETTINGS_FILE)):
            with open(self.main.resourcePath(SettingsController.SETTINGS_FILE), 'r') as file:
                settings = json.load(file)
                language_index = settings.get("language_index", 0)
                theme_index = settings.get("theme_index", 1)
                custom_theme_enabled = settings.get("custom_theme_enabled", False)
                secondary_colors_enabled = settings.get("secondary_colors_enabled", False)
                custom_theme_icon_color = settings.get("custom_theme_icon_color", 0)
                show_save_reminder_window = settings.get("show_save_reminder_window", 0)

                self.checkBox_Use_Custom_Theme.setChecked(custom_theme_enabled)
                self.checkBox_Use_Secondary_Colors.setChecked(secondary_colors_enabled)
                self.comboBox_Language.setCurrentIndex(language_index)
                self.comboBox_Theme.setCurrentIndex(theme_index)
                self.comboBox_Icon_Color.setCurrentIndex(custom_theme_icon_color)
                self.comboBox_Window_Reminding_To_Save.setCurrentIndex(show_save_reminder_window)

                self.loadThem()
        else:
            default_settings = {
                "language_index": 0,
                "theme_index": 1,
                "custom_theme_enabled": False,
                "secondary_colors_enabled": False,
                "custom_theme_icon_color": 0,
                "show_save_reminder_window": 0
            }

            with open(self.main.resourcePath(SettingsController.SETTINGS_FILE), 'w') as file:
                json.dump(default_settings, file, indent=2)
            self.loadSettings()

    def saveSettings(self):
        language_index = self.comboBox_Language.currentIndex()
        theme_index = self.comboBox_Theme.currentIndex()
        custom_theme_enabled = self.checkBox_Use_Custom_Theme.isChecked()
        secondary_colors_enabled = self.checkBox_Use_Secondary_Colors.isChecked()
        custom_theme_icon_color = self.comboBox_Icon_Color.currentIndex()
        show_save_reminder_window = self.comboBox_Window_Reminding_To_Save.currentIndex()

        settings = {
            "language_index": language_index,
            "theme_index": theme_index,
            "custom_theme_enabled": custom_theme_enabled,
            "secondary_colors_enabled": secondary_colors_enabled,
            "custom_theme_icon_color": custom_theme_icon_color,
            "show_save_reminder_window": show_save_reminder_window
        }

        with open(self.main.resourcePath(SettingsController.SETTINGS_FILE), 'w') as file:
            json.dump(settings, file, indent=2)
