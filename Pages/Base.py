from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from dpvldna.WebDriver.Driver import Driver
from time import sleep


class BaseCommands:

    def __init__(self, driver):
        self.inter = driver or Driver()
        self.wait = WebDriverWait(driver=self.inter.driver,timeout=10)

    def Send_keys(self,locator,value):
        self.inter.driver.find_element(*locator).send_keys(value)
        
    def Click(self, *locator):
        try:
            self.wait.until(ec.element_to_be_clickable(*locator)).click()
        
        except NoSuchElementException:
            raise NoSuchElementException("not found element")
        except TimeoutException:
            raise TimeoutException("Timeout")

    def Find_Element(self, *locator):
        try:
            self.wait.until(ec.visibility_of_all_elements_located(*locator))

        except NoSuchElementException:
            raise NoSuchElementException ("not found element")
        except TimeoutException:
            raise TimeoutException("Timeout")
    
    def Find_Elements(self, *locator):
        try:
            self.wait.until(ec.visibility_of_all_elements_located(*locator))

        except NoSuchElementException:
            raise NoSuchElementException ("not found element")
        except TimeoutException:
            raise TimeoutException("Timeout")
    
    def Text(self, locator):
            element = self.inter.driver.find_element(*locator).text
            return element.text
    
    def scroll(self, *locator, css):
        try:
            el1 = self.wait.until(ec.visibility_of_element_located(*locator))
            el2 = self.wait.until(ec.visibility_of_element_located(css))
            
            #1번(위에서) 2번(아래로) 이동 (화면은 위로) / 2번 (아래에서) 1번(위로) (화면은 아래로)
            self.inter.driver.scroll(el2, destination_el=el1)
            
        except NoSuchElementException:
            raise NoSuchElementException ("not found element")
        except TimeoutException:
            raise TimeoutException("Timeout")
            
    def Swip(self, x1,y1,x2,y2):
        
        try:
            self.inter.driver.swipe(x1,y1,x2,y2,900)    
            
        except NoSuchElementException:
            raise NoSuchElementException ("not found element")
        except TimeoutException:
            raise TimeoutException("Timeout")






