from selenium.webdriver.common.by import By
from CiCd.helper.xpath import xpath

course_text = (By.XPATH, xpath.course_text_xpath)
course_button = (By.XPATH, xpath.course_button_xpath)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_site(self):
        self.driver.get('https://qalight.ua/')


class AreasOfStudy(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def study_list(self):
        s_list = []
        labels = self.driver.find_elements(By.XPATH, xpath.areas_of_study_xpath)
        for label in labels:
            a = label.text
            s_list.append(a.title())
        print(s_list)
        # return s_list

    def nearest_courses(self):
        n_list = []
        labels = self.driver.find_elements(By.XPATH, xpath.nearest_courses_xpath)
        for label in labels:
            a = label.text
            n_list.append(a.title())
        print(n_list)
        # return n_list
