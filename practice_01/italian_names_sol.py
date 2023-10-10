def count_freq(input_list):
    """
    Count the frequency of elements in a list.
    :param input_list: (list): The list of elements to be counted.
    :return: (dict): A dictionary where keys are unique elements from the input list, and values
              are the corresponding frequencies.
    """
    count = {}
    for item in input_list:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count


if __name__ == '__main__':
    names = ['Marco Polo', 'Stefani Germanotta', 'Alessandro Volta', 'Gianluigi Buffon', 'Galileo Galilei',
             'Enrico Fermi', 'Leonardo DiCaprio', 'Jorge Bergoglio', 'Luciano Pavarotti', 'Samantha Cristoforetti']
    years_birth = [1254, 1986, 1745, 1978, 1564,
                   1901, 1974, 1936, 1935, 1977]
    years_death = [1324, None, 1827, None, 1642,
                   1954, None, None, 2007, None]
    professions = ['explorer', 'singer', 'physicist', 'footballer', 'physicist',
                   'physicist', 'actor', 'pope', 'singer', 'astronaut']
    nationalities = ['Italian', 'American', 'Italian', 'Italian', 'Italian',
                     'Italian-American', 'American', 'Argentine', 'Italian', 'Italian']

    # 1. Write a function to count the frequencies of professions and nationalities
    count_professions = count_freq(professions)
    print(count_professions)
    count_nationalities = count_freq(nationalities)
    print(count_nationalities)

    # 2. Determine the individual who, among those deceased, had the longest lifespan.
    lifespan_deceased = []
    for i in range(len(years_death)):
        if years_death[i] is not None:
            lifespan_deceased.append(years_death[i] - years_birth[i])
        else:
            lifespan_deceased.append(-1)  # a trick to keep the length of result list unchanged
    print(lifespan_deceased)
    longest_age = max(lifespan_deceased)
    longest_age_idx = lifespan_deceased.index(longest_age) # get the index of the largest element
    print(names[longest_age_idx])

    # 3. Convert all the existing lists into a new data structure: a list of dictionaries. Each dictionary should have
    # the following structure: {'name': 'abc', 'year_birth': 1234, 'year_death': 5678, 'profession': 'ijk', 'nationality': 'XYZ'}
    dict_struct = []
    for i in range(len(names)):
        new_dict = {'name': names[i],
                    'year_birth': years_birth[i],
                    'year_death': years_death[i],
                    'profession': professions[i],
                    'nationality': nationalities[i]}
        dict_struct.append(new_dict)
    print(dict_struct)

    # 4. Use the created dict to identify the youngest living individual among them.
    age_living = []
    for record in dict_struct:
        if record['year_death'] is not None:
            age_living.append(9999) # a trick to keep the length of result list unchanged
        else:
            age_living.append(2023 - record['year_birth'])
    print(age_living)
    youngest_age = min(age_living)
    youngest_age_idx = age_living.index(youngest_age)
    print(names[youngest_age_idx])
