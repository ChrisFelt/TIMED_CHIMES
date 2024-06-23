
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        # QLCDNumber widget customization
        # self.time_remaining.setCursor(Qt.IBeamCursor)  # change mouseover cursor

        # initialize timer
        self._time = QTimer(self)
        self._time.timeout.connect(self.alarm)

        # set time button slot
        self.set_time_button.clicked.connect(self.set_timer)

    def set_timer(self):
        """Sets QLCDNumber display to current value in QTimeEdit"""
        time = self.input_time.time()
        text_time = time.toString("hh:mm")
        self.time_remaining.display(text_time)

    def alarm(self):
        """Plays alarm sound when called"""
        # information message box plays notice sound
        ret = QMessageBox.information(self,"Alarm", "Alarm signal successfully sent.")
        
        if ret == QMessageBox.Ok : 
            print("User chose OK")
        else : 
            print ("User chose Cancel")
