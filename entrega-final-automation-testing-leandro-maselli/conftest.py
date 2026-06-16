import os
import time
from datetime import datetime

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service()

    driver = webdriver.Chrome(
        service=service,
        options=chrome_options
    )

    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver

    time.sleep(1)
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    if report.failed:

        driver = item.funcargs.get("driver")

        if not driver:
            return

        os.makedirs("reports/screens", exist_ok=True)

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filename = (
            f"{item.name}_{timestamp}.png"
        )

        path = os.path.join(
            "reports",
            "screens",
            filename
        )

        driver.save_screenshot(path)

        print(f"\nScreenshot guardado: {path}")