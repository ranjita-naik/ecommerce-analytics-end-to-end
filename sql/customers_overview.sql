SELECT
    state,
    COUNT(DISTINCT customer_unique_id) AS customers
FROM dim_customers
GROUP BY state
ORDER BY customers DESC;

