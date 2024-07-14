from PySide6.QtWidgets import QMainWindow, QStackedWidget

from ui_main_window import Ui_MainWindow
from display_widget import DisplayWidget
from settings_widget import SettingsWidget


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setupUi(self)
        self.setWindowTitle("Timed Chimes")

        # stacked widgets
        self._display = DisplayWidget()
        self._settings = SettingsWidget()

        self.StackedWidget.addWidget(self._display)
        self.StackedWidget.addWidget(self._settings)

        # slots for toggling between stacked widgets
        self._display.open_settings_button.clicked.connect(self.open_settings)
        self._settings.close_settings_button.clicked.connect(self.close_settings)

    def open_settings(self):
        self.StackedWidget.setCurrentIndex(1)
    
    def close_settings(self):
        self.StackedWidget.setCurrentIndex(0)