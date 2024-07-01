import time
from PySide6.QtCore import QTime
NSEC_CONVERSION = 1000000000  # nanosecond conversion constant


class MTimer():
    """Provides monotonic time-keeping tailored for Qt applications. 
    Offers functionality and QTime conversion options not available in QElapsedTimer"""
    def __init__(self, target_time):
        self._target_time = target_time  # QTime object
        self._start_time = 0
        # elapsed time (ns) for current session - sessions are demarcated by pause
        self._elapsed_time = 0
        # cumulative elapsed time (ns) from previous sessions
        self._prev_elapsed = 0

    def __secs_to_nsecs(self, secs) -> int:
        return secs * NSEC_CONVERSION
    
    def __nsecs_to_secs(self, nsecs) -> int:
        return nsecs // NSEC_CONVERSION  # floor value
    
    def __convert_to_qtime(self, nsecs) -> QTime:
        """Converts nanoseconds to a QTime object and returns it"""
        secs = self.__nsecs_to_secs(nsecs)
        return QTime(0, 0, 0).addSecs(secs)
    
    def __convert_from_qtime(self, qtime_object) -> int:
        """Converts QTime object into and returns nanoseconds"""
        secs = QTime(0, 0, 0).secsTo(qtime_object)
        return self.__secs_to_nsecs(secs)
    
    def __update_elapsed_time(self) -> None:
        """Adds current time elapsed from start_time to elapsed_time"""
        if self._start_time == 0:
            return
        else:
            self._elapsed_time = time.monotonic_ns() - self._start_time
        print("MTimer total elapsed time: ", self._elapsed_time + self._prev_elapsed)
    
    def get_qtime(self) -> QTime:
        """Finds the current time remaining on the timer and returns it as a QTime object"""
        nsecs_remaining = self.__convert_from_qtime(self._target_time) - self._elapsed_time - self._prev_elapsed
        return self.__convert_to_qtime(nsecs_remaining)
    
    def start(self) -> None:
        """Starts new session"""
        self._start_time = time.monotonic_ns()
        print("MTimer started.")
    
    def pause(self) -> None:
        """Adds current elapsed time to previous sessions and ends the current session"""
        self.__update_elapsed_time()
        self._prev_elapsed += self._elapsed_time
        self._start_time = 0  # zero start time in case get_qtime called during pause
        self._elapsed_time = 0
        print("MTimer paused.")

    def reset(self, qtime_object) -> None:
        """Zeroes data and updates target_time to the given qtime"""
        self._target_time = qtime_object
        self._elapsed_time = 0
        self._start_time = 0
        print("Mtimer reset.")
    
    def check_time(self) -> bool:
        """Return True if elapsed time >= target time, otherwise False"""
        self.__update_elapsed_time()
        if self._elapsed_time + self._prev_elapsed >= self.__convert_from_qtime(self._target_time):
            return True
        return False
    
    def add_time(self, secs) -> None:
        """Adds the given secs to the timer"""
        # TODO: FIX -- currently resets the clock to 00:00 when 23:59:59 exceeded. 
        nsecs = self.__secs_to_nsecs(secs) + self.__convert_from_qtime(self._target_time)
        self._target_time = self.__convert_to_qtime(nsecs)
    
    def wait_a_sec(self) -> int:
        """Test monotonic timer"""
        self._start_time = time.monotonic_ns()
        time.sleep(1)
        self._elapsed_time = time.monotonic_ns() - self._start_time
        return self._elapsed_time

# test
if __name__ == "__main__":
        print(time.monotonic_ns())
        print(time.time_ns())

        new_timer = MTimer(QTime(0, 0, 0).addSecs(60))
        print(new_timer.wait_a_sec())
        print(new_timer.get_qtime())