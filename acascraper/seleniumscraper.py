from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import time

class Selenium():
 


    def setUp(self):
        
        self.sel = webdriver.Firefox()
        
        # Give the browser a little time; Firefox sometimes throws
        # random errors if you hit it too soon
        time.sleep(1)
 



    def get(self, url):
        self.setUp()
        self.sel.get(url)
        self.data = self.sel.page_source
        self.sel.quit()
        return
         