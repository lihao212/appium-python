from monkey_run_function import *
import time
def runner():

    connect()
    t=msgbox(msg='请在手机上打开要运行的APP程序！',title='')
    time.sleep(5)
    if t=="OK":
        get_pacage()
    run()
if __name__ == '__main__':
    runner()
