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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QSizePolicy, QSpacerItem, QTreeWidgetItem, QWidget)

from qfluentwidgets import (BodyLabel, ComboBox, CompactSpinBox, ListWidget,
    TextBrowser, TransparentToolButton)

class Ui_NovelContent(object):
    def setupUi(self, NovelContent):
        if not NovelContent.objectName():
            NovelContent.setObjectName(u"NovelContent")
        NovelContent.resize(746, 578)
        self.gridLayout = QGridLayout(NovelContent)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(NovelContent)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = TextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_2.addWidget(self.textBrowser, 1, 1, 1, 1)

        self.wgt_style = QFrame(self.widget)
        self.wgt_style.setObjectName(u"wgt_style")
        self.wgt_style.setMinimumSize(QSize(220, 0))
        self.wgt_style.setMaximumSize(QSize(120, 16777215))
        self.wgt_style.setFrameShape(QFrame.Shape.StyledPanel)
        self.wgt_style.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.wgt_style)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.spb_font_size = CompactSpinBox(self.wgt_style)
        self.spb_font_size.setObjectName(u"spb_font_size")

        self.gridLayout_5.addWidget(self.spb_font_size, 1, 1, 1, 1)

        self.spb_font_spacing = CompactSpinBox(self.wgt_style)
        self.spb_font_spacing.setObjectName(u"spb_font_spacing")

        self.gridLayout_5.addWidget(self.spb_font_spacing, 2, 1, 1, 1)

        self.spb_row_spacing = CompactSpinBox(self.wgt_style)
        self.spb_row_spacing.setObjectName(u"spb_row_spacing")

        self.gridLayout_5.addWidget(self.spb_row_spacing, 3, 1, 1, 1)

        self.label_4 = BodyLabel(self.wgt_style)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 4, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 5, 1, 1, 1)

        self.spb_segment_spacing = CompactSpinBox(self.wgt_style)
        self.spb_segment_spacing.setObjectName(u"spb_segment_spacing")

        self.gridLayout_5.addWidget(self.spb_segment_spacing, 4, 1, 1, 1)

        self.label_2 = BodyLabel(self.wgt_style)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_3 = BodyLabel(self.wgt_style)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 3, 0, 1, 1)

        self.label = BodyLabel(self.wgt_style)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)

        self.label_5 = BodyLabel(self.wgt_style)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)

        self.cbb_font_family = ComboBox(self.wgt_style)
        self.cbb_font_family.setObjectName(u"cbb_font_family")

        self.gridLayout_5.addWidget(self.cbb_font_family, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.wgt_style, 1, 2, 1, 1)

        self.wgt_toc = QFrame(self.widget)
        self.wgt_toc.setObjectName(u"wgt_toc")
        self.wgt_toc.setMinimumSize(QSize(220, 0))
        self.wgt_toc.setMaximumSize(QSize(120, 16777215))
        self.wgt_toc.setFrameShape(QFrame.Shape.StyledPanel)
        self.wgt_toc.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.wgt_toc)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.lw_toc = ListWidget(self.wgt_toc)
        self.lw_toc.setObjectName(u"lw_toc")

        self.gridLayout_6.addWidget(self.lw_toc, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.wgt_toc, 1, 0, 1, 1)

        self.frame_top = QFrame(self.widget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_top)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_style = TransparentToolButton(self.frame_top)
        self.btn_style.setObjectName(u"btn_style")

        self.gridLayout_4.addWidget(self.btn_style, 0, 4, 1, 1)

        self.btn_view = TransparentToolButton(self.frame_top)
        self.btn_view.setObjectName(u"btn_view")

        self.gridLayout_4.addWidget(self.btn_view, 0, 3, 1, 1)

        self.lb_chapter = BodyLabel(self.frame_top)
        self.lb_chapter.setObjectName(u"lb_chapter")

        self.gridLayout_4.addWidget(self.lb_chapter, 0, 1, 1, 1)

        self.btn_chapter = TransparentToolButton(self.frame_top)
        self.btn_chapter.setObjectName(u"btn_chapter")

        self.gridLayout_4.addWidget(self.btn_chapter, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_top, 0, 0, 1, 3)

        self.frame_footer = QFrame(self.widget)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_footer.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_footer)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.btn_next_chapter = TransparentToolButton(self.frame_footer)
        self.btn_next_chapter.setObjectName(u"btn_next_chapter")

        self.gridLayout_3.addWidget(self.btn_next_chapter, 0, 3, 1, 1)

        self.btn_prev_chapter = TransparentToolButton(self.frame_footer)
        self.btn_prev_chapter.setObjectName(u"btn_prev_chapter")

        self.gridLayout_3.addWidget(self.btn_prev_chapter, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_footer, 2, 0, 1, 3)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(NovelContent)

        QMetaObject.connectSlotsByName(NovelContent)
    # setupUi

    def retranslateUi(self, NovelContent):
        NovelContent.setWindowTitle(QCoreApplication.translate("NovelContent", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("NovelContent", u"\u6bb5\u8ddd\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("NovelContent", u"\u5b57\u8ddd\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("NovelContent", u"\u884c\u8ddd\uff1a", None))
        self.label.setText(QCoreApplication.translate("NovelContent", u"\u5b57\u53f7\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("NovelContent", u"\u5b57\u4f53\uff1a", None))
        self.btn_style.setText("")
        self.btn_view.setText("")
        self.lb_chapter.setText(QCoreApplication.translate("NovelContent", u"\u7ae0\u8282\u540d", None))
        self.btn_chapter.setText("")
        self.btn_next_chapter.setText("")
        self.btn_prev_chapter.setText("")
    # retranslateUi

