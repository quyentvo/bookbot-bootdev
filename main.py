import sys

from stats import get_words
from stats import get_characters
from stats import sort_list

# allows read to file based on path
def get_book_text(path):
    with open(path) as f:
        return f.read()

# allows input to bookpath
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # gets path based on arg when opening main.py
    book_text = get_book_text(sys.argv[1])
    words = get_words(book_text)
    print(f"Found {words} total words")

    # gets dict of letters within string, then sort it
    characters = get_characters(book_text)
    sorted_characters = sort_list(characters)
    
    # checks .isalpha(), only visual printing, don't modify dict
    for char in sorted_characters:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
main()
