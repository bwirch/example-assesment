import pytest
from login_pom import HomePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from session_util import create_session
from session_util import quit_session

login_url = "https://www.quora.com/"


def test_failed_user_account():
    login_email = "rebekah@quora.com"
    login_password = "secret"
    session = create_session("Chrome", login_url)
    login_page = HomePage(session)
    login_page.login(login_email, login_password)
    alert = WebDriverWait(session, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="alert"]'))
    )
    assert alert
    quit_session(session)


def test_create_account():
    session = create_session("Chrome", login_url)
    login_page = HomePage(session)
    login_page.create_new_account("Bec", "bec@quora.com")
    assert WebDriverWait(session, 10).until(
        EC.presence_of_element_located((By.ID, "confirmation-code"))
    )
    quit_session(session)
