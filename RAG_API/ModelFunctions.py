from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain import hub

# yyz
import utils


def load_data(data_path):
    loader = TextLoader(data_path)
    docs = loader.load()
    return docs

def split(docs, chunk_size = 512):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    return splits

def embedding_save(splits_doc, embeddings, persist_directory):
    vectorstore = Chroma.from_documents(documents=splits_doc, embedding=embeddings,persist_directory=persist_directory)
    vectorstore.persist()
    retriever = vectorstore.as_retriever()
    print("indexing done - 检索数据保存完毕")
    return retriever

def embedding_load(embeddings, persist_directory):
    vectorstore = Chroma(persist_directory=persist_directory,embedding_function=embeddings)
    retriever = vectorstore.as_retriever()
    print("indexing done - 检测到向量数据，已成功读取！")
    return retriever

def prompt_get(data_id):
    prompt = hub.pull("rlm/rag-prompt")
    prompt.messages[0].prompt.template = utils.data_prompt[data_id]
    return prompt

def post_processing(data_id, _docs):
    def __format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    prompt = hub.pull("rlm/rag-prompt")
    prompt.messages[0].prompt.template = prompt_get(data_id)
