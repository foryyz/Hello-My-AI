import sqlite3

# 连接到 SQLite 数据库文件
conn = sqlite3.connect('chroma.sqlite3')

# 创建一个游标对象
cursor = conn.cursor()

# 执行查询所有数据表的 SQL 查询
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# 获取所有数据表名称的结果集
tables = cursor.fetchall()

# 打印结果
print("所有数据表名称:")
for table in tables:
    print(table[0])

# 关闭游标和数据库连接
cursor.close()
conn.close()
