from langchain_community.embeddings import OllamaEmbeddings


data_name = ["保定学院知识库", "食谱推荐"]
data_path = ["data/data1.md", "data/food.json"]
chroma_name = ["bdudb", "fooddb"]
data_prompt = [
    "你是一个回答问题的助手。请使用以下检索到的背景信息来回答问题。如果你不知道答案，直接说你不知道。请用最多三句话来保持回答的简洁性。\n背景信息：{context} \n问题：{question} \n答案：",
    "你是一个回答问题的助手。请使用以下检索到的背景信息来回答问题。如果你不知道答案，直接说你不知道。请用最多三句话来保持回答的简洁性。\n背景信息：{context} \n问题：{question} \n答案："
]

embeddings = OllamaEmbeddings(model="mofanke/acge_text_embedding")

def get_button_labels():
    # 知识库的名字 就是 按钮的标题
    return data_name
