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