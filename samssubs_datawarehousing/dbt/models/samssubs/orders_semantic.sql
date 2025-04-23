{{ config(
    materialized = 'table',
    schema = 'dw_samssubs'
) }}

SELECT
    c.customerfname AS customer_first_name,
    c.customerlname AS customer_last_name,
    e.employeefname AS employee_first_name,
    e.employeelname AS employee_last_name,
    s.storeid,
    d.date_day,
    d.month_of_year,
    d.year_number,
    p.productname,
    om.ordermethod,
    f.quantity,
    f.price_each,
    f.quantity * f.price_each AS total_revenue
FROM {{ ref('fact_orderprocessing') }} f

LEFT JOIN {{ ref('customer_dim') }} c 
    ON f.customer_key = c.customer_key

LEFT JOIN {{ ref('employee_dim') }} e 
    ON f.employeekey = e.employeekey

LEFT JOIN {{ ref('store_dim') }} s 
    ON f.storekey = s.storekey

LEFT JOIN {{ ref('product_dim') }} p 
    ON f.productkey = p.productkey

LEFT JOIN {{ ref('ordermethod_dim') }} om 
    ON f.methodkey = om.methodkey

LEFT JOIN {{ ref('date_dim') }} d 
    ON f.datekey = d.datekey
