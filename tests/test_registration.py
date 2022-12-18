from locators import TestLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from login_func import login


class TestRegistration:
    def test_registration(self, generate_email, valid_password, name, driver):
        email = generate_email
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*TestLocators.USERNAME_FIELD_IN_REGISTRATION_FORM).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_REGISTRATION_FORM).send_keys(generate_email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_REGISTRATION_FORM).send_keys(valid_password)
        driver.find_element(*TestLocators.NEW_USER_REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 4).until(ec.visibility_of_element_located(
            TestLocators.SIGN_IN_BUTTON_IN_LOGIN_FORM))
        login(driver, email, valid_password)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE))
        assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE).text == "Оформить заказ"

    def test_registration_invalid_password(self, generate_email, invalid_password, name, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*TestLocators.USERNAME_FIELD_IN_REGISTRATION_FORM).send_keys(name)
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_REGISTRATION_FORM).send_keys(generate_email)
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_REGISTRATION_FORM).send_keys(invalid_password)
        driver.find_element(*TestLocators.NEW_USER_REGISTRATION_BUTTON).click()
        assert driver.find_element(*TestLocators.INVALID_PASSWORD_TEXT_IN_REGISTRATION_FORM).text == \
               'Некорректный пароль'

