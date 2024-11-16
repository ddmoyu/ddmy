import asyncio

from .ui_manager import Ui_NovelManager
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QTableWidget, QHeaderView
from qfluentwidgets import InfoBar, InfoBarPosition
from src.views.novel.utils.utils import load_json
from qasync import Slot
from .components.importInternet import ImportMsgbox
from src.views.novel.utils.utils import fetch_book_sources

class NovelManager(Ui_NovelManager, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.parent = parent
        self.setupUi(self)

        self.init_ui()
        self.init_signal()
        self.init_data()

    def init_ui(self):
        headers = ["名字", "分组", "地址", "状态"]
        self.table_sources.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_sources.setColumnCount(len(headers))
        self.table_sources.verticalHeader().hide()
        self.table_sources.setHorizontalHeaderLabels(headers)
        self.table_sources.setSelectRightClickedRow(True)

    def init_signal(self):
        self.btn_import_sources_internet.clicked.connect(self.on_import_from_internet)

    def init_data(self):
        self.render_sources_table()


    def render_sources_table(self):
        self.table_sources.clearContents()
        sources = load_json("novel_sources.json")
        if not sources:
            return

        self.table_sources.setRowCount(len(sources))
        for row, source in enumerate(sources):
            self.table_sources.setItem(row, 0, QTableWidgetItem(source["bookSourceName"]))
            group = source.get("bookSourceGroup", "未分组")
            self.table_sources.setItem(row, 1, QTableWidgetItem(group))
            self.table_sources.setItem(row, 2, QTableWidgetItem(source["bookSourceUrl"]))
            status = "启用" if source.get("enabled", False) else "禁用"
            self.table_sources.setItem(row, 3, QTableWidgetItem(status))
        self.table_sources.resizeColumnsToContents()


    def on_import_from_internet(self):
        asyncio.create_task(self.import_feeds_internet())

    @Slot()
    async def import_feeds_internet(self):
        w = ImportMsgbox(self)
        if w.exec():
            url = w.urlLineEdit.text()
            if not url:
                InfoBar.info("", "请输入正确的链接", parent=self, position=InfoBarPosition.BOTTOM)
                return
            InfoBar.info("", "正在导入...", parent=self, position=InfoBarPosition.BOTTOM)
            list = await fetch_book_sources(url, True)
            if not list:
                InfoBar.error("", "没有找到任何资源", parent=self, position=InfoBarPosition.BOTTOM)
                return
            InfoBar.success("", "导入成功, 共{}个".format(len(list)), parent=self, position=InfoBarPosition.BOTTOM)
            self.render_sources_table()

