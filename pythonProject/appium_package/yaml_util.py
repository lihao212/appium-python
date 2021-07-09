
import yaml
from appium_loging import *


class UtilYaml:
    def __init__(self,yaml_file):
        self.yaml_file = yaml_file

    def read_yaml(self):
        with open(self.yaml_file,encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
        return value


class GetYaml:
    def __init__(self,yaml_value):
        self.value = yaml_value

    def get_caps(self):
        caps = self.value['part_caps']
        return caps

    def get_server(self):
        server = self.value['appium_server']
        return server


