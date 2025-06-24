def get_num_words(book):
    return len(book.split())


def get_char_count(book):
    character_count = dict()

    for char in book.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count


def sort_characters(character_count):
    def sort_by_count(e):
        return e["count"]

    character_record = []

    for character in character_count.items():
        character_record.append({"name": character[0], "count": character[1]})

    character_record.sort(reverse=True, key=sort_by_count)

    return character_record
