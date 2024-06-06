from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from HelloUi.views.io_view import View

class MainWindow(QMainWindow):
    def __init__(self, windowTitle="I am MainWindow,Please Update Name!"):
        super().__init__()
        self.windowTitle = windowTitle

        self.main_window_init() # 初始化主窗口
        self.main_button_init() # 初始化按钮
        self.main_layout_init(self.mainButtons) # 初始化布局

        # container = QWidget()
        # container.setLayout(self.layout)
        # self.setCentralWidget(container)

    def main_window_init(self):
        self.setWindowTitle(self.windowTitle)
        self.setGeometry(100, 100, 600, 400)

    def main_button_init(self):
        self.mainButtons = []  # 存储 窗口按钮

        bdu_button = QPushButton("保定学院知识库", self)
        bdu_button.clicked.connect(self.show_window)  # 添加监听器，检测到点击后，执行self.show_io_window
        self.mainButtons.append(bdu_button)

    def main_layout_init(self, buttons):
        # 目前为单布局方案 未创建布局列表
        self.layout = QVBoxLayout()  # 存储 布局
        for button in buttons:
            self.layout.addWidget(button)

    def show_window(self):
        self.other_view = View()
        self.other_view.show()