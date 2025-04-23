{{ config(
    materialized = 'table',
    schema = 'dw_samssubs'
) }}

select
    {{ dbt_utils.generate_surrogate_key(['ordermethod']) }} as methodkey,
    ordermethod
from {{ source('samssubs_landing', '"ORDER"') }}
GROUP BY ordermethod
