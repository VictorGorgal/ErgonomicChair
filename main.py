from PyQt6.QtCore import QPropertyAnimation
from UI.UI_base import Ui_MainWindow
from PyQt6 import QtWidgets as qtw
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from threading import Thread
from win10toast import ToastNotifier


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.toaster = ToastNotifier()
        self.thread = None
        self.page_widgets.setCurrentWidget(self.home_page)  # starts on home page
        self.slide_menu.setMaximumWidth(0)

        self.btn_menu.clicked.connect(lambda: self.toggleMenu(48))  # slide menu

        self.btn_home.clicked.connect(self.home_btn_func)  # side buttons
        self.btn_graphs.clicked.connect(self.graphs_btn_func)
        self.btn_connect.clicked.connect(self.connect_btn_func)
        self.btn_config.clicked.connect(self.config_btn_func)

        self.btn_notification.clicked.connect(self.notification_btn_func)

        self.highlight_button()

        pg.setConfigOptions(antialias=True)  # anti-aliasing
        self.create_graph()

    def home_btn_func(self):
        self.page_widgets.setCurrentWidget(self.home_page)
        self.highlight_button()

    def graphs_btn_func(self):
        self.page_widgets.setCurrentWidget(self.graph_page)
        self.highlight_button()

    def connect_btn_func(self):
        self.page_widgets.setCurrentWidget(self.connection_page)
        self.highlight_button()

    def config_btn_func(self):
        self.page_widgets.setCurrentWidget(self.config_page)
        self.highlight_button()

    def notification_btn_func(self):
        if isinstance(self.thread, Thread):
            if self.thread.is_alive():
                return

        self.thread = Thread(target=self.notification, args=['titulo', 'mensagem', 3])
        self.thread.start()

    def create_graph(self):
        print('aa')
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        self.graphWidget = pg.PlotWidget()  # create graph widget
        self.verticalLayout_8.addWidget(self.graphWidget)
        self.graphWidget.plot(hour, temperature, pen=pg.mkPen(color=(255, 255, 255)))
        self.graphWidget.setBackground((24, 24, 29))  # change background

    def notification(self, title, message, duration):
        self.toaster.show_toast(title, message, duration=duration)

    def highlight_button(self):
        self.btn_home.setAutoFillBackground(False)
        self.btn_graphs.setAutoFillBackground(False)
        self.btn_connect.setAutoFillBackground(False)
        self.btn_config.setAutoFillBackground(False)

        page = self.page_widgets.currentWidget().objectName()
        if page == 'home_page':
            self.btn_home.setAutoFillBackground(True)
        if page == 'graph_page':
            self.btn_graphs.setAutoFillBackground(True)
        if page == 'connection_page':
            self.btn_connect.setAutoFillBackground(True)
        if page == 'config_page':
            self.btn_config.setAutoFillBackground(True)

    def toggleMenu(self, maxWidth):
        width = self.slide_menu.width()
        standard = 0  # minimum width
        widthExtended = standard

        if width == standard:
            widthExtended = maxWidth

        # ANIMATION
        self.animation = QPropertyAnimation(self.slide_menu, b"maximumWidth")
        self.animation.setDuration(150)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.start()

        self.highlight_button()


if __name__ == '__main__':
    import sys

    app = qtw.QApplication([])

    MainWindow = MainWindow()
    MainWindow.show()

    sys.exit(app.exec())
