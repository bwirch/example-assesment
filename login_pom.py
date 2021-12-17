from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    """Quora loginpage object model.

    Attributes:
        driver: selenium webdriver
    """

    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    EMAIL_SIGNUP_BUTTON = (
        By.CSS_SELECTOR,
        ".q-box.qu-pb--small.qu-mb--small.qu-borderBottom > button",
    )
    SIGNUP_NAME = (By.ID, "profile-name")
    SIGNUP_EMAIL = (By.NAME, "email")
    NEXT_BUTTON = (By.CSS_SELECTOR, 'button[type="button"]')

    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def input_username(self, email: str):
        email_input = self.driver.find_element(*HomePage.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    def input_password(self, password: str):
        password_input = self.driver.find_element(*HomePage.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def submit_login(self):
        "To Do: add login button"

    def click_sign_up_email(self):
        sign_up_email_button = self.driver.find_element(*HomePage.EMAIL_SIGNUP_BUTTON)
        sign_up_email_button.click()

    def input_profile_name(self, profile_name: str):
        name_input = self.driver.find_element(*HomePage.SIGNUP_NAME)
        name_input.clear()
        name_input.send_keys(profile_name)

    def input_new_email(self, new_email: str):
        new_email_input = self.driver.find_element(*HomePage.SIGNUP_EMAIL)
        new_email_input.clear()
        new_email_input.send_keys(new_email)

    def signup_next(self):
        next_button = self.driver.find_element(*HomePage.NEXT_BUTTON)
        next_button.click()

    def login(self, email: str, password: str):
        self.input_username(email)
        self.input_password(password)

    def create_new_account(self, profile_name: str, new_email: str):
        self.click_sign_up_email()
        signup_popup = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="dialog"]'))
        )
        self.input_profile_name(profile_name)
        self.input_new_email(new_email)
        self.signup_next()
