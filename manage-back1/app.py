# 引入Flask 基本库
from flask import Flask, render_template
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
# 创建工程实例
app = Flask(__name__)
# 给工程app 配置数据库
# 设置链接数据库的URI  mysql+pymysql://账号:密码@IP:端口/数据库名
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:cnf6553900@www.darlingmeng.top:3306/flask"
#禁止对象的修改追踪
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 创建数据库对象
db = SQLAlchemy(app)

# 模型
class Grade(db.Model):
    # 需要指定主键
    # 指定数据库中字段的类型
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    girlNum = db.Column(db.Integer)
    boyNum = db.Column(db.Integer)
    isDelete = db.Column(db.Boolean, default=False)
    def __init__(self, name, girlNum, boyNum):
        self.name = name
        self.girlNum = girlNum
        self.boyNum = boyNum
    def __str__(self):
        return self.name

class Student(db.Model):
    # 需要指定主键
    # 指定数据库中字段的类型
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    gender = db.Column(db.Integer)
    age = db.Column(db.Integer)
    content = db.Column(db.String(20))
    isDelete = db.Column(db.Boolean, default=False)
    # 外键， 关联的是 类名小写.主键的属性名 对应数据库的字段名为grade
    grade = db.Column(db.Integer, db.ForeignKey("grade.id"))

    def __init__(self, name, gender, age, content, grade):
        self.name = name
        self.gender = gender
        self.age = age
        self.content = content
        self.grade = grade
    def __str__(self):
        return self.name

# 路由
@app.route('/')

@app.route('/index/')
def index():
    return render_template("index.html")

# 视图
def hello_world():
    return '南无阿弥陀佛'

@app.route('/grades/')
def gradesList():
    grades = Grade.query.all()
    return render_template("gradesList.html", grades=grades)

@app.route('/students/')
def studentsList():
    students = Student.query.all()
    return render_template("studentsList.html", students=students)
@app.route('/studentDetail/<sid>/')
def studentDetail(sid):
    stu = Student.query.get(sid)
    return stu
# 创建管理对象
manager = Manager(app)
if __name__ == '__main__':
    # 建表 暂时使用 以后不用
    # db.create_all()
    manager.run()
