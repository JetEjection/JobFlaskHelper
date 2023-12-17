import re
import gspread
from gspread.utils import ValueInputOption
from config.config import DECODED_KEYS, SHEET_NAME, SHEET_TITLE


def spreadsheet_fill(data: list):
    """
    Fills gsheet empty row with index and user specified data
    :param data: list of additional data to fill gsheets with except
    :return: None
    """
    gc = gspread.service_account_from_dict(DECODED_KEYS)

    worksheet = gc.open(SHEET_NAME).worksheet(title=SHEET_TITLE)

    # find values of cells between specified rows
    admission = re.compile("Поступлени")
    dispatch = re.compile("Перевод")
    start_cell = worksheet.find(admission)
    start_row = start_cell.row
    end_cell = worksheet.find(dispatch)
    end_row = end_cell.row
    lst = worksheet.get_values(f"B{start_row}:B{end_row}")

    # empty rows have two possible values: '' or ' ', so try to identify index of empty row
    try:
        row_delta = lst.index([''])
    except ValueError:
        row_delta = lst.index([' '])
    empty_row = start_row + row_delta

    # [row_delta] to keep patient indexing
    values = [row_delta] + data

    worksheet.update(
        values=[values],
        range_name=f"A{empty_row}:K{empty_row}",
        value_input_option=ValueInputOption.user_entered

    )


if __name__ == '__main__':
    spreadsheet_fill(["a", "b", "c"])
