import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def user_login():
    login = "login"
    return login


@pytest.fixture(scope="function")
def user_password():
    password = "password"
    return password
