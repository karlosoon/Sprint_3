from locators import TestLocators


def login(driver, email, valid_password):
    driver.find_element(*TestLocators.EMAIL_FIELD_IN_LOGIN_FORM).send_keys(email)
    driver.find_element(*TestLocators.PASSWORD_FIELD_IN_LOGIN_FORM).send_keys(valid_password)
    driver.find_element(*TestLocators.SIGN_IN_BUTTON_IN_LOGIN_FORM).click()
