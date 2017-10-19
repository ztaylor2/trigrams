"""Run trygrams algoritm on a text file."""

import random


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
    dictionary_of_matching_words = generate_dictionary_from_source_text(raw_book_string)
    pick_word_in_dictionary(dictionary_of_matching_words)


def pick_word_in_dictionary(dictionary_of_matching_words):
    random_key = random.choice(list(dictionary_of_matching_words.keys()))
    print(random.choice(dictionary_of_matching_words[random_key]))




"""Try to keep your code well-factored by creating functions to exe
cute discreet steps of the processing. You might have one function t
hat processes the input into your trigram source. Perhaps there is ano
ther that is responsible for selecting a new word, given a pair of inp
ut words. Maybe there are others.

Create a main function which implements the core of your algo
rithm. It should take two arguments, the path to a source fil
e and an integer representing the number of words to generate.

Try to keep your code well-factored by creating functions to exe
cute discreet steps of the processing. You might have one functio
n that processes the input into your trigram source. Perhaps there
'is another that is responsible for selecting a new word, given a pair
 of input words. Maybe there are others.





if __name__ == '__main__':

    sys.argv

    If you install any additional Python packages (like pytest)
     to accomplish your work, make sure you use pip freeze to cre
    ate a requirements.pip file and include it in your repository.
"""
