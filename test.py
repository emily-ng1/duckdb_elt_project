import csv
import duckdb
import re
from pathlib import Path


duckdb.sql("select 2").show()
# ┌───────┐
# │   2   │
# │ int32 │
# ├───────┤
# │     2 │
# └───────┘

duckdb.sql("select * from read_csv('brands/dior.csv') limit 10").show()
# ┌───────┬─────────┬──────────────────────┬────────┬───┬──────────────────────┬──────────────────────┬──────────────────────┬──────────────────────┐
# │  id   │  brand  │         name         │ price  │ … │      updated_at      │   product_api_url    │  api_featured_image  │    product_colors    │
# │ int64 │ varchar │       varchar        │ double │   │ timestamp with tim…  │       varchar        │       varchar        │       varchar        │
# ├───────┼─────────┼──────────────────────┼────────┼───┼──────────────────────┼──────────────────────┼──────────────────────┼──────────────────────┤
# │   658 │ dior    │ Rouge Dior Liquid    │   26.5 │ … │ 2017-12-23 13:58:4…  │ http://makeup-api.…  │ //s3.amazonaws.com…  │ [{'hex_value': '#F…  │
# │   659 │ dior    │ Rouge Dior Double …  │   27.5 │ … │ 2017-12-23 13:58:4…  │ http://makeup-api.…  │ //s3.amazonaws.com…  │ [{'hex_value': '#F…  │
# │   660 │ dior    │ Rouge Dior           │   27.5 │ … │ 2017-12-23 13:58:4…  │ http://makeup-api.…  │ //s3.amazonaws.com…  │ [{'hex_value': '#E…  │
# │   661 │ dior    │ ROUGE DIOR - Fall …  │   27.5 │ … │ 2017-12-23 13:58:4…  │ http://makeup-api.…  │ //s3.amazonaws.com…  │ [{'hex_value': '#D…  │
# │   662 │ dior    │ Dior Holiday Coutu…  │   77.0 │ … │ 2017-12-23 13:58:4…  │ http://makeup-api.…  │ //s3.amazonaws.com…  │ []                   │
# │   663 │ dior    │ ROUGE DIOR COLLECT…  │   29.5 │ … │ 2017-12-23 13:58:4…  │ http://makeup-api.…  │ //s3.amazonaws.com…  │ [{'hex_value': '#B…  │
# │   664 │ dior    │ DIOR ADDICT LIP TA…  │   25.0 │ … │ 2017-12-23 13:58:4…  │ http://makeup-api.…  │ //s3.amazonaws.com…  │ [{'hex_value': '#A…  │
# │   665 │ dior    │ DIOR ADDICT LACQUE…  │   27.5 │ … │ 2017-12-23 13:58:4…  │ http://makeup-api.…  │ //s3.amazonaws.com…  │ [{'hex_value': '#F…  │
# │   666 │ dior    │ Dior Addict Lipstick │   27.5 │ … │ 2017-12-23 13:58:4…  │ http://makeup-api.…  │ //s3.amazonaws.com…  │ [{'hex_value': '#E…  │
# │   667 │ dior    │ Dior Addict Lipsti…  │   27.5 │ … │ 2017-12-23 13:58:4…  │ http://makeup-api.…  │ //s3.amazonaws.com…  │ [{'hex_value': '#D…  │
# ├───────┴─────────┴──────────────────────┴────────┴───┴──────────────────────┴──────────────────────┴──────────────────────┴──────────────────────┤
# │ 10 rows                                                                                                                    19 columns (8 shown) │
# └─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

with open('brands/maybelline.csv', mode='r') as file:
    reader = csv.DictReader(file)
    fields = reader.fieldnames  # Returns a list of column names
    print(fields)
# ['id', 'brand', 'name', 'price', 'price_sign', 'currency', 'image_link', 'product_link', 'website_link', 'description', 'rating', 
# 'category', 'product_type', 'tag_list', 'created_at', 'updated_at', 'product_api_url', 'api_featured_image', 'product_colors']
