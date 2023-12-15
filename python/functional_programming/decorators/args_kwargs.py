'''
ASSIGNMENT
At Doc2Doc, we spend a lot of time building better debugging tools for ourselves so that the next time we run into a problem, 
we can solve it faster.

Complete the args_logger function. It takes a variable number of positional and keyword arguments and should simply log them 
to the console in the following format.

1Log each position argument in order using asterisks (*) as the prefix and each on its own line.
2.Log each keyword argument in order using asterisks (*) as the prefix and each on its own line. Use the sorted() 
function and the .items() method on the kwargs dictionary to ensure that the arguments are logged in alphabetical order by key.

'''

def args_logger(*args, **kwargs):
    for arg in args:
      print(f"* {arg}")
   
    for key, val in sorted(kwargs.items()):
      print(f"* {key}: {val}")



# Don't edit below this line


def test(*args, **kwargs):
    args_logger(*args, **kwargs)
    print("========================================")


def main():
    test(1, 2, date_str="01/01/2023")
    test(message="Hello World", to_delete="l")
    test(1, 2, 3, 4, 5)
    test("hi", True, name="Lane", age=28)


main()
