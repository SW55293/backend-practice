'''
Implement the count_potions function. It should take a list of our players' inventory (strings) 
as input and return the number of times Healing potion shows up in the list as an integer.
'''

# My soultion
def count_potions(inventory):
    counter = 0
    for x in range(len(inventory)):
        if inventory[x] == "Healing potion":
            counter += 1
    return counter
            
# Given Solution
def count_potions(inventory):
    count = 0
    for item in inventory:
        if item == "Healing potion":
            count += 1
    return count
