from qfluentwidgets import IndeterminateProgressBar, FluentIcon
from src.views.novel.pages.search.ui_search import Ui_NovelSearch
from PySide6.QtWidgets import QWidget, QLayout
from PySide6.QtGui import QColor
from src.views.novel.pages.search.components.book_card import BookCard


class NovelSearch(Ui_NovelSearch, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setupUi(self)
        # self.qvl_book_list = None
        self.progress = None

        self.init_ui()
        self.init_connect()

    def init_ui(self):
        self.container.hide()
        self.btn_stop.setIcon(FluentIcon.PAUSE)
        self.btn_stop.hide()
        self.progress = IndeterminateProgressBar(start=True)
        self.progress.setCustomBarColor(QColor("#383838"), QColor("#383838"))
        self.progressbar_layout.addWidget(self.progress)
        self.progress.hide()

    def init_connect(self):
        self.le_search.returnPressed.connect(self.search_event_handler)
        self.le_search.textChanged.connect(self.search_changed_handler)
        self.btn_stop.clicked.connect(self.search_pause_handler)

    def search_event_handler(self):
        self.container.show()
        self.progress.show()
        self.btn_stop.show()
        self.clear_layout(self.qvl_book_list)
        for item in range(20):
            book = BookCard()
            self.qvl_book_list.addWidget(book)

    def clear_layout(self, layout: QLayout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()  # 异步删除小部件
                else:
                    layout.removeItem(item)
                    if item.layout():
                        self.clear_layout(item.layout())

    def search_changed_handler(self):
        if len(self.le_search.text()) == 0:
            self.container.hide()
            self.progress.hide()
            self.btn_stop.hide()

    def search_pause_handler(self):
        if self.progress.isStarted():
            self.progress.pause()
            self.btn_stop.setIcon(FluentIcon.PLAY)
        else:
            self.progress.resume()
            self.btn_stop.setIcon(FluentIcon.PAUSE)
