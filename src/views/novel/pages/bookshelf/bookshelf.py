from src.views.novel.pages.bookshelf.ui_bookshelf import Ui_NovelBookshelf
from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon
from src.views.novel.pages.bookshelf.componments.group_box import GroupBox


class NovelBookshelf(Ui_NovelBookshelf, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setupUi(self)
        self.initUi()
        self.initSignalSlot()

    def initUi(self):
        self.btn_views.setIcon(FluentIcon.VIEW)
        self.btn_filters.setIcon(FluentIcon.FILTER)
        self.btn_add.setIcon(FluentIcon.DICTIONARY_ADD)

        gp1 = GroupBox()
        gp2 = GroupBox()
        self.verticalLayout.addWidget(gp1)
        self.verticalLayout.addWidget(gp2)

    def initSignalSlot(self):
        pass
