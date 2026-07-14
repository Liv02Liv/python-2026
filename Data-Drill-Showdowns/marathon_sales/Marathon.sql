SELECT 
    CASE
        WHEN final < '03:00:00' THEN 'Sub 3:00'
        WHEN final < '03:30:00' THEN '3:00 - 3:30'
        WHEN final < '04:00:00' THEN '3:30 - 4:00'
        WHEN final < '04:30:00' THEN '4:00 - 4:30'
        WHEN final < '05:00:00' THEN '4:30 - 5:00' 
        WHEN final < '05:30:00' THEN '5:00 - 5:30'
        WHEN final < '06:00:00' THEN '5:30 - 6:00'
        ELSE '6:00+'
    END AS time_bucket,
    COUNT(*) AS runners,
    --COUNT(*) / SUM(COUNT(*)) OVER () AS pct_of_total
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 2) AS pct_of_total
FROM marathon
GROUP BY 1 
ORDER BY
CASE time_bucket
    WHEN 'Sub 3:00' THEN 1
    WHEN '3:00 - 3:30' THEN 2
    WHEN '3:30 - 4:00' THEN 3
    WHEN '4:00 - 4:30' THEN 4
    WHEN '4:30 - 5:00' THEN 5
    WHEN '5:00 - 5:30' THEN 6
    WHEN '5:30 - 6:00' THEN 7
    ELSE 8
END;
