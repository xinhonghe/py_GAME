"""
一.项目配置
    1.配置config 类
    2.配置数据库
    3.集成redis
    4.集成CSRF
    5.配置Session
    6.数据库迁移
二.代码抽取
    1.抽取配置文件
    2.抽取业务逻辑代码到info->init
    3.项目多种配置：使用面向对象的方法重改配置类，利用类的继承实现不同的配置环境
    4.工厂方法创建实例：封装app的创建函数，通过创建app时传入不同值进入不同的配置环境
"""



# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import redis
# from flask_wtf.csrf import CSRFProtect
# from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
# from config import Config
from info import create_app,db


# 传入app运行配置参数
app = create_app('develop')
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