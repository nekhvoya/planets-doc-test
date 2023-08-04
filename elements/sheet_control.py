#     Locators
def sheet_tab(sheet_name):
    return f"type:TabItem and name:{sheet_name}"


class SheetControl:
    def __init__(self, window):
        self.window = window

    def open_sheet(self, sheet_name):
        self.window.click(sheet_tab(sheet_name))
