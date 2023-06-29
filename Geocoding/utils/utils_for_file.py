import json


class GetDataFromFile():

    """Возвращаем список словарей для прямого кодирования"""
    @staticmethod
    def data_from_first_file():
        with open('/home/kochetova/PycharmProjects/pythonProject1/Geocoding/utils/data_for_searching_by_name.json', 'r',
                  encoding='utf-8') as f:
            temp_data = json.load(f)
            data = []
            for i in temp_data:
                data.append(temp_data[i])
            # print(data)
        return data

    """Возвращаем список словарей для обратного кодирования"""
    # @staticmethod
    # def data_from_second_file():
    #     with open('/home/kochetova/PycharmProjects/pythonProject1/Geocoding/utils/'
    #               'data_for_searching_by_coordinates.json', 'r', encoding='utf-8') as f:
    #         temp_data = json.load(f)
    #         data = []
    #         for i in temp_data:
    #             data.append(temp_data[i])
    #         # print(data)
    #     return data