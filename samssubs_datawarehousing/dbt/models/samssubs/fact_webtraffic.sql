{{ config(
    materialized='table',
    schema='dw_samssubs') }}

SELECT
    ts.traffic_source_key,
    wp.webpagekey,
    en.eventnamekey,
    d.datekey,
    COUNT(*)  AS num_of_visits
FROM {{ source('samssubs_web', 'web_traffic_events') }} w
JOIN {{ ref('trafficsource_dim') }} ts 
  ON w.traffic_source = ts.traffic_source
JOIN {{ ref('webpage_dim') }} wp 
  ON w.page_url = wp.page_url
JOIN {{ ref('eventname_dim') }} en 
  ON w.event_name = en.event_name
JOIN {{ ref('date_dim') }} d 
  ON d.date_day = DATE(w.event_timestamp)
GROUP BY
    ts.traffic_source_key,
    wp.webpagekey,
    en.eventnamekey,
    d.datekey