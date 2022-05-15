from pathlib import Path

import pandas


def parse():
    form_path = str(next(
        Path(__file__).parent.parent.parent.glob('Test Form.xlsx')))
    form_df = pandas.read_excel(io=form_path, sheet_name='Form1')
    print(form_df.columns)


if __name__ == '__main__':
    parse()
