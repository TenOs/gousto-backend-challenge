from typing import List
import csv


def load_csv_data(filename: str) -> List[dict]:
    """
    Reads and loads csv data

    :param filename: filename to read
    :return: list of dictionaries
    """
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        return [dict(row) for row in csv_reader]
