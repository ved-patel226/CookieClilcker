from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


def parse_number(value: str) -> int:
    suffix_multipliers = {
        "million": 10**6,
        "billion": 10**9,
        "thousand": 10**3,
        "trillion": 10**12,
    }

    parts = value.lower().split()

    try:
        number = float(parts[0])
    except (ValueError, IndexError):
        raise ValueError(f"Invalid number format: {value}")

    multiplier = suffix_multipliers.get(parts[1], 1) if len(parts) > 1 else 1

    return int(number * multiplier)


def getProducts(driver: WebDriver) -> list:
    allProducts = driver.find_elements(By.CLASS_NAME, "product")
    allProducts = [product.get_attribute("id") for product in allProducts]

    products = []

    for product in allProducts:
        productName0 = driver.find_element(
            By.CSS_SELECTOR, f"#{product} .content .price"
        ).text
        productName0 = productName0.replace(",", "")

        if productName0 != "":
            products.append([product, parse_number(productName0)])

    print(products)

    return products[::-1]
