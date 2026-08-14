-- EV registrations by model year (adoption trend over time)
SELECT model_year, COUNT(*) AS vehicle_count
FROM ev_population
GROUP BY model_year
ORDER BY model_year;