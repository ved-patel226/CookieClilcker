from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def clickCookie(driver: WebDriver) -> list:
    driver.execute_script("Game.ClickCookie()")


def getCookies(driver: WebDriver) -> int:
    cookies = (
        driver.find_element(By.ID, "cookies").get_attribute("innerText").split(" ")[0]
    )

    cookies = cookies.replace("\ncookies\nper", "")
    cookies = int(cookies.replace(",", ""))

    return cookies
