from PageObjects.LandingPage import LandingPage
from Tests.BaseTest import BaseTest


class TestLogin(BaseTest):

    def test_verify_login_functionality_withValida_Credential(self):
        self.landingpage =LandingPage(self.driver)
        self.loginpage =self.landingpage.goto_LoginPage()
        message = self.loginpage.verify_login_functionality_withValida_Credential("manoj_vanigam", "Manoj@123")
        assert message.__contains__("https://d25o0givni0pe6.cloudfront.net/my_campaign.html")

