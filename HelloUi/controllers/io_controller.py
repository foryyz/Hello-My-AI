from langchain_RAG_API import chatgpt_acge_One

class IOController:
    def __init__(self, view):
        self.view = view

    def process_input(self, input_text):
        # 在这里处理输入文本的逻辑
        # output_text = f"Processed: {input_text}"
        output_text = chatgpt_acge_One.return_anwser(input_text)
        self.view.output_textbox.append(output_text)