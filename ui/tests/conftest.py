import datetime
import os
import tempfile

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    options.add_argument("--guest")

    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-sync")

    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,

        
        "safebrowsing.enabled": False,
        "safebrowsing.disable_download_protection": True,
    }
    options.add_experimental_option("prefs", prefs)

    options.add_argument(
        "--disable-features="
        "PasswordLeakDetection,"
        "PasswordManagerOnboarding,"
        "PasswordManagerRedesign,"
        "AutofillEnableAccountWalletStorage,"
        "AutofillEnablePayments"
    )

    tmp_profile = tempfile.mkdtemp(prefix="projectx_chrome_")
    options.add_argument(f"--user-data-dir={tmp_profile}")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            project_root = os.path.dirname(
                os.path.dirname(
                    os.path.dirname(os.path.abspath(__file__))
                )
            )
            screenshots_dir = os.path.join(project_root, "ui", "reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{item.name}_{ts}.png"
            path = os.path.join(screenshots_dir, filename)

            driver.save_screenshot(path)
