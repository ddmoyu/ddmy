# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailRKWeZo.ui'
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

class Ui_NovelDetail(object):
    def setupUi(self, NovelDetail):
        if not NovelDetail.objectName():
            NovelDetail.setObjectName(u"NovelDetail")
        NovelDetail.resize(746, 543)
        self.gridLayout = QGridLayout(NovelDetail)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.detail_layout = QVBoxLayout()
        self.detail_layout.setObjectName(u"detail_layout")
        self.pushButton = QPushButton(NovelDetail)
        self.pushButton.setObjectName(u"pushButton")

        self.detail_layout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.detail_layout, 0, 0, 1, 1)


        self.retranslateUi(NovelDetail)

        QMetaObject.connectSlotsByName(NovelDetail)
    # setupUi

    def retranslateUi(self, NovelDetail):
        NovelDetail.setWindowTitle(QCoreApplication.translate("NovelDetail", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("NovelDetail", u"detail", None))
    # retranslateUi

