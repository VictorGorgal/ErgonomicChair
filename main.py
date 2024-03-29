from PyQt6.QtCore import QPropertyAnimation
from UI.UI_base import Ui_MainWindow
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from winotify import Notification
from winotify.audio import Reminder
from MQTT_SQL.interface import Interface


def generateDailyFrame(color, size):
    if color == (48, 48, 48):
        size -= 5

    policy = qtw.QSizePolicy(qtw.QSizePolicy.Policy.Expanding, qtw.QSizePolicy.Policy.Fixed)
    policy.setHorizontalStretch(size)

    frame = qtw.QPushButton()
    frame.setStyleSheet(f'background-color: rgb{color};\nborder-radius: 10px;')
    frame.setMaximumHeight(20)
    frame.setSizePolicy(policy)

    return frame


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.GREEN = (46, 255, 63)
        self.RED = (255, 46, 46)
        self.GRAY = (48, 48, 48)

        self.notify = Notification(app_id='Cadeira',
                                   title='Title',
                                   msg='Message',
                                   duration='short')
        self.notify.set_audio(Reminder, loop=False)

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

        self.interface = Interface()
        self.updateHome()

        self.checkThreadTimer = qtc.QTimer()
        self.checkThreadTimer.timeout.connect(self.update_measurement)
        self.checkThreadTimer.start(500)

    def home_btn_func(self):
        self.page_widgets.setCurrentWidget(self.home_page)
        self.highlight_button()
        self.updateHome()

    def graphs_btn_func(self):
        self.page_widgets.setCurrentWidget(self.graph_page)
        self.highlight_button()

        self.render_graph()  # refresh graph

    def connect_btn_func(self):
        self.page_widgets.setCurrentWidget(self.connection_page)
        self.highlight_button()

    def config_btn_func(self):
        self.page_widgets.setCurrentWidget(self.config_page)
        self.highlight_button()

    def notification_btn_func(self):
        self.notify.show()

    def updateHome(self):
        self.createDailyProgressBar()
        percentage = self.interface.get_percentage()

        self.daily_ok.setText(f'{percentage} %')
        self.daily_wrong.setText(f'{100 - percentage} %')

    def createDailyProgressBar(self):
        # Clears progress bar
        for i in reversed(range(self.daily_layout.count())):
            self.daily_layout.itemAt(i).widget().setParent(None)

        # Gets info from database interface
        frames = self.interface.get_daily_list()
        total_minutes = 0

        for idx, frame in enumerate(frames):
            # Gets color
            if frame[0] == self.interface.GOOD:
                color = self.GREEN
            elif frame[0] == self.interface.BAD:
                color = self.RED
            else:
                color = self.GRAY

            total_minutes += frame[1]

            # Adds frame to progress bar
            button = generateDailyFrame(color, frame[1])
            if idx == 0:
                button.clicked.connect(lambda: self.update_bar_labels("00:00", "10:09"))
            elif idx == 1:
                button.clicked.connect(lambda: self.update_bar_labels("10:09", "10:39"))
            elif idx == 2:
                button.clicked.connect(lambda: self.update_bar_labels("10:39", "11:21"))
            elif idx == 3:
                button.clicked.connect(lambda: self.update_bar_labels("11:21", "12:04"))
            elif idx == 4:
                button.clicked.connect(lambda: self.update_bar_labels("12:04", "14:42"))
            elif idx == 5:
                button.clicked.connect(lambda: self.update_bar_labels("14:42", "15:24"))
            elif idx == 6:
                button.clicked.connect(lambda: self.update_bar_labels("15:24", "15:50"))
            elif idx == 7:
                button.clicked.connect(lambda: self.update_bar_labels("15:50", "16:09"))
            elif idx == 8:
                button.clicked.connect(lambda: self.update_bar_labels("16:09", "16:36"))
            elif idx == 9:
                button.clicked.connect(lambda: self.update_bar_labels("16:36", "16:54"))
            elif idx == 10:
                button.clicked.connect(lambda: self.update_bar_labels("16:54", "23:59"))
            self.daily_layout.addWidget(button)

    def update_bar_labels(self, startTime, endTime):
        self.start_label.setText(startTime)
        self.end_label.setText(endTime)

    def render_graph(self):
        print('rendering')
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        if hasattr(self, 'graphWidget'):
            self.graphWidget.close()

        self.graphWidget = pg.PlotWidget()  # create graph widget
        self.verticalLayout_8.addWidget(self.graphWidget)
        self.graphWidget.plot(hour, temperature, pen=pg.mkPen(color=(255, 255, 255)))
        self.graphWidget.setBackground((24, 24, 26))  # change background
        self.graphWidget.setLabel('left', '% DO DIA COM POSTURA BOA')
        self.graphWidget.setLabel('bottom', 'DIA DO MES')

    def update_measurement(self):
        text = self.interface.get_real_time()
        sensors = text.split(';')

        correct = sensors.count('1')
        if correct >= 7:
            self.real_time.setText('Correta!')
            self.real_time.setStyleSheet('color: rgb(255, 255, 255);\n'
                                         'background-color: rgb(46, 255, 63);\n'
                                         'border-radius: 10px;')
        else:
            self.real_time.setText('Errada!')
            self.real_time.setStyleSheet('color: rgb(255, 255, 255);\n'
                                         'background-color: rgb(255, 46, 46);\n'
                                         'border-radius: 10px;')

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
