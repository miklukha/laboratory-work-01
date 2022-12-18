# Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc.
# Determine the required attributes-data and attributes-methods in class for working with the text file.

import re


class TextInfo:
    data = None
    words = []

    def __init__(self, filename):
        self.filename = filename

    def open_file(self):
        with open(self.filename, 'r') as file:
            self.data = file.read()
            self.words = re.split(' |, |:|- |\. |\.', self.data)
            return self.data

    def count_number_of_characters(self):
        number_of_characters = 0
        for x in self.words:
            number_of_characters += len(x)
        return number_of_characters

    def count_number_of_words(self):
        return len(self.words) - 1

    def count_number_of_numbers(self):
        number_of_numbers = 0

        for word in self.words:
            if word.isnumeric():
                number_of_numbers += 1
            else:
                continue
        return number_of_numbers

    def count_number_of_sentences(self):
        sentences = self.data.split('.')
        return len(sentences) - 1

    def text_info(self):
        print("Text info:")
        print(f"Text: {self.open_file()}")
        print(f"Numbers of characters: {self.count_number_of_characters()}")
        print(f"Numbers of words: {self.count_number_of_words()}")
        print(f"Numbers of numbers: {self.count_number_of_numbers()}")
        print(f"Numbers of sentences: {self.count_number_of_sentences()}")


word = TextInfo('text.txt')
word.text_info()