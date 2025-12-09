-- Revenue by route
SELECT route_id, SUM(amount) total_revenue
FROM tickets
GROUP BY route_id;

-- Ranking routes
SELECT route_id, SUM(amount),
       RANK() OVER (ORDER BY SUM(amount) DESC) AS rank
FROM tickets
GROUP BY route_id;
