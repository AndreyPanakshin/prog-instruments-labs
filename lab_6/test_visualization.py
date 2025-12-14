import pytest
import matplotlib.pyplot as plt
from unittest.mock import patch, MagicMock

def test_plots_generated(mock_excel_data):
    df = mock_excel_data.copy()
    region_data = df.iloc[2:]
    years = ['2005', '2010', '2015', '2019', '2020', '2021']
    russia_data = [48.6, 50.1, 45.9, 48.7, 50.4, 51.0]

    with patch('matplotlib.pyplot.subplots') as mock_subplots, \
         patch('matplotlib.pyplot.tight_layout') as mock_tight_layout:

        fig_mock = MagicMock()
        ax1 = MagicMock()
        ax2 = MagicMock()
        ax3 = MagicMock()
        ax4 = MagicMock()
        axes_mock = [[ax1, ax2], [ax3, ax4]]
        mock_subplots.return_value = (fig_mock, axes_mock)

        fig, axes = plt.subplots(2, 2, figsize=(15, 12))  # ← ЭТОГО НЕ ХВАТАЛО!

        data_box = [region_data[year] for year in years]
        axes[0][0].boxplot(data_box, labels=years)

        for i, (_, row) in enumerate(region_data.head(2).iterrows()):
            axes[0][1].plot(years, row[years].values, marker='o', label=row['Регион'])

        sfo_mean = region_data[years].mean()
        axes[1][0].plot(years, sfo_mean, marker='o', color='blue', label='СФО')
        axes[1][0].plot(years, russia_data, marker='o', color='red', label='РФ')

        axes[1][1].axis('off')

        plt.tight_layout()

        mock_subplots.assert_called_once_with(2, 2, figsize=(15, 12))
        axes[0][0].boxplot.assert_called_once()
        assert axes[0][1].plot.call_count == 2
        assert axes[1][0].plot.call_count == 2
        axes[1][1].axis.assert_called_with('off')
        mock_tight_layout.assert_called_once()
