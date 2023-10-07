# Declare "database" as a global variable
# I realized that "response" was a bad name, so I changed it to "database"
database = [
    ['hello', [
        'Hi, how can I help you today?']],
    ['thank you', [
        'You are welcome.']],
    ['bye', [
        'Bye!']],
]


def find_utterance(utterance):
    """
    Find a response based on an input utterance.
    :param utterance: (str): The user input utterance to search for in the database.
    :return: (str): The response associated with the matching utterance,
                    or the default response if no match is found.
    """
    utterance = utterance.lower()
    response = database[0][1][0] # default response
    for i in range(len(database)):
        if utterance == database[i][0]:
            response = database[i][1][0]
            break # no need to search anymore
    return response


if __name__ == '__main__':
    print('ELIZA: Hi, I am ELIZA.')
    terminate_term = 'bye'
    user_utterance = ''
    while user_utterance != terminate_term:
        user_utterance = input('> ')
        response = find_utterance(user_utterance)
        print('ELIZA: ', response)

# now the script is in good shape
