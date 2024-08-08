def main():
    book = open_book('./books/Frankenstein.txt')
    word_count = count_words(book)
    print(f'The word count is{word_count}')
    char_count = count_chars(book)

    print(char_count)


def open_book(path):
    with open(path) as f:
        contents = f.read()
        return contents


def count_words(txt):

    split = txt.split()

    return len(split)


def count_chars(txt):

    counts = {}

    lowercase = txt.lower()

    for word in lowercase.split():
        for letter in word:
            if letter in counts:
                counts[letter] += 1
            else:
                counts[letter] = 1

    return counts


main()
