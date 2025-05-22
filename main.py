import sys
from stats import get_book_text
from stats import get_letter_count

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]        # 2nd argument as path to book

    #path = "./books/frankenstein.txt"   removed for CH:3 L:2
    book_text = get_book_text(path)
    num_words = len(book_text.split())
    num_phrase = f"Found {num_words} total words"
    #Found 75767 total words

    letter_count_string = get_letter_count(book_text)
    letter_count_string = letter_count_string.rstrip()

    #print(num_phrase)
    #print("============ BOOKBOT ============")
    #print("Analyzing book found at books/frankenstein.txt...")
    #print("----------- Word Count ----------")
    #print(num_phrase)                                 
    #print("--------- Character Count -------")
    print(letter_count_string) 
    #print("============= END ===============")

  

    book_text = get_book_text(path)


main()