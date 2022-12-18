from locators import TestLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from login_func import login


class TestLogin:
    def test_login_by_sign_in_button_on_main_page(self, test_email, valid_password, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(
            TestLocators.EMAIL_FIELD_IN_LOGIN_FORM))
        login(driver, test_email, valid_password)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE))
        assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE).text == "Оформить заказ"

    def test_login_by_profile_button_on_main_page(self, test_email, valid_password, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(
            TestLocators.EMAIL_FIELD_IN_LOGIN_FORM))
        login(driver, test_email, valid_password)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE))
        assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE).text == "Оформить заказ"

    def test_login_by_sign_in_button_on_registration_page(self, test_email, valid_password, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_ON_REGISTRATION_PAGE).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(TestLocators.SIGN_IN_BUTTON_IN_LOGIN_FORM))
        login(driver, test_email, valid_password)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE))
        assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE).text == "Оформить заказ"

    def test_login_by_sign_in_button_on_forget_password_page(self, test_email, valid_password, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_ON_FORGOT_PASSWORD_PAGE).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(TestLocators.SIGN_IN_BUTTON_IN_LOGIN_FORM))
        login(driver, test_email, valid_password)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE))
        assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE).text == "Оформить заказ"
