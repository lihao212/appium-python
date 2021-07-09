# coding:utf-8
class desir_caps(object):
    def __init__(self,path_caps):
        self.caps = {}
        self.caps["platformName"] = "Android"
        self.caps["appActivity"] = "com.infisense.p2.activity.MainActivity"
        self.caps["automationName"] = "Uiautomator2"
        self.caps["skipServerInstallation"] = True
        self.caps["skipDeviceInitialization"] = True
        self.caps["resetKeyboard"] = True
        self.caps["unicodeKeyboard"] = True
        self.caps["noReset"] = True
        self.path_caps = path_caps

    def set_caps(self):
        self.caps.update(self.path_caps)
        return self.caps