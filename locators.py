from selenium.webdriver.common.by import By


class TestLocators:
    PROFILE_BUTTON = By.XPATH, './/p[text()="Личный Кабинет"]'  # кнопка Личный Кабинет

    NEW_USER_REGISTRATION_BUTTON = \
        By.XPATH, './/button[text()="Зарегистрироваться"]'  # кнопка Зарегистрироваться в окне регистрации

    USERNAME_FIELD_IN_REGISTRATION_FORM = By.XPATH, './/input[@name="name"]'  # поле ввода имени в окне регистрации

    EMAIL_FIELD_IN_REGISTRATION_FORM = By.XPATH, './/fieldset[2]//input'  # поле ввода емейл в окне регистрации

    PASSWORD_FIELD_IN_REGISTRATION_FORM = By.XPATH, './/input[@name="Пароль"]'  # поле ввода пароля в окне регистрации

    EMAIL_FIELD_IN_LOGIN_FORM = By.XPATH, './/input[@name="name"]'  # поле ввода емейл в окне логина

    PASSWORD_FIELD_IN_LOGIN_FORM = By.XPATH, './/input[@name="Пароль"]'  # поле ввода пароля в окне логина

    SIGN_IN_BUTTON_IN_LOGIN_FORM = By.XPATH, './/button[text()="Войти"]'  # кнопка Войти в окне логина

    INVALID_PASSWORD_TEXT_IN_REGISTRATION_FORM = \
        By.XPATH, './/p[@class="input__error text_type_main-default"]'  # надпись Некорректный пароль в окне регистрации

    SIGN_IN_BUTTON_ON_MAIN_PAGE = By.XPATH, './/button[text()="Войти в аккаунт"]'  # кнопка логина на главной

    MAKE_ORDER_BUTTON_ON_MAIN_PAGE = \
        By.XPATH, './/button[text()="Оформить заказ"]'  # кнопка оформить заказ на главной

    SIGN_IN_BUTTON_ON_REGISTRATION_PAGE = By.XPATH, './/a[text()="Войти"]'  # кнопка Войти в окне регистрации

    SIGN_IN_BUTTON_ON_FORGOT_PASSWORD_PAGE = \
        By.XPATH, './/a[text()="Войти"]'  # кнопка Войти в окне восстановления пароля

    SAVE_BUTTON_ON_PROFILE_PAGE = By.XPATH, './/button[text()="Сохранить"]'  # кнопка Сохранить в профиле

    LOGOUT_BUTTON = By.XPATH, './/button[text()="Выход"]'  # кнопка Выход в профиле

    HEADER_ON_LOGIN_PAGE = By.XPATH, './/h2[text()="Вход"]'  # хедер "Вход" в окне логина

    CONSTRUCTOR_BUTTON = By.XPATH, './/p[text()="Конструктор"]'  # кнопка "Конструктор"

    BURGER_BUTTON = By.XPATH, './/div[@class="AppHeader_header__logo__2D0X2"]'  # кнопка бургер

    CONSTRUCTOR_SAUCES_TAB = By.XPATH, './/span[text()="Соусы"]'  # вкладка Соусы

    CONSTRUCTOR_SAUCES_SECTION = By.XPATH, './/h2[text()="Соусы"]'  # раздел Соусы

    CONSTRUCTOR_STUFFING_TAB = By.XPATH, './/span[text()="Начинки"]'  # вкладка Начинки

    CONSTRUCTOR_STUFFING_SECTION = By.XPATH, './/h2[text()="Начинки"]'  # раздел Начинки

    CONSTRUCTOR_BUNS_TAB = By.XPATH, './/span[text()="Булки"]'  # вкладка Булки

    CONSTRUCTOR_BUNS_SECTION = By.XPATH, './/h2[text()="Булки"]'  # раздел Булки
