-- 1. Top 5 funds by AUM
SELECT
scheme_name,
aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT
AVG(nav) AS average_nav
FROM fact_nav;

-- 3. Total SIP investment
SELECT
SUM(amount_inr) AS total_sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP';

-- 4. Transactions by state
SELECT
state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with expense ratio below 1%
SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Highest 1-year return funds
SELECT
scheme_name,
return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- 7. Average expense ratio
SELECT
AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance;

-- 8. Count funds by risk grade
SELECT
risk_grade,
COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;

-- 9. Top states by investment amount
SELECT
state,
SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 5;

-- 10. Average returns by category
SELECT
category,
AVG(return_3yr_pct) AS avg_3yr_return
FROM fact_performance
GROUP BY category
ORDER BY avg_3yr_return DESC;
