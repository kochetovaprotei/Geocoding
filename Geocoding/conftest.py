from utils import allure_logging
import logging
import pytest


@pytest.fixture(scope="function")
def new_fixture():
    logging.info(f"This is info message 2")
