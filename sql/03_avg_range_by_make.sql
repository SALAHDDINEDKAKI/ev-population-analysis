-- Average electric range by make, restricted to makes with more than 100 vehicles
-- (filters out low-sample makes that would otherwise skew the ranking)
SELECT make, COUNT(*) AS vehicle_count, ROUND(AVG(electric_range)::numeric, 1) AS avg_range
FROM ev_population
GROUP BY make
HAVING COUNT(*) > 100
ORDER BY avg_range DESC
LIMIT 10;