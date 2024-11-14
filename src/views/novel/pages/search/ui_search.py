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
from PySide6.QtWidgets import (QApplication, QGridLayout, QScrollArea, QSizePolicy,
    QSpacerItem, QWidget)

from qfluentwidgets import (SearchLineEdit, SmoothScrollArea)

class Ui_NovelSearch(object):
    def setupUi(self, NovelSearch):
        if not NovelSearch.objectName():
            NovelSearch.setObjectName(u"NovelSearch")
        NovelSearch.resize(911, 659)
        NovelSearch.setStyleSheet(u"")
        self.gridLayout = QGridLayout(NovelSearch)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.le_search = SearchLineEdit(NovelSearch)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.le_search, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.container = QScrollArea(NovelSearch)
        self.container.setObjectName(u"container")
        self.container.setWidgetResizable(True)
        self.search_area_2 = SmoothScrollArea()
        self.search_area_2.setObjectName(u"search_area_2")
        self.search_area_2.setGeometry(QRect(0, 0, 909, 637))
        self.container.setWidget(self.search_area_2)

        self.gridLayout.addWidget(self.container, 1, 0, 1, 3)


        self.retranslateUi(NovelSearch)

        QMetaObject.connectSlotsByName(NovelSearch)
    # setupUi

    def retranslateUi(self, NovelSearch):
        NovelSearch.setWindowTitle(QCoreApplication.translate("NovelSearch", u"Form", None))
    # retranslateUi

