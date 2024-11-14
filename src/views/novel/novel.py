from .ui_novel import Ui_Novel
from src.layout.layout import LayoutInterface
from .pages.search.search import NovelSearch
from .pages.bookshelf.bookshelf import NovelBookshelf
from .pages.list.list import NovelList
from .pages.manager.manager import NovelManager
from .pages.detail.detail import NovelDetail
from .pages.content.content import NovelContent
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
        super().__init__(parent = parent)
        self.ui = Ui_Novel()
        self.ui.setupUi(self)
        self.setObjectName("NovelInterface")
        self.page_cache = {}
        self.initTopMenu()

        self.bookshelf = None
        self.list = None
        self.search = None
        self.manager = None
        self.detail = None
        self.content = None

        self.showPage(NovelPage.SEARCH)

    def initTopMenu(self):
        pivot = SegmentedWidget()
        pivot.addItem(routeKey='bookshelf', text="书架", onClick=lambda : self.showPage(NovelPage.BOOKSHELF))
        pivot.addItem(routeKey='list', text="浏览", onClick=lambda : self.showPage(NovelPage.LIST))
        pivot.addItem(routeKey='search', text="搜索", onClick=lambda : self.showPage(NovelPage.SEARCH))
        pivot.addItem(routeKey='manager', text="管理", onClick=lambda : self.showPage(NovelPage.MANAGER))
        pivot.addItem(routeKey='detail', text="详情", onClick=lambda : self.showPage(NovelPage.DETAIL))
        pivot.addItem(routeKey='content', text="阅读", onClick=lambda : self.showPage(NovelPage.CONTENT))
        pivot.setCurrentItem('search')
        self.ui.topMenuLayout.addWidget(pivot)

    def showPage(self, page: NovelPage):
        if page.value not in self.page_cache:
            if page == NovelPage.BOOKSHELF:
                self.bookshelf = NovelBookshelf(self.ui.stack)
                self.page_cache[page.value] = self.bookshelf
                self.ui.bookshelf_layout.addWidget(self.bookshelf)
            elif page == NovelPage.LIST:
                self.list = NovelList(self.ui.stack)
                self.page_cache[page.value] = self.list
                self.ui.list_layout.addWidget(self.list)
            elif page == NovelPage.SEARCH:
                self.search = NovelSearch(self.ui.stack)
                self.page_cache[page.value] = self.search
                self.ui.search_layout.addWidget(self.search)
            elif page == NovelPage.MANAGER:
                self.manager= NovelManager(self.ui.stack)
                self.page_cache[page.value] = self.manager
                self.ui.manager_layout.addWidget(self.manager)
            elif page == NovelPage.DETAIL:
                self.detail= NovelDetail(self.ui.stack)
                self.page_cache[page.value] = self.detail
                self.ui.detail_layout.addWidget(self.detail)
            elif page == NovelPage.CONTENT:
                self.content= NovelContent(self.ui.stack)
                self.page_cache[page.value] = self.content
                self.ui.content_layout.addWidget(self.content)

        self.ui.stack.setCurrentIndex(page.value)