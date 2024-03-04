from selenium.webdriver.chrome.options import Options
from CiCd.helper.pages.header import *

driver = webdriver.Chrome()
driver.maximize_window()
option = Options()
option.add_argument("--start-maximized")
prefs = {"profile.default_content_setting_values.notifications": 1}
option.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=option)

#
# def open_page_header(driver):
#     open_header = Header(driver)
#     open_header.open_site()
#

def click_header(driver):
    header_button = Header(driver)
    header_button.header_about_us()
    header_button.header_courses()
    header_button.header_news()
    header_button.header_knowledge_base()
    header_button.header_faq()
    header_button.header_contacts()
