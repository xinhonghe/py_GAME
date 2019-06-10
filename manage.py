"""
1.配置config 类
2.配置数据库
3.集成redis
4.集成CSRF
5.配置Session
6.数据库迁移
"""



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

class Config():
    #session 加密
    SECRET_KEY = "1234567"

    # 配置config
    DEBUG = True

    # 配置数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/py_GAME"
    SQLALCHEMY_TRACK_MODIFICATION = True
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




app = Flask(__name__)
# 配置config 类
app.config.from_object(Config)
# 配置数据库
db = SQLAlchemy(app)
# 集成redis
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
# 集成CSRF,不需要wtf表单.但是需要csrf验证. 所以我们需要导入wtf中csrfProtect
CSRFProtect(app)
# Session,指定保存位置
Session(app)
# 数据库迁移
manager = Manager(app)
# 迁移命令集成
Migrate(app)
manager.add_command('db',MigrateCommand)





@app.route('/')
def index():
    return "index"


if __name__ == "__main__":
    manager.run()