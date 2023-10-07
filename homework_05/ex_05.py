# method 1
def select_palindromes_v1(list_of_words):
    # The text in the quotes below is a "docstring". It describes the purpose of the function,
    # inputs, outputs, sometimes a few examples of how to use the function. Here I used PyCharm to generate
    # the docstring structure, then used ChatGPT to generate the docstring content and then post-edited it.
    """
    Select palindromic words from a list of words.
    :param list_of_words: list of str. A list of words to search for palindromes.
    :return: list of str. A list containing the palindromic words found in the input list.
    """
    palindrome_list = []
    for word in list_of_words:
        if word == word[::-1] and len(word) > 1:
            palindrome_list.append(word)
    return palindrome_list


# method 2
def is_palindrome(word):
    """
    Check if a word is a palindrome.
    :param word: str. The word to be checked for palindrome status.
    :return: bool. True if the word is a palindrome, False otherwise.
    """
    return word == word[::-1] and len(word) > 1


if __name__ == '__main__':
    word_list = ['a', 'palindrome', 'is', 'a', 'word', 'sentence', 'verse', 'or', 'even', 'number', 'that', 'reads',
                 'the', 'same', 'backward', 'or', 'forward', 'for', 'example', 'kayak', 'deified', 'rotator', 'repaper',
                 'deed', 'peep', 'wow', 'noon', 'civic', 'racecar', 'level', 'mom']

    # A: the function takes one argument, which is a list of words
    palindromes_1 = select_palindromes_v1(word_list)
    print(palindromes_1)

    # B: the function takes one argument, which is a single word
    palindromes_2 = []
    for word in word_list:
        if is_palindrome(word):
            palindromes_2.append(word)
    print(palindromes_2)
