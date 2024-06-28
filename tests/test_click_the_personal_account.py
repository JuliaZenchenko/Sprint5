from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators

class TestButtonClickAndNavigation:
    def test_click_on_the_button_pers_account(self, driver):
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        mess = driver.find_element(*Locators.TITLE_ENTER).text
        assert mess == 'Вход'

    def test_transfer_to_the_pers_account(self, login):
        driver=login
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TITLE_PROFILE)).text
        assert mess == "Профиль"
