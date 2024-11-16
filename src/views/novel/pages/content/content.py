import os, sys, ctypes
from .ui_content import Ui_NovelContent
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication, QMessageBox
from PySide6.QtGui import QFont, QResizeEvent
from PySide6.QtCore import Signal, Slot
from qasync import asyncSlot
# from PySide6.QtWebEngineCore import QWebEnginePage
from webviewpy import Webview, webview_native_handle_kind_t
from src.views.novel.utils.utils import parse_content
import asyncio

os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = '--ignore-certificate-errors'

class WebivewWidget(QWidget):
    html_ready = Signal(str)
    def __init__(self, parent=None, debug=False) -> None:
        super().__init__(parent)
        self.webview = Webview(debug=True, window=int(self.winId()))

        self.webview.bind("__on_load", self.on_load)
        self.webview.bind("get_html", self.get_html)
        self.webview.init("window.__on_load(window.location)")

    def get_html(self, html):
        print(html)
        QMessageBox.information(self, "title", "get html")
        self.html_ready.emit(html)

    def on_load(self, location):
        print(location)
        # QMessageBox.information(self, "title", "loaded content")
        self.webview.eval("""
            const html = document.body.innerHTML
            window.get_html(html)
        """)
        # QMessageBox.information(self, "title", "run eval")


    def __getattr__(self, name):
        return getattr(self.webview, (name))

class NovelContent(Ui_NovelContent, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.parent = parent
        self.setupUi(self)
        self.webview = WebivewWidget()
        self.wv_layout.addWidget(self.webview)
        self.pushButton_3.clicked.connect(self.test_scrapling)
        # self.wv = QWebEnginePage()
        # self.test_webengine()
        # self.test_scrapling()

    def test_scrapling(self):
        self.webview.navigate("https://www.zhongyi6.com/chapter/read/1734/36970")
        self.webview.html_ready.connect(self.render_content)

    @asyncSlot()
    async def test_webengine(self):
        print('test_webengine')
        # self.wv.load("https://www.zhongyi6.com/chapter/read/1734/36970")
        # self.wv.load('https://z.dlxk.com/read/4282/297130.html')
        # self.wv.load('https://www.yizhiqc.com/chapter/1266557#fromapp')
        # self.wv.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, ok):
        print('on_load_finished')
        print('ok')
        if ok:
            print('ok')
            # self.wv.toHtml(self.render_content)
        else:
            print('not ok')

    @Slot(str)
    def render_content(self, html):
        print(html)
        text = parse_content(html, '#body@html')
        # text = parse_content(html, 'p:nth-of-type(n+2)@text')
        # text = parse_content(html, '.rxx-badge@text')
        self.textBrowser.setMarkdown(text)
        font = QFont('霞鹜文楷', 16)
        self.textBrowser.setFont(font)

        # self.textBrowser.setStyleSheet("#textBrowser{}")


