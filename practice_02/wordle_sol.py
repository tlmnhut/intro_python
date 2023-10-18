import argparse

def select_word(count_file, pattern, include_char, exclude_char):
    """
    Select words from a vocabulary file that match specific criteria.
    This function reads a vocabulary file containing words and selects words that meet certain conditions:
    - The word must have the same length as the given pattern.
    - The pattern matches the word in all characters, considering '_' as a wildcard.
    - All characters to be included (include_char) must be present in the word.
    - None of the characters in exclude_char should appear in the word.

    :param count_file: (str): The path to the vocabulary file containing words and their lengths. The vocabulary file
        is assumed to be sorted in descending order of word length.
    :param pattern: (str): The pattern to match against words. '_' is treated as a wildcard.
    :param include_char: (str): A string containing characters that must be present in the selected words.
    :param exclude_char: (str): A string containing characters that must not appear in the selected words.
    :return: list: A list of words that meet all the specified conditions.

    Examples:
        >>> count_file = "vocab_counts.txt"
        >>> pattern = "h__p"
        >>> include_char = "el"
        >>> exclude_char = "zy"
        >>> select_word(count_file, pattern, include_char, exclude_char)
        return: ['help']
    """
    # This solution can be improved with better a strategy, if you are interested in this wordle exercise,
    # you can further improve it

    length = len(pattern) # get word length
    result = [] # the list of words that satisfy all conditions

    with open(count_file, encoding='utf-8') as f:
        # go through each word in the vocab file. pick the words that satisfy all conditions
        for line in f:
            word, word_len = line.strip().split()
            word_len = int(word_len)

            # if the current word length is greater than the target word, skip it and go to the next word
            if word_len > length:
                continue

            # if the current word length is equal to the target word length, we further check other conditions
            elif word_len == length:
                # we need two conditions: first, the pattern must match the current word in all characters,
                # second, all included characters must present in the current word
                count_pattern, count_include = 0, 0
                for i in range(length):
                    if word[i] not in exclude_char: # if a character in the current word is in the excluded list,
                        # we do not need to check this word
                        if pattern[i] == '_' or pattern[i] == word[i]:
                            count_pattern += 1
                        if word[i] in include_char:
                            count_include += 1
                if count_pattern == length and count_include >= len(include_char): # >= because there may be two same
                    # characters in the current word appears in the included list
                    result.append(word)

            # if the current word length is smaller the target word length, we do not need to check anymore,
            # because the vocab file was sorted in descending order
            else:
                break
    return result


if __name__ == '__main__':
    # Solve the Wordle game at https://wordlegame.org/
    # It has multiple languages. You can adjust the word length as well.
    # You may try to play a few times, then you can see that:
    #   gray character: the word does not contain those
    #   yellow character: the word contains this character, but in another position
    #   green character: the word contains this character in the correct position

    # 1. Write a function to help you solve the wordle
    # You can freely design your function as you wish
    # Hint: the previous exercise can help you choose a set of words with a specific number of characters
    # You can read the results of the previous exercise to help you select words

    # I tried and it seems quite tricky for me.
    # Moreover, the vocab lists are limited, there are a lot of words
    # missing in the vocab lists. You may find other better vocab lists on the web.

    lang = 'english'
    word_search = select_word(count_file=f'./results/{lang}_count.txt',
                              pattern='____r__', # green
                              include_char='ona', # yellow, the order of characters does not matter
                              exclude_char='ctjulpgm') # gray, the order of characters does not matter
    for w in word_search:
        print(w)

    # 2. When you finish it, use argparse lib to run the script from the terminal.
    parser = argparse.ArgumentParser(description="Select words from a vocabulary file that match specific criteria.")
    parser.add_argument("-l", "--lang", help="Language of the vocabulary file containing words and their lengths.",
                        default='english')
    parser.add_argument("-p", "--pattern", help="The pattern to match against words. '_' is treated as a wildcard.",
                        default="_______") # default 7 characters
    parser.add_argument("-i" ,"--include_char", help="Characters that must be present in the selected words.", default="")
    parser.add_argument("-e" ,"--exclude_char", help="Characters that must not appear in the selected words.", default="")
    args = parser.parse_args()

    # Example of calling from terminal: python wordle_sol.py -l english -p h__p -i el -e zy
    result = select_word(count_file=f'./results/{args.lang}_count.txt',
                         pattern=args.pattern,
                         include_char=args.include_char,
                         exclude_char=args.exclude_char)
    for w in result:
        print(w)
