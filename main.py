from stats import number_of_words, number_of_characters, get_sorted_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #book = get_book_text("books/frankenstein.txt")
    book = get_book_text(sys.argv[1])

    num_words = number_of_words(book)
    num_characters = number_of_characters(book)
    # print(num_characters)
    sorted_list = get_sorted_list(num_characters)
    print("============ BOOKBOT ============\n"
    f"Analyzing book found at {sys.argv[1]}..\n"
    "----------- Word Count ----------\n"
    f"Found {num_words} total words\n"
    "--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()