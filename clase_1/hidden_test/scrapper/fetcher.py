from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


URL = "https://www.provinciafondos.com.ar/nuestros-fondos"

def download_pdf(url, filepath):

    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    with open(filepath, "wb") as f:
        f.write(response.content)
        
def get_detail_html(url):
    options = Options()
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//h3[contains(., 'Rendimiento')]"
                )
            )
        )
        
        return driver.page_source
    
    finally:
        driver.quit()

def get_html():
    options = Options()

    # después lo activamos
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(URL)

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "a[href*='/nuestros-fondos/']"
                )
            )
        )

        return driver.page_source

    finally:
        driver.quit()