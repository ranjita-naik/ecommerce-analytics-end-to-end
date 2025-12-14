SELECT
    COUNT(DISTINCT order_id)           AS total_orders,
    ROUND(SUM(revenue), 2)             AS total_revenue,
    ROUND(AVG(revenue), 2)             AS avg_order_value,
    ROUND(AVG(review_score), 2)        AS avg_review_score,
    ROUND(
        AVG(CASE WHEN delivery_delay_days <= 0 THEN 1 ELSE 0 END),
        3
    )                                  AS on_time_delivery_rate
FROM fact_orders;

