"""Run trygrams algoritm on a text file."""

import random
import sys


def main(source_file, number_of_words_to_output):
    """Main function that opens our file of text."""
    raw_book_file = open(source_file)
    raw_book_string = raw_book_file.read()
    generate_trigrams_output(raw_book_string, number_of_words_to_output)
    raw_book_file.close()


def generate_dictionary_from_source_text(raw_book_string):
    """The function turns our string into a list."""
    dictionary_of_matching_words = {}
    book_word_list = raw_book_string.split()
    for i, word in enumerate(book_word_list):
        if i == len(book_word_list) - 2:
            break
        key = "{} {}".format(word, book_word_list[i + 1])
        value = "{}".format(book_word_list[i + 2])
        if key in dictionary_of_matching_words:
            dictionary_of_matching_words[key].append(value)
        else:
            dictionary_of_matching_words.update({key: [value]})
    return dictionary_of_matching_words


def generate_trigrams_output(raw_book_string, number_of_words_to_output):
    """."""
    dictionary_of_matching_words = generate_dictionary_from_source_text(raw_book_string)
    i = 0
    output = []
    next_key = random.choice(list(dictionary_of_matching_words.keys()))
    output.extend(next_key.split())
    while i <= len(output):
        if next_key not in dictionary_of_matching_words:
            break
        random_value = random.choice(dictionary_of_matching_words[next_key])
        output.append(random_value)
        first_word = output[len(output) - 1]
        second_word = output[len(output) - 2]
        next_key = "{} {}".format(second_word, first_word)
        i += 1

    print(' '.join(output))


def pick_word_in_dictionary(dictionary_of_matching_words):
    """."""
    random_key = random.choice(list(dictionary_of_matching_words.keys()))
    return random.choice(dictionary_of_matching_words[random_key])


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
    # print(sys.argv[0])
    # print(sys.argv[1])
    # print(sys.argv[2])
    # sys.argv # get things from command line
    # stdout # print 200 words of text to this
