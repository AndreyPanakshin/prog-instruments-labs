import pandas as pd
import numpy as np

def test_descriptive_statistics(mock_excel_data):
    df = mock_excel_data.copy()
    region_rows = df.iloc[2:]  
    year_2005 = region_rows['2005']

    mean_2005 = year_2005.mean()
    assert np.isclose(mean_2005, 48.75), f"Expected 48.75, got {mean_2005}"
