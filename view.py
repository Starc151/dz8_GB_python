
from model import export_data


def request_action_user():
    request = int(input('Выберите действия с записью:\n\
    1. Добавить\n\
    2. Найти\n\
    3. Найти и удалить\n\
    4. Найти и редактировать\n\
    '))
    return request

def add_entry():
    firstName = input('Ведите имя: ')
    lastName = input('Ведите фаилию: ')
    tel = input('Ведите телефон: ')
    data = [firstName, lastName, tel]
    msg = export_data(data)
    print(msg)