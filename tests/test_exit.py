from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestExit:
    def test_exit(self, login):
        driver = login
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_EXIT)).click()
        WebDriverWait(driver, 5).until(EC.url_matches("https://stellarburgers.nomoreparties.site/login"))

        mess = driver.find_element(*Locators.TITLE_ENTER).text
        assert mess == 'Вход'
