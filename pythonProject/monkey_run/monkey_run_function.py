from easygui import *
import re
from subprocess import Popen,PIPE
import os
import time
def get_path():
    path=r'D:logfile/log'
    if not os.path.exists(path):
        os.mkdir(path)
    return path

def get_ip():#获取手机ip
    ip=enterbox(msg='请输入手机IP地址',title='IP',default='')
    if ip==None:
        os._exit(0)
    return ip
def connect():#连接手机
    m=get_ip()
    while m=='':#验证IP输入不为空
        msgbox(msg='',title='IP地址未输入！')
        return connect()
    print("连接手机中-----------")
    address=m+':5555'
    Popen('adb tcpip 5555',stdout=PIPE)
    time.sleep(5)
    m=Popen('adb connect '+address,stdout=PIPE)
    l=str(m.stdout.read())

    f=textbox(msg='',title='链接信息',text=re.findall("b'(.*?):",l))#显示连接信息
    if f==None:
        os._exit(0)
    if re.findall('cannot',f):
        print("请重新检查输入ip是否正确！10s后退出程序！-----------")
        time.sleep(10)
        os._exit(0)

def get_pacage():
    print("获取APP包名和Activity-----------")
    pacage_order=Popen('adb shell dumpsys window | grep mCurrentFocus',stdout=PIPE)
    pacage_txt = str(pacage_order.stdout.read())
    if pacage_txt=="b''":
        Popen('adb shell dumpsys window | grep mCurrentFocus', stdout=PIPE)
        pacage_txt = str(pacage_order.stdout.read())
    detail='Pacage: '+re.findall('u0 (.*?)/',pacage_txt)[0]+'\n'+'Activity: '+re.findall('/(.*?)}',pacage_txt)[0]
    print('已'
          '获取APP包信息：\n{}'.format(detail))
    textbox(msg='',title='APP信息：',text=detail)
def run():
    method = indexbox(msg='请选择运行脚本方式', title='选择脚本方式', choices=('命令行', '脚本文件'))
    if method==0:
        order=enterbox(msg='命令行',title='')
        if order==None:
            os._exit(0)
        print("执行脚本命令中---------")
        title=Popen(order,stdout=PIPE)
        title_text=str(title.stdout.read())
        textbox(msg='',title='运行信息：',text=title_text)
    else:
        txt=fileopenbox(msg='',title='脚本文件:')
        count=int(enterbox(msg='',title='执行次数：',default='1'))
        Popen('adb  push '+txt+'  /data/local/tmp',stdout=PIPE)
        print('执行脚本命令中---------')
        title=Popen('adb shell monkey -f /data/local/tmp/'+txt+' --throttle 500 -v -v '+count,stdout=PIPE)
        title_text=str(title.stdout.read())
        textbox(msg='', title='运行信息：', text=title_text)