# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (SearchLineEdit, SmoothScrollArea, ToolButton)

class Ui_NovelSearch(object):
    def setupUi(self, NovelSearch):
        if not NovelSearch.objectName():
            NovelSearch.setObjectName(u"NovelSearch")
        NovelSearch.resize(911, 659)
        NovelSearch.setStyleSheet(u"")
        self.gridLayout = QGridLayout(NovelSearch)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 9)
        self.container = SmoothScrollArea(NovelSearch)
        self.container.setObjectName(u"container")
        self.container.setWidgetResizable(True)
        self.smoothScrollArea = QWidget()
        self.smoothScrollArea.setObjectName(u"smoothScrollArea")
        self.smoothScrollArea.setGeometry(QRect(0, 0, 909, 624))
        self.gridLayout_2 = QGridLayout(self.smoothScrollArea)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.container.setWidget(self.smoothScrollArea)

        self.gridLayout.addWidget(self.container, 1, 0, 1, 4)

        self.progressbar_layout = QVBoxLayout()
        self.progressbar_layout.setObjectName(u"progressbar_layout")

        self.gridLayout.addLayout(self.progressbar_layout, 2, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.le_search = SearchLineEdit(NovelSearch)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.le_search, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.btn_stop = ToolButton(NovelSearch)
        self.btn_stop.setObjectName(u"btn_stop")

        self.gridLayout.addWidget(self.btn_stop, 0, 2, 1, 1)


        self.retranslateUi(NovelSearch)

        QMetaObject.connectSlotsByName(NovelSearch)
    # setupUi

    def retranslateUi(self, NovelSearch):
        NovelSearch.setWindowTitle(QCoreApplication.translate("NovelSearch", u"Form", None))
        self.btn_stop.setText("")
    # retranslateUi

