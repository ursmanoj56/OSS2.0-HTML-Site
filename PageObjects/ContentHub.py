import time

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage


class ContentHub(BasePage):
    SEARCH_CREATIVES = (By.XPATH, "//input[@placeholder='Search for your campaigns']")
    CREATIVE_NAME = (By.XPATH , "(//span[@class='contenthub-short-text'])[1]")
    CREATIVE_IMAGE = (By.XPATH ,"(//img[@class='contenthub-unsplashv3qhk9rhtju-icon'])[1]")
    DELETE_CREATIVES = (By.XPATH,"(//button[text()='Delete'])[1]")
    CREARTIVE_TYPE = (By.XPATH, "(//div[@class='contenthub-photojpeg'])[1]")
    FILTER_BUTTON = (By.ID ,"openFilterPopup")
    MIME_TYPE_FILTER = (By.XPATH ,"//button[text()='MIME type']")
    JPEG_MIME_TYPE = (By.XPATH ,"//input[@value='image/jpeg']")
    PNG_MIME_TYPE =(By.XPATH, "//input[@value='image/png']")
    VIDEO_MIME_TYPE = (By.XPATH , "//input[@value='video/mp4']")
    APPLY_BUTTON = (By.ID ,"applyFilters")



    def __init__(self, driver):
        super().__init__(driver)

    def validate_Curreet_URL(self):
        return self.get_current_url()

    def validate_search_functionality_inContentHub(self, name):
        self.text_input(self.SEARCH_CREATIVES, name)
        self.press_enter()
        time.sleep(2)
        return self.get_text(self.CREATIVE_NAME)

    def validate_creative_imageDisplayed(self):
        return self.is_displayed(self.CREATIVE_IMAGE)

    def validate_MIME_Type_in_FilterFunctionality(self):
        time.sleep(2)
        self.click_button(self.FILTER_BUTTON)
        time.sleep(2)
        self.click_button(self.MIME_TYPE_FILTER)
        time.sleep(2)
        self.click_button(self.JPEG_MIME_TYPE)
        self.click_button(self.APPLY_BUTTON)
        time.sleep(3)
        return self.get_text(self.CREARTIVE_TYPE)

    def validate_PNG_type(self):
        time.sleep(2)
        self.click_button(self.FILTER_BUTTON)
        time.sleep(2)
        self.click_button(self.MIME_TYPE_FILTER)
        time.sleep(2)
        self.click_button(self.PNG_MIME_TYPE)
        self.click_button(self.APPLY_BUTTON)
        time.sleep(4)
        return self.get_text(self.CREARTIVE_TYPE)

    def validate_video_type(self):
        time.sleep(2)
        self.click_button(self.FILTER_BUTTON)
        time.sleep(2)
        self.click_button(self.MIME_TYPE_FILTER)
        time.sleep(2)
        self.click_button(self.VIDEO_MIME_TYPE)
        self.click_button(self.APPLY_BUTTON)
        time.sleep(4)
        return self.get_text(self.CREARTIVE_TYPE)

    def validate_delete_creatives_functionality(self):
        return self.get_text(self.CREATIVE_NAME)

    def delete_creatives(self):
        self.move_to_element(self.CREARTIVE_TYPE)
        self.click_button(self.DELETE_CREATIVES)
        return self.get_text(self.CREATIVE_NAME)

