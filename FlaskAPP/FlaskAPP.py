# coding=utf-8
from flask import Flask, request, url_for
from db_util import init_db, insert_db, query_db, update_db

""""
第一课时：flask 的路由
"""

app = Flask(__name__)
print "init Flask !!!"
init_db()


@app.route('/')
def hello_world():
    return 'Hello World!'


# 添加参数
@app.route('/index')
def app_index():
    return "index Application!"


# 指定路由的请求方法POST（默认为GET）
@app.route('/method', methods=['POST'])
def app_method():
    return "app_method of Post"


# 路由参数的传递 name
@app.route('/index/<name>')
def user_name(name):
    return "UserName:" + name


# 根据键值对传参
@app.route('/query_user')
def query_user():
    valuse = request.args.get("id")
    return "query user : " + valuse


# 反向路由（根据此方法可以查询某个url）
@app.route('/query_url')
def query_url():
    return "query url : " + url_for("app_index")


# 客户端登录
@app.route('/client/login', methods=['POST'])
def client_login():
    username = request.args.get('username')
    password = request.args.get('password')
    counts = update_db(username, password)

    return "账号：%s , 密码： %s , 回调： %s" % (str(username), str(password), str(counts))
    # return "账号:" + str(username) + ",密码：" + str(password)


if __name__ == '__main__':
    # app.run(debug=True) # 设置debug 模式
    app.run(host='0.0.0.0')
