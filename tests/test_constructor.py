from locators import TestLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from login_func import login

class TestConstructor:
    def test_open_constructor_page_by_constructor_button_from_profile(self, driver, test_email, valid_password):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        login(driver, test_email, valid_password)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(
            TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE))
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(TestLocators.SAVE_BUTTON_ON_PROFILE_PAGE))
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(
            TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE))
        assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE).is_displayed()

    def test_open_constructor_page_by_burger_button_from_profile(self, driver, test_email, valid_password):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        login(driver, test_email, valid_password)
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(
            TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE))
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(
            TestLocators.SAVE_BUTTON_ON_PROFILE_PAGE))
        driver.find_element(*TestLocators.BURGER_BUTTON).click()
        WebDriverWait(driver, 3).until(ec.visibility_of_element_located(
            TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE))
        assert driver.find_element(*TestLocators.MAKE_ORDER_BUTTON_ON_MAIN_PAGE).is_displayed()

    def test_constructor_tab_switch_to_sauces(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.CONSTRUCTOR_SAUCES_TAB).click()
        assert driver.find_element(*TestLocators.CONSTRUCTOR_SAUCES_SECTION).is_displayed()

    def test_constructor_tab_switch_to_stuffing(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.CONSTRUCTOR_STUFFING_TAB).click()
        assert driver.find_element(*TestLocators.CONSTRUCTOR_STUFFING_SECTION).is_displayed()

    def test_constructor_tab_switch_to_buns(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.CONSTRUCTOR_STUFFING_TAB).click()
        driver.find_element(*TestLocators.CONSTRUCTOR_BUNS_TAB).click()
        assert driver.find_element(*TestLocators.CONSTRUCTOR_BUNS_SECTION).is_displayed()
