.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT a.date, a.color, a.pet, a.number, b.number
  FROM students as a, fa17students as b
  WHERE a.date = b.date and a.color = b.color and a.pet = b.pet;

-- Q6
CREATE TABLE sevens AS
  SELECT a.seven
  FROM students as a, checkboxes as b
  WHERE a.time = b.time and b.'7' = 'True' and a.number = 7;

-- Q7
CREATE TABLE fa17favnum AS
  SELECT number, COUNT(*) AS count
  FROM fa17students
  GROUP BY number
  ORDER BY count DESC
  LIMIT 1;


CREATE TABLE fa17favpets AS
  SELECT pet, COUNT(*) AS count
  FROM fa17students
  GROUP BY pet
  ORDER BY count DESC
  LIMIT 10;


CREATE TABLE sp18favpets AS
  SELECT pet, COUNT(*) AS count
  FROM students
  GROUP BY pet
  ORDER BY count DESC
  LIMIT 10;


CREATE TABLE sp18dog AS
  SELECT pet, COUNT(*) as count
  FROM students
  WHERE pet = "dog";


CREATE TABLE sp18alldogs AS
  SELECT pet, COUNT(*) as count
  FROM students
  WHERE pet LIKE '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven, denero, COUNT(*) as count
  FROM students
  where seven = '7'
  GROUP BY denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*) as count
  FROM students
  GROUP BY smallest
  ORDER BY smallest;
