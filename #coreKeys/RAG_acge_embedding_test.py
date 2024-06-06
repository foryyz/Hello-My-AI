import bs4
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms.ollama import Ollama
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI

from langchain_community.document_loaders import TextLoader
# 加载补充文档
loader = TextLoader("../data/data1.md")
docs = loader.load()

# Split - 分词
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)

# Embed
vectorstore = Chroma.from_documents(documents=splits, embedding=OllamaEmbeddings(model="mofanke/acge_text_embedding"))
retriever = vectorstore.as_retriever()
print("indexing done - 检索完毕")

# Prompt - 提示词
prompt = hub.pull("rlm/rag-prompt")
prompt.messages[0].prompt.template="你是一个回答问题的助手。请使用以下检索到的背景信息来回答问题。如果你不知道答案，直接说你不知道。请用最多三句话来保持回答的简洁性。\n背景信息：{context} \n问题：{question} \n答案："
# print(prompt)

# LLM
# llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0,openai_api_key='sk-cXdcebxeIfU9f4tG7e558fF96c35419bB3D66f4e196e8128',openai_api_base='https://api.bianxieai.com/v1')
llm = Ollama(model="qwen:4b")

# Post-processing - 后处理
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# Chain
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# rag_chain.invoke("保定学院的人工智能学院周三上什么课程?")

dataset=["你是什么语言模型？由什么公司开发？",
         "保定学院的人工智能学院周三上什么课程?",
         "2024年张宇阳的年龄是多少？",
         "张宇阳的爱好是什么？"]
for idx, _q in enumerate(dataset, start=1):
    print(f"问题{idx}：{_q}")
    print(rag_chain.invoke(_q))