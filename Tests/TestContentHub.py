from PageObjects.LandingPage import LandingPage
from Tests.BaseTest import BaseTest


class TestContentHub(BaseTest):

    def login(self):
        self.landingpage = LandingPage(self.driver)
        self.loginpage = self.landingpage.goto_LoginPage()
        self.mycampaign = self.loginpage.go_MycampaignDashboard("manoj_vanigam", "Manoj@123")
        self.contenthub = self.mycampaign.navigate_to_ContentHub()

    def test_validate_Curreet_URL(self):
        self.login()
        message = self.contenthub.validate_Curreet_URL()
        assert  message.__contains__("https://d25o0givni0pe6.cloudfront.net/content_hub.html")

    def test_validate_search_functionality_inContentHub(self):
        self.login()
        message = self.contenthub.validate_search_functionality_inContentHub("GoldenDust.mp4")
        message1 = self.contenthub.validate_creative_imageDisplayed()
        assert ("GoldenDust.mp4" in message  and message1 is True)

    def test_validate_MIME_Type_in_FilterFunctionality(self):
        self.login()
        message= self.contenthub.validate_MIME_Type_in_FilterFunctionality()
        message1 = self.contenthub.validate_PNG_type()
        message2 = self.contenthub.validate_video_type()
        assert ("image/jpeg" in message and "image/png" in message1 and "video/mp4" in message2)

    def test_validate_delete_creatives_functionality(self):
        self.login()
        message =self.contenthub.validate_delete_creatives_functionality()
        message1 = self.contenthub.delete_creatives()
        assert message not in  message1
