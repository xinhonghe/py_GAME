"""
导入蓝图
"""
import info.utils.captcha.captcha
from info.modules.passport import passport_blu
from flask import request,abort,current_app
from info.utils.captcha.captcha import captcha
from info import redis_store
from info import constants


@passport_blu.route('/image_code')
def get_image_code():
    """
    前端页生成验证码编号，并将编号并提交到后台去请求验证码图片
    后台生成图片验证码，并把验证码文字内容当作值，验证码编号当作key存储在 redis 中
    后台把验证码图片当作响应返回给前端
    前端申请发送短信验证码的时候带上第1步验证码编号和用户输入的验证码内容
    后台取出验证码编号对应的验证码内容与前端传过来的验证码内容进行对比
    如果一样，则向指定手机发送验证码，如果不一样，则返回验证码错误
    :return:
    """
    # 获取图片验证码
    image_code_id = request.args.get("imageCodeId")
    # 判断是否有值
    if not image_code_id:
        return abort(403)
    # 生成图片验证码
    _,text,image = captcha.generate_captcha()
    # 保存图片验证码
    try:
        redis_store.set("ImageCodeId_"+image_code_id,text,constants.IMAGE_CODE_REDIS_EXPIRES)
    except Exception as e:
        #　保存失败
        current_app.logger.error(e)
        abort(500)
    # 返回验证码
    return image
