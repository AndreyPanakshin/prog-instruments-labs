import csv
from checksum import calculate_checksum, serialize_result
from consts import *

def load_data(file_path: str, delimiter: str = CSV_DELIMITER):
    """Reads CSV and returns a list of strings."""
    with open(file_path, "r", encoding=FILE_ENCODING, newline="") as file:
        reader = csv.reader(file, delimiter=delimiter)
        return list(reader)


def validate_row(row: list[str], patterns: list[re.Pattern]) -> bool:
    """Checks one string for compliance with all patterns."""
    if len(row) != len(patterns):
        return False
    return all(pattern.fullmatch(value.strip()) for pattern, value in zip(patterns, row))