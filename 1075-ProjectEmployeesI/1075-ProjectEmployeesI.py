# Write your MySQL query statement below
SELECT project_id, ROUND(AVG(experience_years),2) as average_years FROM Employee
INNER JOIN Project ON Project.employee_id = Employee.employee_id GROUP BY project_id
[
