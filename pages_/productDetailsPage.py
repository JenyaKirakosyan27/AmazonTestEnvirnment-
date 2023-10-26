from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class ProductDetailsPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_to_add_to_cart_button(self):
        addToCartButtonElement = self._find_element(By.XPATH, "//span[@id = 'submit.add-to-cart']")
        self._click_to_element(addToCartButtonElement)