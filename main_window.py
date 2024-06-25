from PySide6.QtCore import Qt, QTimer, QTime, QElapsedTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from ui_main_window import Ui_MainWindow

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
        self._target_time = self.input_time.time()  # total seconds on timer when time set. DOES NOT CHANGE until timer reset
        self._timer_secs = 0  # track remaining seconds on timer
        self._elapsed_time = QElapsedTimer()  # accurate time keeping

        # timer emits regular signals for updating the app
        self._timer = QTimer()
        self._timer.timeout.connect(self.update_timer)  # calls update_timer at regular intervals

        # set time button slot
        self.set_time_button.clicked.connect(self.set_timer)

        # set play button slot
        self.play_timer_button.clicked.connect(self.start_timer)

    # -------------
    # GENERAL use methods
    def __convert_to_qtime(self, sec) -> QTime:
        """Converts seconds to a QTime object and returns it"""
        return QTime(0, 0, 0).addSecs(sec)
    
    def __convert_from_qtime(self, qtime_object) -> int:
        """Converts QTime object into and returns seconds"""
        return QTime(0, 0, 0).secsTo(qtime_object)
    
    def __elapsed_secs(self) -> int:
        """Returns the seconds elapsed"""
        check_elapsed_time = self._elapsed_time.elapsed()  # milliseconds

        if check_elapsed_time < 0:
            return 0  # elapsed() returns massive negative int before QElapsedTime started
        
        return check_elapsed_time // 1000
    
    def __check_time(self) -> bool:
        """Returns True if elapsed timer meets or exceeds the set time, otherwise returns False"""
        #print("Elapsed: ", self.__elapsed_secs())
        #print("Target: ", self.__convert_from_qtime(self._target_time))
        if self.__elapsed_secs() >= self.__convert_from_qtime(self._target_time):
            return True
        
        return False
    
    def __update_lcd_screen(self):
        """Updates the QLCDNumber screen to the current time remaining"""
        # generate QTime object with current time remaining
        secs_remaining = self.__convert_from_qtime(self._target_time) - self.__elapsed_secs()
        time = self.__convert_to_qtime(secs_remaining)

        # cast time to QLCDNumber screen
        text_time = time.toString("hh:mm")
        self.time_remaining.display(text_time)

    # -------------
    # DISPLAY tab slots
    def set_timer(self):
        """Sets QLCDNumber display to current value in QTimeEdit"""
        # reset elapsed timer and internal data members
        self._elapsed_time = QElapsedTimer()
        self._timer_secs = self.__convert_from_qtime(self.input_time.time())
        self._target_time = self.input_time.time()
        self.__update_lcd_screen()

    def alarm(self):
        """Plays alarm sound when called"""
        # placeholder popup
        ret = QMessageBox.information(self,"Alarm", "Timer timed out.")
                
        if ret == QMessageBox.Ok : 
            print("User chose OK")
        else : 
            print ("User chose Cancel")
    
    def start_timer(self):
        """Starts timer given time from user input"""
        self._timer.start(TIMEOUT_STEP)  # timeout signal sent every (time_step) milliseconds
        self._elapsed_time.start()
        print("Timer started.")
    
    def update_timer(self):
        # secsTo(new_time) returns the number of seconds from this time to the new time
        self._timer_secs -= UPDATE_SEC
        self.__update_lcd_screen()

        # play sound when time is up
        if self.__check_time():
            self._timer.stop()  # STOP THE TIMER FIRST!!!
            self.alarm()
    
    # -------------
    # OPTIONS tab slots
