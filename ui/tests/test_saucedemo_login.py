import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriver, ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_login_standart_user():
    sevrice = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=sevrice)
    driver.maximize_window()

    try:
        driver.get("https://wwww.saucedemo.com/")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visability_of_element_located((By.ID, "user-name"))).send_keys("standart_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        wait.until(EC.visability_of_element_located((By.CLASS_NAME, "inventory_list")))
        assert ("inventory in driver.current_url")
    finally:
        driver.quit()
