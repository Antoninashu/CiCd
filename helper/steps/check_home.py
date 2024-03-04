from selenium.webdriver.chrome.options import Options
from CiCd.helper.pages.header import *

driver = webdriver.Chrome()
driver.maximize_window()
option = Options()
option.add_argument("--start-maximized")
prefs = {"profile.default_content_setting_values.notifications": 1}
option.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=option)


def open_site(driver):
    open_base = BasePage(driver)
    open_base.open_site()


def text_areas_of_study(driver):
    check_text = AreasOfStudy(driver)
    check_text.study_list()


def text_nearest_courses(driver):
    check_c_text = AreasOfStudy(driver)
    check_c_text.nearest_courses()
