from utils.utils_for_file import data_file
from utils.nominatimApi import NominatimApi
import pytest
import allure
from utils.allure_logging import info_log


class TestGeocoding:
    @allure.severity("high")
    @allure.title("Тест прямого кодирования: адрес => координаты")
    @pytest.mark.api
    @pytest.mark.high
    @pytest.mark.usefixtures("new_fixture")
    @pytest.mark.parametrize("test_data", data_file(file_path="utils/data_for_searching_by_name.json"))
    def test_check_from_name(self, test_data, file_path="utils/data_for_searching_by_name.json"):
        result = NominatimApi().search(query=test_data['input_data'])[0]

        with allure.step("Сравнить ширину"):
            assert test_data['latitude'] == result['lat']
            info_log.info(f"{test_data['latitude']} - {result['lat']} Ширина совпадает!")
            allure.attach.file(file_path, attachment_type=allure.attachment_type.JSON)  # просто добавила json
        with allure.step("Сравнить долготу"):
            assert test_data['longitude'] == result['lon']
            info_log.info(f"{test_data['longitude']} - {result['lon']} Долгота совпадает!")

    @allure.severity("high")
    @allure.title("Тест обратного кодирования: координаты => адрес")
    @pytest.mark.api
    @pytest.mark.high
    @pytest.mark.usefixtures("new_fixture")
    @pytest.mark.parametrize("test_data_coordinates",
                             data_file(file_path="utils/data_for_searching_by_coordinates.json"))
    def test_check_from_coordinates(self, test_data_coordinates,
                                    file_path="utils/data_for_searching_by_coordinates.json"):
        result = NominatimApi().reverse(query1=test_data_coordinates['latitude'],
                                        query2=test_data_coordinates['longitude'])

        with allure.step("Сравнить полученный адрес"):
            assert test_data_coordinates['address'] == result['display_name']
            allure.attach.file(file_path, attachment_type=allure.attachment_type.JSON)
            info_log.info(f"{result['display_name']}\n{result['display_name']}\nАдрес совпадает!")
