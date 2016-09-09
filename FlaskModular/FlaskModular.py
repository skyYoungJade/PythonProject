# coding=utf-8
from flask import Flask, render_template
from models import User

app = Flask(__name__)


# Python中允许添加html、css ，but 这样不太好
@app.route('/')
def hello_world():
    return '<h1>Hello World!<h1>'


# 添加渲染的模板 -- index.html
@app.route('/index')
def hello_html():
    return render_template("index.html")


# 自定义渲染模板的内容 -- index.html
@app.route('/custom_modular')
def custom_html():
    content = "hello flask !!!"
    return render_template("index.html", content=content)


# 模板传入对象 -- user_index.html
@app.route('/user')
def user_index():
    user = User(1, "zhangSan")
    return render_template("user_index.html", user=user)


# 模板判断语句 -- user_id.html
@app.route('/query_user/<user_id>')
def query_user(user_id):
    user = None
    if int(user_id) == 1:
        user = User(1, "ZhangSan")
    return render_template("user_id.html", user=user)


# 模板循环语句 -- user_list.html
@app.route('/users')
def user_list():
    users = []
    for i in range(1, 11):
        user = User(i, "list_" + str(i))
        users.append(user)
    return render_template("user_list.html", users=users)


# 模板的继承 -- child_1.html / child_2.html --> base.html
@app.route('/one')
def one_page():
    return render_template("child_1.html")


@app.route('/two')
def two_page():
    return render_template("child_2.html")


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
