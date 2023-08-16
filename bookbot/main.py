
def main():
    book_path = "books/frankenstein.txt"
    # txt = get_book(book_path)
    split(book_path)


def get_book(path):
    with open(path) as f:
        return f.read()
    
def split(path):
    count = 0
    with open(path) as txt:
        words = txt.read()
        splt = words.split()

        for _ in splt :
            count += 1
    print(count)
            


main()