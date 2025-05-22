'''  This was the code used for the first lesson
def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "./books/frankenstein.txt"
    book_words = get_book_text(path)
    print(book_words)
'''
'''  This was the code used for the second lesson
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "./books/frankenstein.txt"
    book_words = get_book_text(path)
    num_words = len(book_words.split())
    print(f"{num_words} words found in the document")
'''

''' This was the code used for the third lesson '''
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_letter_count(book_text):
    letter_count = {}
    for letter in book_text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    sorted_letters = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
    letter_count_string = ""
    for letter, count in sorted_letters:
        letter_count_string += f"{letter}: {count}\n"
        
    return letter_count_string
