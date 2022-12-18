import sys
from model import *
from view import *


def get_request_user():
    request = request_action_user()
    if request == 1:
        data = add_entry()
        msg = add_data(data)
        print_res(msg)
    elif request == 2:
        data = search_entry()
        res = find_data(data)
        answer = 'Найдено:\n'+('\n'.join(res).replace(';', ' '))
        print_res(answer)
    # elif request == 3:
    #     data = search_entry()
    #     res = find_data(data)

    elif request == 4:
        data = search_entry()
        msg =  del_data(data)
        print_res(msg)
    elif request == 5:
        sys.exit()
