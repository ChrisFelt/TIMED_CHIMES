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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(562, 275)
        self.CentralWidget = QWidget(MainWindow)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.StackedWidget = QStackedWidget(self.CentralWidget)
        self.StackedWidget.setObjectName(u"StackedWidget")
        self.StackedWidget.setGeometry(QRect(1, 2, 560, 271))
        MainWindow.setCentralWidget(self.CentralWidget)

        self.retranslateUi(MainWindow)

        self.StackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

