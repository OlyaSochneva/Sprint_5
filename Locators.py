from selenium.webdriver.common.by import By


class TestLocators:
    MAIN_PAGE_LOGIN_BUTTON = By.XPATH, '//button[contains(text(), "Войти в аккаунт")]'  # кнопка «Войти в аккаунт» на главной
    MAIN_PAGE_MENU_BAR = By.XPATH, '//*[contains(@class, "menuContainer")]'  # панель с ингредиентами
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, '//*[@href="/account"]'  # кнопка «Личный кабинет»
    CONSTRUCTOR_BUTTON = By.XPATH, '//*[contains(text(), "Конструктор")]/parent::a'  # кнопка «Конструктор»
    LOGO = By.XPATH, '//*[contains(@class, "header__logo")]'  # логотип

    AUTH_FORM = By.XPATH, '//*[contains(@class, "Auth_login")]'  # форма авторизации
    EMAIL_INPUT_FIELD = By.NAME, 'name'  # поле ввода email на стр./автор.
    PASSWORD_INPUT_FIELD = By.NAME, 'Пароль'  # поле ввода пароля на стр./автор.
    AUTH_FORM_LOGIN_BUTTON = By.XPATH, '//button[contains(text(), "Войти")]'  # кнопка «Войти» на стр./автор.
    GO_TO_REGISTER_PAGE_BUTTON = By.XPATH, '//*[@href="/register"]'  # кнопка «Зарегистрироваться» на стр./автор.
    GO_TO_RESET_PASSWORD_BUTTON = By.XPATH, '//*[contains(text(), "Восстановить пароль")]'  # кнопка восст. пароль на стр./автор.

    RESET_PASSWORD_HEADER = By.XPATH, '//h2[contains(text(), "Восстановление пароля")]'  # заголовок стр восстановления пароля
    RESET_PASSWORD_PAGE_LOGIN_BUTTON = By.XPATH, '//*[contains(text(), "Войти")]'

    REGISTER_FORM = By.XPATH, '//*[contains(@class, "Auth_form")]'  # форма регистрации
    REG_NAME_INPUT_FIELD = By.XPATH, '//label[contains(text(), "Имя")]/following-sibling::input'  # поле ввода имени на стр./рег.
    REG_EMAIL_INPUT_FIELD = By.XPATH, '//label[contains(text(), "Email")]/following-sibling::input'  # поле ввода email на стр./рег.
    REG_PASSWORD_INPUT_FIELD = By.NAME, 'Пароль'  # поле ввода пароля на стр./рег.
    REGISTRATION_BUTTON = By.XPATH, '//button[contains(text(), "Зарегистрироваться")]'  # кнопка «Зарегистрироваться» на стр./рег.
    REGISTER_PAGE_LOGIN_BUTTON = By.XPATH, '//*[contains(text(), "Войти")]'  # кнопка «Войти» на стр./рег.
    WRONG_PASSWORD_TEXT = By.XPATH, '//*[contains(text(), "Некорректный пароль")]'

    ACCOUNT_NAVIGATION_BAR = By.XPATH, '//*[contains(@class, "Account_nav")]'  # панель упр. аккаунтом в личном кабинете
    LOGOUT_BUTTON = By.XPATH, '//*[contains(@class, "Account_button")]'  # кнопка «Выход» в лич./каб.

    BUNS_SECTION_BUTTON = By.XPATH, '//span[contains(text(), "Булки")]/parent::div[contains(@class, "tab_tab")]'  # вкладка «Булки»
    BUNS_SECTION_HEADER = By.XPATH, '//h2[contains(@class, "text") and text()="Булки"]'  # заголовок «Булки»
    SAUCES_SECTION_BUTTON = By.XPATH, '//span[contains(text(), "Соусы")]/parent::div[contains(@class, "tab_tab")]'  # вкладка «Соусы»
    SAUCES_SECTION_HEADER = By.XPATH, '//h2[contains(@class, "text") and text()="Соусы"]'  # заголовок «Соусы»
    FILLINGS_SECTION_BUTTON = By.XPATH, '//span[contains(text(), "Начинки")]/parent::div[contains(@class, "tab_tab")]'  # вкладка «Начинки»
    FILLINGS_SECTION_HEADER = By.XPATH, '//h2[contains(@class, "text") and text()="Начинки"]'  # заголовок «Начинки»
