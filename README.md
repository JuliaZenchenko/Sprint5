# Sprint_5
Автотесты для сервиса Stellar Burgers
Файл test_registration.py:
1. test_registration - Успешная регистрация
2. test_valid_name_not_empty - Проверяет, что имя не пустое.
3. test_valid_email_format- Проверяет, что email содержит символы '@' и '.'. 
4. test_valid_password_length: Проверяет, что пароль содержит минимум 6 символов. 
5. test_registration_incorrect_password - Тест регистрации с неправильным паролем

Файл test_enter.py:
1. test_enter_by_button_the_pers_account - вход через кнопку «Личный кабинет»
2. test_enter_by_the_account_button - вход по кнопке «Войти в аккаунт» на главной
3. test_enter_by_the_registration_form - вход через кнопку в форме регистрации
4. test_enter_by_recover_password - вход через кнопку в форме восстановления пароля

Файл test_click_the_personal_account.py:
1. test_click_on_the_button_pers_account - работа клика по кнопке Личный кабинет 
2. test_transfer_to_the_pers_account - переход по клику в «Личный кабинет»

Файл test_click_the_constructor_and_logo.py:
1. test_click_on_the_button_constructor - Переход из личного кабинета в конструктор через кнопку Конструктор
2. test_click_on_the_logo - Переход из личного кабинета в конструктор через логотип

Файл test_exit.py:
1. test_exit - выход по кнопке «Выйти» в личном кабинете

Файл test_constructor.py:
1. test_constructor_souse- проверка переходов в соусы
2. test_constructor_pan - проверка переходов в булки
3. test_constructor_add - проверка переходов в начинки

