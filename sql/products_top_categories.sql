SELECT
    p.product_category_name AS category,
    ROUND(SUM(f.revenue), 2) AS total_revenue,
    COUNT(DISTINCT f.order_id) AS orders
FROM fact_orders f
JOIN dim_products p
    ON f.product_id = p.product_id
WHERE f.order_status = 'delivered'
GROUP BY category
ORDER BY total_revenue DESC
LIMIT 15;

