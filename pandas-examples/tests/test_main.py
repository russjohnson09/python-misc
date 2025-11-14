import pyarrow.parquet as pa

# https://www.geeksforgeeks.org/data-science/read-a-parquet-file-using-pandas/#
# https://www.kaggle.com/datasets/pawankumargunjan/weather

# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("pawankumargunjan/weather")

# print("Path to dataset files:", path)

#!/bin/bash
# curl -L -o ~/Downloads/weather.zip\
#   https://www.kaggle.com/api/v1/datasets/download/pawankumargunjan/weather

def test_main():
    table = pa.read_table('weather.2016.parquet')

    print(table)

    pass