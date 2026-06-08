import duckdb
from pathlib import Path
from makeup_extract import get_makeup_from_api, convert_json_to_df, df_to_csv
from makeup_load_transform import create_brand_table, con
from queries import stg_maybelline, stg_dior, stg_fenty, stg_clinique, int_makeup_from_all_brands, mart_makeup_from_all_brands


def main():
    brands=["maybelline", "dior", "fenty", "clinique"]
    # 1. Extract
    for brand in brands:
        #get the makeup brand data from the api
        brand_result=get_makeup_from_api(brand)

        #convert the json to pd df (so the enables us to save it as a csv file)
        brand_df=convert_json_to_df(brand_result)

        #save out the csv files into the brands folder
        df_to_csv(brand_df, brand)


    files=[brand.name for brand in Path('brands/').iterdir() if brand.is_file()]
    #['maybelline.csv', "burt's bees.csv", 'dior.csv', 'fenty.csv', 'clinique.csv']

    # 2. Load data - Create tables for each csv brand file in duckdb
    # table: clinique, dior, fenty, maybelline 
    for csv_file in files:
        create_brand_table(csv_file)

    # 3. Transform data - Combine each of the tables together
    # create staging models for all makeup brand
    con.sql(stg_maybelline)
    con.sql(stg_dior)
    con.sql(stg_fenty)
    con.sql(stg_clinique)

    # create int model to combine all stg models
    con.sql(int_makeup_from_all_brands)

    # create mart model
    con.sql(mart_makeup_from_all_brands)

    # note: run "duckdb makeup.duckdb" to interact with database


if __name__ == "__main__":
    main()