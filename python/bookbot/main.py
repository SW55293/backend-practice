from collections import Counter


def main():
    book_path = "books/frankenstein.txt"
    txt = get_book(book_path)
    split(book_path)
    count_letters(book_path)


def get_book(path):
    with open(path) as f:
        return f.read()

    
def split(path):
    count = 0
    words = get_book(path)
    splt = words.split()

    for _ in splt :
        count += 1
    print(count)

def count_letters(path):
    count_of_letters = {}
    letter = get_book(path)
  
    letter = letter.lower()

    count_of_letters  = Counter(letter)

    print(count_of_letters)

    for x, y in count_of_letters.items():
        if x.isalpha:
            print(f'The {x} character was found {y} times')
    '''
    my_dict = {}

    for letter in words:
        if letter in my_dict:
            my_dict[letter] += 1
        else:
         # first entry
            my_dict[letter] = 1
    '''



            


main()