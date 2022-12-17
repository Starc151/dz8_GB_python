
from model import export_data

def request_action_user():
    request = int(input('Выберите действия с записью:\n\
    1. Добавить\n\
    2. Найти\n\
    3. Найти и удалить\n\
    4. Найти и редактировать\n\
    5. Выйти\n\
    '))
    return request

def print_log(msg):
    print(msg)

def add_entry():
    firstName = input('Ведите имя: ')
    lastName = input('Ведите фаилию: ')
    tel = input('Ведите телефон: ')
    data = [firstName, lastName, tel]
    return data

def search_entry():
    search = input('Введите запрос: ')
    with open('DB.csv', 'r') as file:
        data = file.read()
    data = data.split()
    res = []
    for i in data:
        if search in i:
            res.append(i.replace(';', ' '))
    answer = 'Найдено:\n'+''.join(res[0])
    print(answer)