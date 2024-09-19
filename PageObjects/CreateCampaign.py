import time

from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from PageObjects.SearchPage import SearchPage


class CreateCampaign(BasePage):
    CAMPAIGN_NAME= (By.ID, "name")
    CLICK_CALENDER1 = (By.ID ,"calendarIcon")
    NEXT_MONTH = (By.XPATH , "//pre[@class='create-right']")
    CURRENT_MONTH= (By.XPATH, "//p[@class='create-display']")
    SELECT_DATE= (By.XPATH,"//div[text()='{day}']")
    CLICK_CALENDER2 = (By.ID, "calendarIcon1")
    NEXT_MONTH2 = (By.XPATH, "//pre[@class='create-right1']")
    CURRENT_MONTH2 = (By.XPATH, "//p[@class='create-display1']")
    SELECT_DATE2 = (By.XPATH, "(//div[text()='{day}'])[2]")
    SELECT_STATE= (By.ID, "states_dropdown")
    SELECT_DISTRICTS= (By.ID, "Districts")

    NEXT_BUTTON = (By.XPATH ,"//b[text()='Next']")
    CREATED_DATE = (By.XPATH ,"//p[@class='create-selected']")
    CREATED_DATE1 = (By.XPATH ,"//p[@class='create-selected1']")
    CAMPAIGN_NAME1 = (By.ID, "lname")
    SELECT_STATE1 = (By.ID, "states_dropdown")
    SELECT_DISTRICT1 = (By.ID, "districts")
    FROM_DATE = (By.ID, "startDateField")
    END_DATE = (By.ID, "endDateField")

    def __init__(self, driver):
        super().__init__(driver)

    def open_date_picker(self):
        self.click_button(self.CLICK_CALENDER1)
        time.sleep(3)

    def get_current_month_year(self):
        month_year_text = self.get_text(self.CURRENT_MONTH)
        return month_year_text

    def navigate_to_month(self, target_month, target_year):
        month_mapping = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8,
            'September': 9, 'October': 10, 'November': 11, 'December': 12
        }
        reverse_month_mapping = {v: k for k, v in month_mapping.items()}

        target_year = int(target_year)
        target_month_num = month_mapping[target_month]

        while True:
            current_month_year = self.get_current_month_year()
            current_month_str, current_year_str = current_month_year.split()
            current_year = int(current_year_str)
            current_month = month_mapping[current_month_str]

            if current_year == target_year and current_month == target_month_num:
                break
            elif current_year > target_year or (current_year == target_year and current_month > target_month_num):
                self.click_button(self.NEXT_MONTH)
            else:
                self.click_button(self.NEXT_MONTH)

    def select_date(self, day):
        xpath = self.SELECT_DATE[1].format(day=day)  # Format the XPATH string
        date_locator1 = (self.SELECT_DATE[0], xpath)  # Recreate the tuple with the formatted XPATH
        self.click_button(date_locator1)

    def open_date_picker2(self):
        self.click_button(self.CLICK_CALENDER2)
        time.sleep(3)

    def get_current_month_year2(self):
        month_year_text = self.get_text(self.CURRENT_MONTH2)
        return month_year_text

    def navigate_to_month2(self, target_month, target_year):
        month_mapping = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8,
            'September': 9, 'October': 10, 'November': 11, 'December': 12
        }
        reverse_month_mapping = {v: k for k, v in month_mapping.items()}

        target_year = int(target_year)
        target_month_num = month_mapping[target_month]

        while True:
            current_month_year = self.get_current_month_year2()
            current_month_str, current_year_str = current_month_year.split()
            current_year = int(current_year_str)
            current_month = month_mapping[current_month_str]

            if current_year == target_year and current_month == target_month_num:
                break
            elif current_year > target_year or (current_year == target_year and current_month > target_month_num):
                self.click_button(self.NEXT_MONTH2)
            else:
                self.click_button(self.NEXT_MONTH2)

    def select_date2(self, day):
        xpath = self.SELECT_DATE2[1].format(day=day)  # Format the XPATH string
        date_locator1 = (self.SELECT_DATE2[0], xpath)  # Recreate the tuple with the formatted XPATH
        self.click_button(date_locator1)

    def select_state(self,value,value2):
        self.click_button(self.SELECT_STATE)
        time.sleep(2)
        self.select_dropdown_option_by_value(self.SELECT_STATE,value)
        time.sleep(2)
        self.click_button(self.SELECT_DISTRICTS)
        time.sleep(2)
        self.select_dropdown_option_by_value(self.SELECT_DISTRICTS, value2)
        time.sleep(1)

    def validate_alert_text(self):
        self.click_button(self.NEXT_BUTTON)
        time.sleep(3)
        return self.get_alert_text()

    def create_campaign(self, name):
        self.text_input(self.CAMPAIGN_NAME,name)

    def click_NextButton(self):
        self.click_button(self.NEXT_BUTTON)
        return SearchPage(self.driver)

    def getText_campaignname(self):
        return self.get_text(self.CAMPAIGN_NAME)

    def getText_fromDate(self):
        return self.get_text(self.CREATED_DATE)

    def getText_endDate(self):
        return self.get_text(self.CREATED_DATE1)

    def getText_State(self):
        return self.get_text(self.SELECT_STATE)

    def getText_District(self):
        return self.get_text(self.SELECT_DISTRICTS)

    def getText_campaignname1(self):
        return self.get_text(self.CAMPAIGN_NAME1)

    def getText_fromDate1(self):
        return self.get_text(self.FROM_DATE)

    def getText_endDate1(self):
        return self.get_text(self.END_DATE)

    def getText_State1(self):
        return self.get_text(self.SELECT_STATE1)

    def getText_District1(self):
        return self.get_text(self.SELECT_DISTRICT1)





