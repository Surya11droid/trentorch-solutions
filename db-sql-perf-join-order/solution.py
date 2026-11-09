SELECT customers.name
FROM regions
CROSS JOIN customers
ON regions.id = customers.region_id
WHERE regions.name = 'EU'
  AND customers.region_id = regions.id;
