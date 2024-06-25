from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestClick:
    def test_click_on_the_button_pers_account(self, driver):
        driver.find_element(By.XPATH, '//a[@href="/account"]').click()
        mess = driver.find_element(By.XPATH, '//div[@class="Auth_login__3hAey"]/h2').text
        assert mess == 'Вход'
        if mess == 'Вход':
            print("Тест пройден.Клик по кнопке Личный кабинет РАБОТАЕТ")
        else:
            print("Тест не пройден")

    def test_transfer_to_the_pers_account(self, login):
        driver=login
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/account"]'))).click()
        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.LINK_TEXT, "Профиль"))).text
        assert mess=="Профиль"
        if mess == 'Профиль':
            print("Тест пройден. Мы в своем Личном кабинете, на странице Профиль")
        else:
            print("Тест не пройден")