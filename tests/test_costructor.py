from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Locators import TestLocators


class TestConstructor:

    def test_move_to_buns_section(self, driver):
        driver.find_element(*TestLocators.SAUCES_SECTION_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SAUCES_SECTION_HEADER))
        element = driver.find_element(*TestLocators.BUNS_SECTION_BUTTON)
        element.click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUNS_SECTION_HEADER))
        assert 'current' in element.get_attribute('class')

    def test_move_to_sauces_section(self, driver):
        element = driver.find_element(*TestLocators.SAUCES_SECTION_BUTTON)
        element.click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SAUCES_SECTION_HEADER))
        assert 'current' in element.get_attribute('class')

    def test_move_to_fillings_section(self, driver):
        element = driver.find_element(*TestLocators.FILLINGS_SECTION_BUTTON)
        element.click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.FILLINGS_SECTION_HEADER))
        assert 'current' in element.get_attribute('class')
