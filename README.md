## DerzkhyaApi Initial Version
> Команды для запуска в файле setup_commands.txt
___

### Поддерживаемые функции:
* #### Регистрация пользователя:
    * Email(Login)
    * Password
    * Role (default='Пользователь')
    * Full_name

* #### Авторизация:
    * Login
    * Password
    > После авторизации возвращается Token

* #### Получение списка билетов

* #### Работа с отдельными билетами по id:
    * GET
    * POST
    * PUT
    * DELETE
_______

### Для работы с запросами:
* #### Регистрация (https://derzkhyaapi.pythonanywhere.com/DerzkhyaApi/auth-signup/)
    * ##### Передать все нужные параметры
* #### Авторизация (https://derzkhyaapi.pythonanywhere.com/DerzkhyaApi/auth-login/):
    * ##### Передать все нужные параметры
* #### Получение списка билетов (https://derzkhyaapi.pythonanywhere.com/DerzkhyaApi/tikets/?token=user_token):
    ```json
    {
        "token": "user_token",
    }
    ```
* #### Создание билета (https://derzkhyaapi.pythonanywhere.com/DerzkhyaApi/tikets/?token=user_token):
    ```json
    {
        "token": "user_token",
    }
    ```
    > Далее идут все поля для билета, для создания билета
* #### Запросы для отдельных билетов:
    * #### GET(https://derzkhyaapi.pythonanywhere.com/DerzkhyaApi/tiket/?token=user_token):
        ```json
        {
            "token": "user_token",
            "id": "tiket_id"
        }
        ```
    * #### PUT(https://derzkhyaapi.pythonanywhere.com/DerzkhyaApi/tiket/?token=user_token):
        ```json
        {
            "token": "user_token",
            "id": "tiket_id"
        }
        ```
        > Дальше вы в таком же формате вводите название поля, которое хотите изменить и его значение
        ```json
        {
            "token": "user_token",
            "id": "tiket_id",
            "price": 2500
        }
        ```
    * #### DELETE(https://derzkhyaapi.pythonanywhere.com/DerzkhyaApi/tiket/?token=user_token):
        ```json
        {
            "token": "user_token",
            "id": "tiket_id"
        }
        ```




