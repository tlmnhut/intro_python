import os
import argparse

def count_char(vocab_file, save_file=None):
    """
    Count the number of characters in each word from a vocabulary file.
    This function reads a vocabulary file, where each line represents a word, and counts
    the number of characters in each word. It returns a list of word-character count pairs,
    sorted in descending order of character count. Additionally, it calculates the average
    number of characters in the words.

    :param vocab_file: (str): The path to the vocabulary file containing words, with one word per line.
    :param save_file: (str, optional): If provided, the function will save the word-character
            count pairs to a file with the given name.
    :return: tuple of (list of tuples, float): the first element consists of a list of word and its
            corresponding character count. The list is sorted in descending order of character
            count. The second element is the average of character count.
    """
    count = {}
    total_char = 0
    # the encoding='utf-8' may be useful to read characters in some languages
    # we may need it when the character is a non-latin character
    with open(vocab_file, encoding='utf-8') as f:
        for line in f:
            word = line.strip()
            num_char = len(word)
            count[word] = num_char
            total_char += num_char

    # # In some cases, the code above skips the first line in the files,
    # # please check if it happens in your case. If it does, we change the strategy: first, we
    # # read the entire file, then we start to split the entire files to get a list of vocabs
    # with open(vocab_file) as f:
    #     all_words = f.read()
    # all_words = all_words.split()
    # for word in all_words:
    #     count[word] = len(word)
    #     total_char += len(word)

    count_sorted = sorted(count.items(), key=lambda kv: kv[1])[::-1] # sort the dict by values
    avg_char = total_char / len(count)

    if save_file:
        with open(save_file, mode='w', encoding="utf-8") as f:
            for word_count in count_sorted:
                f.write(word_count[0] + ' ' + str(word_count[1]) + '\n')

    return count_sorted, avg_char


if __name__ == '__main__':
    # 1. Go to https://github.com/oprogramador/most-common-words-by-language/tree/master/src/resources
    # and download a few vocab files.
    languages = ['english', 'italian']

    # 2. Read a vocab file, count the number of characters in each word
    # Write the results in a new file with the format:
    #       word_1 length_of_word_1
    #       word_2 length_of_word_2
    #       ... ...
    # You should write a function to do that

    # 3. Use the function above to do the same thing for other vocab files
    # Then, you can just open the result files to see what word is longest for each language

    # 4. Modify the function above to return the average number of characters in a word for each language
    # Then you can see among the languages you chose, which language has more characters per word
    for lang in languages:
        count, avg_char = count_char(vocab_file=f'./vocab_data/{lang}.txt',
                                     save_file=f'./results/{lang}_count.txt')
        print(lang, avg_char)

    # 5. Use argparse to run the script from the terminal
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang', default='english')
    args = parser.parse_args()
    lang = args.lang
    print(lang)
    # In the terminal, now you can call: python multilingual_vocab_sol.py --lang italian
    # It can only take one language though

    # 6. Extra: imagine you have 100 vocab lists in your folder, how can you read all of them without
    # manually input each file name?
    all_files = os.listdir('./vocab_data')
    print(all_files) # ['english.txt', 'italian.txt', ...]
    # then you can iterate through the list:
    for file in all_files:
        lang = file.replace('.txt', '') # delete the .txt extension
        # do something
