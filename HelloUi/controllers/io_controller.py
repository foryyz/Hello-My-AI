# from utils import chatgpt_acge_One
from RAG_API.ModelOne import ModelOne
class Controller:
    def __init__(self, view):
        self.view = view

    def submit_worker(self, input_text, data_id):
        # 在这里处理输入文本的逻辑
        # output_text = f"Answer: {input_text}"
        # output_text = chatgpt_acge_One.return_anwser(input_text)
        output_text = ModelOne(data_id).return_anwser(input_text)
        self.view.output_textbox.append(output_text)