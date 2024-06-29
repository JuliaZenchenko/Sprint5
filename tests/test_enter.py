from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constants
from locators import Locators


class TestEnter:
    def test_enter_by_button_the_pers_account(self, login):
        driver = login
        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TITLE_THE_BURGER)).text
        assert mess=="Соберите бургер"


    def test_enter_by_the_account_button(self, driver):
        email = Constants.EMAIL
        password = Constants.PASSWORD

        driver.find_element(*Locators.BUTTON_ENTER_IN_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON).click()
        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.TITLE_THE_BURGER)).text
        assert mess == "Соберите бургер"


    def test_enter_by_the_registration_form(self, driver):
        email = Constants.EMAIL
        password = Constants.PASSWORD

        driver.find_element(*Locators.PAGE).click()
        driver.find_element(*Locators.BUTTON_REGISTRATION_ON_PAGE_ENTER).click()
        driver.find_element(*Locators.BUTTON_ENTER_ON_PAGE_REGISTRATION).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON).click()

        mess = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TITLE_THE_BURGER)).text
        assert mess == "Соберите бургер"


    def test_enter_by_recover_password(self, driver):
        email = Constants.EMAIL
        password = Constants.PASSWORD

        driver.find_element(*Locators.BUTTON_ENTER_IN_ACCOUNT).click()
        driver.find_element(*Locators.BUTTON_RECOVER_PASSWORD).click()
        driver.find_element(*Locators.EMAIL_FOR_RECOVER_PASSWORD).send_keys(email)
        driver.find_element(*Locators.BUTTON_RECOVER).click()
        driver.refresh()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.BUTTON_ENTER_ON_PAGE_REGISTRATION))
        driver.find_element(*Locators.BUTTON_ENTER_ON_PAGE_REGISTRATION).click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON).click()

        mess = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TITLE_THE_BURGER)).text
        assert mess == "Соберите бургер"
