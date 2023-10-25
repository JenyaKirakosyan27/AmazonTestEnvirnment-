from selenium import webdriver
from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def fill_username_fild(self, username):
        userNameFildElement = self._find_element(By.ID, "ap_email")
        self._fill_field(userNameFildElement, username)
       
    def click_to_continue_button(self):
        continueButtonElement = self._find_element(By.ID, "continue")
        self._click_to_element(continueButtonElement)

    def fill_password_fild(self, password):
        passwordFildElement = self._find_element(By.ID, "ap_password")
        self._fill_field(passwordFildElement, password)
       
    def click_to_signin_button(self):
        signInButtonElement = self._find_element(By.ID, "signInSubmit")
        self._click_to_element(signInButtonElement)
       
    def walidate_continue_button_text(self):
        continueButtonElement = self._find_element(By.ID, "continue")
        if self._get_text(continueButtonElement) != "Continue":
            print("Error:Wrong continue button text")
            exit(2)





