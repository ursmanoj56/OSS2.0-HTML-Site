from PageObjects.LandingPage import LandingPage
from Tests.BaseTest import BaseTest


class TestMyCampaignPage(BaseTest):
    def login(self):
        self.landingpage = LandingPage(self.driver)
        self.loginpage = self.landingpage.goto_LoginPage()
        self.mycampaign = self.loginpage.go_MycampaignDashboard("manoj_vanigam", "Manoj@123")

    def test_validate_search_funcationality(self):
        self.login()
        message =self.mycampaign.validate_search_funcationality("Testcampaign2")
        assert "Testcampaign2" in message

    def test_validate_filter_functionality(self):
        self.login()
        message = self.mycampaign.validate_filter_functionality("GENERATED")
        message1 = self.mycampaign.validate_filter_functionality("REQUESTED")
        message2 = self.mycampaign.validate_filter_functionality("PAYMENT_PENDING")
        # message3 = self.mycampaign.validate_filter_functionality("APPROVED")
        message4 = self.mycampaign.validate_filter_functionality("REJECTED")
        message5 = self.mycampaign.validate_filter_functionality("LIVE")
        message6 = self.mycampaign.validate_filter_functionality("COMPLETED")
        assert ("GENERATED" in message and "REQUESTED" in message1 and "PAYMENT_PENDING" in message2
                 and "REJECTED" in message4 and "LIVE" in message5 and "COMPLETED" in message6)

    def test_validate_search_funcationality_with_filter(self):
        self.login()
        message2 = self.mycampaign.validate_search_funcationality_with_filter("PAYMENT_PENDING","campaign1")
        # message3 = self.mycampaign.validate_search_funcationality_with_filter("APPROVED","assaigntestcampaign")
        message4 = self.mycampaign.validate_search_funcationality_with_filter("REJECTED","has")
        message1 = self.mycampaign.validate_search_funcationality_with_filter("REQUESTED", "nametest12")
        message5 = self.mycampaign.validate_search_funcationality_with_filter("LIVE","assigntestcampaign2")
        message6 = self.mycampaign.validate_search_funcationality_with_filter("COMPLETED","test__6")
        message = self.mycampaign.validate_search_funcationality_with_filter("GENERATED", "test32")

        assert ("test32" in message and "nametest12" in message1 and "campaign1" in message2
                and "has" in message4 and "assigntestcampaign2" in message5 and "test__6" in message6)

    def test_validate_Custamised_Table(self):
        self.login()
        message = self.mycampaign.validate_Custamised_Table()
        message1 = self.mycampaign.inventories_IsDisplayed_in_Custamised()
        assert (message is False and message1 is False)

    def test_search_filter_funcationlity_In_CustamisedFilter(self):
        self.login()
        self.mycampaign.search_filter_funcationlity_In_CustamisedFilter()
        message2 = self.mycampaign.validate_search_funcationality_with_filter("PAYMENT_PENDING", "campaign1")
        # message3 = self.mycampaign.validate_search_funcationality_with_filter("APPROVED","assaigntestcampaign")
        message4 = self.mycampaign.validate_search_funcationality_with_filter("REJECTED", "has")
        message1 = self.mycampaign.validate_search_funcationality_with_filter("REQUESTED", "nametest12")
        message5 = self.mycampaign.validate_search_funcationality_with_filter("LIVE", "assigntestcampaign2")
        message6 = self.mycampaign.validate_search_funcationality_with_filter("COMPLETED", "Testcampaign2")
        message = self.mycampaign.validate_search_funcationality_with_filter("GENERATED", "newcampaign1")

        assert ("newcampaign1" in message and "nametest12" in message1 and "campaign1" in message2
                and "has" in message4 and "assigntestcampaign2" in message5 and "Testcampaign2" in message6)


