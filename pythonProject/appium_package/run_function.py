# coding:utf-8
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium_package.appium_loging import *
from appium.webdriver.common.touch_action import TouchAction
from appium_package.yaml_util import *
import re


class OperateWindow(object):
    @get_log
    def __init__(self,args,ralcaps):
        self.port = args['port']
        self.host = args['host']
        self.driver = webdriver.Remote("http://%s:%s/wd/hub" % (self.host,self.port), ralcaps)
        self.caps = ralcaps
        self.touch = TouchAction(self.driver)

    @get_log
    def process_windows(self, count, pop_info):
        for i in range(count):
            info = pop_info
            loc = '//*[contains(@text，"%s")]' % info
            try:
                WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,loc))[0]).click()
            except Exception as e:
                pass

    @get_log
    def found_thoast(self, thoast_info):
        thoast = thoast_info
        toast_loc = ("xpath", '//*[contains(@text,"%s")]' % thoast)
        try:
            t = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(toast_loc))
            if t:
                raise Exception("Thoast 已确认!")
        except:
            raise Exception("Thoast 信息未找到")

    @get_log
    def into_setting(self):  # 进入设置界面

        set_id = '//*[@resource-id="%s:id/iv_goto_mine"]' % self.caps["appPackage"]  # 通过xpath定位元素
        self.driver.find_element_by_xpath(set_id).click()
        self.driver.implicitly_wait(10)

    @get_log
    def switch_model(self):  # 切换简易模式
        model_id = '//*[@resource-id="%s:id/switch_button"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(model_id).click()
        self.driver.implicitly_wait(10)

    @get_log
    def open_off_pic(self):  # 双光开关
        doublepic_id = '//*[@resource-id="%s:id/iv_pic"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(doublepic_id).click()
        self.driver.implicitly_wait(10)

    @get_log
    def pic_xuan(self):  # 双光旋转开关
        tem_id = '//*[@resource-id="%s:id/iv_xuan"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(tem_id).click()
        self.driver.implicitly_wait(10)

    @get_log
    def operate_shutter(self):  # 打快门开关
        shutter_id = '//*[@resource-id="%s:id/iv_kuaimen"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(shutter_id).click()
        self.driver.implicitly_wait(10)

    @get_log
    def into_picture(self):  # 进入图库
        pic_id = '//*[@resource-id="%s:id/iv_goto_gallery"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(pic_id).click()
        self.driver.implicitly_wait(10)

    @get_log
    def recorde_vedio(self, long_time):  # 拍摄录像
        video_id = '//*[@resource-id="%s:id/iv_recodeing"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(video_id).click()
        self.driver.implicitly_wait(10)
        time.sleep(long_time)
        self.driver.find_element_by_xpath(video_id).click()
        self.driver.implicitly_wait(10)

    @get_log
    def photo_pic(self):  # 拍照
        camera_id = '//*[@resource-id="%s:id/iv_camera"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(camera_id).click()

    @get_log
    def switch_color(self, color_style):  # 切换伪彩
        color_stytle_id = '//*[@resource-id="%s:id/iv_fitter"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(color_stytle_id).click()
        self.driver.implicitly_wait(10)
        size = self.driver.get_window_size()
        print(size)

        def color_chose():
            loc = '//*[@resource-id="%s:id/tv_Name"and@text="%s"]/../android.widget.ImageView' \
                  % (self.caps["appPackage"],color_style)
            try:
                ral = self.driver.find_element_by_xpath(loc)
                if ral:
                    ral.click()
                    time.sleep(1)
                    self.touch.tap(None, size['width'] * 0.5, size['height'] * 0.5, 1).perform()
            except Exception:
                self.driver.swipe(size['width'] * 0.92, size['height'] * 0.95, size['width'] * 0.08,
                                  size['height'] * 0.95, 500)
                self.driver.find_element_by_xpath(loc).click()
                self.touch.tap(None, size['width'] * 0.5, size['height'] * 0.5, 1).perform()

        return color_chose()

    @get_log  # 推出测试
    def link_exit(self):
        self.driver.quit()

    @get_log  # 点测温
    def point_temp(self, point_x, point_y):
        point_id = '//*[@resource-id="%s:id/iv_jia"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(point_id).click()
        self.driver.implicitly_wait(10)
        self.touch.tap(None,point_x, point_y)

    @get_log  # 线测温
    def line_temp(self, start_x, start_y, end_x, end_y):
        line_id = '//*[@resource-id="%s:id/iv_xian"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(line_id).click()
        self.driver.implicitly_wait(10)
        self.driver.swipe(start_x, start_y, end_x, end_y)

    @get_log  # 框测温
    def rect_temp(self, start_x, start_y, end_x, end_y):
        rect_id = '//*[@resource-id="%s:id/iv_kuang"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(rect_id).click()
        self.driver.implicitly_wait(10)
        self.driver.swipe(start_x, start_y, end_x, end_y)

    @get_log  # 等温尺
    def biaochi(self):
        bc_id = '//*[@resource-id="%s:id/iv_biaochi"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(bc_id).click()
        self.driver.implicitly_wait(10)

    @get_log
    def remove(self):  # 删除
        dt_id = '//*[@resource-id="%s:id/iv_eraser"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(dt_id).click()
        self.driver.implicitly_wait(10)

    @get_log
    def get_pic_num(self):  # 获取图库中图片的数量并筛选
        tem_id = '//*[@resource-id="%s:id/selected_album"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(tem_id).click()
        self.driver.implicitly_wait(10)
        pic_id = '//*[@resource-id="%s:id/album_name" and @text="infisense"]/../android.widget.TextView[@index="2"]'\
                 % self.caps[
            "appPackage"]
        WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located((By.XPATH,pic_id)))
        pic_num = self.driver.find_element_by_xpath(pic_id).get_attribute('name')
        self.driver.find_element_by_xpath(pic_id).click()
        logger.info("pic_number: %d" % int(pic_num))

    @get_log
    def get_video_num(self):  # 获取图库中video的数量并筛选
        tem_id = '//*[@resource-id="%s:id/selected_album"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(tem_id).click()
        self.driver.implicitly_wait(10)
        video_id = '//*[@resource-id="%s:id/album_name" and @text="video"]/../android.widget.TextView[@index="2"]' \
                   % self.caps[
            "appPackage"]
        WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located((By.XPATH, video_id)))
        video_num = self.driver.find_element_by_xpath(video_id).get_attribute('name')
        self.driver.find_element_by_xpath(video_id).click()
        logger.info("video_number: %d" % int(video_num))

    @get_log
    def get_all_num(self):  # 获取图库中所有的数量并筛选
        tem_id = '//*[@resource-id="%s:id/selected_album"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(tem_id).click()
        self.driver.implicitly_wait(10)
        all_id = '//*[@resource-id="%s:id/album_name" and @text="全部"]/../android.widget.TextView[@index="2"]' \
                 % self.caps[
            "appPackage"]
        WebDriverWait(self.driver, 30, 0.5).until(EC.visibility_of_element_located((By.XPATH, all_id)))
        all_num = self.driver.find_element_by_xpath(all_id).get_attribute('name')
        self.driver.find_element_by_xpath(all_id).click()
        logger.info("all_number: %d" % int(all_num))

    @get_log
    def pic_de(self):  # 图库中图片删除
        tem_id = '//*[@resource-id="%s:id/button_apply"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(tem_id).click()
        self.driver.implicitly_wait(10)
        tem_id2 = '//*[@resource-id="%s:id/tv_ok"]' % self.caps["appPackage"]
        self.driver.find_element_by_xpath(tem_id2).click()
        self.driver.implicitly_wait(10)

    @get_log
    def choose_pic(self, number):  # 选中图库中图片元素
        size = self.driver.get_window_size()
        for tem_idx in range(number):
            tem_id2 = '//*[@resource-id="%s:id/recyclerview"]/android.widget.FrameLayout[' \
                      '@index="%s"]/android.view.View' % (self.caps["appPackage"], tem_idx % 18)
            el = self.driver.find_element_by_xpath(tem_id2)
            self.touch.tap(el).perform()
            self.driver.implicitly_wait(10)
            tem_id = '//*[@resource-id="%s:id/button_apply"]' % self.caps["appPackage"]
            tem_text = self.driver.find_element_by_xpath(tem_id).text
            self.driver.implicitly_wait(10)
            temp_num = re.findall('删除\((.*?)\)', tem_text)
            time.sleep(0.5)
            if tem_idx % 18 == 17:
                self.driver.swipe(size['width'] * 0.5, size['height'] * 0.9, size['width'] * 0.5, size['height'] * 0.16)
                time.sleep(5)
                new=self.driver.page_source
                print(new)
    @get_log
    def ext_pic(self):  # 退出图库
        tem_id = '//*[@resource-id="%s:id/recyclerview" and @content-desc="转到上一层级"]'
        self.driver.find_element_by_xpath(tem_id).click()
        self.driver.implicitly_wait(10)
