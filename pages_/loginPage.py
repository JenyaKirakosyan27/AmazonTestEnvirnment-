from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from pages_.basePage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver


    def fill_username_fild(self, username):
        #userNameFildElement = self.driver.find_element(By.ID, "ap_email")
        userNameFildElement = self._find_element(By.ID, "ap_email")
        self._fill_field(userNameFildElement, username)
        # userNameFildElement.clear()
        # userNameFildElement.send_keys(username)


    def click_to_continue_button(self):
        #continueButtonElement = self.driver.find_element(By.ID, "continue")
        continueButtonElement = self._find_element(By.ID, "continue")
        #continueButtonElement.click()
        self._click_to_element(continueButtonElement)


    def fill_password_fild(self, password):
        #passwordFildElement = self.driver.find_element(By.ID, "ap_password")
        passwordFildElement = self._find_element(By.ID, "ap_password")
        self._fill_field(passwordFildElement, password)
        # passwordFildElement.clear()
        # passwordFildElement.send_keys(password)


    def click_to_signin_button(self):
        sleep(6)
        #signInButtonElement = self.driver.find_element(By.ID, "signInSubmit")
        signInButtonElement = self._find_element(By.ID, "signInSubmit")
        #signInButtonElement.click()
        self._click_to_element(signInButtonElement)
        sleep(10)


    def walidate_continue_button_text(self):
        continueButtonElement = self._find_element(By.ID, "continue")
        if self._get_text(continueButtonElement) != "Continue":
            print("Error:Wrong continue button text")
            exit(2)





