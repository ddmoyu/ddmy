# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'content.ui'
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

class Ui_NovelContent(object):
    def setupUi(self, NovelContent):
        if not NovelContent.objectName():
            NovelContent.setObjectName(u"NovelContent")
        NovelContent.resize(746, 543)
        self.gridLayout = QGridLayout(NovelContent)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.content_layout = QVBoxLayout()
        self.content_layout.setObjectName(u"content_layout")
        self.pushButton = QPushButton(NovelContent)
        self.pushButton.setObjectName(u"pushButton")

        self.content_layout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.content_layout, 0, 0, 1, 1)


        self.retranslateUi(NovelContent)

        QMetaObject.connectSlotsByName(NovelContent)
    # setupUi

    def retranslateUi(self, NovelContent):
        NovelContent.setWindowTitle(QCoreApplication.translate("NovelContent", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("NovelContent", u"content", None))
    # retranslateUi

