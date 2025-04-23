{{ config(
    materialized = 'table',
    schema = 'dw_samssubs'
) }}

select
    {{ dbt_utils.generate_surrogate_key(['employeeid']) }} as employeekey,
    employeeid,
    employeefname,
    employeelname,
    employeebday,
    storeid
from {{ source('samssubs_landing', 'employee') }}
