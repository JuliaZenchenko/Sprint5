from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators
class TestConctructor:
    def test_constructor_souse(self, login):
        driver = login
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_CONSTRUCTOR_SOUSE)).click()
        element=driver.find_element(*Locators.TITLE_SOUSE)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TITLE_SOUSE)).text
        assert mess == 'Соусы'

    def test_constructor_pan(self, login):
        driver = login
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_CONSTRUCTOR_SOUSE)).click()
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR_PAN).click()
        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TITLE_PAN)).text
        assert mess == 'Булки'

    def test_constructor_add(self, login):
        driver = login
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.BUTTON_CONSTRUCTOR_ADD)).click()
        element=driver.find_element(*Locators.TITLE_ADD)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TITLE_ADD)).text
        assert mess == 'Начинки'
