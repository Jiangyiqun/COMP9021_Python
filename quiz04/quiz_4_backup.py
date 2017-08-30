# Uses data available at http://data.worldbank.org/indicator
# on Forest area (sq. km) and Agricultural land area (sq. km).
# Prompts the user for two distinct years between 1990 and 2004
# as well as for a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area has increased from oldest input year to most recent input year;
# - forest area has increased from oldest input year to most recent input year;
# - the ratio of increase in agricultural land area to increase in forest area determines
#   output order.
# Countries are output from those whose ratio is largest to those whose ratio is smallest.
# In the unlikely case where many countries share the same ratio, countries are output in
# lexicographic order.
# In case fewer than N countries are found, only that number of countries is output.


# Written by Jack (z5129432) and Eric Martin for COMP9021


import sys
import os
import csv
from collections import defaultdict


agricultural_land_filename = 'API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv'
if not os.path.exists(agricultural_land_filename):
    print(f'No file named {agricultural_land_filename} in working directory, giving up...')
    sys.exit()
forest_filename = 'API_AG.LND.FRST.K2_DS2_en_csv_v2.csv'
if not os.path.exists(forest_filename):
    print(f'No file named {forest_filename} in working directory, giving up...')
    sys.exit()
try:
    years = {int(year) for year in
                           input('Input two distinct years in the range 1990 -- 2014: ').split('--')
            }
    if len(years) != 2 or any(year < 1990 or year > 2014 for year in years):
        raise ValueError
except ValueError:
    print('Not a valid range of years, giving up...')
    sys.exit()
try:
    top_n = int(input('Input a strictly positive integer: '))
    if top_n < 0:
        raise ValueError
except ValueError:
    print('Not a valid number, giving up...')
    sys.exit()


countries = []
year_1, year_2 = None, None

############################## Jack's code starts here ##############################
def get_ratio(data_table_1, data_table_2):
    """ get_ratio
Get ratio which is amount1 / amount2
    Arguements: two dictionaries, {country1: amount1, country2, amount2...}
    Returns: an unsorted list[(ratio1, country1), (ratio2, country2), (ratio3, country3) ...]
    """
    country_with_ratio = []
    for country in data_table_1.keys():
        if country in data_table_2.keys():
            country_with_ratio.append((data_table_1[country] / data_table_2[country], country))
    return country_with_ratio

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
    print(list_range)
    print(len(country_sorted_by_ratio))
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

def get_valid_data(csv_file_name, year_1, year_2):
    """ function
Read and handle csv files.
    Arguements: a string of csv file name, such as 'API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv'
    Returns: a dictionary with counries' names and their increase of amount
            {country1: increase amount from year1 to year2, country2: increase amount from year1 to year2...}
    Description:
            because row[4] is for 1960, therefore row[year - 1956] is the correct data
    """
    valid_data = defaultdict()
    with open(csv_file_name, "r", encoding = 'utf-8') as csv_file:
        csv_table = csv.reader(csv_file)
        for row in csv_table:
            if len(row) == 62:  # this row is not an empty line before valid data
                if row[year_2 - 1956] and row[year_1 - 1956]: # if data on these two years exsit
                    if float(row[year_2 - 1956]) > float(row[year_1 - 1956]): # if it is strict increase between two years
                        valid_data[row[0]] = float(row[year_2 - 1956]) - float(row[year_1 - 1956])
        del valid_data['Country Name']
    return valid_data

def sort_ratio(courtry_with_ratio):
    """ sort_ratio
    Arguements: an unsorted list[(ratio1, country1), (ratio2, country2), (ratio3, country3) ...]
    Returns: A list sorted by ratio. If two countries have same ratio, then sort by countries' name.
             Such as: [[ratio1, country1], [ratio2, country2], [ratio3, country3] ...]
    """
    counry_sorted_by_ratio = sorted(courtry_with_ratio, key=lambda tup: (-tup[0], tup[1]))
    return counry_sorted_by_ratio

# calculate year_1 and year_2
years = list(years)
years.sort()
year_1 = years[0]
year_2 = years[1]
# main
agricultural = get_valid_data(agricultural_land_filename, year_1, year_2)
forest = get_valid_data(forest_filename, year_1, year_2)
country_with_ratio = get_ratio(agricultural, forest)
counry_sorted_by_ratio = sort_ratio(country_with_ratio)
countries = get_top_n_countries(counry_sorted_by_ratio, top_n)


############################### Jack's code ends here ###############################

print(f'Here are the top {top_n} countries or categories where, between {year_1} and {year_2},\n'
      '  agricultural land and forest land areas have both strictly increased,\n'
      '  listed from the countries where the ratio of agricultural land area increase\n'
      '  to forest area increase is largest, to those where that ratio is smallest:')
print('\n'.join(country for country in countries))
