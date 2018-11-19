class DefaultConfig():
    # 给工程app 配置数据库
    # 设置链接数据库的URI  mysql+pymysql://账号:密码@IP:端口/数据库名
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:cnf6553900@www.darlingmeng.top:3306/flask"
    # 禁止对象的修改追踪
    SQLALCHEMY_TRACK_MODIFICATIONS = False
