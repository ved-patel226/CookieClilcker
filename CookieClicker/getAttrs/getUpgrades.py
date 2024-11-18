from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def getUpgrades(driver: WebDriver) -> list:
    allUpgrades = driver.find_elements(By.CLASS_NAME, "upgrade")

    if allUpgrades:
        first_upgrade = allUpgrades[0]
        first_upgrade.click()
