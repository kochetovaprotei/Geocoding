from utils.utils_for_file import data_file
from utils.nominatimApi import NominatimApi
import pytest
import allure

"""Тест прямого кодирования"""


@allure.description("test_check_from_name")
@pytest.mark.usefixtures("new_fixture")
@pytest.mark.parametrize("test_data", data_file(file_path="utils/data_for_searching_by_name.json"))
def test_check_from_name(test_data):
    print(f"\nlatitude - {test_data['latitude']}")
    print(f"\nlongitude - {test_data['longitude']}")  # <class 'dict'>

    result = NominatimApi().search(query=test_data['input_data'])[0]  # <class 'dict'>

    assert test_data['latitude'] == result['lat'], f""
    print('Совпала ширина')
    assert test_data['longitude'] == result['lon']
    print('Совпала долгота')
    pass


"""Тест обратного кодирования"""


@allure.description("test_check_from_coordinates")
@pytest.mark.parametrize("test_data_coordinates", data_file(file_path="utils/data_for_searching_by_coordinates.json"))
def test_check_from_coordinates(test_data_coordinates):
    print(f"\naddress - {test_data_coordinates['address']}")  # <class 'dict'>

    result = NominatimApi().reverse(query1=test_data_coordinates['latitude'], query2=test_data_coordinates['longitude'])
    # <class 'dict'>

    assert test_data_coordinates['address'] == result['display_name']
    print(f"Совпал адрес: {result['display_name']}")
    pass
