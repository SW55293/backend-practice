'''
"Map", "filter", and "reduce" are three functions that are commonly used in functional programming. 
They are also the names of three of the most common higher-order functions in functional programming languages.

In Python, the built-in map function takes a function and an iterable (in this case a list), and returns a new 
iterable where the function has been applied to each element of the original iterable. This allows us to compose 
functions that operate on entire lists without having to write a loop and store state in variables. For example:
'''
def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = map(square, nums)
print(list(squared_nums))
# [1, 4, 9, 16, 25]


# map = for loop (in some cases)

'''
ASSIGNMENT
Markdown supports two different styles of bullet points, - and *. We need a function that will convert any - bullet 
points in a document to * bullet points.

Complete the change_bullet_style function. It should take a document (string) as input, and return a single string 
as output. The returned string should have any lines that start with a - character replaced with a * character. Preserve 
any newline \n characters that were in the original document.
'''
def change_bullet_style(document):
    return "\n".join(map(convert_line, document.split("\n")))
    


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
