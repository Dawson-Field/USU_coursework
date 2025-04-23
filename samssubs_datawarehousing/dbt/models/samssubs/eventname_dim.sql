{{ config(
    materialized = 'table',
    schema = 'dw_samssubs'
) }}

select
    {{ dbt_utils.generate_surrogate_key(['event_name']) }} as eventnamekey,
    event_name
from {{ source('samssubs_web', 'web_traffic_events') }}
group by event_name
