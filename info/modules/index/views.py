"""
四．1.从index中导入蓝图
    2.register_blueprint注册蓝图到app函数中
"""
# 创建蓝图对象
from info.modules.index import index_blu
# import logging
from flask import render_template
from flask import current_app



@index_blu.route('/')
def index():
    # 测试打印日志
    # logging.debug('测试debug')
    # logging.warning('测试WARNING')
    # logging.error('测试error')
    # logging.fatal('测试fatal')

    return render_template("news/index.html")

# TODO 在打开网页的时候，浏览器会默认去请求根路径和图标函数
@index_blu.route('/favicon.ico')
def set_favicon():
    # send_static_file　是flask 去查找指定的静态文件所调用的方法
    return current_app.send_static_file('news/favicon.ico')

