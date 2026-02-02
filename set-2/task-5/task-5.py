import pandas as pd
from tabulate import tabulate

def print_excel_as_table(file_path, sheet_name=0):
    # Read Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Print in tabular format
    print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))

if __name__ == "__main__":
    excel_file = "example.xlsx"  # Path to your Excel file
    print_excel_as_table(excel_file)
