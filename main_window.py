from PySide6.QtCore import Qt, QTimer, QTime, QElapsedTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui_main_window import Ui_MainWindow
from m_timer import MTimer

# timeout interval in milliseconds
TIMEOUT_STEP = 1000
# seconds to update on timeout
UPDATE_SEC = TIMEOUT_STEP // 1000


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        # initialize internal time data members
        self._target_time = self.input_time_box.time()  # total seconds on timer when time set. DOES NOT CHANGE until timer reset

        # QTimer emits regular signals for updating the app, but does not have true stopwatch/timer functionality
        self._timer = QTimer()
        self._timer.timeout.connect(self.update_timer)

        # create mtimer for timekeeping
        self._timekeeper = MTimer(QTime(0, 0, 0))

        # set time button slot
        self.set_time_button.clicked.connect(self.set_timer)

        # set play/pause button slot
        self.play_timer_button.clicked.connect(self.play_pause)

        # set repeat button slot
        self.repeat_timer_button.clicked.connect(self.repeat_timer)

        # set +1:00 button slot
        self.plus_one_button.clicked.connect(self.plus_one)

    # -------------
    # GENERAL use methods
    def __update_lcd_screen(self) -> None:
        """Updates the QLCDNumber screen to the current time remaining"""
        # generate QTime object with current time remaining
        time = self._timekeeper.get_qtime()

        # cast time to QLCDNumber screen
        text_time = time.toString("hh:mm")
        self.timer_lcd_screen.display(text_time)
    
    def __alarm(self):
        """Plays alarm sound when called"""
        # placeholder popup
        ret = QMessageBox.information(self,"Alarm", "Timer ended.")
                
        if ret == QMessageBox.Ok : 
            print("User chose OK")
        else : 
            print ("User chose Cancel")
    
    def __start_timer(self):
        """Starts timer given time from user input"""
        self._timer.start(TIMEOUT_STEP)  # timeout signal sent every (time_step) milliseconds
        self._timekeeper.start()
    
    def __pause_timer(self):
        """Pauses the timer"""
        self._timer.stop()
        self._timekeeper.pause()

    # -------------
    # DISPLAY tab slots
    def set_timer(self):
        """Sets QLCDNumber display to current value in QTimeEdit"""
        # TODO: notify user that current timer will be stopped if a timer is currently running
        # stop current timer if it is running
        self._timer.stop()
        # reset internal data members
        self._target_time = self.input_time_box.time()
        self._timekeeper = MTimer(self._target_time)
        self.__update_lcd_screen()
    
    def play_pause(self):
        """Start timer when checked, otherwise pause timer"""
        if self.play_timer_button.isChecked():
            self.__start_timer()
        else:
            self.__pause_timer()

    def repeat_timer(self):
        """Repeats current timer. NOTE: current timer set when "Set Time" button is pressed"""
        # TODO: implement me
        pass

    def plus_one(self):
        """Adds one minute to current timer and refreshes lcd screen"""
        self._timekeeper.add_time(60)
        self.__update_lcd_screen()
    
    def update_timer(self):
        """QTimer slot for timeout signal. Updates screen and checks for alarm"""
        # play sound when time is up
        if self._timekeeper.check_time():
            self._timer.stop()  # STOP THE TIMER FIRST!!!
            self.__alarm()
        else:
            # update screen only if time isn't up - prevents clock from rolling over to 23:59
            self.__update_lcd_screen()
    
    # -------------
    # OPTIONS tab slots
