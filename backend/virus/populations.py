import csv


def list_of_years():
    """Returns a list of all possible years for which the population is known for all countries."""
    with open('csvs/API_SP.POP.TOTL_DS2_en_csv_v2_1120881.csv') as csv_year_list:
        csv_reader = csv.reader(csv_year_list, delimiter=',')
        row_count = 0
        column_count = 0
        year_list = []
        for i in csv_reader:
            if row_count == 2:
                for j in i:
                    if 3 < column_count < 64:
                        year_list.append(j)
                    column_count += 1
            row_count += 1
        return year_list


def list_of_countries():
    """Returns a list of all possible countries where the population is known for all years."""
    with open('csvs/API_SP.POP.TOTL_DS2_en_csv_v2_1120881.csv') as csv_country_list:
        csv_reader = csv.reader(csv_country_list, delimiter=',')
        line_count = 0
        country_list = []
        for i in csv_reader:
            if 2 < line_count < 267:
                country_list.append(i[0])
            line_count += 1
        return country_list

def world_population(country_year):
    """Returns the population corresponding to the given country and year."""
    country = country_year[0]
    year = country_year[1]
    with open('csvs/API_SP.POP.TOTL_DS2_en_csv_v2_1120881.csv') as csv_world_population:
        csv_reader = csv.reader(csv_world_population, delimiter=',')
        line_count = 0
        for i in csv_reader:
            if line_count == 2:
                column = int(i.index(year))
            if i[0] == country:
                row = i
            line_count += 1
        return int(row[column-1])
