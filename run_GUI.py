import sys
from PyQt6.QtWidgets import QApplication
from HelloUi.main_window import MainWindow

# from langchain_RAG_API import chatgpt_acge_One

if __name__ == "__main__":

    app = QApplication(sys.argv)
    main_window = MainWindow("Hello My AI - 基于RAG和多LLM协作的现实系统构建工具")
    main_window.show()
    sys.exit(app.exec())
