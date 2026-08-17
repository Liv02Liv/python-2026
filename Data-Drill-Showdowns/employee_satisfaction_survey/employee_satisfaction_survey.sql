WITH ranked  AS (
SELECT
    Email,
    Satisfaction,
    Timestamp,
    ROW_NUMBER() OVER (PARTITION BY Email ORDER BY Timestamp DESC) AS rn 
FROM survey_responses
)

SELECT 
    Satisfaction,
    COUNT(Email) AS people
FROM ranked 
WHERE rn = 1
GROUP BY 1
ORDER BY 1