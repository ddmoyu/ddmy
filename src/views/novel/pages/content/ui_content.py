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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

from qfluentwidgets import TextBrowser

class Ui_NovelContent(object):
    def setupUi(self, NovelContent):
        if not NovelContent.objectName():
            NovelContent.setObjectName(u"NovelContent")
        NovelContent.resize(746, 543)
        self.gridLayout = QGridLayout(NovelContent)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(NovelContent)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_4.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_4.addWidget(self.pushButton_4, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.textBrowser = TextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 0, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(NovelContent)

        QMetaObject.connectSlotsByName(NovelContent)
    # setupUi

    def retranslateUi(self, NovelContent):
        NovelContent.setWindowTitle(QCoreApplication.translate("NovelContent", u"Form", None))
        self.pushButton_3.setText(QCoreApplication.translate("NovelContent", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("NovelContent", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("NovelContent", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("NovelContent", u"PushButton", None))
    # retranslateUi

