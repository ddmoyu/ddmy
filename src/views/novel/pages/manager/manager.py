import os
import asyncio
from datetime import datetime
from .ui_manager import Ui_NovelManager
from PySide6.QtWidgets import (
    QWidget,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,
    QHBoxLayout,
)
from PySide6.QtCore import Qt, QPoint
from qfluentwidgets import (
    InfoBar,
    InfoBarPosition,
    RoundMenu,
    Action,
    MenuAnimationType,
    SwitchButton,
)
from src.common.tools import load_json
from qasync import Slot
from src.views.novel.utils.u_manager import fetch_book_sources
from src.views.novel.pages.manager.components.import_network import ImportNetworkMsgbox
from src.views.novel.pages.manager.components.import_local import ImportLocalMsgbox
from src.views.novel.utils.u_manager import import_local_source, merge_sources


class NovelManager(Ui_NovelManager, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setupUi(self)
        self.init_ui()
        self.init_signal()
        self.init_data()

    def init_ui(self):
        self.progressBar.hide()

        headers = ["名称", "分组", "链接", "更新时间", "备注", "状态"]
        self.table_sources.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.table_sources.setColumnCount(len(headers))
        self.table_sources.verticalHeader().hide()
        self.table_sources.setHorizontalHeaderLabels(headers)
        self.table_sources.setSelectRightClickedRow(True)
        self.table_sources.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_sources.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table_sources.customContextMenuRequested.connect(self.show_context_menu)
        self.table_sources.horizontalHeader().setSectionResizeMode(
            3, QHeaderView.ResizeMode.Fixed
        )
        self.table_sources.setColumnWidth(3, 145)
        self.table_sources.horizontalHeader().setSectionResizeMode(
            5, QHeaderView.ResizeMode.Fixed
        )
        self.table_sources.setColumnWidth(5, 100)

    def init_signal(self):
        self.btn_import_sources_internet.clicked.connect(self.on_import_from_internet)
        self.btn_import_sources_local.clicked.connect(self.on_import_from_local)
        # self.btn_import_sources_local.clicked.connect(self.show_context_menu)

    def init_data(self):
        self.render_sources_table()

    def show_context_menu(self, pos):
        menu = RoundMenu()
        modify_action = Action("修改", self)
        delete_action = Action("删除", self)
        modify_action.triggered.connect(self.modify_item)
        delete_action.triggered.connect(self.delete_item)
        menu.addAction(modify_action)
        menu.addAction(delete_action)
        pos = QPoint(pos)
        x = pos.x()
        y = pos.y() + 100
        menu.exec_(self.mapToGlobal(QPoint(x, y)), aniType=MenuAnimationType.PULL_UP)

    def toggle_item(self, checked):
        print("toggle item")

    def delete_item(self):
        print("delete item")
        row = self.table_sources.currentRow()
        name = self.table_sources.item(row, 0).text()
        print(name)

    def modify_item(self):
        print("modify item")

    def render_sources_table(self):
        self.table_sources.clearContents()
        sources = load_json("novel_sources.json")
        self.lb_total.setText("共 " + str(len(sources)) + " 条数据")
        if not sources:
            return

        self.table_sources.setRowCount(len(sources))
        for row, source in enumerate(sources):
            self.table_sources.setItem(
                row, 0, QTableWidgetItem(source["bookSourceName"])
            )

            group = source.get("bookSourceGroup", "无")
            self.table_sources.setItem(row, 1, QTableWidgetItem(group))

            url = source.get("bookSourceUrl", "无")
            url_item = QTableWidgetItem(url)
            url_item.setToolTip(url)
            self.table_sources.setItem(row, 2, url_item)

            last_update_time = source.get("lastUpdateTime", 0)
            timestamp_s = float(last_update_time) / 1000.0
            dt_object = datetime.fromtimestamp(timestamp_s)
            formatted_time = dt_object.strftime("%Y-%m-%d %H:%M")
            self.table_sources.setItem(row, 3, QTableWidgetItem(formatted_time))

            comment = source.get("bookSourceComment", "")
            comment_item = QTableWidgetItem(comment)
            comment_item.setToolTip(comment)
            self.table_sources.setItem(row, 4, comment_item)

            switch = SwitchButton()
            switch.setChecked(source.get("enabled", False))
            switch.checkedChanged.connect(self.toggle_item)
            container = QWidget()
            layout = QHBoxLayout(container)
            layout.addWidget(switch)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            container.setLayout(layout)
            self.table_sources.setCellWidget(row, 5, container)

    def on_import_from_internet(self):
        asyncio.create_task(self.import_feeds_internet())

    def on_import_from_local(self):
        w = ImportLocalMsgbox(self)
        if w.exec():
            filepath = w.lineEdit.text()
            if not os.path.exists(filepath):
                InfoBar.error(
                    "", "文件不存在", parent=self, position=InfoBarPosition.BOTTOM
                )
                return
            InfoBar.info(
                "", "正在导入...", parent=self, position=InfoBarPosition.BOTTOM
            )
            source_list = import_local_source(filepath)
            if not source_list:
                InfoBar.error(
                    "", "没有找到任何资源", parent=self, position=InfoBarPosition.BOTTOM
                )
                return
            else:
                source_list = merge_sources(source_list)
                InfoBar.success(
                    "",
                    "导入成功, 共{}个".format(len(source_list)),
                    parent=self,
                    position=InfoBarPosition.BOTTOM,
                )
            self.render_sources_table()

    @Slot()
    async def import_feeds_internet(self):
        w = ImportNetworkMsgbox(self)
        if w.exec():
            url = w.urlLineEdit.text()
            if not url:
                InfoBar.info(
                    "", "请输入正确的链接", parent=self, position=InfoBarPosition.BOTTOM
                )
                return
            InfoBar.info(
                "", "正在导入...", parent=self, position=InfoBarPosition.BOTTOM
            )
            source_list = await fetch_book_sources(url, True)
            if not source_list:
                InfoBar.error(
                    "", "没有找到任何资源", parent=self, position=InfoBarPosition.BOTTOM
                )
                return
            else:
                InfoBar.success(
                    "",
                    "导入成功, 共{}个".format(len(source_list)),
                    parent=self,
                    position=InfoBarPosition.BOTTOM,
                )
            self.render_sources_table()
