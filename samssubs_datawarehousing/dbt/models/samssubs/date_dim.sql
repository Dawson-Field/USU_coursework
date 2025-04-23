{{ config(
    materialized = 'table',
    schema = 'dw_samssubs'
) }}

with cte_date as (
    {{ dbt_date.get_date_dimension("2015-01-01", "2035-12-31") }}
)

select
    date_day as datekey,
    date_day,
    year_number,
    month_of_year,
    day_of_month
from cte_date
