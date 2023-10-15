def main():
    path = "./books/frankenstein.txt"
    file_contents = read_file(path)
    word_count = get_word_count(file_contents)
    character_counts = get_character_counts(file_contents)
    print_report(path, word_count, character_counts)

def read_file(path):

    with open(path) as f:
        file_contents = f.read()

    return file_contents


def get_word_count(file_contents):
    return len(file_contents.split())


def get_character_counts(file_contents):
    character_counts = {}

    for ch in file_contents:
        lower_ch = ch.lower()
        if lower_ch in character_counts:
            character_counts[lower_ch] += 1
            continue

        character_counts[lower_ch] = 1

    return character_counts


def print_report(path, word_count, character_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print(f" ")
    sorted_by_value = dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_by_value.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} time")
    print(" ")
    print("--- End report ---")



main()