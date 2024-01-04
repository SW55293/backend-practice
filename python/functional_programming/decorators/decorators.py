'''
ASSIGNMENT
Complete the markdown_to_text_decorator and convert_md_to_txt functions.

CONVERT_MD_TO_TXT
The convert_md_to_txt function should take a string of Markdown text and return a string of 
text with any "headings" syntax removed. For example:

# This is a heading 1
## This is a heading 2
### This is a heading 3
Copy icon
Should be converted to:

This is a heading 1
This is a heading 2
This is a heading 3
Copy icon
You can use .split("\n") to split a string into a list of strings on each newline, and "\n".join() to join a list 
of lines back into the full string.

I used the .lstrip() method to remove the leading # characters and spaces from each line.

MARKDOWN_TO_TEXT_DECORATOR
Because markdown_to_text_decorator can decorate a function with any number of string arguments, we need to iterate 
over all the given *args and **kwargs values and convert them using convert_md_to_txt. We'll then pass the converted 
values on to the wrapped function. This decorator allows any function to auto-convert its inputs from Markdown headings 
to plain text before processing them.

TIP
In addition to accepting arbitrary inputs in a function definition using the * and ** syntax, you can also pass in 
arbitrary inputs to a function call using a similar syntax. For example:

'''

def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        converted = []
        for x in args:
            converted.append(convert_md_to_txt(x))
        for key, val in kwargs.items():
            kwargs[key] = convert_md_to_txt(val)
        return func(*converted, **kwargs)
                

    return wrapper


def convert_md_to_txt(doc):
    removed = doc.split('\n')
    for x in range(len(removed)):
        line = removed[x]
        removed[x] = line.lstrip('#').lstrip(" ")
    return "\n".join(removed)


# Don't edit below this line


@markdown_to_text_decorator
def concat(first_doc, second_doc):
    return f"""First: {first_doc}
Second: {second_doc}
"""


@markdown_to_text_decorator
def format_as_essay(title, body, conclusion):
    return f"""Title: {title}
Body: {body}
Conclusion: {conclusion}
"""
