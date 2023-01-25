from dpvldna.TestCase.Test import TestRun
from dpvldna.Pages.Naver.naver_webtoon_Day import Naver_Webtoon
from dpvldna.Pages.Naver.naver_webtoon_My import Naver_MY
from dpvldna.Pages.Naver.naver_Favorite_webtoon import Naver_Favorite
from dpvldna.Pages.Naver.naver_Recently import Naver_Pecently

import time

class TestCase(TestRun):

    def testcase_1_Naver(self):
        NW = Naver_Webtoon(self.inter)
        NW.Day_webtoon()

    def testcase_2_Naver_mypage(self):
        MY = Naver_MY(self.inter)
        MY.MyPage_state()
        MY.Swip_Menu()
   
    def testcase_3_Naver_Favorite(self):
        NF = Naver_Favorite(self.inter)
        NF.Total_count()
        NF.Favorite_Order()
        NF.Favorite_edit()
        NF.Favorite_Webtoon()

    def testcase_4_Naver_Recently(self):
        NP = Naver_Pecently(self.inter)
        NP.Total_count()
        NP.Now_View()
        NP.Now_view_edit()
        NP.Webtoon_rank()
        NP.week_webtoon_rank()



