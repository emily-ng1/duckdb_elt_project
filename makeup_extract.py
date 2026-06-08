import requests
import pandas as pd


def get_makeup_from_api(brand):
    url="http://makeup-api.herokuapp.com/api/v1/products.json"

    params = {
        "brand": brand
    }
    response = requests.get(url, params=params)
    results = response.json()
    return results

def convert_json_to_df(json_data):
    df=pd.DataFrame(json_data)
    df_sorted=df.sort_values(by='id')
    return df_sorted

def df_to_csv(df_file, brand):
    df_file.to_csv(f"./brands/{brand}.csv", index=False, header=True)


