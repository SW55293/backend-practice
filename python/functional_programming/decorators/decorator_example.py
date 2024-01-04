'''
ASSIGNMENT
Complete the file_type_aggregator function and decorate the process_doc function with it.

The file_type_aggregator function assumes that the function it decorates will only have 2 positional arguments:

doc, a string
file_type: a string
Fix the wrapper function inside of file_type_aggregator to:

Update the counts dictionary to accurately reflect the number of times each file type has been processed
Calculate the result of calling the decorated function before the given return statements.

def file_type_aggregator(func_to_wrap):
    # dict of file_type -> count
    counts = {}

    def wrapper(doc, file_type):
        nonlocal counts

        counts = {}
        result = None

        return result, counts

    return wrapper


# ?
def process_doc(doc, file_type):
    return f"Processing doc: {doc} with File Type: {file_type}"



'''

def file_type_aggregator(func_to_wrap):
    # dict of file_type -> count
    counts = {}

    def wrapper(doc, file_type):
        nonlocal counts

        if file_type not in counts:
            counts[file_type] = 0
        counts[file_type] += 1
         
        result =  func_to_wrap(doc, file_type)

        return result, counts

    return wrapper


@file_type_aggregator
def process_doc(doc, file_type):
    return f"Processing doc: {doc} with File Type: {file_type}"
