# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'novelFWRoFK.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Novel(object):
    def setupUi(self, Novel):
        if not Novel.objectName():
            Novel.setObjectName(u"Novel")
        Novel.resize(957, 746)
        self.gridLayout = QGridLayout(Novel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.topMenu = QWidget(Novel)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(0, 40))
        self.gridLayout_9 = QGridLayout(self.topMenu)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.topMenuLayout = QVBoxLayout()
        self.topMenuLayout.setObjectName(u"topMenuLayout")

        self.gridLayout_9.addLayout(self.topMenuLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.topMenu, 0, 0, 1, 1)

        self.stack = QStackedWidget(Novel)
        self.stack.setObjectName(u"stack")
        self.stack.setStyleSheet(u"")
        self.list = QWidget()
        self.list.setObjectName(u"list")
        self.gridLayout_3 = QGridLayout(self.list)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stack.addWidget(self.list)
        self.manager = QWidget()
        self.manager.setObjectName(u"manager")
        self.gridLayout_4 = QGridLayout(self.manager)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stack.addWidget(self.manager)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.gridLayout_2 = QGridLayout(self.search)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stack.addWidget(self.search)
        self.detail = QWidget()
        self.detail.setObjectName(u"detail")
        self.gridLayout_5 = QGridLayout(self.detail)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stack.addWidget(self.detail)
        self.bookshelf = QWidget()
        self.bookshelf.setObjectName(u"bookshelf")
        self.gridLayout_7 = QGridLayout(self.bookshelf)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.stack.addWidget(self.bookshelf)
        self.content = QWidget()
        self.content.setObjectName(u"content")
        self.gridLayout_6 = QGridLayout(self.content)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.stack.addWidget(self.content)

        self.gridLayout.addWidget(self.stack, 1, 0, 1, 1)


        self.retranslateUi(Novel)

        self.stack.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Novel)
    # setupUi

    def retranslateUi(self, Novel):
        Novel.setWindowTitle(QCoreApplication.translate("Novel", u"Form", None))
    # retranslateUi

