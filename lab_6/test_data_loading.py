import pandas as pd
import numpy as np

def test_data_loading_structure(mock_excel_data):
    df = mock_excel_data.copy()
    df.set_index('Регион', inplace=True)

    russia_data = df.loc['Российская Федерация'].values
    sfo_data = df.loc['Сибирский федеральный округ'].values
    regions_data = df.iloc[2:].copy()

    # Проверяем, что данные выделены верно
    assert len(russia_data) == 6
    assert len(sfo_data) == 6
    assert regions_data.shape == (4, 6)

    # Проверяем конкретные значения (регрессионная защита)
    np.testing.assert_array_almost_equal(russia_data, [48.6, 50.1, 45.9, 48.7, 50.4, 51.0])
    np.testing.assert_array_almost_equal(sfo_data, [51.6, 52.4, 47.0, 48.8, 49.2, 49.4])
    assert list(regions_data.index) == [
        'Республика Алтай', 'Республика Бурятия',
        'Республика Тыва', 'Республика Хакасия'
    ]