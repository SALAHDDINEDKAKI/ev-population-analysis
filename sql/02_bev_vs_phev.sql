-- Breakdown of vehicle type: BEV vs PHEV
SELECT electric_vehicle_type, COUNT(*) AS vehicle_count
FROM ev_population
GROUP BY electric_vehicle_type
ORDER BY vehicle_count DESC;