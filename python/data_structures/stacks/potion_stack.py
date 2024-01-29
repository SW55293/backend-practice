'''
ASSIGNMENT
Complete the PotionStack class.

It should inherit from the Stack class.
Override the push method in the PotionStack class. If the potion on the top of the stack is of the same 
type as the potion being pushed, then the push operation fails and nothing happens. Otherwise, use the Stack 
classes push method to push the potion onto the stack.

'''

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]


# don't modify above this line


class PotionStack(Stack):
    def push(self, potion):
        if self.peek() == potion:
            return
        super().push(potion)
    
