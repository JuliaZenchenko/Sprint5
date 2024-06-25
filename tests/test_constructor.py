from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConctructor:
    def test_constructor_souse(self, login):
        driver = login
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Соусы']"))).click()

        element=driver.find_element(By.XPATH, "//h2[text()='Соусы']")
        driver.execute_script("arguments[0].scrollIntoView();", element)

        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//h2[text()="Соусы"]'))).text
        assert mess == 'Соусы'
        if mess == 'Соусы':
            print("Тест пройден.Мы нашли Соусы!")
        else:
            print("Тест не пройден")

    def test_constructor_pan(self, login):
        driver = login
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Соусы']"))).click()

        element = driver.find_element(By.XPATH, "//h2[text()='Булки']")
        driver.execute_script("arguments[0].scrollIntoView();", element)

        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//h2[text()="Булки"]'))).text
        assert mess == 'Булки'
        if mess == 'Булки':
            print("Тест пройден.Мы нашли Булки!")
        else:
            print("Тест не пройден")

    def test_constructor_add(self, login):
        driver = login
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Начинки']"))).click()

        element=driver.find_element(By.XPATH, "//h2[text()='Начинки']")
        driver.execute_script("arguments[0].scrollIntoView();", element)

        mess = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//h2[text()="Начинки"]'))).text
        assert mess == 'Начинки'
        if mess == 'Начинки':
            print("Тест пройден.Мы нашли Начинки!")
        else:
            print("Тест не пройден")