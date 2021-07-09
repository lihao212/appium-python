
from appium_package import caps_info, run_function, yaml_util
from appium_package.appium_loging import *
import pytest, os, shutil, allure


@allure.feature('测试模块')
@allure.description("测试脚本运行报告")
class TestAppium:
    @allure.story('配置caps')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step('测试使用')
    @pytest.mark.parametrize('test_config', yaml_util.UtilYaml('test.yaml').read_yaml(), indirect=True)
    def test_01(self, test_config):
        p_caps = yaml_util.GetYaml(test_config).get_caps()
        server = yaml_util.GetYaml(test_config).get_server()
        temp_caps = caps_info.desir_caps(p_caps).set_caps()

        print(temp_caps)
        running = run_function.OperateWindow(server, temp_caps)
        pass
        # logger.info("创建链接！")
        # running.process_windows(5, "允许")
        # time.sleep(5)
        # running.into_picture()
        # time.sleep(1)
        # running.get_pic_num()
        # time.sleep(1)
        # running.choose_pic(10)
        # time.sleep(1)
        # running.pic_de()
        # time.sleep(3.0)
        # running.link_exit()


if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./temp -o ./reports --clean')
    shutil.rmtree('./temp')
    os.mkdir('./temp')

# driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
# driver.swipe()
# time.sleep(10)
# touch=TouchAction(driver)
# lk='resoureceId().'
# size=driver.swipe
#
# def run(count,interval_time):
#     for i in range(0,count):
#         driver.find_element_by_id("com.infisense.usbCamera_fc:id/iv_fitter").click()
#         driver.implicitly_wait(interval_time)
#         touch.tap(None,700, 2200).perform()
#         time.sleep(2)
#         touch.tap(None,256, 656).perform()
#         time.sleep(2)
#         driver.find_element_by_id("com.infisense.usbCamera_fc:id/iv_recodeing").click()
#         time.sleep(2)
#         driver.find_element_by_id("com.infisense.usbCamera_fc:id/iv_camera").click()
#         time.sleep(interval_time)
#         driver.find_element_by_id("com.infisense.usbCamera_fc:id/iv_recodeing").click()
#         time.sleep(interval_time)
#         driver.find_element_by_id("com.infisense.usbCamera_fc:id/iv_goto_gallery").click()
#         driver.implicitly_wait(5)
#         driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='转到上一层级']").click()
#         driver.implicitly_wait(15)
#         print(i)
#         time.sleep(3)
#     print('success')
# try:
#  run(50,2)
# except Exception as e:
#     print(str(e))
#     path = r'D:\blog\test_login_error_01.png'
#     driver.get_screenshot_as_file(path)
# time.sleep(30)
# print("==========================================================================================\n========================================================================")
# driver.quit()
