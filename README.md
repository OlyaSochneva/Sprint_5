### QA Sprint 5

### Автотесты для Stellar Burgers 
Адрес: https://stellarburgers.nomoreparties.site/

#### Локаторы (Locators.py)

#### Фикстуры (conftest.py):

**driver** - инициализирует драйвер с опциями:

- разрешение 1920х1080
- отключены уведомления

**existing_user** - возвращает почту и пароль зарегистрированного пользователя

**new_correct_user** - возвращает сгенерированные имя, почту и пароль для нового пользователя

**new_user_with_wrong_password** - возвращает сгенерированные имя и почту, и неверный (короткий) пароль для нового пользователя

**go_to_login_page(driver)** - переходит на страницу авторизации

**go_to_register_page(driver)** - переходит на страницу регистрации

**go_to_personal_page(driver, existing_user)** 
- авторизуется на сайте с данными existing_user 
- заходит в л/к 

#### Вспомогательные классы (assistant_classes.py):
**User** (self, email, password) - для существующего пользователя

**NewUser** (self, name, email, password) - для нового пользователя

**Generator** - для нового пользователя, содержит 3 стат. метода:

- password_generator - возвращает пароль
- login_generator - возвращает почту формата XXXXX_test@ya.ru
- name_generator - возвращает имя

### Реализованные тесты

#### Регистрация:

#### Тест 1: test_registration_correct_user
Проверка: успешная регистрация (корректные данные)

Тест. класс: TestRegistration

Исп. фикстуры: driver, go_to_register_page, new_correct_user

*где находится: tests/test_registration.py*
#### Тест 2: test_registration_user_wrong_password
Проверка: ошибка регистрации (некорректный пароль)

Тест. класс: TestRegistration

Исп. фикстуры: driver, go_to_register_page, new_user_with_wrong_password

*где находится: tests/test_registration.py*

#### Вход в аккаунт:
#### Тест 3: test_login_by_main_page_login_button
Проверка: вход в аккаунт по кнопке «Войти в аккаунт» на главной

Тест. класс: TestLogin

Исп. фикстуры: driver, go_to_login_page, existing_user

*где находится: tests/test_login.py*
#### Тест 4: test_login_by_personal_account_button
Проверка: вход в аккаунт через кнопку «Личный кабинет»

Тест. класс: TestLogin

Исп. фикстуры: driver, existing_user

*где находится: tests/test_login.py*
#### Тест 5: test_login_by_register_page_login_button
Проверка: вход в аккаунт через кнопку в форме регистрации

Тест. класс: TestLogin

Исп. фикстуры: driver, go_to_register_page, existing_user

*где находится: tests/test_login.py*
#### Тест 6: test_login_by_reset_password_page_login_button
Проверка: вход в аккаунт через кнопку в форме восстановления пароля

Тест. класс: TestLogin

Исп. фикстуры: driver, go_to_login_page, existing_user

*где находится: tests/test_login.py*

#### Личный кабинет:
#### Тест 7: test_move_to_personal_account_by_click_on_button

Проверка: переход в л/к по клику на кнопку «Личный кабинет»

Тест. класс: TestPersonalAccount

Исп. фикстуры: driver, go_to_personal_page 

*где находится: tests/test_personal_account.py* 
#### Тест 8: test_move_from_personal_account_to_constructor
Проверка: переход из л/к по клику на «Конструктор»

Тест. класс: TestPersonalAccount

Исп. фикстуры: driver, go_to_personal_page

*где находится: tests/test_personal_account.py*
#### Тест 9: test_move_from_personal_account_to_main_page_by_logo
Проверка: переход из л/к по клику на лого «Stellar Burgers» 

Тест. класс: TestPersonalAccount

Исп. фикстуры: driver, go_to_personal_page

*где находится: tests/test_personal_account.py*
#### Тест 10: test_exit_personal_account_by_logout_button
Проверка: выход из аккаунта по клику на кнопку «Выход»

Тест. класс: TestPersonalAccount

Исп. фикстуры: driver, go_to_personal_page

*где находится: tests/test_personal_account.py*

#### Конструктор:
#### Тест 11: test_move_to_buns_section
Проверка: «Конструктор», переход к разделу «Булки»

Тест. класс: TestConstructor

Исп. фикстуры: driver

*где находится: tests/test_constructor.py*
#### Тест 12: test_move_to_sauces_section
Проверка: «Конструктор», переход к разделу «Соусы»

Тест. класс: TestConstructor

Исп. фикстуры: driver

*где находится: tests/test_constructor.py*
#### Тест 13: test_move_to_fillings_section
Проверка: «Конструктор», переход к разделу «Начинки»

Тест. класс: TestConstructor

Исп. фикстуры: driver

*где находится: tests/test_constructor.py*

