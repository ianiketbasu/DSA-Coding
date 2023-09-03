# Write your MySQL query statement below
SELECT e.name , b.bonus
from Employee as e
LEFT JOIN Bonus as b ON e.empId = b.empId
WHERE b.Bonus < 1000 OR b.Bonus IS NULL