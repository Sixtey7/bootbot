from stats import get_num_words, count_characters, sort_char_dict
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) == 2:
        path_to_book = sys.argv[1]
        book_contents = get_book_text(path_to_book)

        total_words = get_num_words(book_contents)

        countDict = count_characters(book_contents)

        sortedList = sort_char_dict(countDict)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")   
        print(f"Found {total_words} total words")
        print("--------- Character Count -------")
        for item in sortedList:
            print(f"{item["char"]}: {item["num"]}")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()