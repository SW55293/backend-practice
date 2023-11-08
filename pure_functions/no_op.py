# USELESS NO-OP
def square(x):
    x * x

# this function call makes no sense
# it's just useless computation
square(3)

# USEFUL SIDE-EFFECT (BUT IMPURE)
y = 5
def add_to_y(x):
    y += x

# this function call changes the value of y
# but it's impure, and frankly bad code
add_to_y(5)
# --------------------------------------------

'''
ASSIGNMENT
Complete the markdown_to_text function. It's currently a no-op.

It should:

Remove any # characters that are at the beginning of a line. (headings in markdown)
Remove any * characters that are at the start or end of a word. (emphasis in markdown)
'''

def markdown_to_text(doc_content):
    # Split the input text into lines using line breaks
    lines = doc_content.split("\n")

    # Create a list to store the modified lines
    new_lines = []

    # Iterate through each line in the input text
    for line in lines:
        # Check if the line starts with a '#' character (indicating a heading)
        if line.startswith("#"):
            # Remove the '#' character and any leading/trailing whitespace
            line = line[1:].strip()
        
        # Call the remove_asterisks_from_words function to remove asterisks from words
        new_line = remove_asterisks_from_words(line)

        # Add the modified line to the list of new lines
        new_lines.append(new_line)

    # Join the new lines into a single string with line breaks and return it
    return "\n".join(new_lines)

# Function to remove asterisks from words
def remove_asterisks_from_words(line):
    # Split the line into words
    words = line.split()

    # Iterate through each word in the line
    for i, word in enumerate(words):
        # Check if the word starts with an '*' character
        if word.startswith("*"):
            # Remove the leading '*' character
            word = word[1:]
        # Check if the word ends with an '*' character
        if word.endswith("*"):
            # Remove the trailing '*' character
            word = word[:-1]
        # Check if the word is now empty
        if len(word) == 0:
            # Skip empty words
            continue
        # Update the word in the list of words
        words[i] = word

    # Join the modified words into a single string and return it
    return " ".join(words)
