from PageObjects.LandingPage import LandingPage
from Tests.BaseTest import BaseTest
from Tests.TestData import TestData


class TestLandingPage(BaseTest):

    def test_verfify_login_displaeyd(self):
        self.landingpage =LandingPage(self.driver)
        message = self.landingpage.verfify_login_displaeyd()
        assert message is True

    def test_verify_Explore_is_Displayed(self):
        self.landingpage =LandingPage(self.driver)
        message = self.landingpage.verify_Explore_is_Displayed()
        assert message is True

    def test_verify_Logo_is_displayed(self):
        self.landingpage =LandingPage(self.driver)
        message = self.landingpage.verify_Logo_is_displayed()
        assert message is True

    def test_verify_LandingPageImage_is_displayed(self):
        self.landingpage =LandingPage(self.driver)
        message = self.landingpage.verify_LandingPageImage_is_displayed()
        assert message is True

    def test_verify_Headline_is_displayed(self):
        self.landingpage =LandingPage(self.driver)
        message = self.landingpage.verify_Headline_is_displayed()
        assert message is True

    def test_verify_SUBHeadline_is_displayed(self):
        self.landingpage = LandingPage(self.driver)
        message = self.landingpage.verify_SUBHeadline_is_displayed()
        assert message is True

    def test_verify_Terms_Conditions_is_displayed(self):
        self.landingpage = LandingPage(self.driver)
        message = self.landingpage.verify_Terms_Conditions_is_displayed()
        assert message is True

    def test_verify_Privacy_Policy_is_displayed(self):
        self.landingpage = LandingPage(self.driver)
        message = self.landingpage.verify_Privacy_Policy_is_displayed()
        assert message is True

    def test_verify_ContactUs_background_mage_is_displayed(self):
        self.landingpage = LandingPage(self.driver)
        message = self.landingpage.verify_ContactUs_background_mage_is_displayed()
        assert message is True

    def test_verify_StartCampaign_is_displayed(self):
        self.landingpage = LandingPage(self.driver)
        message = self.landingpage.verify_StartCampaign_is_displayed()
        assert message is True

    def test_verify_Explore_propertes_is_displayed(self):
        self.landingpage = LandingPage(self.driver)
        message = self.landingpage.verify_Explore_propertes_is_displayed()
        assert message is True

    def test_verify_Popular_properties_is_displayed(self):
        self.landingpage = LandingPage(self.driver)
        message = self.landingpage.verify_Popular_properties_is_displayed()
        assert message is True

    def test_validate_Headline_asPer_Publish(self):
        self.landingpage = LandingPage(self.driver)
        message = self.landingpage.validate_Headline_asPer_Publish()
        assert TestData.headline in message

    def test_validate_SubHeadline_asPer_Publish(self):
        self.landingpage = LandingPage(self.driver)
        message = self.landingpage.validate_SubHeadline_asPer_Publish()
        assert TestData.subheadline in message

    def test_verfiy_social_media_links_IsDisplayed(self):
        self.landingpage = LandingPage(self.driver)
        message = self.landingpage.verfiy_social_media_links_IsDisplayed()
        message1 = self.landingpage.verify_twitter_Logo_displayed()
        message2 = self.landingpage.verify_Insta_logo_displayed()
        assert (message is True and message1 is True and message2 is True)

    def test_validate_conactEMail_asPer_Published(self):
        self.landingpage = LandingPage(self.driver)
        message = self.landingpage.validate_conactEMail_asPer_Published()
        assert TestData.mail in message
