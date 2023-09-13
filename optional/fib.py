'''
1. The input n represents the index of the desired Fibonacci value

2. Initialize three values. One will hold the current value, one will hold the parent value
(1 before), and one will hold the grandparent value (2 before the current). You'll need to hard-code the first two values of the sequence. grandparent=0 and parent=1

3. Write a loop that iterates n-1 times. Think about it: We'll want this loop to run exactly once when n=2.

4. Inside the loop update the current based on the parents, then update the parents to their appropriate values.

5. Return the current value once the loop completes


'''

def fib(n):
    if n <= 1:
        return n
    current = 0
    parent = 1
    grandparent = 0
    for x in range(2, n + 1):
        # or [for x in range(0,n-1)]
        current = parent + grandparent
        grandparent = parent
        parent = current
    return current