from src.common.signal_bus import signalBus
from src.views.novel.ui_novel import Ui_Novel
from src.layout.layout import LayoutInterface
from src.views.novel.pages.search.search import NovelSearch
from src.views.novel.pages.bookshelf.bookshelf import NovelBookshelf
from src.views.novel.pages.explore.explore import NovelList
from src.views.novel.pages.manager.manager import NovelManager
from src.views.novel.pages.detail.detail import NovelDetail
from src.views.novel.pages.content.content import NovelContent
from enum import Enum
from qfluentwidgets import SegmentedWidget


class NovelPage(Enum):
    LIST = 0
    MANAGER = 1
    SEARCH = 2
    DETAIL = 3
    BOOKSHELF = 4
    CONTENT = 5


class NovelInterface(LayoutInterface):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.ui = Ui_Novel()
        self.ui.setupUi(self)
        self.setObjectName("NovelInterface")
        self.page_cache = {}

        self.pivot = None
        self.init_top_menu()

        self.bookshelf = None
        self.list = None
        self.search = None
        self.manager = None
        self.detail = None
        self.content = None

        self.show_page(NovelPage.SEARCH)
        self.init_signal()

    def init_signal(self):
        signalBus.novel_change_page.connect(self.change_page)

    def change_page(self, page):
        if page == "bookshelf":
            self.show_page(NovelPage.BOOKSHELF)
        elif page == "list":
            self.show_page(NovelPage.LIST)
        elif page == "search":
            self.show_page(NovelPage.SEARCH)
        elif page == "manager":
            self.show_page(NovelPage.MANAGER)
        elif page == "detail":
            self.show_page(NovelPage.DETAIL)
        elif page == "content":
            self.show_page(NovelPage.CONTENT)

    def init_top_menu(self):
        self.pivot = SegmentedWidget()
        self.pivot.addItem(
            routeKey="bookshelf",
            text="书架",
            onClick=lambda: self.show_page(NovelPage.BOOKSHELF),
        )
        self.pivot.addItem(
            routeKey="list", text="浏览", onClick=lambda: self.show_page(NovelPage.LIST)
        )
        self.pivot.addItem(
            routeKey="search",
            text="搜索",
            onClick=lambda: self.show_page(NovelPage.SEARCH),
        )
        self.pivot.addItem(
            routeKey="manager",
            text="管理",
            onClick=lambda: self.show_page(NovelPage.MANAGER),
        )
        self.pivot.addItem(
            routeKey="content",
            text="阅读",
            onClick=lambda: self.show_page(NovelPage.CONTENT),
        )
        self.pivot.setCurrentItem("search")
        self.ui.topMenuLayout.addWidget(self.pivot)

    def show_page(self, page: NovelPage):
        if page.value not in self.page_cache:
            if page == NovelPage.BOOKSHELF:
                self.bookshelf = NovelBookshelf(self.ui.stack)
                self.page_cache[page.value] = self.bookshelf
                self.ui.bookshelf_layout.addWidget(self.bookshelf)
                self.pivot.setCurrentItem("bookshelf")
            elif page == NovelPage.LIST:
                self.list = NovelList(self.ui.stack)
                self.page_cache[page.value] = self.list
                self.ui.list_layout.addWidget(self.list)
                self.pivot.setCurrentItem("list")
            elif page == NovelPage.SEARCH:
                self.search = NovelSearch(self.ui.stack)
                self.page_cache[page.value] = self.search
                self.ui.search_layout.addWidget(self.search)
                self.pivot.setCurrentItem("search")
            elif page == NovelPage.MANAGER:
                self.manager = NovelManager(self.ui.stack)
                self.page_cache[page.value] = self.manager
                self.ui.manager_layout.addWidget(self.manager)
                self.pivot.setCurrentItem("manager")
            elif page == NovelPage.DETAIL:
                self.detail = NovelDetail(self.ui.stack)
                self.page_cache[page.value] = self.detail
                self.ui.detail_layout.addWidget(self.detail)
                self.pivot.setCurrentItem("detail")
            elif page == NovelPage.CONTENT:
                self.content = NovelContent(self.ui.stack)
                self.page_cache[page.value] = self.content
                self.ui.content_layout.addWidget(self.content)
                self.pivot.setCurrentItem("content")

        self.ui.stack.setCurrentIndex(page.value)
