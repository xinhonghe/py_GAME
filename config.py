"""
1.抽取配置文件
3.项目多种配置：使用面向对象的方法重改配置类，利用类的继承实现不同的配置环境
三．2.修改日志基本配置

"""


import redis
import logging


class Config():
    #session 加密
    SECRET_KEY = "1234567"

    # 配置config
    DEBUG = True

    # 配置数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/py_GAME"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    # 配置redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    #配置Session 配置,指定session　的保存位置
    SESSION_TYPE = "redis"  # session 的存储类型
    SESSION_USE_SIGNER = True   # cooike 中的 session_id 是否加密
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)  #　使用redis 实例
    SESSION_PERMANENT = False   #　是否永久保存
    PERMANENT_SESSION_LIFETIME = 86400 * 2 # 保存期限



class DevelopConfig(Config):
    """开发环境配置"""
    DEBUG = True
    LOG_LEVEL = logging.DEBUG

class ProductConfig(Config):
    """生产环境配置"""
    DEBUG = False
    LOG_LEVEL = logging.ERROR

class TestingConfig(Config):
    """单元测试环境配置"""
    DEBUG = True
    TESTING = True


# 创建字典，方便导入导出
config = {
    'develop':DevelopConfig,
    'product':ProductConfig,
    'testing':TestingConfig
}
