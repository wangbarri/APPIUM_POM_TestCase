from appium import webdriver
from dpvldna.Config.Accounts import IP

class Driver():
    
    def __init__(self):
        desired_caps = {
        "platformName" : "Android",
        "deviceName" : "단말 번호",
        "platformVersion": "단말 버전",
        "automationName": "Appium", # default : Appium
        "newCommandTimeout":"72000",
        "noReset" : True,
        "appPackage": "실행 앱",
        "appActivity": "실행 앱"
            }
        self.driver = webdriver.Remote(IP["device1"]+":4723/wd/hub",desired_caps)