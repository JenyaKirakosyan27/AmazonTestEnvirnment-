from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class CartPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def delete_firstProduct_from_cart(self):
       firstProductDeleteButtonElement = self._find_element(By.XPATH, "(//input[@value = 'Delete'])[1]")
       self._click_to_element(firstProductDeleteButtonElement)

    def save_for_later_firstProduct_from_cart(self):
        firstProductSaveForLeterButtonElement = self._find_element(By.XPATH, "(//input[@name ='submit.save-for-later.8ac998b5-36b3-435b-8715-f53a826c6f1a'])[1]")
        self._click_to_element(firstProductSaveForLeterButtonElement)

