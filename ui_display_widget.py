# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'display_widget.ui'
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
    QSizePolicy, QTimeEdit, QWidget)
import resource_rc

class Ui_DisplayWidget(object):
    def setupUi(self, DisplayWidget):
        if not DisplayWidget.objectName():
            DisplayWidget.setObjectName(u"DisplayWidget")
        DisplayWidget.resize(562, 275)
        self.Widget = QWidget(DisplayWidget)
        self.Widget.setObjectName(u"Widget")
        self.Widget.setGeometry(QRect(1, 2, 560, 271))
        self.timer_lcd_screen = QLCDNumber(self.Widget)
        self.timer_lcd_screen.setObjectName(u"timer_lcd_screen")
        self.timer_lcd_screen.setGeometry(QRect(125, 63, 311, 121))
        self.timer_lcd_screen.setFocusPolicy(Qt.ClickFocus)
        self.timer_lcd_screen.setDigitCount(5)
        self.timer_lcd_screen.setProperty("intValue", 0)
        self.play_timer_button = QPushButton(self.Widget)
        self.play_timer_button.setObjectName(u"play_timer_button")
        self.play_timer_button.setGeometry(QRect(465, 90, 70, 70))
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
        self.repeat_timer_button = QPushButton(self.Widget)
        self.repeat_timer_button.setObjectName(u"repeat_timer_button")
        self.repeat_timer_button.setGeometry(QRect(25, 90, 70, 70))
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
        self.plus_one_button = QPushButton(self.Widget)
        self.plus_one_button.setObjectName(u"plus_one_button")
        self.plus_one_button.setGeometry(QRect(335, 23, 101, 30))
        self.set_time_button = QPushButton(self.Widget)
        self.set_time_button.setObjectName(u"set_time_button")
        self.set_time_button.setGeometry(QRect(365, 203, 71, 41))
        self.input_time_box = QTimeEdit(self.Widget)
        self.input_time_box.setObjectName(u"input_time_box")
        self.input_time_box.setGeometry(QRect(285, 208, 71, 31))
        font = QFont()
        font.setPointSize(12)
        self.input_time_box.setFont(font)
        self.input_time_box.setCurrentSection(QDateTimeEdit.HourSection)
        self.input_time_box.setTime(QTime(0, 0, 0))
        self.open_settings_button = QPushButton(self.Widget)
        self.open_settings_button.setObjectName(u"open_settings_button")
        self.open_settings_button.setGeometry(QRect(40, 205, 35, 35))
        self.open_settings_button.setStyleSheet(u"QPushButton {\n"
"    border: 1px;\n"
"    border-style: outset;\n"
"    background: lightGray;\n"
"    padding: 1px;\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/images/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_settings_button.setIcon(icon2)
        self.open_settings_button.setIconSize(QSize(30, 30))

        self.retranslateUi(DisplayWidget)

        QMetaObject.connectSlotsByName(DisplayWidget)
    # setupUi

    def retranslateUi(self, DisplayWidget):
        DisplayWidget.setWindowTitle(QCoreApplication.translate("DisplayWidget", u"Form", None))
#if QT_CONFIG(tooltip)
        self.Widget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.play_timer_button.setText("")
        self.repeat_timer_button.setText("")
        self.plus_one_button.setText(QCoreApplication.translate("DisplayWidget", u"+1:00", None))
        self.set_time_button.setText(QCoreApplication.translate("DisplayWidget", u"Set Time", None))
#if QT_CONFIG(tooltip)
        self.input_time_box.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.input_time_box.setDisplayFormat(QCoreApplication.translate("DisplayWidget", u"hh:mm", None))
        self.open_settings_button.setText("")
    # retranslateUi

