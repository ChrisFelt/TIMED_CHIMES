import sys
sys.dont_write_bytecode = True  # don't generate .pyc cache file

from PySide6.QtWidgets import QApplication
from main_window import MainWindow

app = QApplication(sys.argv)
window = MainWindow(app)
window.show()
app.exec()