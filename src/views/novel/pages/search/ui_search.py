# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchMcNnqj.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_NovelSearch(object):
    def setupUi(self, NovelSearch):
        if not NovelSearch.objectName():
            NovelSearch.setObjectName(u"NovelSearch")
        NovelSearch.resize(787, 659)
        NovelSearch.setStyleSheet(u"background-color: #000022;")
        self.gridLayout = QGridLayout(NovelSearch)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(NovelSearch)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(NovelSearch)

        QMetaObject.connectSlotsByName(NovelSearch)
    # setupUi

    def retranslateUi(self, NovelSearch):
        NovelSearch.setWindowTitle(QCoreApplication.translate("NovelSearch", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("NovelSearch", u"search", None))
    # retranslateUi

