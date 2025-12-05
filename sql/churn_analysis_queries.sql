-- SQL placeholder file
-- Customer churn percentage
SELECT
SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS churn_rate
FROM customers;


-- Average tenure of churned vs retained customers
SELECT churn, AVG(tenure) AS avg_tenure
FROM customers
GROUP BY churn;