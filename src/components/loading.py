from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QMovie


class LoadingOverlay(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置透明背景
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 设置无边框窗口,始终置顶
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        # 创建布局
        layout = QVBoxLayout(self)

        # 创建标签显示动画
        self.label = QLabel()
        layout.addWidget(self.label, alignment=Qt.AlignCenter)

        # 创建 QMovie 对象
        self.movie = QMovie("src/resource/images/loading.webp")  # 替换为你的动图路径
        self.movie.setScaledSize(QSize(100, 100))  # 设置大小
        self.label.setMovie(self.movie)

        self.hide()  # 初始状态隐藏

    def showEvent(self, event):
        """显示时调整大小以覆盖父组件"""
        if self.parent():
            self.setGeometry(self.parent().rect())
        super().showEvent(event)

    def show_loading(self):
        """显示加载动画"""
        self.show()
        self.movie.start()

    def hide_loading(self):
        """隐藏加载动画"""
        self.movie.stop()
        self.hide()
