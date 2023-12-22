import pandas as pd
file_path = 'annual-enterprise-survey-2021-financial-year-provisional-csv.csv'
try:
    df = pd.read_csv(file_path)
    print("First five lines:")
    print(df.head())
    print("Last five lines:")
    print(df.tail())
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_path}' is empty.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")