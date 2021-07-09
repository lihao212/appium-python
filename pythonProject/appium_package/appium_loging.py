# coding: utf-8
import logging,logging.handlers
import os,time
class logs(object):
    def __init__(self):
        self.logger=logging.getLogger("name")
        LEVELS={'NOSET':logging.NOTSET,
                'DEBUG':logging.DEBUG,
                'INFO':logging.INFO,
                'WARNING':logging.WARNING,
                'ERROR':logging.ERROR,
                'CRITICAL':logging.CRITICAL
                }
        logs_dir=r'D:\logs'
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)
        # 修改log保存位置
        log_time=time.strftime('%Y%m%d%H%M%S',time.localtime())
        logfilename='%s.txt' % log_time
        logfilepath=os.path.join(logs_dir,logfilename)
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=logfilepath,maxBytes=1024*1024*50,backupCount=3,encoding='utf-8')

        #设置输出格式
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s','%Y-%m-%d %H:%M:%S')
        rotatingFileHandler.setFormatter(formatter)

        #控制台句柄
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(formatter)
        if not self.logger.handlers:
        #添加内容到日志句柄中
            self.logger.addHandler(rotatingFileHandler)
            self.logger.addHandler(console)
            self.logger.setLevel(logging.DEBUG)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)


logger=logs()


def get_log(func):  # 装饰器获取测试代码的详细信息
            def try_log(*args,**kwargs):
                if func.__name__ == "__init__":
                    logger.info("[START] %s" % "初始化参数...")
                else:
                    logger.info("[START] %s" % func.__name__)
                start_time=time.time()
                try:
                    func(*args,**kwargs)
                except Exception as e:
                    logger.error("%s" % str(e))
                    # os._exit(0)
                end_time=time.time()
                time_long=(end_time-start_time)*1000
                logger.info("[END] %s,duration of time: %.2fms" %(func.__name__, time_long))
            return try_log