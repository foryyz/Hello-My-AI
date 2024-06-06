from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget
from HelloUi.views.io_view import IOWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 600, 400)

        self.main_button = QPushButton("保定学院知识库", self)
        self.main_button.clicked.connect(self.show_io_window)

        layout = QVBoxLayout()
        layout.addWidget(self.main_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def show_io_window(self):
        self.io_window = IOWindow()
        self.io_window.show()