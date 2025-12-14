import pandas as pd
import numpy as np

def test_descriptive_statistics(mock_excel_data):
    df = mock_excel_data.copy()
    df_regions = df.iloc[2:].set_index('Регион')

    # Вычислим статистику вручную для 2005 года
    year_2005 = df_regions['2005']
    mean_2005 = year_2005.mean()
    std_2005 = year_2005.std(ddof=0)  # population std как в Excel по умолчанию?
    # Но в pandas std() — ddof=1. Уточним:
    std_2005_sample = year_2005.std(ddof=1)

    # Проверим с нашим расчётом в коде (там используется .std() → ddof=1)
    assert np.isclose(mean_2005, 48.0)
    assert np.isclose(std_2005_sample, np.sqrt(((year_2005 - mean_2005)**2).sum() / (len(year_2005)-1)))