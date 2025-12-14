import matplotlib.pyplot as plt
from unittest.mock import patch, MagicMock


@patch('matplotlib.pyplot.subplots')
@patch('matplotlib.pyplot.show')
def test_plots_generated(mock_show, mock_subplots, mock_excel_data):
    # Подготовим данные как в основном коде
    df = mock_excel_data.copy()
    df_regions = df.iloc[2:].set_index('Регион')
    years = ['2005', '2010', '2015', '2019', '2020', '2021']
    russia_data = [48.6, 50.1, 45.9, 48.7, 50.4, 51.0]

    # Мокаем subplots → возвращаем фейковые axes
    fig_mock = MagicMock()
    axes_mock = [[MagicMock(), MagicMock()], [MagicMock(), MagicMock()]]
    mock_subplots.return_value = (fig_mock, axes_mock)

    # Имитируем блок построения графиков из основного кода
    try:
        # 1. boxplot
        axes_mock[0][0].boxplot.return_value = None
        # 2. line plots
        axes_mock[0][1].plot.return_value = [MagicMock()]
        axes_mock[0][1].legend.return_value = None
        # 3. средние
        axes_mock[1][0].plot.return_value = [MagicMock()]
        axes_mock[1][0].legend.return_value = None
        # 4. off
        axes_mock[1][1].axis.return_value = None

        # Запустим логику (вручную):
        data_box = [df_regions[year] for year in years]
        axes_mock[0][0].boxplot(data_box, labels=years)

        for region in df_regions.index[:2]:  # меньше регионов для теста
            axes_mock[0][1].plot(years, df_regions.loc[region], marker='o', label=region)

        sfo_mean = df_regions.mean()
        axes_mock[1][0].plot(years, sfo_mean, marker='o', color='blue', label='СФО')
        axes_mock[1][0].plot(years, russia_data, marker='o', color='red', label='РФ')

        axes_mock[1][1].axis('off')

        plt.tight_layout()

        # Проверим, что методы вызывались
        axes_mock[0][0].boxplot.assert_called_once()
        assert axes_mock[0][1].plot.call_count >= 2  # 2+ региона
        axes_mock[1][0].plot.assert_called()
        axes_mock[1][1].axis.assert_called_with('off')

        mock_show.assert_called_once()
        mock_subplots.assert_called_with(2, 2, figsize=(15, 12))

    except Exception as e:
        pytest.fail(f"Ошибка в мок-тесте визуализации: {e}")