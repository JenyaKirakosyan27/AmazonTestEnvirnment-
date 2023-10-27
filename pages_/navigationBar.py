from selenium.webdriver.common.by import By
from selenium import webdriver
from pages_.basePage import BasePage

class NavigationBar(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_to_cart_button(self):
        cartbuttonElement = self._find_element(By.ID, "nav-cart-count-container")
        self._click_to_element(cartbuttonElement)

    def fill_search_field(self, searchElement):
        textFieldElement = self._find_element(By.NAME, "field-keywords")
        self._fill_field(textFieldElement, searchElement)
       

    def click_to_search_button(self):
        searchButtonElement = self._find_element(By.ID, "nav-search-submit-button")
        self._click_to_element(searchButtonElement)

   

