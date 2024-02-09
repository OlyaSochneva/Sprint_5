from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators


class TestLogin:

    def test_login_by_main_page_login_button(self, driver, go_to_login_page, existing_user):
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(existing_user.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(existing_user.password)
        driver.find_element(*TestLocators.AUTH_FORM_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_MENU_BAR))
        assert expected_conditions.invisibility_of_element(TestLocators.MAIN_PAGE_LOGIN_BUTTON)

    def test_login_by_personal_account_button(self, driver, existing_user):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM))
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(existing_user.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(existing_user.password)
        driver.find_element(*TestLocators.AUTH_FORM_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_MENU_BAR))
        assert expected_conditions.invisibility_of_element(TestLocators.MAIN_PAGE_LOGIN_BUTTON)

    def test_login_by_register_page_login_button(self, driver, go_to_register_page, existing_user):
        driver.find_element(*TestLocators.REGISTER_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM))
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(existing_user.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(existing_user.password)
        driver.find_element(*TestLocators.AUTH_FORM_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_MENU_BAR))
        assert expected_conditions.invisibility_of_element(TestLocators.MAIN_PAGE_LOGIN_BUTTON)

    def test_login_by_reset_password_page_login_button(self, driver, go_to_login_page, existing_user):
        driver.find_element(*TestLocators.GO_TO_RESET_PASSWORD_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.RESET_PASSWORD_HEADER))
        driver.find_element(*TestLocators.RESET_PASSWORD_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM))
        driver.find_element(*TestLocators.EMAIL_INPUT_FIELD).send_keys(existing_user.email)
        driver.find_element(*TestLocators.PASSWORD_INPUT_FIELD).send_keys(existing_user.password)
        driver.find_element(*TestLocators.AUTH_FORM_LOGIN_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_MENU_BAR))
        assert expected_conditions.invisibility_of_element(TestLocators.MAIN_PAGE_LOGIN_BUTTON)
