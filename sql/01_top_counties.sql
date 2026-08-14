-- Top 10 counties by number of EV registrations
SELECT county, COUNT(*) AS ev_count
FROM ev_population
GROUP BY county
ORDER BY ev_count DESC
LIMIT 10;