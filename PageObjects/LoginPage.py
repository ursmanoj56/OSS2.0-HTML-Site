import time

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from PageObjects.MyCampaignPage import MyCampaignPage


class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_AUTH_BUTTON = (By.ID, "authButton")


    def __init__(self, driver):
        super().__init__(driver)

    def verify_login_functionality_withValida_Credential(self,username,password):
        self.text_input(self.USERNAME,username)
        self.text_input(self.PASSWORD,password)
        self.click_button(self.LOGIN_AUTH_BUTTON)
        time.sleep(3)
        return self.get_current_url()

    def go_MycampaignDashboard(self,username,password):
        self.text_input(self.USERNAME, username)
        self.text_input(self.PASSWORD, password)
        self.click_button(self.LOGIN_AUTH_BUTTON)
        return MyCampaignPage(self.driver)