import os

from langchain_community.embeddings import OllamaEmbeddings

# data_name = ["知识库"]
# data_path = ["/home/yyz/PycharmProjects/Hello-My-AI/data/XgameRadar.txt"]
# chroma_name = ["knowsdb"]
# data_prompt = [
#     "你是一个回答问题的助手。请使用以下检索到的背景信息来回答问题。如果你不知道答案，直接说你不知道。请用最多三句话来保持回答的简洁性。\n背景信息：{context} \n问题：{question} \n答案："
# ]

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

class Aigc:
    def __init__(self, data_name, data_path, chromaDB_name, data_prompt="你是一个回答问题的助手。请使用以下检索到的背景信息来回答问题。如果你不知道答案，直接说你不知道。请用最多三句话来保持回答的简洁性。\n背景信息：{context} \n问题：{question} \n答案：", embeddings = OllamaEmbeddings(model="mxbai-embed-large")):
        self.data_name = data_name
        self.data_path = data_path
        self.chromaDB_name = chromaDB_name
        self.chromDB_path_tmp = "~/chromaDB/{}".format(chromaDB_name)
        self.chromDB_path = os.path.expanduser(self.chromDB_path_tmp)

aigcs = [
    Aigc("游戏知识库","/home/yyz/PycharmProjects/Hello-My-AI/data/XgameRadar.txt","knowsdb"),
    Aigc("测试","/home/yyz/PycharmProjects/Hello-My-AI/data/bdu_datas/data_sparkTest.md","testdb")
]

def get_button_labels():
    button_labels = []
    # 知识库的名字 就是 按钮的标题
    for aigc in aigcs:
        button_labels.append(aigc.data_name)
    return button_labels

print(get_button_labels())