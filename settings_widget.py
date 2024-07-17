from PySide6.QtCore import QDir
from PySide6.QtWidgets import QWidget, QFileSystemModel
from ui_settings_widget import Ui_SettingsWidget
import os


class SettingsWidget(QWidget, Ui_SettingsWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # find absolute path of /sounds
        wd = QDir.current()
        # TODO: error catching - check if /sounds exists first!
        path = QDir(wd.path() + "/sounds")

        # list of mp3 files in path
        sounds_list = path.entryList("*.mp3", QDir.Files)

        # populate list widget
        self.sounds_list_view.addItems(sounds_list)
