# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QLCDNumber, QPushButton,
    QSizePolicy, QStackedWidget, QTimeEdit, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(596, 309)
        self.main_window = QStackedWidget(MainWindow)
        self.main_window.setObjectName(u"main_window")
        self.main_window.setGeometry(QRect(6, 19, 561, 271))
        self.main_windowPage1 = QWidget()
        self.main_windowPage1.setObjectName(u"main_windowPage1")
        self.timer_lcd_screen = QLCDNumber(self.main_windowPage1)
        self.timer_lcd_screen.setObjectName(u"timer_lcd_screen")
        self.timer_lcd_screen.setGeometry(QRect(120, 50, 311, 121))
        self.timer_lcd_screen.setFocusPolicy(Qt.ClickFocus)
        self.timer_lcd_screen.setDigitCount(5)
        self.timer_lcd_screen.setProperty("intValue", 0)
        self.play_timer_button = QPushButton(self.main_windowPage1)
        self.play_timer_button.setObjectName(u"play_timer_button")
        self.play_timer_button.setGeometry(QRect(460, 77, 70, 70))
        self.play_timer_button.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid black;\n"
"    border-radius: 35px;\n"
"    border-style: outset;\n"
"    background: lightGray;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon = QIcon()
        icon.addFile(u":/images/play.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/pause.png", QSize(), QIcon.Normal, QIcon.On)
        self.play_timer_button.setIcon(icon)
        self.play_timer_button.setIconSize(QSize(40, 40))
        self.play_timer_button.setCheckable(True)
        self.repeat_timer_button = QPushButton(self.main_windowPage1)
        self.repeat_timer_button.setObjectName(u"repeat_timer_button")
        self.repeat_timer_button.setGeometry(QRect(20, 77, 70, 70))
        self.repeat_timer_button.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid black;\n"
"    border-radius: 35px;\n"
"    border-style: outset;\n"
"    background: lightGray;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }")
        icon1 = QIcon()
        icon1.addFile(u":/images/repeat.png", QSize(), QIcon.Normal, QIcon.Off)
        self.repeat_timer_button.setIcon(icon1)
        self.repeat_timer_button.setIconSize(QSize(40, 40))
        self.plus_one_button = QPushButton(self.main_windowPage1)
        self.plus_one_button.setObjectName(u"plus_one_button")
        self.plus_one_button.setGeometry(QRect(330, 10, 101, 30))
        self.set_time_button = QPushButton(self.main_windowPage1)
        self.set_time_button.setObjectName(u"set_time_button")
        self.set_time_button.setGeometry(QRect(360, 190, 71, 41))
        self.input_time_box = QTimeEdit(self.main_windowPage1)
        self.input_time_box.setObjectName(u"input_time_box")
        self.input_time_box.setGeometry(QRect(280, 195, 71, 31))
        font = QFont()
        font.setPointSize(12)
        self.input_time_box.setFont(font)
        self.input_time_box.setCurrentSection(QDateTimeEdit.HourSection)
        self.input_time_box.setTime(QTime(0, 0, 0))
        self.main_window.addWidget(self.main_windowPage1)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
#if QT_CONFIG(tooltip)
        self.main_window.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.play_timer_button.setText("")
        self.repeat_timer_button.setText("")
        self.plus_one_button.setText(QCoreApplication.translate("MainWindow", u"+1:00", None))
        self.set_time_button.setText(QCoreApplication.translate("MainWindow", u"Set Time", None))
#if QT_CONFIG(tooltip)
        self.input_time_box.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.input_time_box.setDisplayFormat(QCoreApplication.translate("MainWindow", u"hh:mm", None))
    # retranslateUi

