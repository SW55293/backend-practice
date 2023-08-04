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


__Part 2__
<mark> Let's use the Dragon class to have ourselves a little dragon fight. Complete the bottom half of the main() function.
</mark> 

* First, describe() all dragons
* Next, make each dragon attempt to breathe fire at all of the other dragons. The center of each blast should always be at (3,3).
* Call describe() on all the dragons first, then have them breathe fire.

<mark> ORDER MATTERS FOR YOUR SOLUTION 
</mark> 

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

### Extras

__Rectangle__

CHALLENGE
Finish implementing the empty methods of the Rectangle and Square classes.

Keep in mind that a square is just a rectangle where the length and width are equal. You shouldn't have to duplicate any code between the two classes.

__Gas Cost__

Complete the Vehicle, Car, and Truck classes.

VEHICLE CLASS
CONSTRUCTOR
Accepts two parameters (in order) and sets them as instance variables:

max_speed_kph
kilometers_per_liter
GET_PRICE_FOR_TRIP()
The formula for calculating the cost of gas for a trip is:

distance / rate_of_consumption * price

GET_CARGO_CAP_METERS_CUBED()
This method should be left empty. You can use the pass keyword. This will be overridden by child classes.

TRUCK CLASS
CONSTRUCTOR
Calls the parent constructor, then sets the additional truck-specific instance variables as member variables.

GET_PRICE_FOR_TRIP()
Uses the parent method to calculate the cost of gas for a trip, but adds an additional cost to account for the load weight.

The formula for calculating the cost of gas for a trip is:

base_vehicle_cost + (load_weight_kilos * 0.01)

GET_CARGO_CAP_METERS_CUBED()
Returns the cargo capacity of the truck in meters cubed. A truck's bed is 2 meters deep. Return the volume of the truck's bed by multiplying the area of the bed by its depth.

CAR CLASS
CONSTRUCTOR
Calls the parent constructor, then sets the additional car-specific instance variable as a member variable.

GET_PRICE_FOR_TRIP
The car class does not need to override this method.

GET_CARGO_CAP_METERS_CUBED()
Returns the cargo capacity of the car, which was set in the constructor. No fancy calculations needed here.

#### Extras

##### Calculating Gas Cost

__VEHICLE CLASS__

* CONSTRUCTOR
Accepts two parameters (in order) and sets them as instance variables:

max_speed_kph
kilometers_per_liter

* GET_PRICE_FOR_TRIP()
The formula for calculating the cost of gas for a trip is:

distance / rate_of_consumption * price

* GET_CARGO_CAP_METERS_CUBED()
This method should be left empty. You can use the pass keyword. This will be overridden by child classes.

__TRUCK CLASS__

* CONSTRUCTOR
Calls the parent constructor, then sets the additional truck-specific instance variables as member variables.

* GET_PRICE_FOR_TRIP()
Uses the parent method to calculate the cost of gas for a trip, but adds an additional cost to account for the load weight.

The formula for calculating the cost of gas for a trip is:

base_vehicle_cost + (load_weight_kilos * 0.01)

* GET_CARGO_CAP_METERS_CUBED()
Returns the cargo capacity of the truck in meters cubed. A truck's bed is 2 meters deep. Return the volume of the truck's bed by multiplying the area of the bed by its depth.

__CAR CLASS__

* CONSTRUCTOR
Calls the parent constructor, then sets the additional car-specific instance variable as a member variable.

* GET_PRICE_FOR_TRIP
The car class does not need to override this method.

* GET_CARGO_CAP_METERS_CUBED()
Returns the cargo capacity of the car, which was set in the constructor. No fancy calculations needed here.