from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from CiCd.helper.pages.about_us import *
from CiCd.helper.pages.header import *



driver = webdriver.Chrome()
driver.maximize_window()
option = Options()
option.add_argument("--start-maximized")
prefs = {"profile.default_content_setting_values.notifications": 1}
option.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=option)

# url = 'https://qalight.ua/'
# driver.get(url)
hedaer = Header(driver)
about_menu = AboutUs(driver)

about_menu.open_site()
hedaer.header_about_us()
about_menu.qalight_is()
about_menu.administration()
about_menu.our_trainers()
about_menu.gallery()
about_menu.reviews()
