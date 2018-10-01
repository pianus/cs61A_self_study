CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT DISTINCT name, size FROM dogs, sizes
  WHERE dogs.height > sizes.min and dogs.height <= sizes.max
  ORDER BY dogs.name;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_height AS
  SELECT a.name from dogs as a, dogs as b, parents
  WHERE a.name = parents.child and b.name = parents.parent
  Order by b.height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.name as name1, b.name as name2
  FROM dogs as a, dogs as b, parents as c, parents as d
  WHERE a.name = c.child and b.name = d.child and a.name <> b.name
    and c.parent = d.parent and a.name < b.name;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT name1 || ' and ' || name2 || ' are ' || a.size || ' siblings'
  FROM siblings, size_of_dogs as a, size_of_dogs as b
  WHERE name1 = a.name and name2 = b.name and a.size = b.size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

-- Add your INSERT INTOs here
INSERT INTO stacks_helper(dogs, stack_height, last_height)
  SELECT a.name ||', '|| b.name ||', '|| c.name ||', '|| d.name,
         a.height + b.height + c.height + d.height,
         d.height
  FROM dogs as a, dogs as b, dogs as c, dogs as d
  WHERE a.height < b.height and b.height < c.height and c.height < d.height;


CREATE TABLE stacks AS
  SELECT dogs, stack_height from stacks_helper where stack_height > 170 order by stack_height;
