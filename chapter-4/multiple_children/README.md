ASSIGNMENT
The Hero class is provided for you. In this assignment you'll be writing the Archer class that inherits from Hero, and in the next assignment you'll be writing its sibling Wizard class.

Fulfill the following requirements from the game designers.

Archer should inherit from Hero
Archer should setup the hero's name and health
Set a private "number of arrows" that can be passed in as a third parameter to the constructor.
Create a shoot method that takes a target human as input. If there are no arrows left, raise a not enough arrows exception. Otherwise, remove an arrow and deal 10 damage to the target human.