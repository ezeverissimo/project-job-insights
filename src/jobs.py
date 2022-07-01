from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        file_data = csv.reader(file)
        header, *data = file_data
        my_dict = [
            {header[0]: rows[0], header[1]: rows[1], header[2]: rows[2]}
            for rows in data
        ]
    return my_dict


print(read("tests/mocks/jobs.csv"))
