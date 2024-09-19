import time

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from PageObjects.ContentHub import ContentHub
from PageObjects.CreateCampaign import CreateCampaign


class MyCampaignPage(BasePage):
    SEARCH_INPUT = (By.ID, "searchInput")
    CAMPAIGN_NAME =(By.XPATH,"//tbody/tr/td[1]")
    CAMPAIGN_STATUS =(By.XPATH,"//tbody/tr/td[4]")
    CAMPAIGN_NAME_HEADER = (By.XPATH,"//thead/tr/th[1]")
    DURATION_HEADER = (By.XPATH, "//thead/tr/th[2]")
    INVENTORIES_HEADER = (By.XPATH, "//thead/tr/th[3]")
    STATUS_HEADER = (By.XPATH, "//thead/tr/th[4]")
    IMPRESSION_HEADER = (By.XPATH, "//thead/tr/th[5]")
    TOTAL_PRICE_HEADER = (By.XPATH, "//thead/tr/th[6]")
    BOOKING_HEADER = (By.XPATH, "//thead/tr/th[7]")
    ACTION_HEADER = (By.XPATH, "//thead/tr/th[8]")
    SELECT_FILTER = (By.ID, "statusFilter")
    SEARCH_BUTTON=  (By.XPATH,"//img[@class='order-search-icon2']")
    CUSTAMISED_TABLE = (By.ID, "customizeBtn")
    CUSTAMISED_DURATION = (By.XPATH ,"//input[@value='Duration']")
    CUSTAMISED_INVENTORIES =(By.XPATH, "//input[@value='Inventories']")
    CUSTAMISED_APPLY =(By.XPATH ,"//button[text()='Apply']")

    USER_ICON = (By.XPATH, "//div[@class='user-icon']")
    CONTENTHUB = (By.XPATH,"//div[@id='dropdownMenu']/a[4]")
    CREATE_CAMPAIGN= (By.XPATH , "//a[text()='Start New Campaign']")

    def __init__(self, driver):
        super().__init__(driver)

    def validate_search_funcationality(self,name):
        self.text_input(self.SEARCH_INPUT,name)
        self.press_enter()
        return self.get_text(self.CAMPAIGN_NAME)

    def validate_filter_functionality(self,value):
        time.sleep(3)
        self.select_dropdown_option_by_value(self.SELECT_FILTER,value)
        time.sleep(4)
        return self.get_text(self.CAMPAIGN_STATUS)

    def validate_search_funcationality_with_filter(self,value,name):
        time.sleep(2)
        self.select_dropdown_option_by_value(self.SELECT_FILTER, value)
        time.sleep(1)
        self.text_input(self.SEARCH_INPUT, name)
        self.click_button(self.SEARCH_BUTTON)
        time.sleep(3)
        return self.get_text(self.CAMPAIGN_NAME)

    def validate_Custamised_Table(self):
        self.click_button(self.CUSTAMISED_TABLE)
        self.click_button(self.CUSTAMISED_DURATION)
        self.click_button(self.CUSTAMISED_INVENTORIES)
        time.sleep(2)
        self.click_button(self.CUSTAMISED_APPLY)
        time.sleep(2)
        return self.is_displayed(self.DURATION_HEADER)

    def inventories_IsDisplayed_in_Custamised(self):
        return self.is_displayed(self.INVENTORIES_HEADER)

    def search_filter_funcationlity_In_CustamisedFilter(self):
        self.click_button(self.CUSTAMISED_TABLE)
        self.click_button(self.CUSTAMISED_DURATION)
        self.click_button(self.CUSTAMISED_INVENTORIES)
        time.sleep(2)
        self.click_button(self.CUSTAMISED_APPLY)
        time.sleep(2)

    def navigate_to_ContentHub(self):
        self.click_button(self.USER_ICON)
        self.click_button(self.CONTENTHUB)
        return ContentHub(self.driver)

    def navigate_to_CreateCampaign(self):
        self.click_button(self.CREATE_CAMPAIGN)
        return CreateCampaign(self.driver)




