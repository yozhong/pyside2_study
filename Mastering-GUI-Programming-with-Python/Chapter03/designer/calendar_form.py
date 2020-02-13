# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calendar_form.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(860, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.calendar = QCalendarWidget(self.centralwidget)
        self.calendar.setObjectName(u"calendar")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendar.sizePolicy().hasHeightForWidth())
        self.calendar.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.calendar)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.event_time = QTimeEdit(self.groupBox)
        self.event_time.setObjectName(u"event_time")

        self.gridLayout.addWidget(self.event_time, 2, 1, 1, 1)

        self.event_detail = QTextEdit(self.groupBox)
        self.event_detail.setObjectName(u"event_detail")

        self.gridLayout.addWidget(self.event_detail, 4, 0, 1, 3)

        self.allday_check = QCheckBox(self.groupBox)
        self.allday_check.setObjectName(u"allday_check")

        self.gridLayout.addWidget(self.allday_check, 2, 2, 1, 1)

        self.event_category = QComboBox(self.groupBox)
        self.event_category.addItem(QString())
        self.event_category.addItem(QString())
        self.event_category.addItem(QString())
        self.event_category.addItem(QString())
        self.event_category.addItem(QString())
        self.event_category.setObjectName(u"event_category")

        self.gridLayout.addWidget(self.event_category, 2, 0, 1, 1)

        self.event_title = QLineEdit(self.groupBox)
        self.event_title.setObjectName(u"event_title")

        self.gridLayout.addWidget(self.event_title, 0, 0, 1, 3)

        self.add_button = QPushButton(self.groupBox)
        self.add_button.setObjectName(u"add_button")

        self.gridLayout.addWidget(self.add_button, 5, 1, 1, 1)

        self.del_button = QPushButton(self.groupBox)
        self.del_button.setObjectName(u"del_button")

        self.gridLayout.addWidget(self.del_button, 5, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 860, 35))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"My Calendar App", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Event on Date", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Event", None))
        self.allday_check.setText(QCoreApplication.translate("MainWindow", u"All Day", None))
        self.event_category.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Category...", None))
        self.event_category.setItemText(1, QCoreApplication.translate("MainWindow", u"New...", None))
        self.event_category.setItemText(2, QCoreApplication.translate("MainWindow", u"Work", None))
        self.event_category.setItemText(3, QCoreApplication.translate("MainWindow", u"Doctor", None))
        self.event_category.setItemText(4, QCoreApplication.translate("MainWindow", u"Meeting", None))

        self.add_button.setText(QCoreApplication.translate("MainWindow", u"Add/Update", None))
        self.del_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

