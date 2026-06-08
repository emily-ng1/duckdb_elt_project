# Makeup brands | ELT Pipeline | Data Engineering Project

## Introduction
This project demonstrates an end-to-end ELT (Extract, Load, Transform) pipeline using the Makeup API and DuckDB.

The pipeline begins by extracting product data from the Makeup API in JSON format. The raw data is then converted into a DataFrame and persisted as CSV files, creating a reproducible raw data layer and separating data ingestion from transformation logic.

DuckDB is used as the analytical engine for data processing and transformation. Its columnar storage architecture is optimized for analytical workloads, allowing queries to read only the columns required rather than entire rows. This can significantly improve query and transformation performance when working with large datasets.

After loading the raw CSV data into DuckDB, the data is transformed through a layered architecture consisting of staging, intermediate, and mart models. This approach promotes modularity, maintainability, and the creation of analytics-ready datasets for downstream reporting and analysis.

This project highlights how DuckDB can be used to build lightweight yet powerful ELT pipelines for local analytical workloads. For datasets that fit on a single machine, DuckDB can provide excellent performance while avoiding the infrastructure complexity and operational overhead associated with distributed processing frameworks such as PySpark.

## Architecture
TBA

## Pipeline Flow
API → JSON → DataFrame → CSV (Raw Layer) → DuckDB → Staging → Intermediate → Marts

## Technology Used
- Programming Language - Python, SQL
- Data Source - Makeup API
- File Format - CSV
- Storage/ Query Engine - DuckDB

## Dataset Used
https://makeup-api.herokuapp.com/

## Additional notes on duckdb
- duckdb is a columnar database (stores data by columns)
- pros: 
    - speed: it uses a "vectorized execution engine" that process batches of data at once. Which makes it faster than row based db for big data analysis
    - hybrid storage: 
        - duckdb can run entirely in-memory using :memory:
        - but also fully supports persistent disk storage (saves your entire database—tables, indexes, and views—into a single compressed file on your disk) 
    - in process: runs inside your application (python script or CLI tool) rather than separate server. Eliminates the overhead of sending data over a network
        - i.e. separate server: Snowflake is a cloud based data warehouse - when you write python script you must request it over the network (internet) to the Snowflake server
    - Large file or analysis moves from in-memory(RAMS) -> disk
        - i.e. running a query for a large dataset is larger than what's on your computer's RAM it wouldn't error out but instead it writes the extra data to disk into temp files
        - but note RAM is thousand times faster than disk so this will make query slower bc system has to wait for much slower disk read/write speed