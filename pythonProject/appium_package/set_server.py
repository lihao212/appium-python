# coding:utf-8
from subprocess import Popen,PIPE,getoutput
from yaml_util import *
from appium_loging import *

class Controller(object):
    def __init__(self,args):
        self.port = args['port']
        self.host = args['host']
        self.bootstrap_port = args['bootstrap_port']

    @get_log
    def start_server(self):
        cmd = "start appium -a %s -p %s -bp %s " % (self.host,self.port,self.bootstrap_port)
        Popen(cmd,shell=True,stdout=PIPE)

    @get_log
    def test_server(self):
        count = 1
        while count<=5:
            # 查询是否端口已启动，即服务启动
            c = getoutput('netstat -ano | findstr %s' % self.port)
            if c:

                logger.debug('%s 启动成功.........' % self.port)
                break
            else:
                logger.debug('%s 启动中...........'% self.port)
                time.sleep(5)
            count += 1
            if count>5:
                logger.error("无法启动appium_server!")
        return True
    @get_log
    def kill_server(self):
        Popen("taskkill /F /IM node.exe /t", shell=True, stdout=PIPE)
        logger.debug("关闭 appium_server....")
        Popen("adb kill-server", shell=True, stdout=PIPE)
        logger.debug("已关闭 appium_server!")