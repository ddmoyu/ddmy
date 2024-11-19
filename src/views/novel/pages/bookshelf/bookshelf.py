from src.views.novel.pages.bookshelf.ui_bookshelf import Ui_NovelBookshelf
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from qfluentwidgets import FluentIcon
from src.views.novel.pages.bookshelf.components.group_box import GroupBox


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
        self.btn_search.setIcon(FluentIcon.SEARCH)
        self.le_search.hide()

        gp1 = GroupBox()
        gp2 = GroupBox()
        self.verticalLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.verticalLayout.addWidget(gp1)
        self.verticalLayout.addWidget(gp2)

    def initSignalSlot(self):
        self.btn_search.clicked.connect(self.on_btn_search_clicked)

    def on_btn_search_clicked(self):
        if not self.le_search.isVisible():
            self.le_search.show()
        else:
            self.le_search.hide()
