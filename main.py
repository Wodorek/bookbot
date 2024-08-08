def main():
    book = open_book('./books/Frankenstein.txt')
    word_count = count_words(book)
    print(word_count)


def open_book(path):
    with open(path) as f:
        contents = f.read()
        return contents


def count_words(txt):

    split = txt.split()

    return len(split)


main()
