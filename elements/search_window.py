from elements.smart_lookup_results import SmartLookupResults


class SearchWindow:
    def __init__(self, window):
        self.window = window
        self.locator = "type:Window and name:Search > type:Custom and name:Search"

    def smart_lookup_results(self):
        return SmartLookupResults(self.window, f"{self.locator} > name:\"Find anything\" > id:SmartLookupResultContainer")

