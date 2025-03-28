import pandas as pd
from pathlib import Path

def read_file():
    data_path = Path(__file__).parents[1]/"Data"
    return pd.read_csv(data_path/"supahcoolsoft.csv")

if __name__ == "__main__":
    df = read_file()
    print(df.columns)