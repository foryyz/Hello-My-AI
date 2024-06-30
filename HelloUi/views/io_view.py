from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QPushButton, QTextEdit, QApplication, QLabel, QVBoxLayout, QWidget
from HelloUi.controllers.io_controller import Controller
import utils

class View(QMainWindow):
    def __init__(self, aigc_id, view_name):
        super().__init__()

        self.setWindowTitle(view_name)
        self.aigc_id = aigc_id
        self.setGeometry(300, 300, 600, 400)
        self.input_textbox = QTextEdit(self)
        self.output_textbox = QTextEdit(self)
        self.output_textbox.setReadOnly(True)

        self.submit_question_button = QPushButton("↓ 在下方输入文本后，点我执行提交.", self)
        # self.submit_question_button.clicked.connect(self.submit_contorller)
        self.submit_question_button.clicked.connect(lambda checked, aigc_id = self.aigc_id: self.submit_contorller(aigc_id))

        layout = QVBoxLayout()
        layout.addWidget(self.output_textbox)
        layout.addWidget(self.submit_question_button)
        layout.addWidget(self.input_textbox)
        layout.setStretch(5,1)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.controller = Controller(self)

    def submit_contorller(self, aigc_id):
        input_text = self.input_textbox.toPlainText() # 提取文本框的文字
        self.controller.submit_worker(input_text, aigc_id) # 将文字传给submit_worker()
