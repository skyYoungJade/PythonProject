# coding=utf-8
import MySQLdb


def connct_db():
    '''
    链接数据库
    :return:db
    '''
    db = MySQLdb.connect("localhost",  # url
                         "root",  # mysql 用户名
                         "root",  # mysql 密码
                         "test")  # mysql 数据库名
    return db


def init_db():
    '''
    初始化sql并建表 EMPLOYEE
    :return: null
    '''
    db = connct_db()
    cur = db.cursor()  # 使用cursor()方法获取操作游标
    sql = "CREATE TABLE IF NOT EXISTS EMPLOYEE(" \
          "id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY," \
          "username VARCHAR (30) NOT NULL UNIQUE KEY," \
          "password VARCHAR (30) NOT NULL)"

    cur.execute(sql)
    # 关闭连接
    cur.close()


def insert_db(name, pw):
    '''
    添加数据到数据库
    :param name: 用户名
    :param pw: 密码
    :return: null
    '''
    db = connct_db()
    cur = db.cursor()  # 使用cursor()方法获取操作游标
    sql = "INSERT INTO EMPLOYEE (username, password) VALUES ('%s', '%s')" % (str(name), str(pw))
    try:
        # 执行sql语句
        cur.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception, e:
        # 发生错误时回滚
        db.rollback()
        return "Error:" + str(e)


def query_db(name, pw):
    '''
    查询信息
    :param name: 用户名
    :param pw: 密码
    :return: 成功 or 失败
    '''
    db = connct_db()
    cur = db.cursor()  # 使用cursor()方法获取操作游标
    # SQL 查询语句
    sql = "SELECT * FROM EMPLOYEE WHERE username = '%s' AND password = '%s'" % (str(name), str(pw))

    try:
        # 执行sql语句
        cur.execute(sql)
        # 获取所有记录列表
        results = cur.fetchall()
        # 关闭连接
        cur.close()
        if len(results):
            return "Success"
        else:
            return "Failure"
    except Exception, e:
        return "Error: " + str(e)


def update_db(name, pw):
    '''
    更新
    :param name:
    :param pw:
    :return:
    '''
    db = connct_db()
    cur = db.cursor()  # 使用cursor()方法获取操作游标
    sql = "UPDATE EMPLOYEE SET password = '%s' WHERE username = '%s'" % (pw, name)
    try:
        # 执行sql语句
        cur.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 关闭连接
        cur.close()
    except Exception, e:
        # 发生错误时回滚
        db.rollback()
        return "Error: " + str(e)


def delete_db():
    pass


def close_db():
    db = connct_db()
    db.close()  # 关闭数据库连接
