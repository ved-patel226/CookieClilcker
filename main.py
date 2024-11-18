from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

from CookieClicker import *


def main_loop() -> None:
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--user-data-dir=/home/vedpatel/.config/google-chrome")
    chrome_options.add_argument("--profile-directory=Default")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=chrome_options
    )

    driver.get("https://orteil.dashnet.org/cookieclicker/")
    driver.implicitly_wait(0.02)

    Products = getProducts(driver)

    while True:
        clickCookie(driver)

        Products = buyProducts(driver, Products)

        upgrades = driver.find_elements(
            By.CSS_SELECTOR, "#upgrades .crate.upgrade.enabled"
        )
        if upgrades:
            getUpgrades(driver)

        # getUpgrades(driver)

    time.sleep(10)


if __name__ == "__main__":
    main_loop()
