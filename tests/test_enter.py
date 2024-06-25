from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Sprint_5.Sprint_5.tests.constants import Constants
from Sprint_5.Sprint_5.tests.locators import Locators

class TestEnter:
    def test_enter_by_button_the_pers_account(self, login):
        driver=login

        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1'))).text
        assert mess=="Соберите бургер"
        if mess == 'Соберите бургер':
            print("Тест пройден. Мы вошли в свой аккаунт по кнопке Личный кабинет")
        else:
            print("Тест не пройден")

    def test_enter_by_the_account_button(self, driver):
        email = Constants.EMAIL
        password = Constants.PASSWORD

        driver.find_element(By.XPATH, "//section[2]/div[1]/button[1]").click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON).click()
        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1'))).text
        assert mess == "Соберите бургер"
        if mess == 'Соберите бургер':
            print("Тест пройден. Мы вошли в свой аккаунт по кнопке Войти в аккаунт")
        else:
            print("Тест не пройден")

    def test_enter_by_the_registration_form(self, driver):
        email = Constants.EMAIL
        password = Constants.PASSWORD

        driver.find_element(*Locators.PAGE).click()
        driver.find_element(By.XPATH, '//a[@href="/register"]').click()
        driver.find_element(By.XPATH, '//a[@href="/login"]').click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON).click()

        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1'))).text
        assert mess == "Соберите бургер"
        if mess == 'Соберите бургер':
            print("Тест пройден. Мы вошли в свой аккаунт из формы регистрации")
        else:
            print("Тест не пройден")

    def test_enter_by_recover_password(self, driver):
        email = Constants.EMAIL
        password = Constants.PASSWORD

        driver.find_element(By.XPATH, "//section[2]/div[1]/button[1]").click()
        driver.find_element(By.XPATH, '//a[@href="/forgot-password"]').click()
        driver.find_element(By.TAG_NAME, 'input').send_keys(email)
        driver.find_element(By.XPATH, '//form/button[1]').click()
        driver.refresh()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//a[@href="/login"]')))
        driver.find_element(By.XPATH, '//a[@href="/login"]').click()
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON).click()

        mess = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1'))).text
        assert mess == "Соберите бургер"
        if mess == 'Соберите бургер':
            print("Тест пройден. Мы вошли в свой аккаунт по кнопке Вoсстановить пароль")
        else:
            print("Тест не пройден")