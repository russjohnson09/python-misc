import pyarrow.parquet as pa
import pandas as pd

# https://www.geeksforgeeks.org/data-science/read-a-parquet-file-using-pandas/#
# https://www.kaggle.com/datasets/pawankumargunjan/weather

# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("pawankumargunjan/weather")

# print("Path to dataset files:", path)

#!/bin/bash
# curl -L -o ~/Downloads/weather.zip\
#   https://www.kaggle.com/api/v1/datasets/download/pawankumargunjan/weather

def test_load_table():
    table = pa.read_table('weather.2016.parquet')

    print(table)
    df = table.to_pandas()

    print(df.head().T)

    pass

def test_load_table_and_convert_to_pandas_df():
    table = pa.read_table('weather.2016.parquet')
    df = table.to_pandas()

    print(df.head().T)

    pass

def test_read_using_pandas():

    df = pd.read_parquet('weather.2016.parquet')

    print(df)

def test_apply_filter():
    # df = pd.read_parquet('weather.2016.parquet', filters=[('Country', '=', 'ENGLAND')])

    df = pd.read_parquet('weather.2016.parquet')
    df2 = df.filter([('Country', '=', 'ENGLAND')])
    print(df2)


    grouped = df.groupby(['Country']).mean(numeric_only=True)

    print(grouped)
    print(grouped.T) # transposed group