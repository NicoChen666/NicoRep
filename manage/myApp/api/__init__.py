from flask import Blueprint
from flask import render_template
# 蓝图对象(习惯与应用名同名或者用urls)
# myApp = Blueprint("myApp", __name__)
urls = Blueprint("myApp", "urls", template_folder="templates")

# create your urls and views here


@urls.route('/')
# 视图
def index():
    return render_template("index.html")

