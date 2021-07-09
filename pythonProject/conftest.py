import pytest
# coding:utf-8
from appium_package import yaml_util, set_server
from appium_package.appium_loging import *


@pytest.fixture(scope='class', autouse=True)
def test_config(request):
    tem_value=request.param
    set_server.Controller(yaml_util.GetYaml(tem_value).get_server()).start_server()
    m = set_server.Controller(yaml_util.GetYaml(tem_value).get_server()).test_server()
    if m:
        logger.info("appium server start success!")
    yield request.param
    set_server.Controller(yaml_util.GetYaml(request.param).get_server()).kill_server()