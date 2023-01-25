from appium.webdriver.common.appiumby import AppiumBy
from dpvldna.Config.Accounts import *
from dpvldna.Pages.Base import BaseCommands
import time , random

class SinhanPlay_EventPages(BaseCommands):

    first_Popup = (AppiumBy.ID,"com.shcard.smartpay:id/ivPopup")
    first_Popup_close = (AppiumBy.ID,"com.shcard.smartpay:id/ivClose")
    
    Benefit_btn = (AppiumBy.XPATH,"//android.widget.TextView[@text = '혜택']")
    
    Event_menu_btn = (AppiumBy.XPATH,"//android.widget.LinearLayout[@content-desc='이벤트']/android.widget.TextView")
    Event_main_close = (AppiumBy.ID,"com.shcard.smartpay:id/imgv_right_btn")
    
    Event_attendance_check_btn = (AppiumBy.XPATH,"//android.widget.TextView[@text = '매일매일 pLay 출첵하면, 커지는 혜택!']")
    Event_attendance_check_Url_btn = (AppiumBy.XPATH,"//android.widget.Button[@text = '출석체크 이벤트 바로가기']")
    Event_attendance_check_compleate = (AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.widget.Button")
    Event_attendance_check_Point = (AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Image")
    Event_attendance_check_close = (AppiumBy.XPATH,'(//android.view.View[@content-desc="javascript:void(0)"])[2]')
    
    Event_NewYear_btn = (AppiumBy.XPATH,'//android.view.View[@content-desc="2 신년맞이 까망토끼를 찾아라"]')
    Event_NewYear_Url_btn = (AppiumBy.XPATH,'//android.widget.Button[@text = "까망토끼 찾으러 가기"]')
    Event_NewYear_start_btn = (AppiumBy.XPATH,'//android.view.View[@content-desc="까망 토끼 찾으러가기 버튼"]/android.widget.Image')
    Event_NewYear_result_btn = (AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.Button')
    Event_NewYear_Point = (AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Image')
    Event_NewYear_close = (AppiumBy.XPATH,'(//android.view.View[@content-desc="javascript:void(0)"])[2]')
    

    def __init__(self, driver):
        super(SinhanPlay_EventPages,self).__init__(driver)
        self.driver = self.inter.driver
        
    def Event_Page_join(self):
        # 최초 팝업 닫기
        if len(self.driver.find_elements(*self.first_Popup)) > 0:
            self.Click(self.first_Popup_close)
        
        # 이벤트 페이지까지 진입
        self.Click(self.Benefit_btn)
        self.Click(self.Event_menu_btn)
        assert self.driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text = '지금 뜨는 이벤트']").text == "지금 뜨는 이벤트"
    
    def Event_attendance_check(self):
        # 매일매일 Play 출첵 혜택 이벤트 진행
        self.Click(self.Event_attendance_check_btn)

        # 매일매일 Play 출첵 바로가기 버튼 및 포인트 획득 완료
        while True:
            if len(self.driver.find_elements(*self.Event_attendance_check_Url_btn)) > 0:
                self.Click(self.Event_attendance_check_Url_btn)
            
            elif len(self.driver.find_elements(*self.Event_attendance_check_compleate)) > 0:
                    self.Click(self.Event_attendance_check_compleate)
                    break
            else:
                self.Swip(x1=550,y1=2000,x2=550,y2=600)
        self.Text(self.Event_attendance_check_Point) # 획득 포인트 확인
        self.Click(self.Event_attendance_check_close) # 획득 팝업창 닫기
        self.Click(self.Event_main_close) # 이벤트 페이지 나가기
        time.sleep(1)
        self.Click(self.Event_main_close) # 메인화면으로 나가기

    def Event_New_Year(self):
        # 신년맞이 까망 토끼를 찾아라 이벤트 진행
        self.Click(self.Event_NewYear_btn)

        # 까망토끼 찾으러 가기 버튼 탐색 및 선택하기
        while True:
            if len(self.driver.find_elements(*self.Event_NewYear_Url_btn)) > 0:
                self.Click(self.Event_NewYear_Url_btn)
                time.sleep(2)
                a = self.driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.widget.TextView').text
                print("적립" + str(a) + "일차 입니다.")

            elif len(self.driver.find_elements(*self.Event_NewYear_start_btn)) > 0:
                    self.Click(self.Event_NewYear_start_btn)
                    break
            else:
                self.Swip(x1=550,y1=2000,x2=550,y2=600)
        
        # 까망 토끼 카드를 랜덤으로 선택
        one = random.randrange(1,4)
        two = random.randrange(1,4)
        a = (AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[%s]/android.widget.Image'%one)
        b = (AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[%s]/android.widget.Image'%two)
        self.Click(a)
        self.Click(b)
        
        # 랜덤 선택 후 찾기 완료 버튼 선택 및 획득 포인트 확인
        self.Click(self.Event_NewYear_result_btn)
        self.Text(self.Event_NewYear_Point)
        self.Click(self.Event_NewYear_close)

        self.Click(self.Event_main_close)
        time.sleep(1)
        self.Click(self.Event_main_close)












