def export_data(data):
    data_string = ";".join(data)+'\n'
    with open('DB.csv', 'a+') as file:
        if file.write(data_string):
            return 'Данные успешнозаписаны!'
        else:
            return 'Файл не записан'