import re

EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
HEIGHT_PATTERN = r"^[0-2]\.\d{2}$"
SNILS_PATTERN = r"^\\d{11}$"
PASSPORT_PATTERN = r"^\d{2} \d{2} \d{6}$"
OCCUPATION_PATTERN = r"^[a-zA-Zа-яА-ЯёЁ\s-]+$"
LONGITUDE_PATTERN = r"^-?(?:180(?:\\.0+)?|1[0-7][0-9](?:\\.[0-9]+)?|[0-9]{1,2}(?:\\.[0-9]+)?)$"
HEX_COLOR_PATTERN = r"^#[0-9a-fA-F]{6}$"
ISSN_PATTERN = r"^\d{4}-\d{3}[\dX]$"
LOCALE_PATTERN = r"^[a-z]{2}(?:-[A-Za-z]{2,})?$"
TIME_PATTERN = r"^(?:[01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](?:\.[0-9]{1,6})?$"

DEFAULT_FILE_PATH = "75.csv"
DEFAULT_VARIANT = 75
FILE_ENCODING = "utf-16"
CSV_DELIMITER = ";"

def get_validation_patterns() -> list[re.Pattern]:
    """Returns a list of compiled templates for verification."""
    patterns = [
        EMAIL_PATTERN,
        HEIGHT_PATTERN,
        SNILS_PATTERN,
        PASSPORT_PATTERN,
        OCCUPATION_PATTERN,
        LONGITUDE_PATTERN,
        HEX_COLOR_PATTERN,
        ISSN_PATTERN,
        LOCALE_PATTERN,
        TIME_PATTERN
    ]
    return [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
