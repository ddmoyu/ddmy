# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'novel.ui'
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
        self.list_layout = QVBoxLayout()
        self.list_layout.setObjectName(u"list_layout")

        self.gridLayout_3.addLayout(self.list_layout, 0, 0, 1, 1)

        self.stack.addWidget(self.list)
        self.manager = QWidget()
        self.manager.setObjectName(u"manager")
        self.gridLayout_4 = QGridLayout(self.manager)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.manager_layout = QVBoxLayout()
        self.manager_layout.setObjectName(u"manager_layout")

        self.gridLayout_4.addLayout(self.manager_layout, 0, 0, 1, 1)

        self.stack.addWidget(self.manager)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.gridLayout_2 = QGridLayout(self.search)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.search_layout = QVBoxLayout()
        self.search_layout.setObjectName(u"search_layout")

        self.gridLayout_2.addLayout(self.search_layout, 0, 0, 1, 1)

        self.stack.addWidget(self.search)
        self.detail = QWidget()
        self.detail.setObjectName(u"detail")
        self.gridLayout_5 = QGridLayout(self.detail)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.detail_layout = QVBoxLayout()
        self.detail_layout.setObjectName(u"detail_layout")

        self.gridLayout_5.addLayout(self.detail_layout, 0, 0, 1, 1)

        self.stack.addWidget(self.detail)
        self.bookshelf = QWidget()
        self.bookshelf.setObjectName(u"bookshelf")
        self.gridLayout_7 = QGridLayout(self.bookshelf)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.bookshelf_layout = QVBoxLayout()
        self.bookshelf_layout.setObjectName(u"bookshelf_layout")

        self.gridLayout_7.addLayout(self.bookshelf_layout, 0, 0, 1, 1)

        self.stack.addWidget(self.bookshelf)
        self.content = QWidget()
        self.content.setObjectName(u"content")
        self.gridLayout_6 = QGridLayout(self.content)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.content_layout = QVBoxLayout()
        self.content_layout.setObjectName(u"content_layout")

        self.gridLayout_6.addLayout(self.content_layout, 0, 0, 1, 1)

        self.stack.addWidget(self.content)

        self.gridLayout.addWidget(self.stack, 1, 0, 1, 1)


        self.retranslateUi(Novel)

        self.stack.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Novel)
    # setupUi

    def retranslateUi(self, Novel):
        Novel.setWindowTitle(QCoreApplication.translate("Novel", u"Form", None))
    # retranslateUi

