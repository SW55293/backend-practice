'''
ASSIGNMENT
Being a complex piece of software, Doc2Doc needs a good logging system so that users and developers alike can 
see what's going on under the hood.

Complete the get_logger function. It takes a formatter function as a parameter and should return a new function.

This new function prints the formatted inputs using the given formatter function parameter. The inputs should be passed
into the formatter function in the order they are given to the logger function.

TIP
colon_delimit and dash_delimit functions are examples of formatters that would be passed into our get_logger function.
'''


def get_logger(formatter):
    def new_funct(f,s):
        print(formatter(f,s))
    return new_funct


# Don't edit below this line


def test(first, errors, formatter):
    print("Logs:")
    logger = get_logger(formatter)
    for err in errors:
        logger(first, err)
    print("====================================")


def colon_delimit(first, second):
    return f"{first}: {second}"


def dash_delimit(first, second):
    return f"{first} - {second}"


def main():
    db_errors = [
        "out of memory",
        "cpu is pegged",
        "networking issue",
        "invalid syntax",
    ]
    test("Doc2Doc FATAL", db_errors, colon_delimit)

    mail_errors = [
        "email too large",
        "non alphanumeric symbols found",
    ]
    test("Doc2Doc WARNING", mail_errors, dash_delimit)


main()
