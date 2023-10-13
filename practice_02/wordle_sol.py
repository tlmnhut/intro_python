
def select_word(count_file, pattern, include_char, exclude_char):
    length = len(pattern)
    result = []

    with open(count_file) as f:
        for line in f:
            word, word_len = line.strip().split()
            word_len = int(word_len)

            if word_len > length:
                continue

            elif word_len == length:
                count_pattern, count_include = 0, 0
                for i in range(length):
                    if word[i] not in exclude_char:
                        if pattern[i] == '_' or pattern[i] == word[i]:
                            count_pattern += 1
                        if word[i] in include_char:
                            count_include += 1
                if count_pattern == length and count_include >= len(include_char):
                    result.append(word)

            else:
                break
    return result


if __name__ == '__main__':
    word_search = select_word(count_file='./results/english_count.txt',
                              pattern='we_s___',
                              include_char='it',
                              exclude_char='codlngprvab')
    for w in word_search:
        print(w)
