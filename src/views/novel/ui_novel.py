# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'novelOCkLsX.ui'
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
    QStackedWidget, QWidget)

class Ui_Novel(object):
    def setupUi(self, Novel):
        if not Novel.objectName():
            Novel.setObjectName(u"Novel")
        Novel.resize(957, 746)
        self.gridLayout = QGridLayout(Novel)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stack = QStackedWidget(Novel)
        self.stack.setObjectName(u"stack")
        self.stack.setStyleSheet(u"")
        self.list = QWidget()
        self.list.setObjectName(u"list")
        self.gridLayout_3 = QGridLayout(self.list)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_6 = QPushButton(self.list)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_3.addWidget(self.pushButton_6, 0, 0, 1, 1)

        self.stack.addWidget(self.list)
        self.manager = QWidget()
        self.manager.setObjectName(u"manager")
        self.gridLayout_4 = QGridLayout(self.manager)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_5 = QPushButton(self.manager)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_4.addWidget(self.pushButton_5, 0, 0, 1, 1)

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
        self.pushButton_2 = QPushButton(self.detail)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_5.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.stack.addWidget(self.detail)
        self.bookshelf = QWidget()
        self.bookshelf.setObjectName(u"bookshelf")
        self.gridLayout_7 = QGridLayout(self.bookshelf)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButton_3 = QPushButton(self.bookshelf)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_7.addWidget(self.pushButton_3, 0, 0, 1, 1)

        self.stack.addWidget(self.bookshelf)
        self.bookmark = QWidget()
        self.bookmark.setObjectName(u"bookmark")
        self.gridLayout_8 = QGridLayout(self.bookmark)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pushButton_4 = QPushButton(self.bookmark)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_8.addWidget(self.pushButton_4, 0, 0, 1, 1)

        self.stack.addWidget(self.bookmark)
        self.content = QWidget()
        self.content.setObjectName(u"content")
        self.gridLayout_6 = QGridLayout(self.content)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton = QPushButton(self.content)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_6.addWidget(self.pushButton, 0, 0, 1, 1)

        self.stack.addWidget(self.content)

        self.gridLayout.addWidget(self.stack, 0, 0, 1, 1)


        self.retranslateUi(Novel)

        self.stack.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Novel)
    # setupUi

    def retranslateUi(self, Novel):
        Novel.setWindowTitle(QCoreApplication.translate("Novel", u"Form", None))
        self.pushButton_6.setText(QCoreApplication.translate("Novel", u"list", None))
        self.pushButton_5.setText(QCoreApplication.translate("Novel", u"manager", None))
        self.pushButton_2.setText(QCoreApplication.translate("Novel", u"detail", None))
        self.pushButton_3.setText(QCoreApplication.translate("Novel", u"\u4e66\u67b6", None))
        self.pushButton_4.setText(QCoreApplication.translate("Novel", u"\u4e66\u7b7e", None))
        self.pushButton.setText(QCoreApplication.translate("Novel", u"content", None))
    # retranslateUi

