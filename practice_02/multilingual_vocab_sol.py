
def count_char(vocab_file, save_file=None):
    count = {}
    total_char = 0
    with open(vocab_file) as f:
        for line in f:
            word = line.strip()
            num_char = len(word)
            count[word] = num_char
            total_char += num_char

    count_sorted = sorted(count.items(), key=lambda kv: kv[1])[::-1]
    avg_char = total_char / len(count)

    if save_file:
        with open(save_file, 'w') as f:
            for word_count in count_sorted:
                f.write(word_count[0] + ' ' + str(word_count[1]) + '\n')

    return count_sorted, avg_char


if __name__ == '__main__':
    languages = ['english', 'italian', 'vietnamese']
    for lang in languages:
        count, avg_char = count_char(vocab_file=f'./vocab_data/{lang}.txt',
                                     save_file=f'./results/{lang}_count.txt')
        print(lang, avg_char)
