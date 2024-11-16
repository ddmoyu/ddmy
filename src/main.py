# -*- coding: utf-8 -*-

import os
import sys
# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
libs_dir = os.path.join(current_dir, "../libs")
os.environ["PATH"] = os.path.abspath(libs_dir) + os.pathsep + os.environ.get("PATH", "")

import asyncio
from PySide6.QtWidgets import QApplication
from views.view import MainWindow
from qfluentwidgets import setTheme, Theme
from qasync import QEventLoop

if __name__ == '__main__':
    setTheme(Theme.DARK)
    app = QApplication(sys.argv)

    event_loop = QEventLoop(app)
    asyncio.set_event_loop(event_loop)

    app_close_event = asyncio.Event()
    app.aboutToQuit.connect(app_close_event.set)

    w = MainWindow()
    w.show()

    event_loop.run_until_complete(app_close_event.wait())
    event_loop.close()
    # app.exec()