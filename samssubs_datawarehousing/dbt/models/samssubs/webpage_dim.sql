{{ config(
    materialized = 'table',
    schema = 'dw_samssubs'
) }}

select
    {{ dbt_utils.generate_surrogate_key(['page_url']) }} as webpagekey,
    page_url
from {{ source('samssubs_web', 'web_traffic_events') }}
group by page_url
