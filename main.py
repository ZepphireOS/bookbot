import sys
from stats import get_number_of_words, get_letter_count, dict_sort

def get_book_text(filename):
    with open(filename) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filename = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analysing books found at " + filename)
    print("----------- Word Count ----------")
    word_count = get_number_of_words(filename)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # Get the dictionary
    dic = get_letter_count(filename)
    # Sort the dictionary
    sorted_dic = dict_sort(dic)
    # Print the results
    for item in sorted_dic:
        print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

main()