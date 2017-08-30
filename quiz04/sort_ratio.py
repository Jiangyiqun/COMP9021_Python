from get_valid_data import get_valid_data
from get_ratio import get_ratio
from get_top_n_countries import get_top_n_countries

def sort_ratio(courtry_with_ratio):
    """ sort_ratio
    Arguements: an unsorted list[(ratio1, country1), (ratio2, country2), (ratio3, country3) ...]
    Returns: A list sorted by ratio. If two countries have same ratio, then sort by countries' name.
             Such as: [[ratio1, country1], [ratio2, country2], [ratio3, country3] ...]
    """
    counry_sorted_by_ratio = sorted(courtry_with_ratio, key=lambda tup: (-tup[0], tup[1]))
    return counry_sorted_by_ratio


# Test Codes
if __name__ == "__main__":
    agricultural_land_filename = 'API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv'
    forest_filename = 'API_AG.LND.FRST.K2_DS2_en_csv_v2.csv'
    year_1 = 1992
    year_2 = 1999
    agricultural = get_valid_data(agricultural_land_filename, year_1, year_2)
    forest = get_valid_data(forest_filename, year_1, year_2)
    country_with_ratio = get_ratio(agricultural, forest)
    print(sort_ratio(country_with_ratio))
