def test_home_page():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from CiCd.helper.steps import check_home

    driver = webdriver.Chrome()
    driver.maximize_window()
    option = Options()
    option.add_argument("--start-maximized")
    prefs = {"profile.default_content_setting_values.notifications": 1}
    option.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=option)

    check_home.open_site(driver)
    check_home.text_areas_of_study(driver)
    check_home.text_nearest_courses(driver)
