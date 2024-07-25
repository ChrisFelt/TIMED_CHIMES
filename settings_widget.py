from PySide6.QtCore import QDir
from PySide6.QtWidgets import QWidget, QFileSystemModel
from ui_settings_widget import Ui_SettingsWidget
import os


class SettingsWidget(QWidget, Ui_SettingsWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # set sounds directory
        self._wd = QDir.current()
        
        self._path = QDir(self._wd.path() + "/sounds")
        # create sounds directory if it does not exist    
        if not self._path.exists():    
            QDir().mkdir("/sounds")

        # list of mp3 files in path
        sounds_list = self._path.entryList("*.mp3", QDir.Files)

        # populate list widget
        self.sounds_list_view.addItems(sounds_list)
        # list widget slots
        self.sounds_list_view.currentItemChanged.connect(self.update_sound_label)      

    # -------------
    # SETTINGS tab slots
    def update_sound_label(self, current, previous):
        self.sound_title_label.setText(current.text())
        print(current.text())

