from view import *


def get_request_user():
    request = request_action_user()
    if request == 1:
        data = add_entry()
        msg = export_data(data)
        print_log(msg)
    # elif request == 2:

    # elif request == 3:

    # elif request ==4
