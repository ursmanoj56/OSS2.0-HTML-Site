import time

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class SearchPage(BasePage):
    CAMPAIGN_NAME = (By.ID ,"lname")
    SELECT_STATE = (By.ID, "states_dropdown")
    SELECT_DISTRICT = (By.ID,"districts")
    FROM_DATE = (By.ID, "startDateField")
    END_DATE = (By.ID ,"endDateField")
    MAP_VIEW = (By.XPATH ,"//img[@class='listview-map-pin-icon']")
    LIST_VIEW =(By.XPATH , "//img[@class='listview-filter-button-child']")
    MAP = (By.ID ,"map")
    CART_ITEM = (By.XPATH, "//div[@class='listview-cart1']")
    BILLBOARD_IMAGE = (By.XPATH ,"(//img[@class='images-list'])[1]")
    BILLBOARD_NAME = (By.XPATH ,"(//b[@class='listview-sunnybank-outbound8'])[1]")
    BILLBOARD_STATE = (By.XPATH ,"(//div[@class='listview-queensland5'])[1]")
    BILLBOARD_PRICE = (By.XPATH , "(//div[@class='listview-aud-50005'])[1]")
    BILLBOARD_RESOLUTION = (By.XPATH ,"(//div[@class='listview-x608'])[1]")
    BILLBOARD_NEXT_SLOT = (By.XPATH ,"(//div[@class='listview-nov-2024'])[1]")
    BILLBOARD_IMPRESSION = (By.XPATH , "(//div[@class='listview-availability-value'])[1]")
    BILLBOARD_SCREENS = (By.XPATH, "(//div[@class='listview-number-of-screens'])[1]")

    def __init__(self, driver):
        super().__init__(driver)

    def validate_CurrentURL(self):
        return self.get_current_url()

    def validate_MAPview_ListView(self):
        self.click_button(self.MAP_VIEW)
        return self.is_displayed(self.MAP)

    def ListView_displayed(self):
        self.click_button(self.LIST_VIEW)
        return self.is_displayed(self.MAP)

    def validate_BillboardDetails_displayed(self):
        return self.is_displayed(self.BILLBOARD_IMAGE)

    def billboard_Name_is_displayed(self):
        return self.is_displayed(self.BILLBOARD_NAME)

    def billboard_State_isDisplayed(self):
        return self.is_displayed(self.BILLBOARD_STATE)

    def billboard_price_IsDisplayed(self):
        return self.is_displayed(self.BILLBOARD_PRICE)

    def billboard_resolution_Displayed(self):
        return self.is_displayed(self.BILLBOARD_RESOLUTION)

    def billboard_nextSlot_is_Displayed(self):
        return self.is_displayed(self.BILLBOARD_NEXT_SLOT)

    def billboard_Impresssion_isDisplayed(self):
        return self.is_displayed(self.BILLBOARD_IMPRESSION)

    def billboard_No_of_Screens(self):
        return self.is_displayed(self.BILLBOARD_SCREENS)
