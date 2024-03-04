from CiCd.helper.weiters import weit
from CiCd.helper.xpath import xpath
from CiCd.helper.pages.base import BasePage


class AboutUs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def qalight_is(self):
        weit.base_waits(self.driver, xpath.qalight_is_xpath)

    def administration(self):
        weit.base_waits(self.driver, xpath.administration_xpath)

    def our_trainers(self):
        weit.base_waits(self.driver, xpath.our_trainers_xpath)

    def gallery(self):
        weit.base_waits(self.driver, xpath.gallery_xpath)

    def reviews(self):
        weit.base_waits(self.driver, xpath.reviews_xpath)