import os
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QUrl, Qt
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

class NetworkImageViewer(QGraphicsView):
    def __init__(self, parent=None, cache_dir="image_cache"):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.network_manager = QNetworkAccessManager(self)
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)

    def load_image(self, image_path):
        # 判断是否为网络图片
        if image_path.startswith(('http://', 'https://')):
            self.load_network_image(image_path)
        else:
            # 处理本地图片（相对路径或绝对路径）
            self.load_local_image(image_path)

    def load_local_image(self, image_path):
        # 将相对路径转换为绝对路径
        abs_path = os.path.abspath(image_path)

        if os.path.exists(abs_path):
            pixmap = QPixmap(abs_path)
            self.display_image(pixmap)
        else:
            print(f"Local image not found: {abs_path}")

    def load_network_image(self, url):
        cache_path = os.path.join(self.cache_dir, url.split("/")[-1])

        if os.path.exists(cache_path):
            # 如果缓存存在,直接从缓存加载
            self.load_from_cache(cache_path)
        else:
            # 否则从网络下载
            request = QNetworkRequest(QUrl(url))
            reply = self.network_manager.get(request)
            reply.finished.connect(lambda: self.on_image_loaded(reply, cache_path))

    def load_from_cache(self, cache_path):
        pixmap = QPixmap(cache_path)
        self.display_image(pixmap)

    def on_image_loaded(self, reply, cache_path):
        if reply.error() == QNetworkReply.NetworkError.NoError:
            data = reply.readAll()
            pixmap = QPixmap()
            pixmap.loadFromData(data)

            # 保存到缓存
            pixmap.save(cache_path)

            self.display_image(pixmap)
        else:
            print(f"Error loading image: {reply.errorString()}")
        reply.deleteLater()

    def display_image(self, pixmap):
        self.scene.clear()
        self.scene.addPixmap(pixmap)
        self.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
