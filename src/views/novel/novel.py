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
from PySide6.QtCore import Qt

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
        self.page_cache = {}
        self.setObjectName("NovelInterface")
        self.initTopMenu()

        self.bookshelf = None
        self.list = None
        self.search = None
        self.manager = None
        self.detail = None
        self.content = None

        # self.showPage(NovelPage.SEARCH)
        self.search = NovelSearch(self.ui.stack)
        # self.ui.stack.setCurrentWidget(self.search)
        self.ui.stack.setCurrentIndex(NovelPage.SEARCH.value)

    def initTopMenu(self):
        pivot = SegmentedWidget()
        pivot.addItem(routeKey='bookshelf', text="书架", onClick=lambda : self.showPage(NovelPage.BOOKSHELF))
        pivot.addItem(routeKey='list', text="列表", onClick=lambda : self.showPage(NovelPage.LIST))
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
                self.ui.stack.addWidget(self.bookshelf)
            elif page == NovelPage.LIST:
                self.list = NovelList(self.ui.stack)
                self.page_cache[page.value] = self.list
                self.ui.stack.addWidget(self.list)
            elif page == NovelPage.SEARCH:
                self.search = NovelSearch(self.ui.stack)
                self.page_cache[page.value] = self.search
                self.ui.stack.addWidget(self.search)
            elif page == NovelPage.MANAGER:
                self.manager= NovelManager(self.ui.stack)
                self.page_cache[page.value] = self.manager
                self.ui.stack.addWidget(self.manager)
            elif page == NovelPage.DETAIL:
                self.detail= NovelDetail(self.ui.stack)
                self.page_cache[page.value] = self.detail
                self.ui.stack.addWidget(self.detail)
            elif page == NovelPage.CONTENT:
                self.content= NovelContent(self.ui.stack)
                self.page_cache[page.value] = self.content
                self.ui.stack.addWidget(self.content)

        print(self.page_cache)
        print(page.value)
        self.ui.stack.setCurrentIndex(page.value)
        print(self.ui.stack.currentIndex())


    def showEvent(self, event):
        super().showEvent(event)


    def resizeEvent(self, event):
        super().resizeEvent(event)
        current_wgt = self.ui.stack.currentWidget()
        if current_wgt.objectName() == 'search':
            self.search.resize(self.ui.stack.size())
        elif current_wgt.objectName() == 'bookshelf':
            self.bookshelf.resize(self.ui.stack.size())
        elif current_wgt.objectName() == 'list':
            self.list.resize(self.ui.stack.size())
        elif current_wgt.objectName() == 'manager':
            self.manager.resize(self.ui.stack.size())
        elif current_wgt.objectName() == 'detail':
            self.detail.resize(self.ui.stack.size())
        elif current_wgt.objectName() == 'content':
            self.content.resize(self.ui.stack.size())