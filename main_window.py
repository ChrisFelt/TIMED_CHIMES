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
        self._target_time = self.input_time_box.time()  # total seconds on timer when time set. DOES NOT CHANGE until timer reset
        self._timer_secs = 0  # track remaining seconds on timer
        self._elapsed_time = QElapsedTimer()  # accurate time keeping
        # self._elapsed_msecs = 0

        # timer emits regular signals for updating the app
        self._timer = QTimer()
        self._timer.timeout.connect(self.update_timer)  # calls update_timer at regular intervals

        # track time spent paused in milliseconds
        self._paused_msecs = 0
        self._elapsed_pause = QElapsedTimer()  # current pause session

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
    def __convert_to_qtime(self, time, msec=False) -> QTime:
        """Converts seconds to a QTime object and returns it"""
        # convert to seconds if time passed as msecs
        if msec is True:
            time = time // 1000
        return QTime(0, 0, 0).addSecs(time)
    
    def __convert_from_qtime(self, qtime_object) -> int:
        """Converts QTime object into and returns seconds"""
        return QTime(0, 0, 0).secsTo(qtime_object)
    
    def __elapsed_secs(self) -> int:
        """Returns the seconds elapsed"""
        if self._elapsed_time.elapsed() < 0:
            return 0  # elapsed() returns massive negative int before QElapsedTime started
        
        # pause logic: subtract paused msecs from elapsed time
        elapsed_msecs = self._elapsed_time.elapsed() - self._paused_msecs
        print("Elapsed msecs: ", elapsed_msecs)
        return elapsed_msecs // 1000
    
    def __check_time(self) -> bool:
        """Returns True if elapsed timer meets or exceeds the set time, otherwise returns False"""
        if self.__elapsed_secs() >= self.__convert_from_qtime(self._target_time):
            return True
        
        return False
    
    def __update_lcd_screen(self) -> None:
        """Updates the QLCDNumber screen to the current time remaining"""
        # generate QTime object with current time remaining
        secs_remaining = self.__convert_from_qtime(self._target_time) - self.__elapsed_secs()
        time = self.__convert_to_qtime(secs_remaining)

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
        # start elapsed timer only if it hasn't started yet
        if self._elapsed_time.elapsed() < 0:
            self._elapsed_time.start()

        # pause logic: increment time paused, if any
        print("Pause time: ", self._elapsed_pause.elapsed())
        if self._elapsed_pause.elapsed() > 0:
            self._paused_msecs += self._elapsed_pause.elapsed()
            print("Total paused time: ", self._paused_msecs)

        self._elapsed_pause = QElapsedTimer()  # always reset pause elapsed timer
        
        print("Timer started.")
    
    def __pause_timer(self):
        """Pauses the timer"""
        self._timer.stop()
        self._elapsed_pause.start()
        print("Timer paused.")

    # -------------
    # DISPLAY tab slots
    def set_timer(self):
        """Sets QLCDNumber display to current value in QTimeEdit"""
        # TODO: notify user that current timer will be stopped if a timer is currently running
        # stop current timer if it is running
        self._timer.stop()
        # reset elapsed timer and internal data members
        self._elapsed_time = QElapsedTimer()
        self._timer_secs = self.__convert_from_qtime(self.input_time_box.time())
        self._target_time = self.input_time_box.time()
        self._elapsed_pause = QElapsedTimer()
        self._paused_msecs = 0
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
        # TODO: implement me
        pass
    
    def update_timer(self):
        """QTimer slot for timeoue signal. Updates screen and checks for alarm"""
        # secsTo(new_time) returns the number of seconds from this time to the new time
        self._timer_secs -= UPDATE_SEC
        self.__update_lcd_screen()

        # play sound when time is up
        if self.__check_time():
            self._timer.stop()  # STOP THE TIMER FIRST!!!
            self.__alarm()
    
    # -------------
    # OPTIONS tab slots
