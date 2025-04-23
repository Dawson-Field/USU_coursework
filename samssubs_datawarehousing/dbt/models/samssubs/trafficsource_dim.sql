{{ config(
    materialized = 'table',
    schema = 'dw_samssubs'
) }}

select
    {{ dbt_utils.generate_surrogate_key(['traffic_source']) }} as traffic_source_key,
    traffic_source
from {{ source('samssubs_web', 'web_traffic_events') }}
group by traffic_source
