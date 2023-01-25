from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from dpvldna.Config.Accounts import *
from dpvldna.Pages.Base import BaseCommands
import time, random

class Naver_Favorite(BaseCommands):
    Favorite_webtoon = (AppiumBy.ACCESSIBILITY_ID,"관심웹툰")

    total_count = (AppiumBy.ID,"com.nhn.android.webtoon:id/textview_my_info_tab_all")
    
    Order_btn = (AppiumBy.ID,"com.nhn.android.webtoon:id/my_info_sort_type")
    Update_Order_btn = (AppiumBy.XPATH,'//android.widget.TextView[@text = "업데이트순"]')
    New_Order_btn = (AppiumBy.XPATH,'//android.widget.TextView[@text = "최근등록순"]')
    Order_exit_btn = (AppiumBy.XPATH,"//android.widget.Button[@content-desc='취소']/android.widget.ImageView")
    Order_assert = (AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView')
    # 편집 버튼
    edit_btn = (AppiumBy.ID,"com.nhn.android.webtoon:id/textview_my_info_edit")
    # 선택 버튼
    edit_select = (AppiumBy.ID,"com.nhn.android.webtoon:id/textview_my_edit_top_select_all")
    # 취소 버튼
    edit_cancel = (AppiumBy.ID,"com.nhn.android.webtoon:id/textview_my_edit_bottom_cancel")
    # 선택삭제
    edit_Delete_Selection = (AppiumBy.ID,"com.nhn.android.webtoon:id/textview_my_edit_bottom_delete")
    # 웹툰 선택
    edit_webtoon = (AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]")
    # 선택해제
    edit_Deselect = (AppiumBy.XPATH,"//android.widget.TextView[@text = '선택해제']")
    
    edit_alert_massage = (AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView")
    edit_alert_ok = (AppiumBy.ID,"android:id/button1")
    edit_alert_webtoon_delete = (AppiumBy.ID,"android:id/button1")
    edit_alert_webtoon_not_delete = (AppiumBy.ID,"android:id/button2")
    
    favorite_webtoon = (AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]")
    favorite_webtoon_date = (AppiumBy.ID,"com.nhn.android.webtoon:id/favorite_webtoon_update_text")
    favorite_webtoon_alram = (AppiumBy.XPATH,"(//android.widget.ImageView[@content-desc='알림 켜져있음'])")

    def __init__(self, driver):
        super(Naver_Favorite, self).__init__(driver)
        self.driver = self.inter.driver 

    def Total_count(self):
        self.Click(self.favorite_webtoon)
        # 전체 등록 개수 확인
        self.Text(self.total_count)
        
        if self.inter.driver.find_elements(*self.total_count) == "전체 50":
            print("전체 50건 관심웹툰 등록 완료하였습니다.")
        
    def Favorite_Order(self):
        # 관심웹툰 최근등록순 / 업데이트 순 정렬 기능 확인 및 무작위 위치 터치로 팝업창 닫힘 확인

        self.Click(self.Order_btn)
        self.Click(self.Update_Order_btn)
        assert self.driver.find_element(*self.Order_assert).text == "업데이트순" , "체크되지 않았습니다."
        
        self.Click(self.Order_btn)
        self.Click(self.New_Order_btn)
        assert self.driver.find_element(*self.Order_assert).text == "최근등록순" , "체크되지 않았습니다."

        self.Click(self.Order_btn)
        touch = TouchAction(self.inter.driver)
        touch.tap(x=random.randrange(1,1300) , y=random.randrange(1,1300)).release().perform()

    def Favorite_edit(self):

        # 편집 화면 이동 확인
        self.Click(self.edit_btn)

        # 버튼 노출 확인
        self.Find_Element(self.edit_select)
        self.Find_Element(self.edit_Delete_Selection)
        self.Find_Element(self.edit_cancel)
        
        # 웹툰 1개 선택
        self.Click(self.edit_webtoon)
        
        # 웹툰 선택 시 선택해제 버튼 노출 확인 및 클릭
        self.Find_Element(self.edit_Deselect)
        self.Click(self.edit_Deselect)
        assert self.driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout/android.widget.TextView[2]").text == "선택" , "선택해제가 되지 않았습니다."

        # 편집화면 내 취소 버튼 클릭 확인
        self.Click(self.edit_cancel)
        self.Click(self.edit_btn)

        # 웹툰 미선택 시 선택삭제 팝업 노출 확인
        self.Click(self.edit_Delete_Selection)
        time.sleep(1)
        assert self.driver.find_element(*self.edit_alert_massage).text == "삭제 선택한 웹툰이 없습니다."
        self.Click(self.edit_alert_ok)
        
        
        # 웹툰 항목이 존재 할 경우 선택삭제 확인(각 웹툰선택)
        self.Click(self.edit_webtoon)
        self.Click(self.edit_Delete_Selection)
        assert self.driver.find_element(*self.edit_alert_massage).text == "관심웹툰에서 삭제하시겠습니까?"
        self.Click(self.edit_alert_webtoon_not_delete)

        
        self.Click(self.edit_Delete_Selection)
        assert self.driver.find_element(*self.edit_alert_massage).text == "관심웹툰에서 삭제하시겠습니까?"
        self.Click(self.edit_alert_webtoon_delete)

        # 웹툰 항목이 존재 할 경우 선택삭제 확인(전체 웹툰선택)
        self.Click(self.edit_btn)
        self.Click(self.edit_select)
        self.Click(self.edit_Delete_Selection)
        assert self.driver.find_element(*self.edit_alert_massage).text == "관심웹툰에서 삭제하시겠습니까?"
        self.Click(self.edit_alert_webtoon_not_delete)

        
        self.Click(self.edit_Delete_Selection)
        assert self.driver.find_element(*self.edit_alert_massage).text == "관심웹툰에서 삭제하시겠습니까?"
        self.Click(self.edit_alert_webtoon_delete)

    def Favorite_Webtoon(self):
        # 웹툰 선택 및 웹툰 페이지 진입 
        self.Click(self.Favorite_webtoon)
        self.driver.back()
        self.Find_Element(self.favorite_webtoon_date)

        # 웹툰 알람 선택 및 해제 확인
        self.Click(self.favorite_webtoon_alram) # 알람 off
        assert len(self.driver.find_elements(AppiumBy.XPATH,"//android.widget.ImageView[@text = '알림 꺼져있음']")) > 0 

        self.driver.find_element(AppiumBy.XPATH,"//android.widget.ImageView[@text = '알림 꺼져있음']").click()
        assert len(self.driver.find_elements(AppiumBy.XPATH,"//android.widget.ImageView[@text = '알림 켜져있음']")) > 0 










