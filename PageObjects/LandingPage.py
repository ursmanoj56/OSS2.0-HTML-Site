from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from PageObjects.LoginPage import LoginPage


class LandingPage(BasePage):
    LANDINGPAGE_LOGO = (By.XPATH, "//img[@class='landing-your-logo-icon']")
    EXPLORE_BUTTON = (By.XPATH, "//button[text()='Explore']")
    LOGIN_BUTTON =(By.XPATH, "//button[text()='Login']")
    LANDINGPAGE_IMAGE =(By.XPATH,"//img[@class='landing-mask-group-icon']")
    HEADLINE =(By.XPATH,"//p[@class='landing-maximise']")
    SUBHEADLINE = (By.XPATH,"//h3[@class='landing-with-the-largest']")
    EXPLORE_PROPERTIES = (By.XPATH,"//div[@class='landing-frame-parent1']")
    POPULAR_PROPERTIES = (By.XPATH,"//div[@class='landing-featured-properties']")
    TERMS_CONDITION = (By.ID,"Termsandconditions")
    PRIVACY_POLICY =(By.ID,"privacypolicy")
    FACEBOOK_ID =(By.ID,"FacebookId")
    TWITTER_ID =(By.ID,"TwitterID")
    INSTAGRAM_ID=(By.ID,"InstagramID")
    ADDRESS =(By.XPATH,"//h3[@class='landing-e-89-new-delhi']")
    EMAIL=(By.XPATH,"//h3[@class='landing-billboardcom']")
    CONTACT_US_HEADER= (By.XPATH,"//h1[@class='landing-any-questions']")
    CONTACT_US_SUBHEADER= (By.XPATH,"//h1[@class='landing-write-to-us']")
    CONTACT_US_DISPLAYED = (By.XPATH, "//div[@class='landing-questions-wrapper-wrapper']")
    CONTACTUS_IMAGE =(By.XPATH,"//img[@class='landing-mask-group-icon7']")
    START_CAMPAIGN=(By.XPATH,"//button[text()='Start Campaign']")
    CLIENT_ICON1 =(By.XPATH,"//img[@class='landing-testimonial-content-child']")
    CLIENT_ICON2 =(By.XPATH,"//img[@class='landing-page-item']")
    CLIENT_ICON3 =(By.XPATH,"//img[@class='landing-ellipse-icon']")
    CLIENT_NAME1 =(By.XPATH,"//h3[@class='landing-haylie-baptista']")
    CLIENT_NAME2 = (By.XPATH, "//h3[@class='landing-hannah-schmitt']")
    CLIENT_NAME3 = (By.XPATH, "//h3[@class='landing-alena-saris']")
    CLIENT_LOGO1= (By.XPATH,"//img[@class='landing-mask-group-icon1']")
    CLIENT_LOGO2 = (By.XPATH, "//img[@class='landing-mask-group-icon2']")
    CLIENT_LOGO3 = (By.XPATH, "//img[@class='landing-mask-group-icon3']")
    CLIENT_SAYS1=(By.XPATH,"//div[@class='landing-lorem-ipsum-dolor']")
    CLIENT_SAYS2 = (By.XPATH, "//div[@class='landing-lorem-ipsum-dolor1']")
    CLIENT_SAYS3 = (By.XPATH, "//div[@class='landing-lorem-ipsum-dolor2']")


    def __init__(self, driver):
        super().__init__(driver)

    def verfify_login_displaeyd(self):
        return self.is_displayed(self.LOGIN_BUTTON)

    def verify_Explore_is_Displayed(self):
        return self.is_displayed(self.EXPLORE_BUTTON)

    def verify_Logo_is_displayed(self):
        return self.is_displayed(self.LANDINGPAGE_LOGO)

    def verify_LandingPageImage_is_displayed(self):
        return self.is_displayed(self.LANDINGPAGE_IMAGE)

    def verify_Headline_is_displayed(self):
        return self.is_displayed(self.HEADLINE)

    def validate_Headline_asPer_Publish(self):
        return self.get_text(self.HEADLINE)

    def verify_SUBHeadline_is_displayed(self):
        return self.is_displayed(self.SUBHEADLINE)

    def validate_SubHeadline_asPer_Publish(self):
        return self.get_text(self.SUBHEADLINE)

    def verify_Terms_Conditions_is_displayed(self):
        self.scroll_into_view(self.TERMS_CONDITION)
        return self.is_displayed(self.TERMS_CONDITION)

    def verify_Privacy_Policy_is_displayed(self):
        self.scroll_into_view(self.PRIVACY_POLICY)
        return self.is_displayed(self.PRIVACY_POLICY)

    def verify_ContactUs_background_mage_is_displayed(self):
        self.scroll_into_view(self.CONTACTUS_IMAGE)
        return self.is_displayed(self.CONTACTUS_IMAGE)

    def verify_StartCampaign_is_displayed(self):
        self.scroll_into_view(self.START_CAMPAIGN)
        return self.is_displayed(self.START_CAMPAIGN)

    def verify_Explore_propertes_is_displayed(self):
        self.scroll_into_view(self.EXPLORE_PROPERTIES)
        return self.is_displayed(self.EXPLORE_PROPERTIES)

    def verify_Popular_properties_is_displayed(self):
        self.scroll_into_view(self.POPULAR_PROPERTIES)
        return self.is_displayed(self.POPULAR_PROPERTIES)

    def verfiy_social_media_links_IsDisplayed(self):
        self.scroll_into_view(self.FACEBOOK_ID)
        return self.is_displayed(self.FACEBOOK_ID)

    def verify_twitter_Logo_displayed(self):
        return self.is_displayed(self.TWITTER_ID)

    def verify_Insta_logo_displayed(self):
        return self.is_displayed(self.INSTAGRAM_ID)

    def validate_conactEMail_asPer_Published(self):
        self.scroll_into_view(self.EMAIL)
        return self.get_text(self.EMAIL)

    def goto_LoginPage(self):
        self.click_button(self.LOGIN_BUTTON)
        return LoginPage(self.driver)



