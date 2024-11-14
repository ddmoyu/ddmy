# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bookshelf.ui'
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

class Ui_NovelBookshelf(object):
    def setupUi(self, NovelBookshelf):
        if not NovelBookshelf.objectName():
            NovelBookshelf.setObjectName(u"NovelBookshelf")
        NovelBookshelf.resize(746, 543)
        self.gridLayout = QGridLayout(NovelBookshelf)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bookshelf_layout = QVBoxLayout()
        self.bookshelf_layout.setObjectName(u"bookshelf_layout")
        self.pushButton = QPushButton(NovelBookshelf)
        self.pushButton.setObjectName(u"pushButton")

        self.bookshelf_layout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.bookshelf_layout, 0, 0, 1, 1)


        self.retranslateUi(NovelBookshelf)

        QMetaObject.connectSlotsByName(NovelBookshelf)
    # setupUi

    def retranslateUi(self, NovelBookshelf):
        NovelBookshelf.setWindowTitle(QCoreApplication.translate("NovelBookshelf", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("NovelBookshelf", u"\u4e66\u67b6", None))
    # retranslateUi

