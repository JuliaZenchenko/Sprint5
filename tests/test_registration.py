from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from locators import Locators

faker = Faker()
class TestRegistration:
    def test_registration(self, driver):
        name = faker.name()
        email = faker.email()
        password = faker.password(length=6)

        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.BUTTON_REGISTRATION_ON_PAGE_ENTER).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL_FOR_REGISTRATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGISTRATION_ON_PAGE_REGISTRATION).click()

        WebDriverWait(driver, 3).until(EC.url_matches("https://stellarburgers.nomoreparties.site/login"))
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON).click()

        mess = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TITLE_THE_BURGER)).text
        assert mess == "Соберите бургер"

    def test_valid_random_name_not_empty(self):
        name = faker.name()
        assert name, "Имя не должно быть пустым."

    def test_valid_random_email_format(self):
        email = faker.email()
        assert "@" in email and "." in email, "Email должен содержать символы '@' и '.'."

    def test_valid_random_password_length(self):
        password = faker.password(length=10)  # Генерация случайного пароля длиной 10 символов
        assert len(password) >= 6, "Пароль должен содержать минимум 6 символов."

    def test_registration_incorrect_password(self, driver):
        name = faker.name()
        email = faker.email()
        password = "123"

        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.BUTTON_REGISTRATION_ON_PAGE_ENTER).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGISTRATION_ON_PAGE_REGISTRATION).click()

        mess = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.TITLE_INCORRECT_PASSWORD)).text
        assert mess == 'Некорректный пароль'




