"""
视图蓝图模块
五．1.在index.py中的init文件中创建蓝图，并
    2.创建views文件中导入具体的视图函数路由
"""

from flask import Blueprint

index_blu = Blueprint('index',__name__)

from .views import *