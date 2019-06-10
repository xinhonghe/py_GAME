"""
四．1.从index中导入蓝图
    2.register_blueprint注册蓝图到app函数中
"""
# 创建蓝图对象
from info.modules.index import index_blu
# import logging



@index_blu.route('/')
def index():
    # 测试打印日志
    # logging.debug('测试debug')
    # logging.warning('测试WARNING')
    # logging.error('测试error')
    # logging.fatal('测试fatal')

    return "index"

