#     Locators
def button(parent_locator, button_name):
    return f"{parent_locator} > type:Button and name:\"{button_name}\""


class LowerRibbon:
    def __init__(self, window, locator):
        self.window = window
        self.locator = locator

    def click_button(self, button_name):
        self.window.click(button(self.locator, button_name))
