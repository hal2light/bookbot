from stats import get_book_text
from stats import get_num_words
from stats import count_chars
from stats import sort_chars
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_num_words(text)
    char_count_list = sort_chars(text)
    char_count = ""
    for dic in char_count_list:
        char_count += f"{dic["char"]}: {dic["num"]}\n"

    print(f'''
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
{word_count}
--------- Character Count -------
{char_count[:-1]}
============= END ===============''')
main()
    

