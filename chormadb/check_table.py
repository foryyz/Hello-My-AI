import sqlite3

def read_table(database_file, table_name):
    # 连接到 SQLite 数据库文件
    conn = sqlite3.connect(database_file)

    # 创建一个游标对象，用于执行 SQL 查询
    cursor = conn.cursor()

    try:
        # 执行查询语句
        cursor.execute(f"SELECT * FROM {table_name};")

        # 获取所有查询结果
        rows = cursor.fetchall()

        # 打印结果
        print(f"Table: {table_name}")
        for row in rows:
            print(row)

        print()  # 打印空行分隔每个表的输出

    except sqlite3.Error as e:
        print(f"SQLite 错误：查询 {table_name} 表时出错：", e)

    finally:
        # 关闭游标对象和数据库连接
        cursor.close()
        conn.close()

# 调用函数依次读取指定的表
tables_to_read = [
    "migrations",
    "embeddings_queue",
    "collection_metadata",
    "segments",
    "segment_metadata",
    "tenants",
    "databases",
    "collections",
    "embeddings",
    "embedding_metadata",
    "max_seq_id",
    "embedding_fulltext_search",
    "embedding_fulltext_search_data",
    "embedding_fulltext_search_idx",
    "embedding_fulltext_search_content",
    "embedding_fulltext_search_docsize",
    "embedding_fulltext_search_config"
]

database_file = 'chroma.sqlite3'

for table_name in tables_to_read:
    read_table(database_file, table_name)
