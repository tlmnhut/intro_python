def convert_percentage(percentage_list, is_higher):
    """
    Convert the percentages from higher to lower, or vice versa.
    :param percentage_list: (list of float): A list of percentages to be converted.
    :param is_higher: (list of int 0 1): A list of binary indicators where 1 means that the corresponding
            percentage in percentage_list represents a higher value in city_a compared to city_b, and
            0 means it represents a lower value.
    :return: list of float: A list containing the converted percentages.
    """
    comp_percent_convert = []
    for i in range(len(is_higher)):
        if is_higher[i]:
            comp_percent_convert.append((1 - 1 / (1 + percentage_list[i] / 100)) * 100)
        else:
            comp_percent_convert.append((1/(1 - percentage_list[i]/100) - 1) * 100)
    return comp_percent_convert


def result_format(city_a, city_b, percentage_list, is_higher):
    """
    Create the formatted text to compare cost of living in the two cities.
    :param city_a: (str): The name of the first city.
    :param city_b: (str): The name of the second city.
    :param percentage_list: (list of float): A list of percentage differences for different factors.
    :param is_higher: (list of int 0 1): A list of binary indicators where 1 means that the corresponding
            percentage in percentage_list represents a higher value in city_a compared to city_b, and
            0 means it represents a lower value.
    :return: A formatted text containing the comparison of various factors between the two cities.
    """
    # round the results
    round_results = [round(percent, 1) for percent in percentage_list]

    # if is_higher[0] is 0, then we can retrieve the term "higher" by higher_lower[0]
    higher_lower = ['higher', 'lower']
    lh_convert = [higher_lower[i] for i in is_higher]

    conversion_text = f"""
        Consumer Prices in {city_b} are {round_results[0]}% {lh_convert[0]} than in {city_a} (without rent)
        Consumer Prices Including Rent in {city_b} are {round_results[1]}% {lh_convert[1]} than in {city_a}
        Rent Prices in {city_b} are {round_results[2]}% {lh_convert[2]} than in {city_a}
        Restaurant Prices in {city_b} are {round_results[3]}% {lh_convert[3]} than in {city_a}
        Groceries Prices in {city_b} are {round_results[4]}% {lh_convert[4]} than in {city_a}
        Local Purchasing Power in {city_b} is {round_results[5]}% {lh_convert[5]} than in {city_a}
        """
    return conversion_text


if __name__ == '__main__':
    city_A = 'Bolzano-Bozen'
    city_B = 'Milan'

    # data retrieved on Otc 3 2023
    # comp_percent = [consumer_AB, consumer_rent_AB, rent_AB, restaurant_AB, grocery_AB, lpp_AB]
    comp_percent = [8.9, 20.6, 42.8, 13.6, 9.6, 50.6]
    is_higher = [0, 0, 0, 0, 0, 1]

    # first convert the percentage
    convert_results = convert_percentage(percentage_list=comp_percent, is_higher=is_higher)

    # then format the text
    final_text = result_format(city_a=city_A, # if the list of params are too long, you can use one line for each param
                               city_b=city_B,
                               percentage_list=convert_results,
                               is_higher=is_higher)

    # print the results
    print(final_text)

    # now the script is much more manageable
