from stats import get_char_count, get_num_words, sort_characters


def get_book_text(path_to_file):
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
        return file_contents


def print_report(word_count, book_location, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for character_record in sorted_characters:
        if character_record["name"].isalpha():
            print(f"{character_record["name"]}:\
 {character_record["count"]}")

    print("============= END ===============")


def main():
    path_to_book = './books/frankenstein.txt'
    loaded_book = get_book_text(path_to_book)

    word_count = get_num_words(loaded_book)
    sorted_chars = sort_characters(get_char_count(loaded_book))

    print_report(word_count, path_to_book, sorted_chars)


main()
