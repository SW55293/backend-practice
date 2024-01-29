'''
ASSIGNMENT
Write a function is_balanced(input_str) that takes a string input_str as input and returns True if the 
parentheses in the string are balanced, and False otherwise. Use a stack to keep track of the parentheses.

Note: You only need to consider the characters ( and ) for this challenge.

TIP
We've created a class named Stack with some helpful functions that you can use to complete the is_balanced function.


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


def is_balanced(input_str):
    stack = Stack()
    
    for char in input_str:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.pop() is None:
                return False
    return stack.peek() is None