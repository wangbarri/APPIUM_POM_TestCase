from appium.webdriver.common.appiumby import AppiumBy
from dpvldna.Config.Accounts import *
from dpvldna.Pages.Base import BaseCommands
import time

class Naver_MY(BaseCommands):

    MyPage = (AppiumBy.ID,"com.nhn.android.webtoon:id/my")
    Favorite_webtoon = (AppiumBy.ACCESSIBILITY_ID,"관심웹툰")
    Favorite_image = (AppiumBy.ID,"com.nhn.android.webtoon:id/empty_image")
    
    recently_seen = (AppiumBy.ACCESSIBILITY_ID,"최근 본")
    recently_image = (AppiumBy.ID,"com.nhn.android.webtoon:id/imageview_myrecent_empty")
    temporary_storage = (AppiumBy.ACCESSIBILITY_ID,"임시저장")
    comment = (AppiumBy.ACCESSIBILITY_ID,"댓글")
    comment_image = (AppiumBy.ID,"com.nhn.android.webtoon:id/imageview_empty")
    locker = (AppiumBy.ACCESSIBILITY_ID,"보관함")

                                 
    def __init__(self, driver):
        super(Naver_MY,self).__init__(driver)

    def MyPage_state(self):
        #마이페이지 진입 각 메뉴 노출 및 항목 미존재 시 안내 문구 확인

        self.Click(self.MyPage)
        # 마이페이지 확인
        a = self.inter.driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView').text
        assert a == "MY" , "마이페이지가 아닙니다."

        # 관심웹툰  (저장된 웹툰이 없는 겨우 빈 메시지 노출확인)
        self.Click(self.Favorite_webtoon)
        a =  self.inter.driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView').text                                                  
        time.sleep(1)
        assert a == "관심웹툰이 없습니다." , "메시지가 노출되지 않았습니다."
        self.Find_Element(self.Favorite_image)

        # 최근 본 (저장된 웹툰이 없는 겨우 빈 메시지 노출확인)
        self.Click(self.recently_seen)
        time.sleep(1)
        
        b =  self.inter.driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView').text                                                  
        assert b == "최근 본 웹툰이 없습니다." , "메시지가 노출되지 않았습니다."
        self.Find_Element(self.recently_image)

        # 임시저장 (저장된 웹툰이 없는 겨우 빈 메시지 노출확인)
        self.Click(self.temporary_storage)
        time.sleep(2)

        c =  self.inter.driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView').text                                                 
        assert c == "임시저장 웹툰이 없습니다." , "메시지가 노출되지 않았습니다."
        self.Find_Element(self.Favorite_image)

        # 댓글 (저장된 웹툰이 없는 겨우 빈 메시지 노출확인)
        self.Click(self.comment)
        time.sleep(2)
        
        d =  self.inter.driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView').text                                                  
        assert d == "작성한 댓글이 없습니다." , "메시지가 노출되지 않았습니다."
        self.Find_Element(self.comment_image)

        # 보관함 (저장된 웹툰이 없는 겨우 빈 메시지 노출확인)
        self.Click(self.locker)
        time.sleep(2)

        f =  self.inter.driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[1]').text                                                  
        assert f == "보관중인 콘텐츠가 없습니다." , "메시지가 노출되지 않았습니다."
    
    def Swip_Menu(self):
        # 메뉴 스와이프 이동 확인
        for i in range(6):
            if len(self.inter.driver.find_elements(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView')) > 0:
                self.Swip(x1=1010, y1=1220, x2=100, y2=1220)
            else:
                self.Swip(x1=100, y1=1220, x2=1010, y2=1220)

