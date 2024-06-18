import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators
from assistant_classes import User
from assistant_classes import NewUser
from assistant_classes import Generator


@pytest.fixture(scope="function")
def driver():
    my_options = Options()
    service = Service(executable_path="/Users/olyasochneva/Downloads/WebDriver/bin/chromedriver")
    my_options.add_argument("--window-size=1920,1080")
    my_options.add_argument("--disable-web-security")
    my_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=my_options, service=service)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def existing_user():
    return User('olga_sochneva_5111@yandex.ru', '123456')


@pytest.fixture(scope="function")
def new_correct_user():
    return NewUser(Generator.name_generator(), Generator.login_generator(), Generator.password_generator())


@pytest.fixture(scope="function")
def new_user_with_wrong_password():
    return NewUser(Generator.name_generator(), Generator.login_generator(), '123')


@pytest.fixture(scope="function")
def go_to_login_page(driver):
    driver.find_element(*TestLocators.MAIN_PAGE_LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM))


@pytest.fixture(scope="function")
def go_to_register_page(driver):
    driver.find_element(*TestLocators.MAIN_PAGE_LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM))
    driver.find_element(*TestLocators.GO_TO_REGISTER_PAGE_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(TestLocators.REGISTER_FORM))


@pytest.fixture(scope="function")
def go_to_personal_page(driver, existing_user):
    driver.find_element(*TestLocators.MAIN_PAGE_LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM))
    driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(existing_user.email)
    driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(existing_user.password)
    driver.find_element(*TestLocators.AUTH_FORM_LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_MENU_BAR))
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(TestLocators.ACCOUNT_NAVIGATION_BAR))
