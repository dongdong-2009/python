import requests
import sys,re,time,itchat,os
from itchat.content import *

#KEY = '8edce3ce905a4c1dbb965e6b35c3834d'  # 这个key可以直接拿来用
KEY = "7c1ccc2786df4e1685dda9f7a98c4ec9"


# 向api发送请求
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'pth-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

# 注册方法
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    # a or b的意思是，如果a有内容，那么返回a，否则返回b
    return reply or defaultReply


itchat.auto_login(hotReload=True)
itchat.run()