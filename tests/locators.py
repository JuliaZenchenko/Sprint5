from selenium.webdriver.common.by import By


class Locators:
    EMAIL = (By.XPATH, '//input[@name="name"]') # Поле Email
    PASSWORD = (By.XPATH, '//input[@name="Пароль"]') #Поле пароль
    BUTTON = (By.XPATH, '//form/button') #Кнопка Войти
    PAGE = (By.XPATH, '//a[@href="/account"]') #Страница с надписью Вход
    NAME = (By.XPATH, '//label[contains(text(), "Имя")]/following-sibling::input[@type="text"]')  # Поле Имя
    EMAIL_FOR_REGISTRATION = (By.XPATH, '//label[contains(text(), "Email")]/following-sibling::input[@type="text"]')  # Поле Email на странице Регистрация
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//a[@href="/account"]') #Кнопка Личный кабинет
    BUTTON_LOGO = (By.XPATH, '//a[@href="/"]')  # Кнопка Логотип
    BUTTON_CONSTRUCTOR = ((By.XPATH, '//li[1]//p')) #Кнопка Конструктор
    BUTTON_CONSTRUCTOR_SOUSE = (By.XPATH, "//span[text()='Соусы']") #Кнопка Соусы
    BUTTON_CONSTRUCTOR_PAN = (By.XPATH, "//span[text()='Булки']") #Кнопка Булки
    BUTTON_CONSTRUCTOR_ADD = (By.XPATH, "//span[text()='Начинки']") #Кнопка Начинки
    BUTTON_ENTER_IN_ACCOUNT = (By.XPATH, '//button[text()="Войти в аккаунт"]') #Кнопка Войти в аккаунт
    BUTTON_REGISTRATION_ON_PAGE_ENTER=(By.XPATH, '//a[@href="/register"]') #Кнопка Зарегистрироваться на странице Вход
    BUTTON_ENTER_ON_PAGE_REGISTRATION = (By.XPATH, '//a[@href="/login"]') #Кнопка Войти на странице Регистрация
    BUTTON_RECOVER_PASSWORD = (By.XPATH, '//a[@href="/forgot-password"]') #Кнопка Восстановить пароль
    BUTTON_EXIT = (By.XPATH, "//li[3]/button") #Кнопка Выход
    EMAIL_FOR_RECOVER_PASSWORD = (By.TAG_NAME, 'input') # Поле Email на странице Восстановление пароля
    BUTTON_RECOVER = (By.XPATH, '//form/button[1]') #Кнопка Восстановить
    BUTTON_REGISTRATION_ON_PAGE_REGISTRATION=(By.XPATH, '//form/button') #Кнопка Регистрация
    TITLE_THE_BURGER = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]') #Заголовок бургер
    TITLE_INCORRECT_PASSWORD =(By.XPATH, "//p[text()='Некорректный пароль']") #Сообщение Некорректный пароль на странице Регистрация
    TITLE_ENTER = (By.XPATH, '//div[@class="Auth_login__3hAey"]/h2') #Заголовок Вход
    TITLE_PROFILE = (By.LINK_TEXT, "Профиль") #Заголовок Профиль
    TITLE_SOUSE = (By.XPATH, '//h2[text()="Соусы"]') #Заголовок Соусы
    TITLE_PAN = (By.XPATH, '//h2[text()="Булки"]')  # Заголовок Булки
    TITLE_ADD = (By.XPATH, '//h2[text()="Начинки"]')  # Заголовок Начинки