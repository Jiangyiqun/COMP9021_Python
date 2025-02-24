import csv
from collections import defaultdict

def get_valid_data(csv_file_name, year_1, year_2):
    """ get_valid_data
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


# Test Codes
if __name__ == "__main__":
    agricultural_land_filename = 'API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv'
    forest_filename = 'API_AG.LND.FRST.K2_DS2_en_csv_v2.csv'
    year_1 = 1992
    year_2 = 1999
    print(get_valid_data(agricultural_land_filename, year_1, year_2))
    