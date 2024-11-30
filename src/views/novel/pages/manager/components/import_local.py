from qfluentwidgets import MessageBoxBase, SubtitleLabel, LineEdit, PushButton
from PySide6.QtWidgets import QHBoxLayout, QFileDialog


class ImportLocalMsgbox(MessageBoxBase):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.titleLabel = SubtitleLabel()
        self.titleLabel.setText("从本地导入书源")

        self.horizontalLayout = QHBoxLayout()

        self.lineEdit = LineEdit()
        self.lineEdit.setPlaceholderText("请选择书源 .json 文件")
        self.lineEdit.setClearButtonEnabled(True)

        self.selectButton = PushButton()
        self.selectButton.setText("选择")
        self.selectButton.clicked.connect(self.open_file_dialog)

        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.addWidget(self.selectButton)

        self.viewLayout.addWidget(self.titleLabel)
        self.viewLayout.addLayout(self.horizontalLayout)

        self.widget.setMinimumWidth(420)

    def open_file_dialog(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "选择书源文件", "", "JSON Files (*.json)"
        )
        if file_name:
            self.lineEdit.setText(file_name)
