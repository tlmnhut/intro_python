response = [
    ['hello', [
        'Hi, how can I help you today?']],
    ['thank you', [
        'You are welcome.']],
    ['bye', [
        'Bye!']],
]

print('Hi, I am ELIZA.')
utterance = input('> ')
utterance = utterance.lower()
if utterance == response[0][0]:
    print('ELIZA: ', response[0][1][0]) # careful with the indexing in a nested list
elif utterance == response[1][0]:
    print('ELIZA: ', response[1][1][0])
elif utterance == response[2][0]:
    print('ELIZA: ', response[2][1][0])
else: # does not match anything
    print('ELIZA: ', response[0][1][0]) # return a random response, or you can say "I don't understand" etc

# later you will learn how to match more complex patterns with regular expression
