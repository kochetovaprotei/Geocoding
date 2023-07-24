import allure
import pytest
import logging
import datetime

logging.basicConfig(filename="allure_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log",
                    format='%(asctime)s - [%(name)s] - [%(levelname)4s] - %(message)s - (%(filename)s:%(lineno)s)',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

logging.info(f"This is info message")
http_log = logging.getLogger("HTTP")

