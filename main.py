def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_char_count(text)
    report_print(book_path, num_words, character_count)
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text):
    normalized_text = text.lower()
    char_dict = {}
    for char in normalized_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def report_print(book,word_count, character_count):
    print(f"--- Begin report for {book} ---")
    print(f"{word_count} words found in the document")
    for char in character_count:
        if char.isalpha():
            print(f"The '{char}' character was found {character_count[char]} times")

main()
