response = [
    ['hello', [
        'Hi, how can I help you today?']],
    ['thank you', [
        'You are welcome.']],
    ['bye', [
        'Bye!']],
]

print('ELIZA: Hi, I am ELIZA.')
terminate_term = 'bye'
utterance = ''
while utterance != terminate_term: # endless conversation until we say the specific term 'bye'
    utterance = input('> ')
    utterance = utterance.lower()

    match = 0 # a flag variable to check if we can match any utterance in the database
    for i in range(len(response)):
        if utterance == response[i][0]:
            print('ELIZA: ', response[i][1][0]) # careful with the indexing in a nested list
            match = 1 # now we can match an utterance
            break # end the loop, because we do not need to search anymore
            # later we will see how to handle multiple matches, but for now just assume that there is only one match
    if not match: # if we cannot match any utterance, return a random response, or you can say "I don't understand" etc
        print('ELIZA: ', response[0][1][0])

# later you will learn how to match more complex patterns with regular expression
