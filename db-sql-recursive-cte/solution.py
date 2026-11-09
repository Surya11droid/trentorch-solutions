WITH RECURSIVE reports(id, name, depth) AS (
  SELECT id, name, 1 FROM employees WHERE manager_id = 1   -- anchor
  UNION ALL
  SELECT e.id, e.name, r.depth + 1                          -- recursive step
  FROM employees e
  JOIN reports r ON e.manager_id = r.id
)
SELECT id, name, depth FROM reports;
