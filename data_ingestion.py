import pandas as pd
import os

folder_path = "data/raw"

csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

for file in csv_files:
    print("\n" + "="*60)
    print("Dataset:", file)

    file_path = os.path.join(folder_path, file)

    df = pd.read_csv(file_path)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())