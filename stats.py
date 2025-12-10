def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words():
    text = get_book_text("./books/frankenstein.txt")
    number_of_words = len(text.split())
    return f"Found {number_of_words} total words"

def count_chars():
    text = get_book_text("./books/frankenstein.txt")
    lowered_text = text.lower()
    char_list = ["t","p","c"]
    chars = {}
    for char in char_list:
        char_count = lowered_text.count(char)
        chars[char] = char_count
    return chars






