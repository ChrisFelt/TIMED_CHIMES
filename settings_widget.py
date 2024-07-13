from PySide6.QtWidgets import QWidget
from ui_settings_widget import Ui_SettingsWidget


class SettingsWidget(QWidget, Ui_SettingsWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
