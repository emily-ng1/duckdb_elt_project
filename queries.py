# transformation queries

# staging
stg_maybelline='''
    create table stg_maybelline as
    select
        id as makeup_id,
        brand,
        name as makeup_name,
        price,
        currency,
        rating,
        product_type,
        created_at
    from maybelline
    '''

stg_dior='''
    create table stg_dior as
    select
        id as makeup_id,
        brand,
        name as makeup_name,
        price,
        currency,
        rating,
        product_type,
        created_at
    from dior
    '''

stg_fenty='''
    create table stg_fenty as
    select
        id as makeup_id,
        brand,
        name as makeup_name,
        price,
        currency,
        rating,
        product_type,
        created_at
    from fenty
    '''

stg_clinique='''
    create table stg_clinique as
    select
        id as makeup_id,
        brand,
        name as makeup_name,
        price,
        currency,
        rating,
        product_type,
        created_at
    from clinique
    '''

# intermediate
int_makeup_from_all_brands='''
    create table int_makeup as
    select *
    from stg_maybelline

    union all

    select *
    from stg_dior

    union all

    select *
    from stg_fenty

    union all

    select *
    from stg_clinique
    '''

# mart
mart_makeup_from_all_brands='''
    create table makeup as
    select
        makeup_id,
        brand,
        makeup_name,
        price,
        currency,
        rating,
        product_type,
        created_at
    from int_makeup
'''