def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words():
    text = get_book_text("./books/frankenstein.txt")
    number_of_words = len(text.split())
    return f"Found {number_of_words} total words"
