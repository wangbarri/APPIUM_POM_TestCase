from dpvldna.TestCase.Test import TestRun
from dpvldna.Pages.Sinhan.SinhanPlay_Event import SinhanPlay_EventPages
from dpvldna.Pages.Sinhan.SinhanPlus_Event import SinhanPlus_EventPages





class TestCase(TestRun):

    def testcase_1_SinhanPlay_Event(self):
        SH = SinhanPlay_EventPages(self.inter)
        SH.Event_Page_join()
        SH.Event_attendance_check()
        SH.Event_New_Year()
        
    def testcase_2_SinhanPlus_Event(self):
        SP = SinhanPlus_EventPages(self.inter)
        SP.Shihan_Plus_page_join()