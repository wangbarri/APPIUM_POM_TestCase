from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait as wd
from selenium.webdriver.support import expected_conditions as ec
import unittest
import os, time

class AppBuild_Test(unittest.TestCase):
 
    def setUp(self):

        # app = os.path.join(os.path.dirname(__file__), r'C:\ProgramData\Jenkins\.jenkins\workspace\AOS\app\build\outputs\apk\debug', 'app-debug.apk')
        # app = os.path.abspath(app)

        desired_caps = {
        # "app" : app,
        "platformName" : "Android",
        "deviceName" : "R3CN305LTJZ",
        "platformVersion": "12",
        "automationName": "Appium", # default : Appium
        "newCommandTimeout":"72000",
        "appPackage": "com.example.buillld",
        "appActivity": "com.example.buillld.MainActivity",
        "noReset" : True,
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

    def test_case_1_button(self):
        
        click = wd(driver=self.driver, timeout=5).until(ec.element_to_be_clickable((AppiumBy.ID,"com.example.buillld:id/button")))
        click.click()
    
    def test_case_2_Number(self):
        click = wd(driver=self.driver, timeout=5).until(ec.element_to_be_clickable((AppiumBy.ID,"com.example.buillld:id/button")))
        click.click()
        
        for x in range(1,7):
            number = self.driver.find_element(AppiumBy.ID,"com.example.buillld:id/textView%x" %x).text

            print(number,end="  ")

        

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppBuild_Test)
    unittest.TextTestRunner(verbosity=2).run(suite)