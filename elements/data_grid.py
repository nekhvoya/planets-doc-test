#     Locators
def cell(id):
    return f"type:DataItem and id:{id}"


class DataGrid:
    def __init__(self, window):
        self.window = window

    def select_cell(self, id):
        self.window.click(cell(id))