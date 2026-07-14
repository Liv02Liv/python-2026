SELECT * FROM coffee;

WITH cte AS (SELECT strftime('%m', date) AS month, store, SUM(sales) AS total_sales
                FROM coffee
                GROUP BY month, store)

SELECT month, store, total_sales,
       total_sales - LAG(total_sales) OVER(PARTITION BY store ORDER BY month) AS mom_sales
FROM cte
ORDER BY month, store;