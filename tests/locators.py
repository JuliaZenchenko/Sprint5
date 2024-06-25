from selenium.webdriver.common.by import By


class Locators:
    EMAIL = (By.XPATH, '//fieldset[1]/div[1]/div[1]/input[1]') # Кнопка Email
    PASSWORD = (By.XPATH, '//fieldset[2]/div[1]/div[1]/input[1]') #Кнопка пароль
    BUTTON = (By.XPATH, '//form/button') #Кнопка Войти
    PAGE=(By.XPATH, '//a[@href="/account"]') #Страница с надписью Вход
