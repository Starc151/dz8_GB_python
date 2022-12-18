
from model import *

def request_action_user():
    request = int(input('Выберите действия с записью:\n\
    1. Добавить\n\
    2. Найти\n\
    3. Найти и редактировать\n\
    4. Найти и удалить\n\
    5. Выйти\n\
    '))
    return request

def print_res(msg):
    print(msg)

def add_entry():
    firstName = input('Ведите имя: ')
    lastName = input('Ведите фаилию: ')
    tel = input('Ведите телефон: ')
    data = [firstName, lastName, tel]
    return data

def search_entry():
    search = input('Введите запрос: ')
    return search
