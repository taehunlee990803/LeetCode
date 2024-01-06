# Write your MySQL query statement below
SELECT firstName, lastName, city, state FROM Person
LEFT JOIN address 
ON Person.personID = address.personID;
[object Object]
