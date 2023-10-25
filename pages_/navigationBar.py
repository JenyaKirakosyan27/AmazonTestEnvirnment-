from selenium.webdriver.common.by import By
from selenium import webdriver
from pages_.basePage import BasePage

class NavigationBar():
    def __init__(self,driver: webdriver.Chrome):
        self.driver = driver

    def click_to_cart_button(self):
        cartbuttonElement = self.driver.find_element(By.ID, "nav-cart-count-container")
        cartbuttonElement.click()

    def fill_search_field(self, searchElement):
        textFieldElement = self.driver.find_element(By.NAME, "field-keywords")
        textFieldElement.clear()
        textFieldElement.send_keys(searchElement)

    def click_to_search_button(self):
        searchButtonElement = self.driver.find_element(By.ID, "nav-search-submit-button")
        searchButtonElement.click()

    def click_to_first_product(self):
        firstProductElement = self.driver.find_element(By.XPATH, "(//div[@class='a-section aok-relative s-image-square-aspect'])[1]")
        firstProductElement.click()

   

