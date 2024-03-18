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
* #### Регистрация (http://127.0.0.1:8000/DerzkhyaApi/auth-signup/)
    * ##### Передать все нужные параметры
* #### Авторизация (http://127.0.0.1:8000/DerzkhyaApi/auth-login/):
    * ##### Передать все нужные параметры
* #### Получение списка билетов (http://127.0.0.1:8000/DerzkhyaApi/tikets/?token=user_token):
    ```json
    {
        "token": "user_token",
    }
    ```
* #### Создание билета (http://127.0.0.1:8000/DerzkhyaApi/tikets/?token=user_token):
    ```json
    {
        "token": "user_token",
    }
    ```
    > Далее идут все поля для билета, для создания билета
* #### Запросы для отдельных билетов:
    * #### GET(http://127.0.0.1:8000/DerzkhyaApi/tiket/?token=user_token):
        ```json
        {
            "token": "user_token",
            "id": "tiket_id"
        }
        ```
    * #### PUT(http://127.0.0.1:8000/DerzkhyaApi/tiket/?token=user_token):
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
    * #### DELETE(http://127.0.0.1:8000/DerzkhyaApi/tiket/?token=user_token):
        ```json
        {
            "token": "user_token",
            "id": "tiket_id"
        }
        ```




