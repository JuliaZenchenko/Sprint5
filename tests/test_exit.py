from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestExit:
    def test_exit(self, login):
        driver = login

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/account"]'))).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, "//li[3]/button"))).click()
        WebDriverWait(driver, 3).until(EC.url_matches("https://stellarburgers.nomoreparties.site/login"))

        mess = driver.find_element(By.XPATH, '//div[@class="Auth_login__3hAey"]/h2').text
        assert mess == 'Вход'
        if mess =='Вход':
            print("Тест пройден. Выход из профиля получился")
        else:
            print("Тест не пройден.")
