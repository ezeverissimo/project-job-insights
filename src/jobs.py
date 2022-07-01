from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        my_dict = csv.DictReader(file)

        return list(my_dict)
