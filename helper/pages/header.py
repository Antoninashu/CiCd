from CiCd.helper.weiters import weit
from CiCd.helper.pages.base import *


class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def header_about_us(self):
        weit.base_waits(self.driver, xpath.about_us_xpath)

    def header_courses(self):
        weit.base_waits(self.driver, xpath.courses_xpath)

    def header_news(self):
        weit.base_waits(self.driver, xpath.news_xpath)

    def header_knowledge_base(self):
        weit.base_waits(self.driver, xpath.knowledge_base_xpath)

    def header_faq(self):
        weit.base_waits(self.driver, xpath.faq_xpath)

    def header_contacts(self):
        weit.base_waits(self.driver, xpath.contacts_xpath)
