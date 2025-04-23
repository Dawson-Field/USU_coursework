{{ config(
    materialized = 'table',
    schema = 'dw_samssubs'
) }}

SELECT
    d.date_day,
    d.month_of_year,
    ts.traffic_source,
    wp.page_url AS webpage_url,
    en.event_name AS event_type,
    f.num_of_visits
FROM {{ ref('fact_webtraffic') }} f

LEFT JOIN {{ ref('trafficsource_dim') }} ts
    ON f.traffic_source_key = ts.traffic_source_key

LEFT JOIN {{ ref('webpage_dim') }} wp
    ON f.webpagekey = wp.webpagekey

LEFT JOIN {{ ref('eventname_dim') }} en
    ON f.eventnamekey = en.eventnamekey

LEFT JOIN {{ ref('date_dim') }} d
    ON f.datekey = d.datekey
