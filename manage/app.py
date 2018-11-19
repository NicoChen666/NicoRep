from myApp.app import create_app
from flask_script import Manager

# 创建工程实例
app = create_app()

# 创建管理对象
manager = Manager(app)
if __name__ == '__main__':
    # 建表 暂时使用 以后不用
    # db.create_all()
    manager.run()
