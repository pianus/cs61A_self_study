This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite 1

	>>> from ants import *

	Case Example
		>>> x = 5
		>>> x
		5

	Case MyEx
		>>> y = 15
		>>> y += 10
		>>> y
		25

	Case EC
		>>> from ants import *
		>>> hive, layout = Hive(AssaultPlan()), dry_layout
		>>> dimensions = (1, 9)
		>>> colony = AntColony(None, hive, ant_types(), layout, dimensions)
		>>> # Testing Slow
		>>> slow = SlowThrower()
		>>> bee = Bee(3)
		>>> colony.places["tunnel_0_0"].add_insect(slow)
		>>> colony.places["tunnel_0_4"].add_insect(bee)
		>>> slow.action(colony)
		>>> colony.time = 1
		>>> bee.action(colony) #first action
		>>> colony.time
		1
		>>> bee.place.name # SlowThrower should cause slowness on odd turns
		'tunnel_0_4'
		>>> colony.time += 1
		>>> bee.action(colony) # 2nd action
		>>> colony.time
		2
		>>> bee.place.name # SlowThrower should cause slowness on odd turns
		'tunnel_0_3'
		>>> colony.time += 1
		>>> colony.time
		3
		>>> bee.action(colony) # 3rd action
		>>> bee.place.name
		'tunnel_0_3'
		>>> colony.time += 1
		>>> bee.action(colony) # 4th action, should act like normal
		>>> bee.place.name
		'tunnel_0_2'
		>>> colony.time += 2
		>>> bee.action(colony) # 5th action, should act like normal
		>>> bee.place.name
		'tunnel_0_1'
		>>> colony.time += 1
		>>> bee.action(colony) # 5th action, should act like normal
		>>> bee.place.name
		'tunnel_0_0'
