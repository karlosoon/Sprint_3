import pytest
from selenium.webdriver import Chrome
from my_test_data import MyTestData


@pytest.fixture()
def test_email():
    return MyTestData.test_email


@pytest.fixture()
def generate_email():
    return MyTestData.generate_email()


@pytest.fixture()
def valid_password():
    return MyTestData.valid_password


@pytest.fixture()
def invalid_password():
    return MyTestData.invalid_password


@pytest.fixture()
def name():
    return MyTestData.name


@pytest.fixture()
def driver():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()



