-- If, LEFT
SELECT 
    employee_id, IF ((employee_id % 2) = 0 || (LEFT(name, 1) = 'M'), 0, salary) AS bonus
FROM Employees
ORDER BY employee_id;