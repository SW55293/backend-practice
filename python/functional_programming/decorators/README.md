#### Args and Kwargs

- *args collects positional arguments into a tuple
- **kwargs collects keyword arguments into a dictionary


```python
def print_arguments(*args, **kwargs):
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

print_arguments("hello", "world", a=1, b=2)
# Positional arguments: ('hello', 'world')
# Keyword arguments: {'a': 1, 'b': 2}

```

1. Positional Arguments
    - passed in by position
```python
def sub(a, b):
    return a - b

res = sub(3, 2)

print(res)
# 1
```

2. Keyword Arguments 
    - These are passed in by name
```python
def sub(a, b):
    return a - b

res = sub(b=3, a=2)

print(res)
# -1
```

__Any positional arguments must come before keyword arguments__ 
__Python will try to match up the arguments you pass in with the arguments in the function definition by position first, and then by name__