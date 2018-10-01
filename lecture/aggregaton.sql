create table animals as
  select "dog" as kind, 4 as legs, 20 as weight union
  select "cat", 4, 10 union
  select "ferret", 4, 10 union
  select "parrot", 2, 6 union
  select "penguin", 2, 10 union
  select "t-rex", 2, 12000;

select max(legs) from animals;

create table dogs as
  select "Fido" as name, 1 as age, "woof" as phrase union
  select "Sparky", 2, "woof" union
  select "Lassie", 2, "I'll save you!" union
  select "Floofy", 3, "Much doge";
  
