def main():
    book_path = "books/frankenstein.txt"
    book_name = book_path[6:-4]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"---  Book report for: {book_name}  ---")
    print(f"{num_words} words in the document.\n")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times.")
    print(f"\n---  End report  ---")

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path, mode="r", newline=None) as f:
        return f.read()

main()
