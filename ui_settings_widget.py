# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QWidget)
import resource_rc

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.resize(596, 309)
        self.Widget = QWidget(SettingsWidget)
        self.Widget.setObjectName(u"Widget")
        self.Widget.setGeometry(QRect(6, 19, 561, 271))
        self.sounds_list = QListWidget(self.Widget)
        self.sounds_list.setObjectName(u"sounds_list")
        self.sounds_list.setGeometry(QRect(255, 30, 281, 171))
        self.label = QLabel(self.Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 10, 49, 16))
        self.play_list_button = QPushButton(self.Widget)
        self.play_list_button.setObjectName(u"play_list_button")
        self.play_list_button.setGeometry(QRect(461, 207, 75, 24))
        icon = QIcon()
        icon.addFile(u":/images/play.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/stop.png", QSize(), QIcon.Normal, QIcon.On)
        self.play_list_button.setIcon(icon)
        self.play_list_button.setCheckable(True)
        self.remove_sound_button = QPushButton(self.Widget)
        self.remove_sound_button.setObjectName(u"remove_sound_button")
        self.remove_sound_button.setGeometry(QRect(254, 207, 75, 24))
        self.import_sound_button = QPushButton(self.Widget)
        self.import_sound_button.setObjectName(u"import_sound_button")
        self.import_sound_button.setGeometry(QRect(350, 207, 91, 24))
        self.randomize_sound = QCheckBox(self.Widget)
        self.randomize_sound.setObjectName(u"randomize_sound")
        self.randomize_sound.setGeometry(QRect(20, 40, 121, 20))
        self.auto_repeat_sound = QCheckBox(self.Widget)
        self.auto_repeat_sound.setObjectName(u"auto_repeat_sound")
        self.auto_repeat_sound.setGeometry(QRect(20, 70, 121, 20))
        self.lock_display = QCheckBox(self.Widget)
        self.lock_display.setObjectName(u"lock_display")
        self.lock_display.setGeometry(QRect(20, 100, 121, 20))
        self.hide_time = QCheckBox(self.Widget)
        self.hide_time.setObjectName(u"hide_time")
        self.hide_time.setGeometry(QRect(20, 130, 121, 20))

        self.retranslateUi(SettingsWidget)

        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"Form", None))
#if QT_CONFIG(tooltip)
        self.Widget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("SettingsWidget", u"Sounds", None))
        self.play_list_button.setText("")
        self.remove_sound_button.setText(QCoreApplication.translate("SettingsWidget", u"Remove", None))
        self.import_sound_button.setText(QCoreApplication.translate("SettingsWidget", u"Import New...", None))
#if QT_CONFIG(tooltip)
        self.randomize_sound.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.randomize_sound.setText(QCoreApplication.translate("SettingsWidget", u"Randomize Sound", None))
#if QT_CONFIG(tooltip)
        self.auto_repeat_sound.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.auto_repeat_sound.setText(QCoreApplication.translate("SettingsWidget", u"Auto Repeat", None))
#if QT_CONFIG(tooltip)
        self.lock_display.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lock_display.setText(QCoreApplication.translate("SettingsWidget", u"Lock Display", None))
#if QT_CONFIG(tooltip)
        self.hide_time.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.hide_time.setText(QCoreApplication.translate("SettingsWidget", u"Hide Time", None))
    # retranslateUi

