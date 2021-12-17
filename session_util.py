from selenium import webdriver


def create_session(driver: str, url: str):
    driver_names = {
        "Chrome": webdriver.Chrome,
        "Edge": webdriver.Edge,
        "Firefox": webdriver.Firefox,
        "Safari": webdriver.Safari,
    }

    browser = None

    if driver in driver_names:
        browser = driver_names[driver]()
        browser.get(url)
        return browser
    else:
        raise Exception("No driver found")


def quit_session(driver: webdriver.Remote):
    driver.quit()
