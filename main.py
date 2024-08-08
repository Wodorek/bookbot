def main():
    book = open_book('./books/Frankenstein.txt')
    word_count = count_words(book)
    print(f'The word count is {word_count}')
    char_count = count_chars(book)
    print(char_count)
    generate_report('./books/Frankenstein.txt')


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


def generate_report(book):

    txt = open_book(book)
    char_counts = count_chars(txt)

    counts_list = []

    for char in char_counts:
        counts_list.append({'letter': char, 'num': char_counts[char]})

    sorted_count = sorted(counts_list, reverse=True, key=lambda x: x['num'])

    print(f'Displaying report for ${book}')
    print('')
    print(f'Found ${count_words(txt)} words in document')
    for entry in sorted_count:
        print(f'letter "{entry['letter']}" was found {entry['num']} times')
    print('')
    print('report end')


main()
