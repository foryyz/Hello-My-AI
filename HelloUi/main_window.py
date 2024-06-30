from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from HelloUi.views.io_view import View
import utils


class MainWindow(QMainWindow):
    def __init__(self, windowTitle="I am MainWindow,Please Update Name!"):
        super().__init__()
        self.windowTitle = windowTitle

        self.main_window_init() # 初始化主窗口
        self.main_button_init() # 初始化按钮
        self.main_layout_init(self.mainButtons) # 初始化布局

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def main_window_init(self):
        self.setWindowTitle(self.windowTitle)
        self.setGeometry(100, 100, 250, 100)
        # self.button_labels = ["保定学院知识库", "食谱推荐", "Test", "Test2"] #使用utils文件资源替代
        self.button_labels = utils.get_button_labels()

    def main_button_init(self):
        self.mainButtons = []  # 存储 窗口按钮

        for index,button_label in enumerate(self.button_labels):
            button = QPushButton(button_label, self)
            # button.setFixedSize(120,60)
            # button.clicked.connect(self.show_view) # 改为信号与槽机制中传递参数
            button.clicked.connect(lambda checked, aigc_id=index, view_name=button_label: self.show_view(aigc_id, view_name))
            self.mainButtons.append(button)

    def main_layout_init(self, buttons):
        self.central_widget = QWidget(self)  # 创建中央 widget
        self.setCentralWidget(self.central_widget)  # 将中央 widget 设置到主窗口
        self.layout = QVBoxLayout(self.central_widget)  # 创建布局并设置到中央 widget
        self.layout.addStretch(1)  # 添加伸缩因子

        for button in buttons:
            self.layout.addWidget(button)
        self.layout.addStretch(1)  # 再次添加伸缩因子，将按钮放置在窗口中央

    def show_view(self,aigc_id, view_name):
        mine_view = View(aigc_id,view_name)
        mine_view.show()