import random as r

class CommonData:
    main_url = 'https://stellarburgers.nomoreparties.site/'
    test_user_email = 'ksenia_zavalishina_7_123@ya.ru'
    test_user_password = '123456'
    invalid_password = '12345'


    @staticmethod
    def reg_data():
        name_seq = ['Кс', 'Ен', 'Ия', 'Зава', 'Лиши', 'На']
        name = f'{r.choice(name_seq)}'
        login = f'vredinazanuda{r.randint(100, 1000)}@ya.ru'
        pass_seq = ['dog', 'kitten', 'parrot', 'meow', 'toxic', 'hamster']
        password = f'{r.choice(pass_seq)}{r.randint(100, 1000)}'
        return {'name': name, 'login': login, 'password': password}


