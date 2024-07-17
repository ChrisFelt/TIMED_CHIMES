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
        SettingsWidget.resize(562, 275)
        self.Widget = QWidget(SettingsWidget)
        self.Widget.setObjectName(u"Widget")
        self.Widget.setGeometry(QRect(1, 2, 560, 271))
        self.label = QLabel(self.Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(259, 21, 49, 16))
        self.play_list_button = QPushButton(self.Widget)
        self.play_list_button.setObjectName(u"play_list_button")
        self.play_list_button.setGeometry(QRect(460, 218, 75, 24))
        icon = QIcon()
        icon.addFile(u":/images/play.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/images/stop.png", QSize(), QIcon.Normal, QIcon.On)
        self.play_list_button.setIcon(icon)
        self.play_list_button.setCheckable(True)
        self.remove_sound_button = QPushButton(self.Widget)
        self.remove_sound_button.setObjectName(u"remove_sound_button")
        self.remove_sound_button.setGeometry(QRect(253, 218, 75, 24))
        self.import_sound_button = QPushButton(self.Widget)
        self.import_sound_button.setObjectName(u"import_sound_button")
        self.import_sound_button.setGeometry(QRect(349, 218, 91, 24))
        self.randomize_sound_box = QCheckBox(self.Widget)
        self.randomize_sound_box.setObjectName(u"randomize_sound_box")
        self.randomize_sound_box.setGeometry(QRect(31, 51, 121, 20))
        self.auto_repeat_box = QCheckBox(self.Widget)
        self.auto_repeat_box.setObjectName(u"auto_repeat_box")
        self.auto_repeat_box.setGeometry(QRect(31, 81, 121, 20))
        self.lock_display_box = QCheckBox(self.Widget)
        self.lock_display_box.setObjectName(u"lock_display_box")
        self.lock_display_box.setGeometry(QRect(31, 111, 121, 20))
        self.hide_time_box = QCheckBox(self.Widget)
        self.hide_time_box.setObjectName(u"hide_time_box")
        self.hide_time_box.setGeometry(QRect(31, 141, 121, 20))
        self.close_settings_button = QPushButton(self.Widget)
        self.close_settings_button.setObjectName(u"close_settings_button")
        self.close_settings_button.setGeometry(QRect(40, 218, 75, 24))
        self.sounds_list_view = QListWidget(self.Widget)
        self.sounds_list_view.setObjectName(u"sounds_list_view")
        self.sounds_list_view.setGeometry(QRect(255, 40, 281, 171))
        self.sounds_list_view.raise_()
        self.label.raise_()
        self.play_list_button.raise_()
        self.remove_sound_button.raise_()
        self.import_sound_button.raise_()
        self.randomize_sound_box.raise_()
        self.auto_repeat_box.raise_()
        self.lock_display_box.raise_()
        self.hide_time_box.raise_()
        self.close_settings_button.raise_()

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
        self.randomize_sound_box.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.randomize_sound_box.setText(QCoreApplication.translate("SettingsWidget", u"Randomize Sound", None))
#if QT_CONFIG(tooltip)
        self.auto_repeat_box.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.auto_repeat_box.setText(QCoreApplication.translate("SettingsWidget", u"Auto Repeat", None))
#if QT_CONFIG(tooltip)
        self.lock_display_box.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lock_display_box.setText(QCoreApplication.translate("SettingsWidget", u"Lock Display", None))
#if QT_CONFIG(tooltip)
        self.hide_time_box.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.hide_time_box.setText(QCoreApplication.translate("SettingsWidget", u"Hide Time", None))
        self.close_settings_button.setText(QCoreApplication.translate("SettingsWidget", u"Close", None))
    # retranslateUi

