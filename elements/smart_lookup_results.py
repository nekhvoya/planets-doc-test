from utils.wait_utils import wait_element


#     Locators
def first_result(parent_locator):
    return f"{parent_locator} > id:FirstSelectedItemAfterSearchBox > type:Group > type:Text"


class SmartLookupResults:
    def __init__(self, window, locator):
        self.window = window
        self.locator = locator

    def get_first_result(self):
        return wait_element(lambda: self.window.get_attribute(first_result(self.locator), "Name"))
