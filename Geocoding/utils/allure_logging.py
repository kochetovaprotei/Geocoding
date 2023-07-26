import logging
import datetime

logging.basicConfig(
    filename="allure_logs/allure_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log",
    format="%(asctime)s - [%(name)s] - [%(levelname)4s] - %(message)s - (%(filename)s:%(lineno)s)",
    datefmt="%H:%M:%S",
    level=logging.INFO)

logging.info(f"This is info message")  # для примера
info_log = logging.getLogger("INFO")
http_log = logging.getLogger("HTTP")
