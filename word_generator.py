"""
Word Generator for Hangman Game
By: Suryakiran Santhosh
"""


from random import randint


def word_generator() -> str:
    """
    return a random word(string type) from a long list of words
    """

    # randomly generate a number in the range of the line number
    line_number = randint(a=1, b=854)
    counter = 0

    # open file with words
    with open(file="words.txt", mode="r") as file:
        for line in file.readlines():
            if counter == line_number:
                return line.rstrip("\n").lstrip(" ")
            counter += 1
