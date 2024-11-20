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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QSizePolicy,
    QSpacerItem, QTableWidgetItem, QWidget)

from qfluentwidgets import (BodyLabel, IndeterminateProgressBar, PushButton, TableWidget)

class Ui_NovelManager(object):
    def setupUi(self, NovelManager):
        if not NovelManager.objectName():
            NovelManager.setObjectName(u"NovelManager")
        NovelManager.resize(899, 572)
        self.gridLayout = QGridLayout(NovelManager)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 9)
        self.wgt_sources = QWidget(NovelManager)
        self.wgt_sources.setObjectName(u"wgt_sources")
        self.gridLayout_3 = QGridLayout(self.wgt_sources)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(6)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.progressBar = IndeterminateProgressBar(self.wgt_sources)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout_3.addWidget(self.progressBar, 3, 1, 1, 1)

        self.widget = QWidget(self.wgt_sources)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(460, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.btn_ping = PushButton(self.widget)
        self.btn_ping.setObjectName(u"btn_ping")

        self.gridLayout_2.addWidget(self.btn_ping, 0, 1, 1, 1)

        self.btn_import_sources_local = PushButton(self.widget)
        self.btn_import_sources_local.setObjectName(u"btn_import_sources_local")

        self.gridLayout_2.addWidget(self.btn_import_sources_local, 0, 4, 1, 1)

        self.btn_import_sources_internet = PushButton(self.widget)
        self.btn_import_sources_internet.setObjectName(u"btn_import_sources_internet")

        self.gridLayout_2.addWidget(self.btn_import_sources_internet, 0, 3, 1, 1)

        self.btn_group_manager = PushButton(self.widget)
        self.btn_group_manager.setObjectName(u"btn_group_manager")

        self.gridLayout_2.addWidget(self.btn_group_manager, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 0, 1, 1, 1)

        self.table_sources = TableWidget(self.wgt_sources)
        self.table_sources.setObjectName(u"table_sources")

        self.gridLayout_3.addWidget(self.table_sources, 1, 1, 1, 1)

        self.widget_2 = QWidget(self.wgt_sources)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_total = BodyLabel(self.widget_2)
        self.lb_total.setObjectName(u"lb_total")

        self.gridLayout_4.addWidget(self.lb_total, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget_2, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.wgt_sources, 0, 0, 1, 1)


        self.retranslateUi(NovelManager)

        QMetaObject.connectSlotsByName(NovelManager)
    # setupUi

    def retranslateUi(self, NovelManager):
        NovelManager.setWindowTitle(QCoreApplication.translate("NovelManager", u"Form", None))
        self.btn_ping.setText(QCoreApplication.translate("NovelManager", u"\u6821\u9a8c", None))
        self.btn_import_sources_local.setText(QCoreApplication.translate("NovelManager", u"\u672c\u5730\u5bfc\u5165", None))
        self.btn_import_sources_internet.setText(QCoreApplication.translate("NovelManager", u"\u7f51\u7edc\u5bfc\u5165", None))
        self.btn_group_manager.setText(QCoreApplication.translate("NovelManager", u"\u5206\u7ec4\u7ba1\u7406", None))
        self.lb_total.setText(QCoreApplication.translate("NovelManager", u"\u4e66\u6e90", None))
    # retranslateUi

