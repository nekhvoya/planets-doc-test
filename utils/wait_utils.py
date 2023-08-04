import datetime
from RPA.core.windows.locators import ElementNotFound


def wait_element(condition, timeout=60):
    current_time = datetime.datetime.now()
    result = None
    while not result and datetime.datetime.now() < current_time + datetime.timedelta(0, timeout):
        try:
            result = condition()
        except ElementNotFound:
            pass
    return result
