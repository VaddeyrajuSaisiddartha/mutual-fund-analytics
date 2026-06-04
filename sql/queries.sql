-- Top 5 funds by AUM
SELECT * FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- Monthly average NAV
SELECT strftime('%Y-%m', date) AS month,
AVG(nav)
FROM fact_nav
GROUP BY month;

-- Total SIP inflows
SELECT SUM(sip_inflow_crore)
FROM fact_sip;

-- Transactions by state
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Funds with expense ratio < 1
SELECT *
FROM fact_performance
WHERE expense_ratio < 1;

-- Top performing funds
SELECT *
FROM fact_performance
ORDER BY return_1yr DESC
LIMIT 10;

-- Fund count by categorys
SELECT category, COUNT(*)
FROM dim_fund
GROUP BY category;

-- Average AUM by fund house
SELECT fund_house, AVG(aum_crore)
FROM fact_aum
GROUP BY fund_house;

-- Total folios
SELECT SUM(folio_count)
FROM fact_folio;