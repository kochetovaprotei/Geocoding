import json

"""Открыть файл на чтение и забрать данные из него"""


def data_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        temp_data = json.load(f)
        data = []
        for i in temp_data:
            data.append(temp_data[i])
    return data
