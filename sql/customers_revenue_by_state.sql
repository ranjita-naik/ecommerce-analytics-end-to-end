SELECT
    c.state,
    ROUND(SUM(f.revenue), 2) AS total_revenue
FROM fact_orders f
JOIN dim_customers c
    ON f.customer_id = c.customer_id
WHERE f.order_status = 'delivered'
GROUP BY c.state
ORDER BY total_revenue DESC;

