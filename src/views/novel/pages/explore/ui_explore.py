# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'explore.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidgetItem,
    QSizePolicy, QSpacerItem, QWidget)

from qfluentwidgets import (ListWidget, SearchLineEdit, SingleDirectionScrollArea, ToolButton)

class Ui_NovelExplore(object):
    def setupUi(self, NovelExplore):
        if not NovelExplore.objectName():
            NovelExplore.setObjectName(u"NovelExplore")
        NovelExplore.resize(1036, 766)
        self.gridLayout = QGridLayout(NovelExplore)
        self.gridLayout.setObjectName(u"gridLayout")
        self.category = ListWidget(NovelExplore)
        self.category.setObjectName(u"category")
        self.category.setMinimumSize(QSize(140, 0))
        self.category.setMaximumSize(QSize(150, 16777215))

        self.gridLayout.addWidget(self.category, 1, 1, 3, 1)

        self.widget = QWidget(NovelExplore)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 0))
        self.widget.setMaximumSize(QSize(220, 16777215))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.list = ListWidget(self.widget)
        self.list.setObjectName(u"list")
        self.list.setMinimumSize(QSize(0, 0))
        self.list.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.list, 1, 0, 1, 1)

        self.le_search = SearchLineEdit(self.widget)
        self.le_search.setObjectName(u"le_search")

        self.gridLayout_2.addWidget(self.le_search, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 1, 0, 3, 1)

        self.book_footer = QWidget(NovelExplore)
        self.book_footer.setObjectName(u"book_footer")
        self.book_footer.setMaximumSize(QSize(16777215, 50))
        self.gridLayout_3 = QGridLayout(self.book_footer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_next = ToolButton(self.book_footer)
        self.btn_next.setObjectName(u"btn_next")

        self.gridLayout_3.addWidget(self.btn_next, 2, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.btn_prev = ToolButton(self.book_footer)
        self.btn_prev.setObjectName(u"btn_prev")

        self.gridLayout_3.addWidget(self.btn_prev, 2, 3, 1, 1)

        self.lb_total = QLabel(self.book_footer)
        self.lb_total.setObjectName(u"lb_total")

        self.gridLayout_3.addWidget(self.lb_total, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.book_footer, 3, 2, 1, 1)

        self.book_list = SingleDirectionScrollArea(NovelExplore)
        self.book_list.setObjectName(u"book_list")
        self.book_list.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 634, 690))
        self.book_list.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.book_list, 1, 2, 2, 1)


        self.retranslateUi(NovelExplore)

        QMetaObject.connectSlotsByName(NovelExplore)
    # setupUi

    def retranslateUi(self, NovelExplore):
        NovelExplore.setWindowTitle(QCoreApplication.translate("NovelExplore", u"Form", None))
        self.btn_next.setText(QCoreApplication.translate("NovelExplore", u"->", None))
        self.btn_prev.setText(QCoreApplication.translate("NovelExplore", u"<-", None))
        self.lb_total.setText(QCoreApplication.translate("NovelExplore", u"\u7b2c\u4e00\u9875", None))
    # retranslateUi

