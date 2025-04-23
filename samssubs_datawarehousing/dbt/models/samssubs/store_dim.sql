{{ config(
    materialized = 'table',
    schema = 'dw_samssubs'
) }}

select
    {{ dbt_utils.generate_surrogate_key(['storeid']) }} as storekey,
    storeid,
    address,
    city,
    state,
    zip
from {{ source('samssubs_landing', 'store') }}
