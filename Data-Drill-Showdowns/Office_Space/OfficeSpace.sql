-- SELECT * FROM employees;

-- WITH RECURSIVE hier AS (

-- SELECT id, employee, manager, employee AS hierarchy
-- FROM employees 
-- WHERE manager IS NULL;

-- UNION ALL

-- SELECT e.id, e.employee, e.manager,
--         CONCAT(h.hierarchy, '>', e.employee) AS hierarchy
-- FROM    employees e INNER JOIN hier h ON e.manager = h.employee)

-- SELECT * FROM hier;