CREATE TABLE x AS SELECT 20 AS X;
with ints(n) as (select 1 union select n+1 from ints, X where n < X)

SELECT 
