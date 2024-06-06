import sys
from PyQt6.QtWidgets import QApplication
from HelloUi.main_window import MainWindow

# from langchain_RAG_API import chatgpt_acge_One

if __name__ == "__main__":

    app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec())
