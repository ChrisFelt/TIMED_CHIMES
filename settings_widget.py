from PySide6.QtCore import QDir
from PySide6.QtWidgets import QWidget, QFileSystemModel
from ui_settings_widget import Ui_SettingsWidget
import os


class SettingsWidget(QWidget, Ui_SettingsWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # find absolute path of /sounds
        self._wd = QDir.current()
        # TODO: error catching - check if /sounds exists first!
        self._path = QDir(self._wd.path() + "/sounds")

        # create sounds directory if it does not exist    
        if not self._path.exists():    
            QDir().mkdir("/sounds")


        # list of mp3 files in path
        sounds_list = self._path.entryList("*.mp3", QDir.Files)

        # populate list widget
        self.sounds_list_view.addItems(sounds_list)


