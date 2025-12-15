SELECT
    c.customer_unique_id,
    c.state,
    
    COUNT(DISTINCT f.order_id) AS order_count,
    ROUND(SUM(f.revenue), 2) AS total_revenue,
    
    ROUND(AVG(f.review_score), 2) AS avg_review,
    
    MIN(f.order_purchase_timestamp) AS first_purchase,
    MAX(f.order_purchase_timestamp) AS last_purchase
FROM fact_orders f
JOIN dim_customers c
    ON f.customer_id = c.customer_id
GROUP BY c.customer_unique_id, c.state;

