import unittest
import time

from dpvldna.WebDriver.Driver import Driver


class TestRun(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.inter = Driver()

    def setUp(self):
        pass
        

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
       cls.inter.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRun)
    unittest.TextTestRunner(verbosity=2).run(suite)