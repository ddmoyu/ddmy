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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (PushButton, SearchLineEdit, SmoothScrollArea, TransparentToolButton)

class Ui_NovelBookshelf(object):
    def setupUi(self, NovelBookshelf):
        if not NovelBookshelf.objectName():
            NovelBookshelf.setObjectName(u"NovelBookshelf")
        NovelBookshelf.resize(1062, 718)
        self.gridLayout = QGridLayout(NovelBookshelf)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.wgt_top_tools = QWidget(NovelBookshelf)
        self.wgt_top_tools.setObjectName(u"wgt_top_tools")
        self.gridLayout_3 = QGridLayout(self.wgt_top_tools)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer = QSpacerItem(630, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.btn_views = TransparentToolButton(self.wgt_top_tools)
        self.btn_views.setObjectName(u"btn_views")

        self.gridLayout_3.addWidget(self.btn_views, 0, 0, 1, 1)

        self.btn_filters = TransparentToolButton(self.wgt_top_tools)
        self.btn_filters.setObjectName(u"btn_filters")

        self.gridLayout_3.addWidget(self.btn_filters, 0, 1, 1, 1)

        self.btn_group_manager = PushButton(self.wgt_top_tools)
        self.btn_group_manager.setObjectName(u"btn_group_manager")

        self.gridLayout_3.addWidget(self.btn_group_manager, 0, 5, 1, 1)

        self.btn_add = TransparentToolButton(self.wgt_top_tools)
        self.btn_add.setObjectName(u"btn_add")

        self.gridLayout_3.addWidget(self.btn_add, 0, 4, 1, 1)

        self.le_search = SearchLineEdit(self.wgt_top_tools)
        self.le_search.setObjectName(u"le_search")
        self.le_search.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_3.addWidget(self.le_search, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.wgt_top_tools, 0, 0, 1, 1)

        self.scrollarea = SmoothScrollArea(NovelBookshelf)
        self.scrollarea.setObjectName(u"scrollarea")
        self.scrollarea.setWidgetResizable(True)
        self.book_scrollarea = QWidget()
        self.book_scrollarea.setObjectName(u"book_scrollarea")
        self.book_scrollarea.setGeometry(QRect(0, 0, 1060, 675))
        self.gridLayout_2 = QGridLayout(self.book_scrollarea)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.scrollarea.setWidget(self.book_scrollarea)

        self.gridLayout.addWidget(self.scrollarea, 1, 0, 1, 1)


        self.retranslateUi(NovelBookshelf)

        QMetaObject.connectSlotsByName(NovelBookshelf)
    # setupUi

    def retranslateUi(self, NovelBookshelf):
        NovelBookshelf.setWindowTitle(QCoreApplication.translate("NovelBookshelf", u"Form", None))
        self.btn_views.setText("")
        self.btn_filters.setText("")
        self.btn_group_manager.setText(QCoreApplication.translate("NovelBookshelf", u"\u5206\u7ec4\u7ba1\u7406", None))
        self.btn_add.setText("")
    # retranslateUi

