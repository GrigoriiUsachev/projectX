from ui.pages.login_page import LoginPage
from ui.pages.inventory_page import InventoryPage


def test_login_standard_user(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")
    InventoryPage(driver).wait_loaded()