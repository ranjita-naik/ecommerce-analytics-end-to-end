SELECT
    order_status,
    COUNT(DISTINCT order_id) AS orders
FROM fact_orders
GROUP BY order_status
ORDER BY orders DESC;

