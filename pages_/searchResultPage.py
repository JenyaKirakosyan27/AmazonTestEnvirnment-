from selenium.webdriver.common.by import By
from selenium import webdriver
from pages_.basePage import BasePage

class SearchResultPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_to_first_product(self):
        firstProductElement = self._find_element(By.XPATH, "(//div[@class='a-section aok-relative s-image-square-aspect'])[1]")
        self._click_to_element(firstProductElement)

 
