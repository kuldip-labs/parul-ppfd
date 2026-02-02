import pandas as pd

def get_csv_average_pandas(file_path, column_name):
    try:
        # Load the CSV file
        df = pd.read_csv(file_path)

        # Calculate the mean of the specified column
        average = df[column_name].mean()

        return average
    except FileNotFoundError:
        return "Error: File not found."
    except KeyError:
        return f"Error: Column '{column_name}' not found."
    except Exception as e:
        return f"An error occurred: {e}"


# Usage
file = 'data.csv'
col = 'Price'
print(f"The average of {col} is: {get_csv_average_pandas(file, col)}")