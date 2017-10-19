"""This module will create a function that will take the first 2 words from a given block of text and return the immediately following word in all possible places."""


def main(source_file, number_of_words_to_output):
    """Main function that opens our file of text."""
    raw_book_file = open(source_file)
    raw_book_string = raw_book_file.read()
    generate_dictionary_from_source_text(raw_book_string)
    print(raw_book_file.read(), 100)
    raw_book_file.close()


def generate_dictionary_from_source_text(raw_book_string):
    """The function turns our string into a list."""
    book_word_list = raw_book_string.split()
    print(book_word_list)





"""Try to keep your code well-factored by creating functions to execute discreet steps of the processing. You might have one function that processes the input into your trigram source. Perhaps there is another that is responsible for selecting a new word, given a pair of input words. Maybe there are others.

Create a main function which implements the core of your algorithm. It should take two arguments, the path to a source file and an integer representing the number of words to generate.

Try to keep your code well-factored by creating functions to execute discreet steps of the processing. You might have one function that processes the input into your trigram source. Perhaps there is another that is responsible for selecting a new word, given a pair of input words. Maybe there are others.





if __name__ == '__main__': 

	sys.argv

	If you install any additional Python packages (like pytest) to accomplish your work, make sure you use pip freeze to create a requirements.pip file and include it in your repository.
"""
