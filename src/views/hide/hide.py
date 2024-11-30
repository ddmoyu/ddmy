#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
隐藏窗口、包含 Webview
通过 webview 获取页面 html 内容，并发送给主进程

Author: ddmoyu
Email: daydaymoyu@gmail.com
Date: 2024-11-30
"""

from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Slot
from src.common.signal_bus import signalBus, WebviewType
from src.views.hide.wv_widget import WebviewWidget


class HideWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.wv = WebviewWidget(debug=False)
        self.wv.on_load.connect(self.on_load)
        self.wv_type = WebviewType.URL

        self.layout().addWidget(self.wv)
        self.resize(1080, 720)

        signalBus.wv_url.connect(self.navigate)

    def on_load(self, location):
        self.wv.bind("loaded", self.on_loaded)
        self.wv.eval("""
                    window.addEventListener("load", (event) => {
                        let html = document.documentElement.outerHTML
                        window.loaded(html)
                    });
                """)

    def on_loaded(self, html):
        signalBus.wv_html.emit(self.wv_type, html)

    @Slot(str)
    def navigate(self, wv_type: WebviewType, url):
        self.wv_type = wv_type
        self.wv.navigate(url)
