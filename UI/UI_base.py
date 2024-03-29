# Form implementation generated from reading ui file 'UI_base.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setStyleSheet("background-color: rgb(24,24,26);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 32))
        self.top_bar.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.top_bar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.top_bar.setLineWidth(0)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toggle_menu = QtWidgets.QFrame(self.top_bar)
        self.toggle_menu.setMaximumSize(QtCore.QSize(70, 32))
        self.toggle_menu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.toggle_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.toggle_menu.setLineWidth(0)
        self.toggle_menu.setObjectName("toggle_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.toggle_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_menu = QtWidgets.QPushButton(self.toggle_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setMinimumSize(QtCore.QSize(45, 0))
        self.btn_menu.setMaximumSize(QtCore.QSize(45, 32))
        self.btn_menu.setStyleSheet("QPushButton:pressed {\n"
"    border-style: inset;\n"
"}")
        self.btn_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/menu-b.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QtCore.QSize(32, 32))
        self.btn_menu.setAutoDefault(False)
        self.btn_menu.setDefault(False)
        self.btn_menu.setFlat(True)
        self.btn_menu.setObjectName("btn_menu")
        self.verticalLayout_2.addWidget(self.btn_menu)
        self.horizontalLayout.addWidget(self.toggle_menu)
        self.frame = QtWidgets.QFrame(self.top_bar)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 32))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.content.setLineWidth(0)
        self.content.setObjectName("content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.slide_menu = QtWidgets.QFrame(self.content)
        self.slide_menu.setMinimumSize(QtCore.QSize(0, 300))
        self.slide_menu.setMaximumSize(QtCore.QSize(48, 1000))
        self.slide_menu.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.slide_menu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.slide_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.slide_menu.setLineWidth(0)
        self.slide_menu.setObjectName("slide_menu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.slide_menu)
        self.horizontalLayout_4.setContentsMargins(0, 0, 2, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.icons_frame = QtWidgets.QFrame(self.slide_menu)
        self.icons_frame.setMinimumSize(QtCore.QSize(0, 300))
        self.icons_frame.setMaximumSize(QtCore.QSize(46, 1000))
        self.icons_frame.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.icons_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.icons_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.icons_frame.setLineWidth(0)
        self.icons_frame.setObjectName("icons_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.icons_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_home = QtWidgets.QPushButton(self.icons_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_home.setAutoFillBackground(False)
        self.btn_home.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border-style: inset;\n"
"}")
        self.btn_home.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/c1-b4.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_home.setIcon(icon1)
        self.btn_home.setIconSize(QtCore.QSize(32, 32))
        self.btn_home.setCheckable(False)
        self.btn_home.setChecked(False)
        self.btn_home.setAutoDefault(False)
        self.btn_home.setDefault(False)
        self.btn_home.setFlat(True)
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout_4.addWidget(self.btn_home)
        self.btn_graphs = QtWidgets.QPushButton(self.icons_frame)
        self.btn_graphs.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_graphs.sizePolicy().hasHeightForWidth())
        self.btn_graphs.setSizePolicy(sizePolicy)
        self.btn_graphs.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_graphs.setAutoFillBackground(False)
        self.btn_graphs.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border-style: inset;\n"
"}")
        self.btn_graphs.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/c2-b1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_graphs.setIcon(icon2)
        self.btn_graphs.setIconSize(QtCore.QSize(32, 32))
        self.btn_graphs.setFlat(True)
        self.btn_graphs.setObjectName("btn_graphs")
        self.verticalLayout_4.addWidget(self.btn_graphs)
        self.btn_connect = QtWidgets.QPushButton(self.icons_frame)
        self.btn_connect.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_connect.sizePolicy().hasHeightForWidth())
        self.btn_connect.setSizePolicy(sizePolicy)
        self.btn_connect.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_connect.setAutoFillBackground(False)
        self.btn_connect.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border-style: inset;\n"
"}")
        self.btn_connect.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/c3-b1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_connect.setIcon(icon3)
        self.btn_connect.setIconSize(QtCore.QSize(32, 32))
        self.btn_connect.setFlat(True)
        self.btn_connect.setObjectName("btn_connect")
        self.verticalLayout_4.addWidget(self.btn_connect)
        self.btn_config = QtWidgets.QPushButton(self.icons_frame)
        self.btn_config.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_config.sizePolicy().hasHeightForWidth())
        self.btn_config.setSizePolicy(sizePolicy)
        self.btn_config.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_config.setAutoFillBackground(False)
        self.btn_config.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border-style: inset;\n"
"}")
        self.btn_config.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/c4-b1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_config.setIcon(icon4)
        self.btn_config.setIconSize(QtCore.QSize(32, 32))
        self.btn_config.setFlat(True)
        self.btn_config.setObjectName("btn_config")
        self.verticalLayout_4.addWidget(self.btn_config)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4.addWidget(self.icons_frame)
        self.horizontalLayout_2.addWidget(self.slide_menu)
        self.frame_3 = QtWidgets.QFrame(self.content)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 2))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 2))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3.addWidget(self.frame_2)
        self.page_widgets = QtWidgets.QStackedWidget(self.frame_3)
        self.page_widgets.setEnabled(True)
        self.page_widgets.setAutoFillBackground(False)
        self.page_widgets.setLineWidth(0)
        self.page_widgets.setObjectName("page_widgets")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.home_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.daily_progress = QtWidgets.QFrame(self.home_page)
        self.daily_progress.setMinimumSize(QtCore.QSize(0, 20))
        self.daily_progress.setMaximumSize(QtCore.QSize(16777215, 20))
        self.daily_progress.setStyleSheet("background-color: rgb(48, 48, 48);\n"
"border-radius: 10px;")
        self.daily_progress.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.daily_progress.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.daily_progress.setLineWidth(0)
        self.daily_progress.setObjectName("daily_progress")
        self.daily_layout = QtWidgets.QHBoxLayout(self.daily_progress)
        self.daily_layout.setContentsMargins(0, 0, 0, 0)
        self.daily_layout.setSpacing(0)
        self.daily_layout.setObjectName("daily_layout")
        self.verticalLayout_5.addWidget(self.daily_progress)
        self.frame_4 = QtWidgets.QFrame(self.home_page)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_4.setLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_6.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_6.setAutoFillBackground(False)
        self.frame_6.setStyleSheet("background-color: rgb(26, 26, 29);\n"
"border-radius: 10px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_9.setLineWidth(0)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(172, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.daily_ok = QtWidgets.QLabel(self.frame_9)
        self.daily_ok.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.daily_ok.setFont(font)
        self.daily_ok.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 255, 63);\n"
"border-radius: 10px;")
        self.daily_ok.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.daily_ok.setObjectName("daily_ok")
        self.horizontalLayout_5.addWidget(self.daily_ok)
        spacerItem2 = QtWidgets.QSpacerItem(172, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.frame_6)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_10.setLineWidth(0)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(172, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.daily_wrong = QtWidgets.QLabel(self.frame_10)
        self.daily_wrong.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.daily_wrong.setFont(font)
        self.daily_wrong.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 46, 46);\n"
"border-radius: 10px;")
        self.daily_wrong.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.daily_wrong.setObjectName("daily_wrong")
        self.horizontalLayout_6.addWidget(self.daily_wrong)
        spacerItem4 = QtWidgets.QSpacerItem(172, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_6.addWidget(self.frame_10)
        spacerItem5 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_6.addItem(spacerItem5)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_6.addWidget(self.label_4)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.real_time = QtWidgets.QLabel(self.frame_6)
        self.real_time.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.real_time.setFont(font)
        self.real_time.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 46, 46);\n"
"border-radius: 10px;")
        self.real_time.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.real_time.setObjectName("real_time")
        self.horizontalLayout_9.addWidget(self.real_time)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        spacerItem8 = QtWidgets.QSpacerItem(20, 75, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_6.addItem(spacerItem8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 20, 25, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        self.start_label = QtWidgets.QLabel(self.frame_6)
        self.start_label.setMinimumSize(QtCore.QSize(200, 40))
        self.start_label.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.start_label.setFont(font)
        self.start_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-radius: 10px;")
        self.start_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.start_label.setObjectName("start_label")
        self.horizontalLayout_10.addWidget(self.start_label)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(-1, 20, 25, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.end_label = QtWidgets.QLabel(self.frame_6)
        self.end_label.setMinimumSize(QtCore.QSize(200, 40))
        self.end_label.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.end_label.setFont(font)
        self.end_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 36, 36);\n"
"border-radius: 10px;")
        self.end_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.end_label.setObjectName("end_label")
        self.horizontalLayout_11.addWidget(self.end_label)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem9)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.page_widgets.addWidget(self.home_page)
        self.graph_page = QtWidgets.QWidget()
        self.graph_page.setObjectName("graph_page")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.graph_page)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_7 = QtWidgets.QFrame(self.graph_page)
        self.frame_7.setMinimumSize(QtCore.QSize(860, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_7.setLineWidth(0)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem10 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout_7.addItem(spacerItem10)
        self.graph_frame = QtWidgets.QFrame(self.frame_7)
        self.graph_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.graph_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.graph_frame.setObjectName("graph_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.graph_frame)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.graph_frame)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setLineWidth(0)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.verticalLayout_7.addWidget(self.graph_frame)
        self.horizontalLayout_7.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.graph_page)
        self.frame_8.setMinimumSize(QtCore.QSize(350, 0))
        self.frame_8.setMaximumSize(QtCore.QSize(350, 16777215))
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_8.setLineWidth(0)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem11 = QtWidgets.QSpacerItem(22, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_11.setMaximumSize(QtCore.QSize(16777215, 300))
        self.frame_11.setStyleSheet("background-color: rgb(26, 26, 29);\n"
"border-radius: 10px;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_11.setLineWidth(0)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_8.addWidget(self.frame_11)
        spacerItem12 = QtWidgets.QSpacerItem(22, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.horizontalLayout_7.addWidget(self.frame_8)
        self.page_widgets.addWidget(self.graph_page)
        self.connection_page = QtWidgets.QWidget()
        self.connection_page.setObjectName("connection_page")
        self.label_3 = QtWidgets.QLabel(self.connection_page)
        self.label_3.setGeometry(QtCore.QRect(670, 290, 211, 71))
        self.label_3.setObjectName("label_3")
        self.page_widgets.addWidget(self.connection_page)
        self.config_page = QtWidgets.QWidget()
        self.config_page.setObjectName("config_page")
        self.btn_notification = QtWidgets.QPushButton(self.config_page)
        self.btn_notification.setGeometry(QtCore.QRect(30, 20, 131, 41))
        self.btn_notification.setAutoFillBackground(False)
        self.btn_notification.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border-radius:10px;    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(55, 55, 55);\n"
"    border-style: inset;\n"
"    border-radius:10px;    \n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.btn_notification.setFlat(True)
        self.btn_notification.setObjectName("btn_notification")
        self.page_widgets.addWidget(self.config_page)
        self.verticalLayout_3.addWidget(self.page_widgets)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.page_widgets.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadeira"))
        self.label.setText(_translate("MainWindow", "Análise diária:"))
        self.daily_ok.setText(_translate("MainWindow", "- %"))
        self.daily_wrong.setText(_translate("MainWindow", "- %"))
        self.label_4.setText(_translate("MainWindow", "Postura atual:"))
        self.real_time.setText(_translate("MainWindow", "----"))
        self.label_5.setText(_translate("MainWindow", "Início do período:"))
        self.start_label.setText(_translate("MainWindow", "---"))
        self.label_7.setText(_translate("MainWindow", "Fim do período:"))
        self.end_label.setText(_translate("MainWindow", "---"))
        self.label_2.setText(_translate("MainWindow", "Seu progresso:"))
        self.label_3.setText(_translate("MainWindow", "Connections"))
        self.btn_notification.setText(_translate("MainWindow", "Notification"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
