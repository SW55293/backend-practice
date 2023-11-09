## WHAT IS A PURE FUNCTION?

A pure function is a function that has two properties:

* It always returns the same value given the same arguments.

* Its evaluation has no side effects

### EXAMPLE OF A PURE FUNCTION

```python

def findMax(nums):
    max_val = float('-inf')
    for num in nums:
        if max_val < num:
            max_val = num
    return max_val

```

### EXAMPLE OF AN IMPURE FUNCTION

```python

# instead of returning a value
# this function modifies a global variable
global_max = float('-inf')

def findMax(nums):
    for num in nums:
        if global_max < num:
            global_max = num


```

#### faq's

- Return the same result if given the same arguments. They are deterministic.
- Do not change the external state of the program. For example, they do not change any variables outside of their scope.
- Do not perform any I/O operations (like reading from disk, accessing the internet, or writing from the console)
- Do not call any functions that do any of the above

> Pure functions contain all the code inside of a function, they do not call or need
> anything outside of it's scope

### Pass by Reference vs Value

* Pass by reference: A function can mutate the original value that was passed into it
* Pass by value: A function can not mutate the original value that was passed into it, it gets a copy

__In Python, these types are passed by reference:__

- Lists
- Dictionaries
- Sets

__These types are passed by value:__

- Integers
- Floats
- Strings
- Booleans
- Tuples

### EXAMPLE OF PASS BY REFERENCE (MUTABLE)

```python

def modify_list(lst):
    lst.append(4)
    # my_list = [1, 2, 3, 4]

my_list = [1, 2, 3]
# my_list = [1, 2, 3]
modify_list(my_list)
# my_list = [1, 2, 3, 4]

```

### EXAMPLE OF PASS BY VALUE (IMMUTABLE)

```python

def attempt_to_modify(num):
    num += 1

my_num = 1
# my_num = 1
attempt_to_modify(my_num)
# my_num = 1

```