from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators


class TestPersonalAccount:

    def test_move_to_personal_account_by_click_on_button(self, driver, go_to_personal_page):
        assert expected_conditions.visibility_of_element_located(TestLocators.ACCOUNT_NAVIGATION_BAR)

    def test_move_from_personal_account_to_constructor(self, driver, go_to_personal_page):
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_MENU_BAR))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_move_from_personal_account_to_main_page_by_logo(self, driver, go_to_personal_page):
        driver.find_element(*TestLocators.LOGO).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.MAIN_PAGE_MENU_BAR))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_exit_personal_account_by_logout_button(self, driver, go_to_personal_page):
        driver.find_element(*TestLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM))
        assert expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM)
