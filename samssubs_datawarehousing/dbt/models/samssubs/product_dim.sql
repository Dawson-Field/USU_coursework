{{ config(
    materialized = 'table',
    schema = 'dw_samssubs'
) }}

select
    {{ dbt_utils.generate_surrogate_key(['productid']) }} as productkey,
    productid,
    productname,
    productcalories
from {{ source('samssubs_landing', 'product') }}
