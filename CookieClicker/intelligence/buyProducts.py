from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from CookieClicker.getAttrs import getProducts, getCookies
import random


def buyProducts(driver: WebDriver, Products: list[str, int]) -> list[str, int]:
    CookieAmount = getCookies(driver)

    Products.sort(key=lambda x: x[1], reverse=True)

    for i in range(len(Products) - 1):
        if (
            Products[i][1] <= CookieAmount
            and Products[i][1] <= 0.5 * Products[i - 1][1]
        ):
            driver.find_element(By.ID, Products[i][0]).click()
            Products = getProducts(driver)

            return Products

        randomArray = []

    for i in range(2):
        randomArray.append(i)

    randomchoice = random.choice(randomArray)

    if randomchoice == 1 and CookieAmount > Products[0][1]:
        driver.find_element(By.ID, "product0").click()
        Products = getProducts(driver)

    elif randomchoice == 2 and CookieAmount > Products[1][1]:
        driver.find_element(By.ID, "product1").click()
        Products = getProducts(driver)

    return Products
