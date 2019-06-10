"""
2.抽取业务逻辑代码到info->init
4.工厂方法创建实例：封装app的创建函数，通过创建app时传入不同值进入不同的配置环境
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from config import config
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
# 创建数据库扩展对象db
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    # 配置config 类
    app.config.from_object(config[config_name])
    # 配置数据库
    # db = SQLAlchemy(app)
    db.init_app(app)    # 通过app方法初始化app
    # 集成redis
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_HOST,port=config[config_name].REDIS_PORT)
    # 集成CSRF,不需要wtf表单.但是需要csrf验证. 所以我们需要导入wtf中csrfProtect
    CSRFProtect(app)
    # Session,指定保存位置
    Session(app)

    return app