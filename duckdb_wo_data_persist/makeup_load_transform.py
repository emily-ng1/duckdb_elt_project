# duckdb is a columnar database (stores data by columns)
    # pros: 
        # speed: it uses a "vectorized execution engine" that process batches of data at once. Which makes it faster than row based db for big data analysis
        # hybrid storage: 
            # duckdb can run entirely in-memory using :memory:
            # but also fully supports persistent disk storage (saves your entire database—tables, indexes, and views—into a single compressed file on your disk) 
        # in process: runs inside your application (python script or CLI tool) rather than separate server. Eliminates the overhead of sending data over a network
            # i.e. separate server: Snowflake is a cloud based data warehouse - when you write python script you must request it over the network (internet) to the Snowflake server
        # Large file or analysis moves from in-memory(RAMS) -> disk
            # i.e. running a query for a large dataset is larger than what's on your computer's RAM it wouldn't error out but instead it writes the extra data to disk into temp files
            # but note RAM is thousand times faster than disk so this will make query slower bc system has to wait for much slower disk read/write speed

import duckdb
import re
from pathlib import Path


def create_brand_table(csv_file):
    brand_name=csv_file.split('.')[0]
    brand_name=re.sub(r"[^a-z0-9]+", "_", brand_name)
    
    create_table_query=f'''
    create table {brand_name} (
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
    duckdb.sql(create_table_query)

    copy_and_load_csv__into_table_query=f"copy {brand_name} from 'brands/{csv_file}'"
    duckdb.sql(copy_and_load_csv__into_table_query)

    show_data_query=f"select * from {brand_name} limit 10"
    duckdb.sql(show_data_query).show()
