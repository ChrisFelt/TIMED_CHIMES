from PySide6.QtWidgets import QMainWindow, QStackedWidget

from display_widget import DisplayWidget
from settings_widget import SettingsWidget


class MainWindow(QStackedWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.resize(596, 309)

        # stacked widgets
        self._display = DisplayWidget()
        self._settings = SettingsWidget()

        self.addWidget(self._display)
        self.addWidget(self._settings)

        # slots for toggling between stacked widgets
