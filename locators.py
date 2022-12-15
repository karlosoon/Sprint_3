from selenium.webdriver.common.by import By


class TestLocators:
    PROFILE_BUTTON = By.XPATH, '//*[@id="root"]/div/header/nav/a' # кнопка Личный Кабинет

    IN_PROFILE_NEW_USER_REGISTRATION_BUTTON = \
        By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a' # кнопка Зарегистрироваться в личном кабинете

    NEW_USER_REGISTRATION_BUTTON = \
        By.XPATH, '//*[@id="root"]/div/main/div/form/button' # кнопка Зарегистрироваться в окне регистрации

    USERNAME_FIELD_IN_REGISTRATION_FORM = \
        By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input[@name="name"]' # поле ввода имени в окне регистрации

    EMAIL_FIELD_IN_REGISTRATION_FORM = \
        By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input' # поле ввода емейл в окне регистрации

    PASSWORD_FIELD_IN_REGISTRATION_FORM = \
        By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input' # поле ввода пароля в окне регистрации

    EMAIL_FIELD_IN_LOGIN_FORM = \
        By.CSS_SELECTOR, '#root > div > main > div > form > fieldset:nth-child(1) > div > div > input' # поле ввода емейл в окне логина

    PASSWORD_FIELD_IN_LOGIN_FORM = \
        By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input' # поле ввода пароля в окне логина

    SIGN_IN_BUTTON_IN_LOGIN_FORM = \
        By.XPATH, '//*[@id="root"]/div/main/div/form/button[text()="Войти"]' # кнопка Войти в окне логина

    EMAIL_FIELD_IN_PROFILE = \
        By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul/li[2]/div/div/input' # поле с емейл в личном кабинете

    INVALID_PASSWORD_TEXT_IN_REGISTRATION_FORM = \
        By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p' # надпись Некорректный пароль в окне регистрации

    SIGN_IN_BUTTON_ON_MAIN_PAGE = By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button' # кнопка логина на главной

    MAKE_ORDER_BUTTON_ON_MAIN_PAGE = \
        By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button[text()="Оформить заказ"]' # кнопка оформить заказ на главной

    SIGN_IN_BUTTON_ON_REGISTRATION_PAGE = By.XPATH, '//*[@id="root"]/div/main/div/div/p/a' # кнопка Войти в окне регистрации

    SIGN_IN_BUTTON_ON_FORGOT_PASSWORD_PAGE = By.XPATH, '//*[@id="root"]/div/main/div/div/p/a' # кнопка Войти в окне восстановления пароля

    SAVE_BUTTON_ON_PROFILE_PAGE = By.XPATH, '//*[@id="root"]/div/main/div/div/div/div/button[2]' # кнопка Сохранить в профиле

    LOGOUT_BUTTON = By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button' # кнопка Выйти в профиле

    HEADER_ON_LOGIN_PAGE = By.XPATH, '//*[@id="root"]/div/main/div/h2[text()="Вход"]' # хедер "Вход" в окне логина

    CONSTRUCTOR_BUTTON = By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a' # кнопка "Конструктор"

    BURGER_BUTTON = By.XPATH, '//*[@id="root"]/div/header/nav/div' # кнопка бургер

    CONSTRUCTOR_SAUCES_TAB = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span' # вкладка Соусы

    CONSTRUCTOR_SAUCES_SECTION = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]' # раздел Соусы

    CONSTRUCTOR_STUFFING_TAB = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span' # вкладка Начинки

    CONSTRUCTOR_STUFFING_SECTION = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]' # раздел Начинки

    CONSTRUCTOR_BUNS_TAB = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span' # вкладка Булки

    CONSTRUCTOR_BUNS_SECTION = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]' # раздел Булки