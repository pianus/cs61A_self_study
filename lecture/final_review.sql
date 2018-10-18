create table cards as
  select "warbot" as name, 1 as cost, 1 as attack, 3 as armor union
  select "Puddlestomper", 2,3,2 union
  select "Blingtron 3000", 5,3,4 union
  select "Annoy-o-tron", 1,1,2 union
  select "Jeeves", 3,1,4 union
  select "Madder Bomber", 5,5,4 union
  select "Piloted Shredder", 4,4,3;

create table bears as
  select "Oski" as name, 300 as weight union
  select "Pooh", 350 union
  select "Yogi", 425 union
  select "Po", 375 union
  select "Gummy", 425;

create table above_average
with averages(digit, mean) as (
  select weight/100, avg(weight)
  from bears
  group by weight/100
  having count(*) > 1
)
select weight, name
  from bears, averages
  where weight >= mean and digit = weight /100;
