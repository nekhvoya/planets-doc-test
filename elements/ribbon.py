from elements.lower_ribbon import LowerRibbon


#     Locators
def tab(tab_name):
    return f"type:TabItem and name:{tab_name}"


class Ribbon:
    def __init__(self, window):
        self.window = window

    def lower_ribbon(self):
        return LowerRibbon(self.window, "name:\"Lower Ribbon\"")

    def open_tab(self, tab_name):
        self.window.click(tab(tab_name))
