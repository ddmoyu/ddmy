# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'searchGGupRD.ui'
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
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (SearchLineEdit, SmoothScrollArea)

class Ui_NovelSearch(object):
    def setupUi(self, NovelSearch):
        if not NovelSearch.objectName():
            NovelSearch.setObjectName(u"NovelSearch")
        NovelSearch.resize(787, 659)
        NovelSearch.setStyleSheet(u"")
        self.gridLayout = QGridLayout(NovelSearch)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(NovelSearch)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.le_search = SearchLineEdit(self.widget)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_2.addWidget(self.le_search, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(243, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(243, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.container = QScrollArea(self.widget)
        self.container.setObjectName(u"container")
        self.container.setWidgetResizable(True)
        self.search_area = SmoothScrollArea()
        self.search_area.setObjectName(u"search_area")
        self.search_area.setGeometry(QRect(0, 0, 783, 629))
        self.container.setWidget(self.search_area)

        self.gridLayout_2.addWidget(self.container, 1, 0, 1, 3)


        self.verticalLayout.addWidget(self.widget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(NovelSearch)

        QMetaObject.connectSlotsByName(NovelSearch)
    # setupUi

    def retranslateUi(self, NovelSearch):
        NovelSearch.setWindowTitle(QCoreApplication.translate("NovelSearch", u"Form", None))
    # retranslateUi

