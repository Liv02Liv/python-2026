WITH RECURSIVE date_skeleton AS (

SELECT '2015-07-01' AS stay_date

UNION ALL

SELECT
    DATE(stay_date, '+1 day')
FROM date_skeleton
WHERE stay_date <= '2017-08-31'
)


,daily_occupancy AS (
SELECT 
    ds.stay_date,
    COUNT(b.booking_id) AS nights_occupied
FROM date_skeleton ds 
    LEFT JOIN hotel b 
        ON ds.stay_date BETWEEN b.checkin_date AND DATE(b.checkout_date, '-1 day')
        AND b.is_canceled = 0
GROUP BY ds.stay_date
)

SELECT
    --DATE_FORMAT(stay_date, '%Y-%m-01') AS month_start,
    strftime('%Y-%m-%d', stay_date) AS month_start,
    SUM(nights_occupied) AS total_nights_occupied,
    COUNT(*) * 200 AS available_nights,
    --SUM(nights_occupied) / (COUNT(*) * 200) AS occupancy_rate
    --ROUND(
        --SUM(nights_occupied) * 1.0 / (COUNT(*) * 200),
        --5
    --) AS occupancy_rate
    printf(
    '%.5f',
    SUM(nights_occupied) * 1.0 / (COUNT(*) * 200)
) AS occupancy_rate

FROM daily_occupancy
GROUP BY 1




