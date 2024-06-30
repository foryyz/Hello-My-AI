from RAG_API.ModelOne import ModelOne
from utils import aigcs
class Controller:
    def __init__(self, view):
        self.view = view

    def submit_worker(self, input_text, aigc_id):
        # 在这里处理输入文本的逻辑
        # output_text = f"Answer: {input_text}"
        # output_text = chatgpt_acge_One.return_anwser(input_text)
        output_text = ModelOne(aigc_id).return_anwser(input_text)
        self.view.output_textbox.append(output_text)