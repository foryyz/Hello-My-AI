from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtWidgets import QMainWindow, QPushButton, QTextEdit, QApplication, QLabel, QVBoxLayout, QWidget
from HelloUi.controllers.io_controller import Controller
import utils
from PyQt6 import QtCore,QtWidgets

class View(QMainWindow):
    def __init__(self, data_id, view_name):
        super().__init__()


        self.setWindowTitle(view_name)
        self.data_id = data_id
        self.setGeometry(300, 300, 600, 400)
        self.resize(645, 612)

        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")



        self.input_textbox = QTextEdit(parent=self.centralwidget)
        self.input_textbox.setGeometry(QtCore.QRect(3, 450, 551, 121))
        self.input_textbox.setStyleSheet("background-color: black;")
        font = QFont("Arial", 10)
        self.input_textbox.setFont(font)
        self.input_textbox.setStyleSheet("border: 2px solid black;")
        self.input_textbox.setStyleSheet("box-shadow: 3px 3px 6px grey;")
        self.input_textbox.setStyleSheet("selection-color: white; selection-background-color: darkblue;")
        self.input_textbox.setStyleSheet("cursor-color: red;")
        self.input_textbox.setStyleSheet("cursor-width: 2px;")
        self.input_textbox.setPlaceholderText('请在此输入消息...')


        self.output_textbox = QTextEdit(parent=self.centralwidget)
        self.output_textbox.setReadOnly(True)
        self.output_textbox.setGeometry(QtCore.QRect(3, 0, 641, 441))
        self.output_textbox.setStyleSheet("background-color: black;")
        self.output_textbox.setFont(font)
        self.output_textbox.setStyleSheet("border: 1px solid black;")
        self.output_textbox.setStyleSheet("box-shadow: 2px 2px 5px grey;")
        self.output_textbox.setStyleSheet("selection-color: white; selection-background-color: darkblue;")
        self.output_textbox.setStyleSheet("cursor-color: red;")
        self.output_textbox.setStyleSheet("cursor-width: 2px;")


        self.submit_question_button = QPushButton("点我执行提交",parent=self.centralwidget)
        self.submit_question_button.setIcon(QIcon.fromTheme("mail-send"))
        # self.submit_question_button.clicked.connect(self.submit_contorller)
        self.submit_question_button.clicked.connect(lambda checked, data_id = self.data_id: self.submit_contorller(data_id))
        self.submit_question_button.setGeometry(QtCore.QRect(560, 450, 81, 121))
        self.submit_question_button.setIconSize(QSize(560,450))
        self.submit_question_button.show()

        self.setCentralWidget(self.centralwidget)

        self.controller = Controller(self)



    def submit_contorller(self, data_id):
        input_text = self.input_textbox.toPlainText() # 提取文本框的文字
        self.controller.submit_worker(input_text,data_id) # 将文字传给submit_worker()

