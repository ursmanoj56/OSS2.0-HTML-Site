from PageObjects.LandingPage import LandingPage
from Tests.BaseTest import BaseTest


class TestSearchPage(BaseTest):

    def login(self):
        self.landingpage = LandingPage(self.driver)
        self.loginpage = self.landingpage.goto_LoginPage()
        self.mycampaign = self.loginpage.go_MycampaignDashboard("manoj_vanigam", "Manoj@123")
        self.createcampaign = self.mycampaign.navigate_to_CreateCampaign()
        self.createcampaign.create_campaign("test143")
        self.createcampaign.open_date_picker()
        self.createcampaign.navigate_to_month("October", 2024)  # June 2024
        self.createcampaign.select_date(21)
        self.createcampaign.open_date_picker2()
        self.createcampaign.navigate_to_month2("October", 2024)  # June 2024
        self.createcampaign.select_date2(21)
        self.createcampaign.select_state("59d203e278d0675bdf1fff1a", "barcoo")
        self.searchpage=self.createcampaign.click_NextButton()

    def test_valuidate_currentURL(self):
        self.login()
        message = self.searchpage.validate_CurrentURL()
        assert "https://d25o0givni0pe6.cloudfront.net/property_list.html" in message

    def test_validate_MAPview_ListView(self):
        self.login()
        message = self.searchpage.validate_MAPview_ListView()
        message1 =self.searchpage.ListView_displayed()
        message2 = self.searchpage.validate_MAPview_ListView()

        assert (message is True and message1 is False and message2 is True)

    def test_validate_BillboardDetails_displayed(self):
        self.login()
        message = self.searchpage.validate_BillboardDetails_displayed()
        message1 = self.searchpage.billboard_Name_is_displayed()
        message2 = self.searchpage.billboard_State_isDisplayed()
        message3 = self.searchpage.billboard_price_IsDisplayed()
        message4 = self.searchpage.billboard_resolution_Displayed()
        message5 = self.searchpage.billboard_nextSlot_is_Displayed()
        message6 = self.searchpage.billboard_Impresssion_isDisplayed()
        message7 = self.searchpage.billboard_No_of_Screens()

        assert (message is True and message1 is True and message2 is True and message3 is True and message4 is True and message5 is True and message6 is True and message7 is True)
