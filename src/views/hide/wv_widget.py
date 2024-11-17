from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Signal, Slot
from webviewpy import Webview, Webview_Version, webview_native_handle_kind_t

class AbstractWebview(QWidget):
    on_load = Signal(str)

    def navigate(self, url):
        pass

    def bind(self, fname, func):
        pass

    def eval(self, js):
        pass


class WebviewWidget(AbstractWebview):
    def __init__(self, parent=None, debug=True):
        super().__init__(parent)
        self.webview = None
        self.webview = Webview(debug, window=self.winId())
        self.webview.bind("__on_load", self._on_load)
        self.webview.init("""window.__on_load(window.location.href)""")

    def bind(self, fname, func):
        self.webview.bind(fname, func)

    def eval(self, js):
        self.webview.eval(js)

    def get_controller(self):
        return self.webview.get_native_handle(webview_native_handle_kind_t.WEBVIEW_NATIVE_HANDLE_KIND_BROWSER_CONTROLLER)

    def get_hwnd(self):
        return self.webview.get_native_handle(webview_native_handle_kind_t.WEBVIEW_NATIVE_HANDLE_KIND_UI_WIDGET)

    def _on_load(self, href):
        self.on_load.emit(href)

    def navigate(self, url):
        self.webview.navigate(url)