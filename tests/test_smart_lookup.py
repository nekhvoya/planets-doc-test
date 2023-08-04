from conftest import window
import pytest

from elements.sheet_control import SheetControl
from elements.data_grid import DataGrid
from elements.ribbon import Ribbon
from elements.search_window import SearchWindow


@pytest.mark.parametrize("work_book", ["Assignment_AQA_2023.xlsx"])
def test_smart_lootkup(window):
    sheet_control = SheetControl(window)
    sheet_control.open_sheet("planets")

    data_grid = DataGrid(window)
    data_grid.select_cell("A9")

    ribbon_tabs = Ribbon(window)
    ribbon_tabs.open_tab("Review")
    ribbon_tabs.lower_ribbon().click_button("Smart Lookup")

    search_window = SearchWindow(window)
    first_result = search_window.smart_lookup_results().get_first_result()
    assert first_result == "Naboo - Wikipedia Article"
