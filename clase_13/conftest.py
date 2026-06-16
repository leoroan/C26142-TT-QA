import pathlib
import pytest

from selenium import webdriver

target = pathlib.Path("reports/screens")
target.mkdir(parents=True, exist_ok=True)


@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            file_name = target / f"{item.name}.png"

            driver.save_screenshot(
                str(file_name)
            )