from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from pathlib import Path

screens_dir = Path(
    "reports/screens"
)

screens_dir.mkdir(
    parents=True,
    exist_ok=True
)


def before_scenario(context, scenario):

    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


def after_scenario(context, scenario):

    context.driver.quit()


def after_step(context, step):

    if step.status == "failed":

        try:

            nombre = (
                step.name.replace(" ", "_")
                + ".png"
            )

            context.driver.save_screenshot(
                str(
                    screens_dir / nombre
                )
            )

        except WebDriverException:
            pass

