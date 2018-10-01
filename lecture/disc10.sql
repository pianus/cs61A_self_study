create table records as
  select "Ben Bitdiddle" as Name, "Computer" as Division, "Wizard" as Title, 60000 as Salary, "Oliver Warbucks" as Supervisor union
  select "Alyssa P Hacker", "Computer", "Programmer", 40000, "Ben Bitdiddle" union
  select "Cy D Fect", "Computer", "Programmer", 35000, "Ben Bitdiddle" union
  select "Lem E Tweakit", "Computer", "technician", 25000, "Ben Bitdiddle" union
  select "Louis Reasoner", "Computer", "Programmer Trainee", 30000, "Alyssa P Hacker" union
  select "Oliver Warbucks", "Administration", "Big Wheel", 150000, "Oliver Warbucks" union
  select "Eben Scrooge", "Accounting", "Chief Accountant", 75000, "Oliver Warbucks" union
  select "Robert Cratchet", "Accounting", "Scrivener", 18000, "Eben Scrooge";

create table meetings as
  select "Accounting" as Division, "Monday" as Day, "9am" as Time union
  select "Computer", "Wednesday", "4pm" union
  select "Administration", "Monday", "11am" union
  select "Administration", "Thursday", "1pm";
