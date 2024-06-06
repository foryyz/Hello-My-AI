from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QPushButton, QTextEdit, QApplication, QLabel, QVBoxLayout, QWidget
from HelloUi.controllers.io_controller import IOController

class IOWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IO View")
        self.setGeometry(300, 300, 600, 400)
        self.input_textbox = QTextEdit(self)
        self.output_textbox = QTextEdit(self)
        self.output_textbox.setReadOnly(True)
        # self.output_textbox.setReadOnly(True)

        self.control_button = QPushButton("请在下方输入你的问题：↓", self)
        self.control_button.clicked.connect(self.process_input)

        layout = QVBoxLayout()
        layout.addWidget(self.output_textbox)
        layout.addWidget(self.control_button)
        layout.addWidget(self.input_textbox)
        layout.setStretch(5,1)


        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.controller = IOController(self)

    def process_input(self):
        input_text = self.input_textbox.toPlainText()
        self.controller.process_input(input_text)
