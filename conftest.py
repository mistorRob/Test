import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup_teardown():
    link = "https://ohota26.ru/"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.get(link)

    yield browser

    browser.quit()
