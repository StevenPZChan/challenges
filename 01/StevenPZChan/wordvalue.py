from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as f:
        return f.read().splitlines()


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[c] for c in word.upper() if c in LETTER_SCORES])


def max_word_value(word_list = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if word_list == None:
        word_list = load_words()

    return max(word_list, key=calc_word_value)


if __name__ == "__main__":
    print(max_word_value())
