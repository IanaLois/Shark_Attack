import random
from words import word_list

def new_word():
    """
    Retrieves a new randomised word from the imported word list
    """
    random_word = random.choice(word_list)
    return random_word.upper()