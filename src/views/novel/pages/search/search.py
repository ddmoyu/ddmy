from qfluentwidgets import FlowLayout, IndeterminateProgressBar, FluentIcon
from .ui_search import Ui_NovelSearch
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QColor


class NovelSearch(Ui_NovelSearch, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setupUi(self)
        self.qvl_book_list = None
        self.progress = None

        self.init_ui()
        self.init_connect()

    def init_ui(self):
        self.container.hide()
        self.btn_stop.setIcon(FluentIcon.PAUSE)
        self.btn_stop.hide()
        self.qvl_book_list = FlowLayout(self.smoothScrollArea)
        self.qvl_book_list.setHorizontalSpacing(20)
        self.qvl_book_list.setVerticalSpacing(10)
        self.progress = IndeterminateProgressBar(start=True)
        self.progress.setCustomBarColor(QColor("#383838"), QColor("#383838"))
        self.progressbar_layout.addWidget(self.progress)
        self.progress.hide()

    def init_connect(self):
        self.le_search.returnPressed.connect(self.search_event_handler)
        self.le_search.textChanged.connect(self.search_changed_handler)
        self.btn_stop.clicked.connect(lambda: self.progress.pause())

    def search_event_handler(self):
        self.container.show()
        self.progress.show()
        self.btn_stop.show()
        self.qvl_book_list.removeAllWidgets()
        for item in range(20):
            # self.qvl_book_list.addWidget(book_item)
            pass

    def search_changed_handler(self):
        if len(self.le_search.text()) == 0:
            self.container.hide()
            self.progress.hide()
            self.btn_stop.hide()
