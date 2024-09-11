import subprocess
import time
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = 'YOUR CHROME DRIVER PATH!'
URL = "http://192.168.0.1"
USERNAME = "user"
PASSWORD = "YOUR PASSWORD!"

def run_selenium_script():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 10)

    def login():
        driver.get(URL)
        wait.until(EC.presence_of_element_located((By.ID, 'txtUser'))).send_keys(USERNAME)
        wait.until(EC.presence_of_element_located((By.ID, 'txtPwd'))).send_keys(PASSWORD)
        wait.until(EC.element_to_be_clickable((By.ID, 'btnLogin'))).send_keys(Keys.RETURN)

    def navigate_to_apn_settings():
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="#internet_setting"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="#apn_setting"]'))).click()

    def set_default_profile():
        select_element = wait.until(EC.presence_of_element_located((By.NAME, 'profile')))
        select = Select(select_element)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='3internet']")))
            select.select_by_value("three.co.uk")
            wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Set as default"]'))).click()
            time.sleep(2)
            select.select_by_value("3internet")
            time.sleep(4)
        except:
            wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='three.co.uk']")))
            select.select_by_value("3internet")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Set as default"]'))).click()

    try:
        login()
        navigate_to_apn_settings()
        set_default_profile()
    finally:
        time.sleep(5)
        driver.quit()

run_selenium_script()