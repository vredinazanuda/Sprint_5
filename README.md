## Тема "UI тестирование" курс ЯндексПрактикум | Sprint_5

Для тестирования был выбран сервис [Stellar Burgers](https://stellarburgers.nomoreparties.site/) 

>Космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.
Папка tests содержит файлы с тестами, проверяющими функциональность сервиса 


### Список тестовых файлов и описание проверок:

#### [Регистрация](tests/test_registration.py)
  - успешная регистрация - test_registration_valid_data_successful_registration,
  - ошибка для некорректного пароля - test_registration_invalid_password_error_received.

#### [Вход](tests/test_sign_in.py)
  - вход по кнопке «Войти в аккаунт» на главной - test_authorization_via_sign_in_account_button,
  - вход через кнопку «Личный кабинет» - test_authorization_via_account_button,
  - вход через кнопку в форме регистрации - test_authorization_via_sign_in_register_button,
  - вход через кнопку в форме восстановления пароля - test_authorization_via_sign_in_forgot_password_button.

#### [Переход в «Личный кабинет»](tests/test_access_profile.py)
  - с главной страницы - test_access_to_profile_from_main,
  - из ленты заказов - test_access_to_profile_from_feed.

#### [Переход из Личного кабинета в Конструктор](tests/test_from_profile_to_constructor.py)
  - по клику на кнопку «Конструктор» - test_click_from_profile_on_constructor,
  - по клику на логотип Stellar Burgers - test_click_from_profile_on_logo_burgers.

#### [Выход](tests/test_exit_from_account.py)
   - выход при клике по кнопке «Выйти» в личном кабинете - test_exit_from_account.

#### [Раздел «Конструктор»](tests/test_constructor_sections.py)
  - на закладку «Булки» - test_constructor_section_buns,
  - на закладку «Соусы» - test_constructor_section_sauces,
  - на закладку «Начинки» - test_constructor_section_fillings.


### [Фикстуры](tests/conftest.py)
  -  driver - инициализирует драйвер браузера, используется во всех без исключения тестах,
  -  sign_in - для входа под тестовым юзером во всех тестах, где нужна авторизация (кроме тестов регистрации, тестов входа и тестов разделов конструктора).


### [Локаторы](tests/locators.py)
Локаторы разделены на классы, соответствующие страницам.

### [Тестовые данные](tests/data.py)

- данные тестового пользователя, зарегистрированного в системе, для тестов, где нужна авторизация,
- статический метод reg_data - для генерации имени, логина и пароля 

### Для установки зависимости  
```shell
pip3 install -r requirements.txt
```

### Запустить тесты 
```shell
pytest -v
```
