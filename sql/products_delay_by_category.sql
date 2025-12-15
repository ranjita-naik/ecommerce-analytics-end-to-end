SELECT
    p.product_category_name AS category,
    ROUND(AVG(f.delivery_delay_days), 2) AS avg_delay
FROM fact_orders f
JOIN dim_products p
    ON f.product_id = p.product_id
WHERE f.order_status = 'delivered'
GROUP BY category
HAVING COUNT(*) > 50  -- reduce noise
ORDER BY avg_delay DESC
LIMIT 20;

