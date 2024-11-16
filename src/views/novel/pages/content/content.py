import os
from .ui_content import Ui_NovelContent
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QFont
from qasync import asyncSlot
from PySide6.QtWebEngineCore import QWebEnginePage
from src.views.novel.utils.utils import parse_content

os.environ['QTWEBENGINE_CHROMIUM_FLAGS'] = '--ignore-certificate-errors'

class NovelContent(Ui_NovelContent, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent = parent)
        self.parent = parent
        self.setupUi(self)
        self.wv = QWebEnginePage()
        self.test_webengine()

    @asyncSlot()
    async def test_webengine(self):
        print('test_webengine')
        self.wv.load("https://www.zhongyi6.com/chapter/read/1734/36970")
        # self.wv.load('https://z.dlxk.com/read/4282/297130.html')
        # self.wv.load('https://www.yizhiqc.com/chapter/1266557#fromapp')
        self.wv.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, ok):
        print('on_load_finished')
        print('ok')
        if ok:
            self.wv.toHtml(self.render_content)
        else:
            print('not ok')

    def render_content(self, html):
        print(html)
        text = parse_content(html, '#body@html')
        # text = parse_content(html, 'p:nth-of-type(n+2)@text')
        # text = parse_content(html, '.rxx-badge@text')
        self.textBrowser.setMarkdown(text)
        font = QFont('霞鹜文楷', 16)
        self.textBrowser.setFont(font)

        # self.textBrowser.setStyleSheet("#textBrowser{}")


