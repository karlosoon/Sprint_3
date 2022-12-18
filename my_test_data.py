import random


class MyTestData:
    @staticmethod
    def generate_email():
        return 'maxim_karlo' + str(random.randint(1000, 9999)) + '@yandex.ru'

    valid_password = '123123'
    invalid_password = '123'
    test_email = 'test9999@yandex.ru'
    name = 'Maxim'
