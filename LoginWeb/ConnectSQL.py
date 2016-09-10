# coding=utf-8
import MySQLdb


class MysqlUtil(object):
    def __init__(self):
        self.db = self.__connectdb()
        self.__create_table(self.db)

    # 链接数据库
    def __connectdb(self):
        db = MySQLdb.connect("localhost",  # url
                             "root",  # mysql 用户名
                             "root",  # mysql 密码
                             "test")  # mysql 数据库名
        print "链接数据库"
        return db

    # 建表
    def __create_table(self, db):
        cur = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "CREATE TABLE IF NOT EXISTS userTable  (id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY," \
              "username VARCHAR (30) NOT NULL ," \
              "password VARCHAR (30) NOT NULL)"
        cur.execute(sql)

    # 查询用户是否存在
    def qurey_user(self, user_name, user_password):
        cur = self.db.cursor()  # 使用cursor()方法获取操作游标
        cur.execute("SELECT * FROM userTable WHERE username=%s AND password=%s", (user_name, user_password))
        if cur.rowcount > 0:
            return True
        else:
            return False

    # 插入用户
    def insert_user(self, username, userpassword):
        cur = self.db.cursor()
        cur.execute("INSERT INTO userTable (username,password) VALUES (%s,%s)", (username, userpassword))
        self.db.commit()
        if cur.rowcount > 0:
            return True
        else:
            return False
