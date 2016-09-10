# coding=utf-8
from flask import Flask, render_template, request
import ConnectSQL as sql

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello SQL!'


@app.route('/login', methods=['GET', 'POST'])
def login_web():
    if request.method == 'POST':
        user_name = request.form["user_name"]
        user_password = request.form["user_password"]
        s = sql.MysqlUtil()  # 初始化mysql
        b = s.qurey_user(user_name, user_password)
        if b:  # 登录成功
            return "登录成功！！"
        else:
            return "登录失败！！"
            # return render_template("login_web.html", message=b)
    else:
        return render_template("login_web.html")


@app.route('/register', methods=["GET", "POST"])
def register_web():
    if request.method == 'POST':
        user_name = request.form["user_name"]
        user_password = request.form["user_password"]
        s = sql.MysqlUtil()  # 初始化mysql
        b = s.insert_user(user_name, user_password)
        if b:  # 登录成功
            return "注册成功！！"
        else:
            return "注册失败！！"
            # return render_template("login_web.html", message=b)
    else:
        return render_template("register_web.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
