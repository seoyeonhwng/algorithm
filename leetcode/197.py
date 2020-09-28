# Write your MySQL query statement below
SELECT
    a.id as 'Id'
FROM
    weather as a
    join weather as b on DATEDIFF(a.recordDate, b.recordDate) = 1
WHERE
    a.Temperature > b.Temperature