__version__ = "0.0.1"

from typing import Dict

from openpyxl import load_workbook, Workbook


def excel_to_dictionary(file_name: str, sheet_name: str = "Sheet1", title_row: int = 1) -> Dict:
    workbook: Workbook = load_workbook(file_name)

    dictionary = {column[title_row]: column[title_row + 1] for column in
                  [list(i) for i in zip(*workbook[sheet_name].values)]}

    return dictionary
