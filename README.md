> 项目启动时间：2024/06/02
>
> 最后更新时间：2024/06/08
>
> 当前版本：V0.101

# Hello My AI

项目名称：Hello My AI - 基于RAG和多LLM协作的现实系统构建工具

核心成员：待定

核心技术图示：https://github.com/langchain-ai/rag-from-scratch



# 0 更新日志

```
a0.001 - 2024-06-02 - [yyz]
核心算法实现,本地ollama模型和第三方LLM调取.

V0.100 - 2024-06-05 - [yyz]
核心算法 模块化,设计前端代码框架.(PyQT)

V0.101 - 2024-06-06 - [yyz]
前端代码框架优化,前后端逻辑实现。前端主窗口MainWindow类模块化.
- 后续前端代码暂由[JYY]接管.

V0.101 - 2024-06-08 - [tg]
发现向量永久性存储的方式，代码更新位置：chatgpt_acge.py中Chroma.from_documents()方法添加关键参数：
persist_directory="chormadb"

- 查询存储内容：将find_all_table.py返回的chroma.sqlite3数据库表名传给check_table.py。
- check_table.py查询所有表。

```



# 1 具体实现

## 1.1 开发路线：

第一阶段：核心算法实现，双前端设计，基础架构完毕。产出效果尚可。

- RAG模型检索、LLM模型输出、输入文档优化
  - 输入文档优化方式不唯一：
    - 过渡：使用第三方大模型处理 或 使用python脚本处理
    - 最终：使用本地大模型处理（需要解决速度问题） 或 使用国产第三方大模型处理（安全）
  - RAG检索方式不唯一：
    - 过渡：使用**Huggingface**平台开源Embedding模型
    - 优化：通过微调模型 或 调整参数的形式，提高检索质量
    - 其他方案：如果时间和技术能力允许，可以训练开发自己的Embedding模型
  - 输入文档的优化方案：
    - 暂定为 - 统一转化为json（用大模型处理效果很好）

预计开发时间 - 2024年8月中，互联网+大赛前

取得成绩后，继续优化参加后续比赛，如2025年计算机设计大赛 人工智能类 等。

如在互联网+大赛时未取得任何成绩或成绩非常不理想，**视情况终止项目或解散团队**。

## 1.2 技术栈

- 前端：PyQt, OpenWebUI
- 后端：不使用框架开发
- 数据库：LanceDB、
- 版本管理：Git
- LLM框架：Ollama

