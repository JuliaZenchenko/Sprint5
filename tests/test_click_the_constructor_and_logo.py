from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestButtonClickConstructorLogo:
    def test_click_on_the_button_constructor(self, login):
        driver = login
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_CONSTRUCTOR)).click()
        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TITLE_THE_BURGER)).text
        assert mess == "Соберите бургер"

    def test_click_on_the_logo(self, login):
        driver = login
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_LOGO)).click()
        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TITLE_THE_BURGER)).text
        assert mess == "Соберите бургер"
