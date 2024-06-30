import os
from langchain_community.vectorstores import Chroma
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# yyz
import utils
from utils import aigcs
import RAG_API.ModelFunctions as mf

class ModelOne:
    def __init__(self, aigc_id):
        data_path = aigcs[aigc_id].data_path
        chromadb_path = aigcs[aigc_id].chromDB_path
        print("Tips: 检索数据位置为：" + chromadb_path)
        embeddings = utils.embeddings

        if os.path.exists(chromadb_path):
            retriever = mf.embedding_load(embeddings,chromadb_path)
        else:
            docs = mf.load_data(data_path)
            splits_doc = mf.split(docs)
            retriever = mf.embedding_save(splits_doc,embeddings,chromadb_path)

        # Post-processing - 后处理
        def __format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        prompt = hub.pull("rlm/rag-prompt")
        prompt.messages[0].prompt.template = "你是一个回答问题的助手。请使用以下检索到的背景信息来回答问题。如果你不知道答案，直接说你不知道。请用最多三句话来保持回答的简洁性。\n背景信息：{context} \n问题：{question} \n答案："

        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0,openai_api_key='sk-cXdcebxeIfU9f4tG7e558fF96c35419bB3D66f4e196e8128',openai_api_base='https://api.bianxieai.com/v1')

        # Chain
        self.rag_chain = (
                {"context": retriever | __format_docs, "question": RunnablePassthrough()}
                | prompt
                | llm
                | StrOutputParser()
        )

    def return_anwser(self, input_text):
        output_text = self.rag_chain.invoke(input_text)
        return output_text