# coding=utf-8
from flask import Flask, request, url_for, send_from_directory, abort, Response, jsonify
from db_util import init_db, insert_db, query_db, update_db
import os.path
from werkzeug.utils import secure_filename  # werkzeug库可以判断文件名是否安全
import json

""""
第一课时：flask 的路由
"""

UPLOAD_FOLDER = '/FlaskApp/files'

app = Flask(__name__)
init_db()
# 指定下载文件路径
dirpath = os.path.join(app.root_path, 'files')
app.config['UPLOAD_FOLDER'] = 'static/uploads/'  # 上传文件指定路径
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])  # 规定4种文件格式


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


# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


# 上传图片
@app.route('/upload', methods=['POST'])
def upload_image():
    upload_file = request.files['photo']  # 接收的文件
    if upload_file and allowed_file(upload_file.filename):
        filename = secure_filename(upload_file.filename)
        upload_file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
        return 'hello, ' + request.form.get('name', 'default') + '.success'
    else:
        return 'hello,' + request.form.get('name', 'default') + '.failed'


# 返回json数据
@app.route('/getjson', methods=['GET'])
def get_json():
    content = {'info': 'qwertyuio', 'date': '2016-08-08', 'state': '1'}
    # return Response(json.dumps(content), mimetype='application/json') # 用json模板
    return jsonify(content)  # flask jsonify模板


if __name__ == '__main__':
    # app.run(debug=True)  # 设置debug 模式
    app.run(host='0.0.0.0')  # host='0.0.0.0'
