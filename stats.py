def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    number_of_words = len(text.split())
    return f"Found {number_of_words} total words"

def count_chars(text):
    lowered_text = text.lower()
    chars = []
    char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","æ","â","ê","ë","ô"]
    for char in char_list:
        char_count = lowered_text.count(char)
        chars.append({"char":char,"num":char_count})
    return chars

def sort_chars(text):
    def sort_on(items):
        return items["num"]
    chars = count_chars(text)
    chars.sort(reverse=True,key=sort_on)
    return chars

