from PageObjects.LandingPage import LandingPage
from Tests.BaseTest import BaseTest


class TestCreateCampaign(BaseTest):
    def login(self):
        self.landingpage = LandingPage(self.driver)
        self.loginpage = self.landingpage.goto_LoginPage()
        self.mycampaign = self.loginpage.go_MycampaignDashboard("manoj_vanigam", "Manoj@123")
        self.createcampaign = self.mycampaign.navigate_to_CreateCampaign()

    def test_select_date(self):
        self.login()
        self.createcampaign.open_date_picker()
        self.createcampaign.navigate_to_month("October", 2024)  # June 2024
        self.createcampaign.select_date(21)

    def test_select_date2(self):
        self.login()
        self.createcampaign.open_date_picker2()
        self.createcampaign.navigate_to_month2("October", 2024)  # June 2024
        self.createcampaign.select_date2(21)

    def test_selectState(self):
        self.login()
        self.createcampaign.select_state("59d203e278d0675bdf1fff1a","barcoo")

    def test_get_alert_text(self):
        self.login()
        message = self.createcampaign.validate_alert_text()
        assert "Please enter all campaign details." in message

    def test_create_Campiagn(self):
        self.login()
        self.createcampaign.create_campaign("test143")
        self.createcampaign.open_date_picker()
        self.createcampaign.navigate_to_month("October", 2024)  # June 2024
        self.createcampaign.select_date(21)
        self.createcampaign.open_date_picker2()
        self.createcampaign.navigate_to_month2("October", 2024)  # June 2024
        self.createcampaign.select_date2(21)
        self.createcampaign.select_state("59d203e278d0675bdf1fff1a", "barcoo")
        self.createcampaign.click_NextButton()

    def test_validateCreateCampaign_details_inSearchPage(self):
        self.login()
        self.createcampaign.create_campaign("test143")
        self.createcampaign.open_date_picker()
        self.createcampaign.navigate_to_month("October", 2024)  # June 2024
        self.createcampaign.select_date(21)
        self.createcampaign.open_date_picker2()
        self.createcampaign.navigate_to_month2("October", 2024)  # June 2024
        self.createcampaign.select_date2(21)
        self.createcampaign.select_state("59d203e278d0675bdf1fff1a", "barcoo")
        message = self.createcampaign.getText_campaignname()
        message1 = self.createcampaign.getText_fromDate()
        message2 = self.createcampaign.getText_endDate()
        message3 = self.createcampaign.getText_State()
        message4 = self.createcampaign.getText_District()
        self.createcampaign.click_NextButton()
        message5 = self.createcampaign.getText_campaignname1()
        message6 = self.createcampaign.getText_fromDate()
        message7 = self.createcampaign.getText_endDate1()
        message8 = self.createcampaign.getText_State1()
        message9 = self.createcampaign.getText_District1()
        assert (message in message5 and message1 in message6 and message2 in message7 and message3 in message8 and message4 in message9)










