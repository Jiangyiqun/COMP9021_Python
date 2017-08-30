from collections import defaultdict
from get_valid_data import get_valid_data

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


# Test Codes
if __name__ == "__main__":
    agricultural_land_filename = 'API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv'
    forest_filename = 'API_AG.LND.FRST.K2_DS2_en_csv_v2.csv'
    year_1 = 1992
    year_2 = 1999
    agricultural = get_valid_data(agricultural_land_filename, year_1, year_2)
    forest = get_valid_data(forest_filename, year_1, year_2)
    print(get_ratio(agricultural, forest))
