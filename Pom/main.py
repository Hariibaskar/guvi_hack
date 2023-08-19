# Code With usage of POM
# main.py
# executable code

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data import Hari_Data
from locators import Hari_Locators
import time

from selenium.webdriver.support.select import Select

# Code With usage of POM

class health:
    def __init__(self, url):
        self.driver = webdriver.Edge()
        self.url = url
        
        
    
    
    def login(self):       
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=Hari_Locators().username_locator).send_keys(Hari_Data().username)
        self.driver.find_element(by=By.NAME, value=Hari_Locators().password_locator).send_keys(Hari_Data().password)
        self.driver.find_element(by=By.XPATH, value=Hari_Locators().submit_button).click()
        time.sleep(5)
        dropdown_button=self.driver.find_element(by=By.XPATH, value=Hari_Locators().dropdown_locator)
        dd = Select(dropdown_button)
        dd.select_by_value('Seoul CURA Healthcare Center')  
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.XPATH, value=Hari_Locators().checkbox_locator).click()
        self.driver.find_element(by=By.XPATH, value=Hari_Locators().radiobutton_locator).click()
        time.sleep(5)
        self.driver.find_element(by=By.ID, value=Hari_Locators().date_locator).send_keys(Hari_Data().date)
        self.driver.find_element(by=By.XPATH, value=Hari_Locators().comment_locator).send_keys(Hari_Data().comment)
        self.driver.implicitly_wait(5)
        self.driver.find_element(by=By.XPATH, value=Hari_Locators().bookapp_locator).click()
        time.sleep(4)

s = health(Hari_Data().url)

s.login()