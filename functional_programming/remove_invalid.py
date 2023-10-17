'''
ASSIGNMENT
Complete the remove_invalid_lines function. It should scan the document and remove any 
lines that start with the old bullet point style -. Preserve any newline \n characters that were in the original
document.
'''

def remove_invalid_lines(document):
    return "\n".join(
        filter(lambda line: not line.startswith("-"), document.split("\n"))
    )