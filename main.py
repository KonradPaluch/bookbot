def get_book_text(path_to_file):
    with open(path_to_file, 'r') as f:
        file_contents = f.read()
        return file_contents

def main():
    path_to_book = './books/frankenstein.txt'
    loaded_book = get_book_text(path_to_book)
    print(loaded_book)

main()