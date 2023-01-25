from appium.webdriver.common.appiumby import AppiumBy
from dpvldna.Config.Accounts import *
from dpvldna.Pages.Base import BaseCommands
import time , random

class SinhanPlus_EventPages(BaseCommands):

    first_Popup = (AppiumBy.ID,"com.shcard.smartpay:id/ivPopup")
    first_Popup_close = (AppiumBy.ID,"com.shcard.smartpay:id/ivClose")

    Wallet_btn = (AppiumBy.XPATH,'//android.widget.TextView[@text = "월렛"]')
    Sinhan_Plus_btn = (AppiumBy.ID,"com.shcard.smartpay:id/fabPlus")
    Event_page_btn = (AppiumBy.XPATH,'//android.widget.TextView[@text = "이벤트+"]')
    Event_ALL_list_btn = (AppiumBy.ID,"com.shcard.smartpay:id/shsp_benefit_event_arrow")
    Event_attendance_check_btn = (AppiumBy.XPATH,'//android.view.View[@text = "신한플러스 출석퀴즈"]')
    count_point = (AppiumBy.ID,'countPoint')
    Quiz_btn = (AppiumBy.XPATH,'//android.widget.Button[@text = "퀴즈 풀고 출석하기"]')
    Quiz_correct = (AppiumBy.XPATH,'//android.view.View[@content-desc="3. 400만원 이상 구매시 1.5p 혜택"]')
    Quiz_correct_check_btn = (AppiumBy.XPATH,'//android.widget.Button[@text = "정답확인"]')
    Check_btn = (AppiumBy.ACCESSIBILITY_ID,"확인")
    
    def __init__(self, driver):
        super(SinhanPlus_EventPages,self).__init__(driver)
        self.driver = self.inter.driver

    def Shihan_Plus_page_join(self):
        # 신한플러스 출석 퀴즈 페이지 진입 및 포인트 획득
        if len(self.driver.find_elements(*self.first_Popup)) > 0:
            self.Click(self.first_Popup_close)
        # 월렛 버튼 선택
        self.Click(self.Wallet_btn)
        # 신한 플러스 버튼 선택
        self.Click(self.Sinhan_Plus_btn)
        # 이벤트+ 탭 선택
        self.Click(self.Event_page_btn)
        # 전체 이벤트 보기 선택
        self.Click(self.Event_ALL_list_btn)
        # 출석체크 이벤트 선택
        self.Click(self.Event_attendance_check_btn)
        time.sleep(5) # 진입 로딩 대기
        self.Swip(x1=550,y1=2000,x2=550,y2=670)
        self.Click(self.Quiz_btn) # 퀴즈 풀고 출첵하기 버튼 선택
        self.Swip(x1=550,y1=2000,x2=550,y2=670) # 퀴츠 창 element 확인을 위한 화면 스크롤
        self.Click(self.Quiz_correct) # 정답 선택
        self.Click(self.Quiz_correct_check_btn) # 정답 확인
        self.Click(self.Check_btn)













