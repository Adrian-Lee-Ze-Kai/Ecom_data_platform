-- Which are the top 10 members by spending

SELECT m.membership_id, SUM(t.total_cost) as total_spending
FROM members m
INNER JOIN transactions t ON m.membership_id = t.membership_id
GROUP BY m.membership_id
ORDER BY total_spending DESC
LIMIT 10;
