# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listDIgjus.ui'
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

class Ui_NovelList(object):
    def setupUi(self, NovelList):
        if not NovelList.objectName():
            NovelList.setObjectName(u"NovelList")
        NovelList.resize(746, 543)
        self.gridLayout = QGridLayout(NovelList)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.list_layout = QVBoxLayout()
        self.list_layout.setObjectName(u"list_layout")
        self.pushButton = QPushButton(NovelList)
        self.pushButton.setObjectName(u"pushButton")

        self.list_layout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.list_layout, 0, 0, 1, 1)


        self.retranslateUi(NovelList)

        QMetaObject.connectSlotsByName(NovelList)
    # setupUi

    def retranslateUi(self, NovelList):
        NovelList.setWindowTitle(QCoreApplication.translate("NovelList", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("NovelList", u"detail", None))
    # retranslateUi

