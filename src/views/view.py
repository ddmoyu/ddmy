# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

from qfluentwidgets import (
    FluentWindow,
    SystemThemeListener,
    NavigationItemPosition,
    SplashScreen,
)
from qfluentwidgets import FluentIcon

from src.views.home.home import HomeInterface
from src.views.novel.novel import NovelInterface
from src.views.photo.photo import PhotoInterface
from src.views.video.video import VideoInterface
from src.views.live.live import LiveInterface
from src.views.download.download import DownloadInterface
from src.views.settings.settings import SettingsInterface

from src.layout.layout import LayoutInterface
from src.common.signal_bus import signalBus


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.splashScreen = SplashScreen("")
        self.init_window()
        self.themeListener = SystemThemeListener(self)

        self.homeInterface = HomeInterface(self)
        self.novelInterface = NovelInterface(self)
        self.photoInterface = PhotoInterface(self)
        self.videoInterface = VideoInterface(self)
        self.liveInterface = LiveInterface(self)
        self.downloadInterface = DownloadInterface(self)
        self.settingsInterface = SettingsInterface(self)

        self.connect_signal_to_slot()

        self.init_navigation()

        self.splashScreen.finish()

        self.themeListener.start()

    def init_window(self):
        self.resize(1124, 720)
        self.setWindowIcon(QIcon(":/images/logo.png"))
        self.setWindowTitle("home")

        self.splashScreen = SplashScreen(self.windowIcon(), self)
        self.splashScreen.setIconSize(QSize(106, 106))
        self.splashScreen.raise_()

        # desktop = QApplication.primaryScreen().availableGeometry()
        # w, h = desktop.width(), desktop.height()
        # self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)
        self.show()
        QApplication.processEvents()

    def connect_signal_to_slot(self):
        signalBus.switchToSampleCard.connect(self.switch_to_sample)

    def init_navigation(self):
        self.addSubInterface(
            self.homeInterface,
            FluentIcon.HOME,
            self.tr("Home"),
            position=NavigationItemPosition.TOP,
        )
        self.addSubInterface(
            self.novelInterface,
            FluentIcon.BOOK_SHELF,
            "Novel",
            position=NavigationItemPosition.SCROLL,
        )
        self.addSubInterface(
            self.photoInterface,
            FluentIcon.PHOTO,
            "Photo",
            position=NavigationItemPosition.SCROLL,
        )
        self.addSubInterface(
            self.videoInterface,
            FluentIcon.VIDEO,
            "Video",
            position=NavigationItemPosition.SCROLL,
        )
        self.addSubInterface(
            self.liveInterface,
            FluentIcon.PLAY,
            "Live",
            position=NavigationItemPosition.SCROLL,
        )
        self.addSubInterface(
            self.downloadInterface,
            FluentIcon.DOWNLOAD,
            "Download",
            position=NavigationItemPosition.SCROLL,
        )
        self.addSubInterface(
            self.settingsInterface,
            FluentIcon.SETTING,
            "Settings",
            position=NavigationItemPosition.BOTTOM,
        )

    def closeEvent(self, e):
        self.themeListener.terminate()
        self.themeListener.deleteLater()
        super().closeEvent(e)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        if hasattr(self, "splashScreen"):
            self.splashScreen.resize(self.size())

    def switch_to_sample(self, route_key):
        interfaces = self.findChildren(LayoutInterface)
        for w in interfaces:
            if w.objectName() == route_key:
                self.stackedWidget.setCurrentWidget(w, False)
