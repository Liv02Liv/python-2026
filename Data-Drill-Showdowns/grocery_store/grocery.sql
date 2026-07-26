WITH transaction_products AS (
SELECT DISTINCT
    transaction_id,
    product_name
FROM grocery
)

, product_pairs AS (
SELECT 
    a.transaction_id,
    a.product_name AS p1,
    b.product_name AS p2
FROM transaction_products a 
    INNER JOIN transaction_products b 
    ON a.transaction_id = b.transaction_id 
    AND a.product_name < b.product_name
)

SELECT
    p1,
    p2,
    COUNT(*) AS trans 
FROM product_pairs 
GROUP BY 1, 2
ORDER BY 3 DESC