# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manager.ui'
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

class Ui_NovelManager(object):
    def setupUi(self, NovelManager):
        if not NovelManager.objectName():
            NovelManager.setObjectName(u"NovelManager")
        NovelManager.resize(746, 543)
        self.gridLayout = QGridLayout(NovelManager)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.manager_layout = QVBoxLayout()
        self.manager_layout.setObjectName(u"manager_layout")
        self.pushButton = QPushButton(NovelManager)
        self.pushButton.setObjectName(u"pushButton")

        self.manager_layout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.manager_layout, 0, 0, 1, 1)


        self.retranslateUi(NovelManager)

        QMetaObject.connectSlotsByName(NovelManager)
    # setupUi

    def retranslateUi(self, NovelManager):
        NovelManager.setWindowTitle(QCoreApplication.translate("NovelManager", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("NovelManager", u"manager ", None))
    # retranslateUi

