def get_frank_book():
    with open("books/frankenstein.txt") as f:
        return f.read()


def get_number_words(text):
    words = text.split()
    return len(words)


def count_text_characters(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def convert_to_list_dicts(characters):
    list = []
    for char in characters:
        if char.isalpha():
            list.append({"char": char, "num": characters[char]})
    return list


def sort_on(dict):
    return dict["num"]


def print_list(list):
    for reg in list:
        print(reg)
        char = reg["char"]
        number = reg["num"]
        print(f"{char} was found {number} times")


def print_characters_report():
    book = get_frank_book()
    number_words = get_number_words(book)
    characters = count_text_characters(book)
    list = convert_to_list_dicts(characters)
    list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_words} found in the document")
    print_list(list)
    print("--- End report ---")


def main():
    print_characters_report()


main()
