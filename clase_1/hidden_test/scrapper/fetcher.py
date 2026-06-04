from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

URL = "https://www.provinciafondos.com.ar/nuestros-fondos"


def build_driver():

    options = Options()

    # headless real
    options.add_argument("--headless=new")

    # estabilidad
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # menos ruido
    options.add_argument("--log-level=3")

    # tamaño consistente
    options.add_argument("--window-size=1920,1080")

    return webdriver.Chrome(options=options)


def download_pdf(url, filepath):

    response = requests.get(url, timeout=30)

    response.raise_for_status()

    with open(filepath, "wb") as f:
        f.write(response.content)


def get_html():

    driver = build_driver()

    try:

        driver.get(URL)

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "a[href*='/nuestros-fondos/']")
            )
        )

        return driver.page_source

    finally:

        driver.quit()


def get_detail_html(url):

    driver = build_driver()

    try:

        driver.get(url)

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h3[contains(., 'Rendimiento')]")
            )
        )

        return driver.page_source

    finally:

        driver.quit()


def get_cuotapartes_html(fondo_id):

    driver = build_driver()

    try:

        url = (
            "https://www.provinciafondos.com.ar/"
            f"nuestros-fondos/cuotaparte/{fondo_id}"
        )

        driver.get(url)

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, "//h3[contains(., 'Histórico valores')]")
            )
        )

        return driver.page_source

    finally:

        driver.quit()
