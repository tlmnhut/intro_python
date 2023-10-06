# A
word_list = ['a', 'palindrome', 'is', 'a', 'word', 'sentence', 'verse', 'or', 'even', 'number',
             'that', 'reads', 'the', 'same', 'backward', 'or', 'forward', 'for', 'example',
             'kayak', 'deified', 'rotator', 'repaper', 'deed', 'peep', 'wow', 'noon', 'civic',
             'racecar', 'level', 'mom']
palindrome_list, not_palindrome_list = [], []
for word in word_list:
    if word == word[::-1]:
        palindrome_list.append(word)
    else:
        not_palindrome_list.append(word)
print('palindromes:', palindrome_list)
print('not palindromes:', not_palindrome_list)

# if you do not consider a word consisting of only a single character is a palindrome (since it is trivial):
palindrome_list, not_palindrome_list = [], []
for word in word_list:
    if word == word[::-1] and len(word) > 1: # must be more than 1 character
        palindrome_list.append(word)
    else:
        not_palindrome_list.append(word)
print('palindromes, more than one character:', palindrome_list)
print('not palindromes:', not_palindrome_list)

# if you want to remove duplicate words
palindrome_set = set(palindrome_list)
not_palindrome_set = set(not_palindrome_list)
print('palindromes, more than one character, non-duplicate:', palindrome_set)
print('not palindromes, non-duplicate:', not_palindrome_set)
print('\n')

# B
name_list = ['Achille', 'Adamo', 'Adelmo', 'Adeodatus', 'Adriano', 'Andrea', 'Afonso', 'Adelasia',
             'Adele', 'Adriana', 'Agnese', 'Albina', 'Alessandra', 'Alessia', 'Fiore', 'Loreto']
o_list, a_list, the_rest_list = [], [], []
for name in name_list:
    if name[-1] == 'o':
        o_list.append(name)
    elif name[-1] == 'a':
        a_list.append(name)
    else:
        the_rest_list.append(name)
print('names ending with o:', o_list)
print('names ending with a:', a_list)
print('other names:', the_rest_list)
print('\n')

# C
# m: masculine name, f: feminine name, u: unisex name
categories = ['m', 'm', 'm', 'm', 'm', 'u', 'm', 'f', 'f', 'f', 'f', 'f', 'f', 'f', 'u', 'u']
mas_list, fem_list, uni_list = [], [], []
for i in range(len(categories)): # use the index, not the item
    if categories[i] == 'm':
        mas_list.append(name_list[i]) # then use the same index to select the name
    elif categories[i] == 'f':
        fem_list.append(name_list[i])
    elif categories[i] == 'u':
        uni_list.append(name_list[i])
    else: # you can use else to add unisex names, but I prefer using else to do nothing for now.
    # suppose that in the future we see another category, e.g. 'unk' for unknown, then we can avoid adding 'unk'
    # to the unisex category. It is not similar to the case of palindromes - not palindromes, since a word is either
    # a palindrome or not a palindrome, there is no the third case.
        pass # do nothing
print('masculine names:', mas_list)
print('feminine names:', fem_list)
print('unisex names:', uni_list)
