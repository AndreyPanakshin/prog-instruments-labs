import pandas as pd
import pytest


@pytest.fixture
def mock_excel_data():
    """Return a mock DataFrame resembling real Excel regional statistics.

    Contains data for:
    - 'Российская Федерация'
    - 'Сибирский федеральный округ'
    - Four republics: Altai, Buryatia, Tuva, Khakassia
    Years: 2005–2021 (selected years)

    Returns
    -------
    pd.DataFrame
        Mock dataset with 'Регион' and yearly columns.
    """
    data = {
        "Регион": [
            "Российская Федерация",
            "Сибирский федеральный округ",
            "Республика Алтай",
            "Республика Бурятия",
            "Республика Тыва",
            "Республика Хакасия",
        ],
        "2005": [48.6, 51.6, 45.0, 50.0, 48.0, 52.0],
        "2010": [50.1, 52.4, 47.0, 51.0, 50.0, 53.0],
        "2015": [45.9, 47.0, 42.0, 46.0, 44.0, 48.0],
        "2019": [48.7, 48.8, 46.0, 48.0, 47.0, 50.0],
        "2020": [50.4, 49.2, 47.5, 49.5, 48.0, 51.0],
        "2021": [51.0, 49.4, 48.0, 50.0, 48.5, 51.5],
    }
    return pd.DataFrame(data)
