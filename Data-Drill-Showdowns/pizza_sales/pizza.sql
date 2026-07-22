SELECT * FROM price_history;

WITH mrd AS (
SELECT 
    t.order_detail_id,
    t.order_date,
    t.pizza_id,
    t.quantity,
    MAX(effective_date) AS most_recent_date
 FROM transactions t 
    LEFT JOIN price_history ph 
        ON t.pizza_id = ph.pizza_id
        AND t.order_date >= ph.effective_date
GROUP BY 1, 2, 3, 4
),

full_transaction_data AS (
SELECT 
    m.*,
    ph.price
FROM mrd m 
    LEFT JOIN price_history ph 
        ON ph.pizza_id = m.pizza_id
        AND m.most_recent_date = ph.effective_date
)

SELECT SUM(price * quantity) FROM full_transaction_data;