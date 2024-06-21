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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLCDNumber, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTabWidget, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(596, 309)
        self.main_window = QTabWidget(MainWindow)
        self.main_window.setObjectName(u"main_window")
        self.main_window.setGeometry(QRect(6, 19, 561, 271))
        self.display_tab = QWidget()
        self.display_tab.setObjectName(u"display_tab")
        self.time_remaining = QLCDNumber(self.display_tab)
        self.time_remaining.setObjectName(u"time_remaining")
        self.time_remaining.setGeometry(QRect(120, 50, 311, 121))
        self.time_remaining.setDigitCount(5)
        self.time_remaining.setProperty("intValue", 0)
        self.play_timer_button = QPushButton(self.display_tab)
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
        self.repeat_timer_button = QPushButton(self.display_tab)
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
        self.plus_one_button = QPushButton(self.display_tab)
        self.plus_one_button.setObjectName(u"plus_one_button")
        self.plus_one_button.setGeometry(QRect(330, 10, 101, 30))
        self.set_time_button = QPushButton(self.display_tab)
        self.set_time_button.setObjectName(u"set_time_button")
        self.set_time_button.setGeometry(QRect(10, 200, 531, 31))
        self.main_window.addTab(self.display_tab, "")
        self.options_tab = QWidget()
        self.options_tab.setObjectName(u"options_tab")
        self.listWidget = QListWidget(self.options_tab)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(255, 30, 281, 171))
        self.label = QLabel(self.options_tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 10, 49, 16))
        self.play_list_button = QPushButton(self.options_tab)
        self.play_list_button.setObjectName(u"play_list_button")
        self.play_list_button.setGeometry(QRect(461, 207, 75, 24))
        icon2 = QIcon()
        icon2.addFile(u":/images/play.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/images/stop.png", QSize(), QIcon.Normal, QIcon.On)
        self.play_list_button.setIcon(icon2)
        self.play_list_button.setCheckable(True)
        self.remove_sound_button = QPushButton(self.options_tab)
        self.remove_sound_button.setObjectName(u"remove_sound_button")
        self.remove_sound_button.setGeometry(QRect(254, 207, 75, 24))
        self.import_sound_button = QPushButton(self.options_tab)
        self.import_sound_button.setObjectName(u"import_sound_button")
        self.import_sound_button.setGeometry(QRect(350, 207, 91, 24))
        self.randomize_sound = QCheckBox(self.options_tab)
        self.randomize_sound.setObjectName(u"randomize_sound")
        self.randomize_sound.setGeometry(QRect(20, 40, 121, 20))
        self.auto_repeat_sound = QCheckBox(self.options_tab)
        self.auto_repeat_sound.setObjectName(u"auto_repeat_sound")
        self.auto_repeat_sound.setGeometry(QRect(20, 70, 121, 20))
        self.lock_display = QCheckBox(self.options_tab)
        self.lock_display.setObjectName(u"lock_display")
        self.lock_display.setGeometry(QRect(20, 100, 121, 20))
        self.zen_mode = QCheckBox(self.options_tab)
        self.zen_mode.setObjectName(u"zen_mode")
        self.zen_mode.setGeometry(QRect(20, 160, 121, 20))
        self.hide_time = QCheckBox(self.options_tab)
        self.hide_time.setObjectName(u"hide_time")
        self.hide_time.setGeometry(QRect(20, 130, 121, 20))
        self.main_window.addTab(self.options_tab, "")

        self.retranslateUi(MainWindow)

        self.main_window.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.play_timer_button.setText("")
        self.repeat_timer_button.setText("")
        self.plus_one_button.setText(QCoreApplication.translate("MainWindow", u"+1:00", None))
        self.set_time_button.setText(QCoreApplication.translate("MainWindow", u"Set Time", None))
        self.main_window.setTabText(self.main_window.indexOf(self.display_tab), QCoreApplication.translate("MainWindow", u"Display", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sounds", None))
        self.play_list_button.setText("")
        self.remove_sound_button.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.import_sound_button.setText(QCoreApplication.translate("MainWindow", u"Import New...", None))
#if QT_CONFIG(tooltip)
        self.randomize_sound.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.randomize_sound.setText(QCoreApplication.translate("MainWindow", u"Randomize Sound", None))
#if QT_CONFIG(tooltip)
        self.auto_repeat_sound.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.auto_repeat_sound.setText(QCoreApplication.translate("MainWindow", u"Auto Repeat", None))
#if QT_CONFIG(tooltip)
        self.lock_display.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lock_display.setText(QCoreApplication.translate("MainWindow", u"Lock Display", None))
#if QT_CONFIG(tooltip)
        self.zen_mode.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.zen_mode.setText(QCoreApplication.translate("MainWindow", u"Zen Mode", None))
#if QT_CONFIG(tooltip)
        self.hide_time.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.hide_time.setText(QCoreApplication.translate("MainWindow", u"Hide Time", None))
        self.main_window.setTabText(self.main_window.indexOf(self.options_tab), QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

