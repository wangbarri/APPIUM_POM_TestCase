from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from dpvldna.Config.Accounts import *
from dpvldna.Pages.Base import BaseCommands
import time, random

class Naver_Pecently(BaseCommands):

    recently_seen = (AppiumBy.ACCESSIBILITY_ID,"최근 본")
    # 전체 개수
    total_count = (AppiumBy.ID,"com.nhn.android.webtoon:id/textview_my_info_tab_all")
    
    # 지금 볼 버튼
    Now_view_btn = (AppiumBy.ID,"com.nhn.android.webtoon:id/textview_my_info_tab_now")
    
    # 웹툰 제목 , 새 이야기 element
    webtoon_title = (AppiumBy.ID,"com.nhn.android.webtoon:id/recent_webtoon_title")
    succession_webtoon = (AppiumBy.ID,"com.nhn.android.webtoon:id/recent_webtoon_description")
    
    # 지금 볼 화면 웹툰 선택
    Now_view_webtoon = (AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]")

    # 편집 버튼    
    edit_btn = (AppiumBy.ID,"com.nhn.android.webtoon:id/textview_my_info_edit")
    # 선택 버튼
    edit_select = (AppiumBy.ID,"com.nhn.android.webtoon:id/textview_my_edit_top_select_all")
    # 취소 버튼
    edit_cancel = (AppiumBy.ID,"com.nhn.android.webtoon:id/textview_my_edit_bottom_cancel")
    # 선택삭제
    edit_Delete_Selection = (AppiumBy.ID,"com.nhn.android.webtoon:id/textview_my_edit_bottom_delete")
    # 웹툰 선택
    edit_webtoon = (AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup")
    # 선택해제
    edit_Deselect = (AppiumBy.XPATH,"//android.widget.TextView[@text = '선택해제']")

    edit_alert_massage = (AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.TextView")
    edit_alert_ok = (AppiumBy.ID,"android:id/button1")
    edit_alert_webtoon_delete = (AppiumBy.ID,"android:id/button1")
    edit_alert_webtoon_not_delete = (AppiumBy.ID,"android:id/button2")

    webtoon_clear = (AppiumBy.ID,"com.nhn.android.webtoon:id/textview_recent_now_clear")
    rank_reset_btn = (AppiumBy.ID,"com.nhn.android.webtoon:id/icon_refresh_recommendcomponenthome")
    week_rank_btn = (AppiumBy.XPATH,"//android.widget.ImageView[@content-desc='더보기']")
    week_rank_guide = (AppiumBy.XPATH,"//android.widget.ImageView[@content-desc='도움말']")
    Order_btn = (AppiumBy.ID,"com.nhn.android.webtoon:id/my_info_sort_type")
    ALL_Order_btn = (AppiumBy.XPATH,'//android.widget.TextView[@text = "전체"]')
    Man_Order_btn = (AppiumBy.XPATH,'//android.widget.TextView[@text = "남성"]')
    Wommen_Order_btn = (AppiumBy.XPATH,'//android.widget.TextView[@text = "여성"]')

    def __init__(self, driver):
        super(Naver_Pecently, self).__init__(driver)
        self.driver = self.inter.driver 

    def Total_count(self):
        self.Click(self.recently_seen)
        # 전체 등록 개수 확인
        self.Text(self.total_count)
        
        if self.inter.driver.find_elements(*self.total_count) == "전체 100":
            print("전체 50건 관심웹툰 등록 완료하였습니다.")
        
    def Now_View(self):
        # 최근 본 전체 리스트에서 웹툰 선택 후 페이지 진입 확인
        self.Click(self.Now_view_webtoon)
        self.driver.back()

        # 전체 웹툰 중 최신 이야기를 보지 않은 웹툰이 지금 볼 웹툰에 항목이 노출되는지 확인

        new_story = self.driver.find_elements(*self.succession_webtoon)
        for i in new_story:
            b = i.find_element(*self.succession_webtoon).text[:5]
            print(b)
        
        assert b == "새 이야기" , "새로운 이야기가 존재 하지 않습니다."

        self.Click(self.Now_view_btn)

    def Now_view_edit(self):
        # 지금 볼 편집 화면 이동 확인
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
        assert self.driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView[2]").text == "선택" , "선택해제가 되지 않았습니다."

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
        assert self.driver.find_element(*self.edit_alert_massage).text == "최근 본 웹툰에서 삭제하시겠습니까?"
        self.Click(self.edit_alert_webtoon_not_delete)

        
        self.Click(self.edit_Delete_Selection)
        assert self.driver.find_element(*self.edit_alert_massage).text == "최근 본 웹툰에서 삭제하시겠습니까?"
        self.Click(self.edit_alert_webtoon_delete)

        # 웹툰 항목이 존재 할 경우 선택삭제 확인(전체 웹툰선택)
        self.Click(self.edit_btn)
        self.Click(self.edit_select)
        self.Click(self.edit_Delete_Selection)
        assert self.driver.find_element(*self.edit_alert_massage).text == "최근 본 웹툰에서 삭제하시겠습니까?"
        self.Click(self.edit_alert_webtoon_not_delete)

        

        self.Click(self.edit_Delete_Selection)
        assert self.driver.find_element(*self.edit_alert_massage).text == "최근 본 웹툰에서 삭제하시겠습니까?"
        self.Click(self.edit_alert_webtoon_delete)

        # 전체 웹툰 중 지금 볼 웹툰이 없는 경우 지금 볼 화면에 클리어 웹툰 문구 확인
        self.Find_Element(self.webtoon_clear)
        self.driver.find_element(AppiumBy.ID,"com.nhn.android.webtoon:id/textview_recent_now_clear_description").text == "최근 감상한 작품 100개 중,새로운 에피소드가 생긴 작품들을 모두 감상하셨네요!"

    def Webtoon_rank(self):
        # 웹툰 랭킹으로 다른 추천 변경 버튼 클릭 및 페이지 수 카운트 확인
        self.Find_Element((AppiumBy.ACCESSIBILITY_ID,"1페이지"))
        self.Click(self.rank_reset_btn)

        # 웹툰 랭킹 1 ~ 9윌까지 노출 확인
        count = 1
        for a in range(9):
            if len(self.driver.find_elements(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%s]" %a)) > 0:
               print(str(count) + "위")                                         
            
            count += 1
            if count == 6:
                self.Swip(x1=1000,y1=1500,x2=100,y2=1500)

        # 독자들이 많이 본 추천 완결
        self.Click(self.rank_reset_btn)
        self.Find_Element((AppiumBy.ACCESSIBILITY_ID,"2페이지"))

        count = 1
        for a in range(30):
            if len(self.driver.find_elements(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[%s]" %a)) > 0:
               print(str(count) + "위")                                         
            
            count += 1
            if count == 3:
                self.Swip(x1=1000,y1=1500,x2=100,y2=1500)

    def week_webtoon_rank(self):
        # 이번 주 추천완결 신작 웹툰 랭킹 진입
        self.Click(self.week_rank_btn)
        assert self.driver.find_element(AppiumBy.ID,"com.nhn.android.webtoon:id/curation_title").text == "이번 주 추천완결 신작 웹툰 랭킹"
        self.Click(self.week_rank_guide)
        # 정렬 확인
        self.Click(self.Order_btn)
        self.Click(self.ALL_Order_btn)
        assert self.driver.find_element(*self.Order_btn).text == "전체" , "체크되지 않았습니다."
        
        self.Click(self.Order_btn)
        self.Click(self.Man_Order_btn)
        assert self.driver.find_element(*self.Order_btn).text == "남성" , "체크되지 않았습니다."

        self.Click(self.Order_btn)
        self.Click(self.Wommen_Order_btn)
        assert self.driver.find_element(*self.Order_btn).text == "여성" , "체크되지 않았습니다."

        self.Click(self.Order_btn)
        self.Click((AppiumBy.XPATH,'//android.widget.Button[@content-desc="취소"]/android.widget.ImageView'))
        self.Click(self.Order_btn)
        
        touch = TouchAction(self.inter.driver)
        touch.tap(x=random.randrange(1,1300) , y=random.randrange(1,1300)).release().perform()
        
        self.driver.back()
        # 전체 홈 가기
        self.Click(self.total_count)

