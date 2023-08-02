### ASSIGNMENT

#### Archer
The Hero class is provided for you. In this assignment you'll be writing the Archer class that inherits from Hero, and in the next assignment you'll be writing its sibling Wizard class.

__Fulfill the following requirements from the game designers.__

* Archer should inherit from Hero
* Archer should setup the hero's name and health
* Set a private "number of arrows" that can be passed in as a third parameter to the constructor.
* Create a shoot method that takes a target human as input. If there are no arrows left, raise a not enough arrows exception. Otherwise, remove an arrow and deal 10 damage to the target human.

#### Wizard

Let's extend the Hero class by adding a second child class: the Wizard. Wizard heroes are more powerful than archer heroes. They cast spells at other humans instead of shooting them, and casting does 25 damage instead of 10 but also costs 25 mana.

__Fulfill the following requirements.__

* Wizard should inherit from Hero
* Wizard should set up the hero's name and health
* Set a private "mana" variable that can be passed in as a third parameter to the constructor.
* Create a cast method that takes a target human as input. If there is not enough mana left, raise a not enough mana exception. Otherwise, remove 25 mana from the wizard and deal 25 damage to the target human.

#### Dragons

__Complete the unit's in_area method and the dragon's breathe_fire method.__

* IN_AREA
If the unit's position is in the rectangle defined by the parameters, return True. Otherwise, return False. x_1 and y_1 make up the bottom-left point of the rectangle. x_2 and y_2 define the top-right point.

* BREATHE_FIRE
This method causes the dragon to breathe a swath of fire in the target area. The target area is centered at (x,y). The area stretches for __fire_range in either direction inclusively.

* For each unit in the units array, print {} is hit by the fire if the unit is within the blast, where {} is the name of the unit.

__Let's use the Dragon class to have ourselves a little dragon fight. Complete the bottom half of the main() function.__

* First, describe() all dragons
* Next, make each dragon attempt to breathe fire at all of the other dragons. The center of each blast should always be at (3,3).
* Call describe() on all the dragons first, then have them breathe fire.

==ORDER MATTERS FOR YOUR SOLUTION==
Make sure to do everything in ascending index order. For example, when Black Dragon breathes fire, it should breathe fire on the other dragons in this order:

Green Dragon
Red Dragon
Blue Dragon

TIPS
```
COPYING A LIST
To get a new copy of a list, use the copy() method. If you don't, your new variable will just be a reference to the same list.

nums = [4, 3, 2, 1]
nums_copy = nums.copy()
# nums_copy is [4, 3, 2, 1]

DELETE FROM A LIST

nums = [4, 3, 2, 1]
del nums[1]
# nums is [4, 2, 1]
```