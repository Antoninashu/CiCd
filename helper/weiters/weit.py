from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def base_waits(driver, xpath):
    waiters = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
    waiters.click()

# def base_field(dr, xpath, user_data_copy):
#     elem = WebDriverWait(dr, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
#     elem.send_keys(data)

def base_lable(dr, xpath):
    elem = WebDriverWait(dr, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
    return elem.text



