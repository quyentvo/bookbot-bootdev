# returns total amount of words in string
def get_words(book_text):
    return len(book_text.split())

# sorting key for list
def sort_on(items):
    return items["num"]

# sorts dictionary
def sort_list(items):
    result = []
    for name in items:
        result.append({"char": name, "num": items[name]})
    result.sort(reverse=True, key=sort_on)
    return result

# checks total count of characters, increases if it exists
def get_characters(book_text):
    my_dict = {}
    book_text = book_text.lower()

    for char in book_text:
            if char in my_dict:
                my_dict[char] += 1
            else:
                my_dict[char] = 1

    return my_dict
