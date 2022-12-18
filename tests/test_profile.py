from locators import TestLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from login_func import login


class TestProfile:
    def test_open_profile_page_from_main_page(self, driver, test_email, valid_password):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_ON_MAIN_PAGE).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(TestLocators.EMAIL_FIELD_IN_LOGIN_FORM))
        login(driver, test_email, valid_password)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE))
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(TestLocators.SAVE_BUTTON_ON_PROFILE_PAGE))
        assert driver.find_element(*TestLocators.SAVE_BUTTON_ON_PROFILE_PAGE).is_displayed()

    def test_logout(self, driver, test_email, valid_password):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        login(driver, test_email, valid_password)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE))
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(TestLocators.SIGN_IN_BUTTON_IN_LOGIN_FORM))
        assert driver.find_element(*TestLocators.HEADER_ON_LOGIN_PAGE).text == "Вход"
