from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators


class TestRegistration:

    def test_registration_correct_user(self, driver, go_to_register_page, new_correct_user):
        driver.find_element(*TestLocators.REG_NAME_INPUT_FIELD).send_keys(new_correct_user.name)
        driver.find_element(*TestLocators.REG_EMAIL_INPUT_FIELD).send_keys(new_correct_user.email)
        driver.find_element(*TestLocators.REG_PASSWORD_INPUT_FIELD).send_keys(new_correct_user.password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM))
        assert expected_conditions.visibility_of_element_located(TestLocators.AUTH_FORM)

    def test_registration_user_wrong_password(self, driver, go_to_register_page, new_user_with_wrong_password):
        driver.find_element(*TestLocators.REG_NAME_INPUT_FIELD).send_keys(new_user_with_wrong_password.name)
        driver.find_element(*TestLocators.REG_EMAIL_INPUT_FIELD).send_keys(new_user_with_wrong_password.email)
        driver.find_element(*TestLocators.REG_PASSWORD_INPUT_FIELD).send_keys(new_user_with_wrong_password.password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.WRONG_PASSWORD_TEXT))
        assert expected_conditions.visibility_of_element_located(TestLocators.WRONG_PASSWORD_TEXT)
