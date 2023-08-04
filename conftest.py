from RPA.Windows import Windows
import pytest
import os

work_dir = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def window(work_book) -> Windows:
    window = Windows()
    window.windows_run(f"{work_dir}/workbooks/{work_book}")
    window.control_window("Assignment_AQA_2023 - Excel")
    window.maximize_window()
    yield window
    window.close_current_window()
