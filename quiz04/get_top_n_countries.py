def get_top_n_countries(country_sorted_by_ratio, top_n):
    """ get_top_n_countries
    Arguements: a sorted list [[ratio1, country1], [ratio2, country2], [ratio3, country3] ...]
    Returns: a list with proper printable format, such as
                ['country1 (ratio1)', 'country2 (ratio2)', 'country3 (ratio3)'...]
    """
    countries = []
    # if length of list is less than top_n, then print the entire list
    list_range = min(top_n, len(country_sorted_by_ratio))
    # if ratio is the same, then extend list_range
    while list_range < len(country_sorted_by_ratio):
        if country_sorted_by_ratio[list_range][0] == country_sorted_by_ratio[list_range - 1][0]:
            list_range += 1
        else:
            break
    for i in range(list_range):
        if country_sorted_by_ratio[i]:
            countries.append(
                country_sorted_by_ratio[i][1]
                + ' ('
                + '%.2f' % country_sorted_by_ratio[i][0]
                + ')'
                )
    return countries


# Test Codes
if __name__ == "__main__":
    top_n = 4
    country_sorted_by_ratio = [
        (128.35226732698018, 'Middle East & North Africa'),
        (56.42857142857143, 'Tajikistan'),
        (46.35428571428572, 'Egypt, Arab Rep.'),
        (17.585714285714285, 'Kyrgyz Republic'),
        (17.585714285714285, 'Azerbaijan'),
        (15.585714285714285, 'South Asia')
        ]
    countries = get_top_n_countries(country_sorted_by_ratio, top_n)
    print(countries)
    print('\n'.join(country for country in countries))