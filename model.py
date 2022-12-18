def add_data(data_file):
    data_string = ";".join(data_file)+'\n'
    with open('DB.csv', 'a+') as file:
        if file.write(data_string):
            return 'Данные успешно записаны!'
        else:
            return 'Файл не записан'

def find_data(in_data):
    with open('DB.csv', 'r') as file:
        data_file = file.read()
    data_file = data_file.split()
    res = []
    for i in data_file:
        if in_data in i:
            res.append(i)
    return res

def del_data(in_data):
    data = find_data(in_data)
    data_del = [data[0]]
    data_del = str(data_del[0])
    with open('DB.csv', 'r') as file:
        data_file = file.read()
        data_file = data_file.split()
        data_file.remove(data_del)
        data_string = "\n".join(data_file)+'\n'
    with open('DB.csv', 'w') as file:
       file.write(data_string)
    return 'Данные удалены'


