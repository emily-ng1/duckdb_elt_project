import duckdb
import re
from pathlib import Path

con = duckdb.connect("makeup.duckdb") # create a connection to the duckdb database so the data/ table can persist after running the script


def create_brand_table(csv_file):
    brand_name=csv_file.split('.')[0]
    brand_name=re.sub(r"[^a-z0-9]+", "_", brand_name)
    
    create_table_query=f'''
    create or replace table {brand_name} (
        id VARCHAR, 
        brand VARCHAR, 
        name VARCHAR, 
        price FLOAT, 
        price_sign VARCHAR, 
        currency VARCHAR, 
        image_link VARCHAR, 
        product_link VARCHAR, 
        website_link VARCHAR, 
        description VARCHAR, 
        rating FLOAT, 
        category VARCHAR, 
        product_type VARCHAR, 
        tag_list VARCHAR[], 
        created_at TIMESTAMP, 
        updated_at TIMESTAMP, 
        product_api_url VARCHAR, 
        api_featured_image VARCHAR, 
        product_colors STRUCT(
            hex_value VARCHAR,
            colour_name VARCHAR
        )[]
    );
    '''
    con.sql(create_table_query)

    # use copy from to load csv files to duckdb (also works with parquet and json as well)
    copy_and_load_csv__into_table_query=f"copy {brand_name} from 'brands/{csv_file}'"
    con.sql(copy_and_load_csv__into_table_query)
