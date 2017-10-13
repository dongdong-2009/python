#coding=utf8
import itchat
import time


itchat.auto_login(hotReload=True)

nn = '面向对象'
#想给谁发信息，先查找到这个朋友
mps = itchat.search_mps(name=nn)
if len(mps) != 0 :
    print('找到%d个公众号[%s]' % (len(mps),nn))
    for key,value in mps[0].items():
        if key == "UserName":
            print(">>>",key,"---->",value)

mm = "BAICY百辰悦装饰·段鹏飞"
m1 = "晏明伟"
m2 = 'LoyaStone'
users = itchat.search_friends(name=mm)
users1 = itchat.search_friends(name=m1)
users2 = itchat.search_friends(name=m2)
if len(users) == 0 and len(users1) and len(users2):
    print("没有找到用户")
else:
    print("找到用户>>>>%s,%s,%s" % (mm,m1,m2))
    for key,value in mps[0].items():
        if key == "UserName":
            print(">>>",key,"---->",value)
    #找到UserName
    userName = users[0]['UserName']
    userName1 = users1[0]['UserName']
    userName2 = users2[0]['UserName']
    #然后给他发消息
    while 1:
        #itchat.send("【coming from akon】现在:",toUserName=userName)
        itchat.send("【coming from akon】现在:", toUserName=userName1)
        #itchat.send("【coming from akon】现在:", toUserName=userName2)
        itchat.send(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),toUserName = userName1)
        time.sleep(10)