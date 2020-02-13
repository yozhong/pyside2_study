# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'category_window.ui'
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

class Ui_Categorywindow(object):
    def setupUi(self, Categorywindow):
        if Categorywindow.objectName():
            Categorywindow.setObjectName(u"Categorywindow")
        Categorywindow.resize(260, 166)
        self.verticalLayout_2 = QVBoxLayout(Categorywindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Categorywindow)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.category_entry = QLineEdit(Categorywindow)
        self.category_entry.setObjectName(u"category_entry")

        self.verticalLayout.addWidget(self.category_entry)

        self.submit_btn = QPushButton(Categorywindow)
        self.submit_btn.setObjectName(u"submit_btn")

        self.verticalLayout.addWidget(self.submit_btn)

        self.cancel_btn = QPushButton(Categorywindow)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.verticalLayout.addWidget(self.cancel_btn)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Categorywindow)

        QMetaObject.connectSlotsByName(Categorywindow)
    # setupUi

    def retranslateUi(self, Categorywindow):
        Categorywindow.setWindowTitle(QCoreApplication.translate("Categorywindow", u"New Category", None))
        self.label.setText(QCoreApplication.translate("Categorywindow", u"Please enter a new category name:", None))
        self.submit_btn.setText(QCoreApplication.translate("Categorywindow", u"Submit", None))
        self.cancel_btn.setText(QCoreApplication.translate("Categorywindow", u"Cancel", None))
    # retranslateUi

