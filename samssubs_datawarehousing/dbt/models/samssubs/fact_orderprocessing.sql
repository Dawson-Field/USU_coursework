{{ config(
    materialized = 'table',
    schema = 'dw_samssubs'
) }}

SELECT
    c.customer_key,
    e.employeekey,
    s.storekey,
    p.productkey,
    om.methodkey,
    d.datekey,
    od.orderlineqty AS quantity,
    od.orderlineprice AS price_each
FROM {{ source('samssubs_landing', '"ORDER"') }} o
JOIN {{ source('samssubs_landing', 'orderdetails') }} od 
  ON o.ordernumber = od.ordernumber
JOIN {{ ref('customer_dim') }} c 
  ON o.customerid = c.customerid
JOIN {{ ref('employee_dim') }} e 
  ON o.employeeid = e.employeeid
JOIN {{ ref('store_dim') }} s 
  ON e.storeid = s.storeid  
JOIN {{ ref('product_dim') }} p 
  ON od.productid = p.productid
JOIN {{ ref('ordermethod_dim') }} om 
  ON o.ordermethod = om.ordermethod
JOIN {{ ref('date_dim') }} d 
  ON d.date_day = o.orderdate


