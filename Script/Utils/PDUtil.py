import pandas as pd


# ReusableAsset_COE00079
def find_header_with_keyword(excel_path, keyword):
    with pd.ExcelFile(excel_path) as xls:
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet_name, header=None)

            for idx, row in df.iterrows():
                if keyword in row.values:
                    return idx
    return None


def print_full_df(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)
