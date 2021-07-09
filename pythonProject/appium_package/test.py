from appium import webdriver
from appium_package import caps_info,appium_loging,process_except,run_function

from appium.webdriver.common.touch_action  import TouchAction
# coding:utf-8
import time,datetime
caps_info.desir_caps(11,"PDSM00","com.infisense.usbCamera_rc")

driver=run_function.control_link()
driver.creat_link()
proce=process_except.solve()
proce.process_windows(5,"允许")
running=run_function.operate()
running.photo_pic()
running.switch_color('彩虹1')
driver.quit()