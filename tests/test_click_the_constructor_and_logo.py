from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConcLogo:
    def test_click_on_the_button_constructor(self, login):
        driver = login

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/account"]'))).click()
        driver.find_element(By.XPATH, '//a[@href="/account"]').click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//li[1]//p'))).click()

        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1'))).text
        assert mess == "Соберите бургер"
        if mess == 'Соберите бургер':
            print("Тест пройден. Переход из личного кабинета в конструктор через кнопку Конструктор")
        else:
            print("Тест не пройден")

    def test_click_on_the_logo(self, login):
        driver = login
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/account"]'))).click()
        driver.find_element(By.XPATH, '//a[@href="/account"]').click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[1]/a[1]'))).click()

        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1'))).text
        assert mess == "Соберите бургер"
        if mess == 'Соберите бургер':
            print("Тест пройден. Переход из личного кабинета в конструктор через логотип")
        else:
            print("Тест не пройден")