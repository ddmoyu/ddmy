import re
from qfluentwidgets import MessageBoxBase, SubtitleLabel, LineEdit
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QUrl

class ImportMsgbox(MessageBoxBase):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.titleLabel = SubtitleLabel('从网络上导入书源')
        self.urlLineEdit = LineEdit()

        self.urlLineEdit.setPlaceholderText('请输入书源的链接')
        self.urlLineEdit.setClearButtonEnabled(True)
        self.urlLineEdit.setFocus()

        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addWidget(self.urlLineEdit)

        self.widget.setMinimumWidth(420)
        self.paste_clipboard_url()

    def is_valid_url(self, url):
        regex = re.compile(
            r'^(http|https)://'
            r'.+\..+',
            re.IGNORECASE
        )
        return re.match(regex, url) is not None

    def paste_clipboard_url(self):
        clipboard = QApplication.clipboard()
        clipboard_text = clipboard.text().strip()
        if self.is_valid_url(clipboard_text):
            self.urlLineEdit.setText(clipboard_text)

