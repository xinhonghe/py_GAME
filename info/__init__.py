"""
2.抽取业务逻辑代码到info->init
4.工厂方法创建实例：封装app的创建函数，通过创建app时传入不同值进入不同的配置环境
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from redis import StrictRedis
from config import config
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
import logging
# 从日志模块导入
from logging.handlers import RotatingFileHandler
# 创建数据库扩展对象db
db = SQLAlchemy()
redis_store = None   # type:StrictRedis



"""
日志
    1.直接从python中导入日志模块
        loggers     提供应用程序代码直接使用的接口
        handlers    用于将日志记录发送到指定的目的位置
        filters     提供更细粒度的日志过滤功能，用于决定哪些日志记录将会被输出（其它的日志记录将会被忽略）
        formatters  用于控制日志信息的最终输出格式
    2.修改日志基本配置
        例：logging.basicConfig(level=logging.DEBUG)
    3.集成日志到当前项目,在配置文件中添加配置
    4.在业务逻辑代码中，写入具体日志的业务逻辑代码
        创建logs文件夹，日志会自动生成，文件夹需要自己创建
    5.在忽略文件中添加日志文件
    6.记得git提交代码
"""
def set_log(config_name):
    # 通过不同的人配置创建出不同日志记录
    # 设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


# 封装app创建函数
def create_app(config_name):
    # 配置日志，并传入指定模式，以便获取指定配置所对应的日志等级
    set_log(config_name)
    app = Flask(__name__)
    # 配置config 类
    app.config.from_object(config[config_name])
    # 配置数据库
    # db = SQLAlchemy(app)
    db.init_app(app)    # 通过app方法初始化app
    # 集成redis
    # 变量声明类型
    global redis_store
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_HOST,port=config[config_name].REDIS_PORT)
    # 集成CSRF,不需要wtf表单.但是需要csrf验证. 所以我们需要导入wtf中csrfProtect
    CSRFProtect(app)
    # Session,指定保存位置
    Session(app)
    # TODO 五．2.注册根路由蓝图,将导入移到这里来，解决循环导入问题
    from info.modules.index import index_blu
    app.register_blueprint(index_blu)
    # TODO 七．2.注册登录注册路由蓝图，解决循环导入
    from info.modules.passport import passport_blu
    app.register_blueprint(passport_blu)

    return app