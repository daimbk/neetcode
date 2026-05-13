-- Write your query below
SELECT
    s.seller_name
FROM seller s
LEFT JOIN orders o 
ON  s.seller_id = o.seller_id
    AND o.sale_date > '2019-12-31'
    AND o.sale_date < '2021-01-01'
WHERE o.seller_id IS NULL
ORDER BY s.seller_name
