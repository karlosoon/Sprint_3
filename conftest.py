import pytest
import random
from selenium.webdriver import Chrome


@pytest.fixture()
def test_email():
    return 'test9999@yandex.ru'


@pytest.fixture()
def generate_email():
    return 'maxim_karlo' + str(random.randint(1000, 9999)) + '@yandex.ru'


@pytest.fixture()
def valid_password():
    return '123123'


@pytest.fixture()
def invalid_password():
    return '123'


@pytest.fixture()
def name():
    return 'Maxim'


@pytest.fixture()
def driver():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()



