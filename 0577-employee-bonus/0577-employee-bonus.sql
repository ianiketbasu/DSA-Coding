# Write your MySQL query statement below
# SELECT e.name , b.bonus
# from Employee as e
# LEFT JOIN Bonus as b ON e.empId = b.empId
# WHERE b.Bonus < 1000 OR b.Bonus IS NULL


SELECT name ,bonus
FROM Employee
LEFT JOIN Bonus USING (empId)
WHERE COALESCE(bonus,0) < 1000;