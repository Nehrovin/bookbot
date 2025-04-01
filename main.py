from stats import num_of_words
from stats import count_characters
from stats import sort_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    filepath = "./books/frankenstein.txt"
    word_count = num_of_words(get_book_text(filepath))
    num_of_characters = count_characters(get_book_text(filepath))
    list_to_report = sort_list(num_of_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in list_to_report:
        if item["char"].isalpha() == True:
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
main()
