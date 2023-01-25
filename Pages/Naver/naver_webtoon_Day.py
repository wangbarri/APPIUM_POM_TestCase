from appium.webdriver.common.appiumby import AppiumBy
from dpvldna.Config.Accounts import *
from dpvldna.Pages.Base import BaseCommands
import time

class Naver_Webtoon(BaseCommands):


    Monday = (AppiumBy.XPATH,'//android.widget.TextView[@content-desc="월요 연재"]')
    Tuesday = (AppiumBy.XPATH,'//android.widget.TextView[@content-desc="화요 연재"]')
    Wednesday = (AppiumBy.XPATH,'//android.widget.TextView[@content-desc="수요 연재"]')
    Thursday = (AppiumBy.XPATH,'//android.widget.TextView[@content-desc="목요 연재"]')
    Friday = (AppiumBy.XPATH,'//android.widget.TextView[@content-desc="금요 연재"]')
    Saturday = (AppiumBy.XPATH,'//android.widget.TextView[@content-desc="토요 연재"]')
    Sunday = (AppiumBy.XPATH,'//android.widget.TextView[@content-desc="일요 연재"]')
    
    Favorite_btn = (AppiumBy.XPATH, '(//android.widget.Button[@content-desc="관심"])[2]/android.widget.ImageView')

    def __init__(self, driver):
        super(Naver_Webtoon,self).__init__(driver)
    
    def Day_webtoon(self):
        # 일 별 웹툰 확인
        count = 1
        page = 5
        # 클릭
        self.Click(self.Monday)
        # 해당 웹툰 리스트 순으로 검색 및 스와이프
        for i in range(len(Wetoon_monday)):
            toon = (AppiumBy.XPATH, '//android.widget.TextView[@text = "%s"]' %Wetoon_monday[i])
            self.Click(toon)
            self.Click(self.Favorite_btn)
            time.sleep(1.5)
            self.inter.driver.back()
            
            count += 1
            
            print(count)
            print(page)

            if count == page:
                self.inter.driver.swipe(520,1880,520,1300,1000)
                page += 2
    
        
                
                
