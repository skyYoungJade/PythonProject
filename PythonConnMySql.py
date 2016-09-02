# coding=utf-8
import MySQLdb

"""""
执行事务

事务机制可以确保数据一致性。
事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。
  原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
  一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
  隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
  持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。
Python DB API 2.0 的事务提供了两个方法 commit 或 rollback。
"""

# 连接数据库
db = MySQLdb.connect("localhost",  # url
                     "root",  # mysql 用户名
                     "root",  # mysql 密码
                     "test")  # mysql 数据库名
cur = db.cursor()  # 使用cursor()方法获取操作游标
try:
    cur.execute("DROP TABLE IF EXISTS pythonTb")  # 如果数据存在就删除
    cur.execute("CREATE TABLE pythonTb (id INT(10) PRIMARY KEY,name VARCHAR(20) )")  # 创建数据库

    # SQL 插入语句
    cur.execute("INSERT pythonTb (id, name) VALUES (2,'Jack')")
    # 提交到数据库执行
    db.commit()

    # SQL 查询
    cur.execute("SELECT * FROM pythonTb")

    # 获取所有记录的列表
    results = cur.fetchall()
    for row in results:
        db_id = row[0]
        name = row[1]
        print "id = %d && name = %s" % (db_id, name)

    # 更新SQL
    cur.execute("UPDATE pythonTb SET name = 'Mac' WHERE id = 1")
    db.commit()

    # 删除 SQL
    cur.execute("DELETE FROM pythonTb WHERE id = 1 ")
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()

db.close()  # 关闭数据库
