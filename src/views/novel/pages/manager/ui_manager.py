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

from qfluentwidgets import (BodyLabel, PushButton, TableWidget)

class Ui_NovelManager(object):
    def setupUi(self, NovelManager):
        if not NovelManager.objectName():
            NovelManager.setObjectName(u"NovelManager")
        NovelManager.resize(899, 572)
        self.gridLayout = QGridLayout(NovelManager)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.wgt_sources = QWidget(NovelManager)
        self.wgt_sources.setObjectName(u"wgt_sources")
        self.gridLayout_3 = QGridLayout(self.wgt_sources)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lb_total = BodyLabel(self.wgt_sources)
        self.lb_total.setObjectName(u"lb_total")

        self.gridLayout_3.addWidget(self.lb_total, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(460, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.btn_import_sources_internet = PushButton(self.wgt_sources)
        self.btn_import_sources_internet.setObjectName(u"btn_import_sources_internet")

        self.gridLayout_3.addWidget(self.btn_import_sources_internet, 0, 2, 1, 1)

        self.btn_import_sources_local = PushButton(self.wgt_sources)
        self.btn_import_sources_local.setObjectName(u"btn_import_sources_local")

        self.gridLayout_3.addWidget(self.btn_import_sources_local, 0, 3, 1, 1)

        self.table_sources = TableWidget(self.wgt_sources)
        self.table_sources.setObjectName(u"table_sources")

        self.gridLayout_3.addWidget(self.table_sources, 1, 0, 1, 4)


        self.gridLayout.addWidget(self.wgt_sources, 0, 0, 1, 1)


        self.retranslateUi(NovelManager)

        QMetaObject.connectSlotsByName(NovelManager)
    # setupUi

    def retranslateUi(self, NovelManager):
        NovelManager.setWindowTitle(QCoreApplication.translate("NovelManager", u"Form", None))
        self.lb_total.setText(QCoreApplication.translate("NovelManager", u"\u4e66\u6e90", None))
        self.btn_import_sources_internet.setText(QCoreApplication.translate("NovelManager", u"\u7f51\u7edc\u5bfc\u5165", None))
        self.btn_import_sources_local.setText(QCoreApplication.translate("NovelManager", u"\u672c\u5730\u5bfc\u5165", None))
    # retranslateUi

