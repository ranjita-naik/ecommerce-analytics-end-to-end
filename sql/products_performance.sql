SELECT
    p.product_category_name AS category,
    
    COUNT(DISTINCT f.order_id) AS total_orders,
    ROUND(SUM(f.revenue), 2) AS total_revenue,
    ROUND(AVG(f.review_score), 2) AS avg_review,
    
    ROUND(AVG(f.delivery_delay_days), 2) AS avg_delay

FROM fact_orders f
JOIN dim_products p ON f.product_id = p.product_id

WHERE f.order_status = 'delivered'

GROUP BY category
ORDER BY total_revenue DESC;

