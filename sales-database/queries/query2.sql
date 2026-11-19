-- Which are the top 3 items that are frequently bought by members

SELECT i.item_name, SUM(ti.quantity) as total_purchases
FROM items i
INNER JOIN transaction_items ti ON i.item_id = ti.item_id
GROUP BY i.item_name
ORDER BY total_purchases DESC
LIMIT 3;