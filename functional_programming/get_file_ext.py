'''
ASSIGNMENT
Complete the categorize_file function. It should take in a single argument, filename, and return a string representing 
the category of the file. The categories are as follows:

Text if the file ends with .txt
Document if the file ends with .docx
Code if the file ends with .py
Unknown if the file ends with anything else
The last line of the function is already written for you. It does the heavy lifting of parsing the extension out of 
the filename. You just need to write the logic for determining the category.

The last line expects an anonymous get_category function to exist. You should create that function using a lambda 
expression. It should take in a single argument, extension, and return a string representing the category of the file.

TIP
I used the built-in dictionaries .get method to implement this.

'''

def categorize_file(filename):
    get_category = lambda x: x.get()

    return get_category(filename[filename.rfind(".") :])


# Don't edit below this line


def test(filename):
    category = categorize_file(filename)
    print(f"The file {filename} is of type {category}")


def main():
    files = [
        "document1.txt",
        "notes.docx",
        "essay.docx",
        "bot.py",
        "unknown.xyz",
    ]

    for file in files:
        test(file)


main()
