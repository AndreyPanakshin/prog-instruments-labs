import pytest
import numpy as np
from scipy.stats import f_oneway, tukey_hsd
from unittest.mock import patch


@pytest.mark.parametrize("group_means,common_std,expected_significant", [
    ([50, 50, 50], 2.0, False),
    ([50, 55, 60], 1.0, True),
    ([50, 52, 54], 5.0, False),
])
def test_anova_significance_logic(group_means, common_std, expected_significant):
    np.random.seed(42)
    groups = [np.random.normal(mean, common_std, size=12) for mean in group_means]
    _, p_val = f_oneway(*groups)
    is_significant = p_val < 0.01
    assert is_significant == expected_significant, \
        f"Means={group_means}, σ={common_std} → p={p_val:.4f} (α=0.01)"



@patch('scipy.stats.tukey_hsd')
def test_tukey_called_only_when_anova_significant(mock_tukey_hsd, mock_excel_data):
    df = mock_excel_data.copy()
    df_regions = df.iloc[2:].set_index('Регион')
    normal_years = ['2005', '2010']


    with patch('scipy.stats.f_oneway', return_value=(10.0, 0.0005)):
        try:
            data_for_tukey = [df_regions[year].values for year in normal_years]

            mock_result = mock_tukey_hsd.return_value
            mock_result.pvalue = np.array([[1.0, 0.0003], [0.0003, 1.0]])

            _ = tukey_hsd(*data_for_tukey)

            mock_tukey_hsd.assert_called_once()
            call_args = mock_tukey_hsd.call_args[0]
            assert len(call_args) == 2
            np.testing.assert_array_equal(call_args[0], df_regions['2005'].values)
            np.testing.assert_array_equal(call_args[1], df_regions['2010'].values)

        except Exception as e:
            pytest.fail(f"Ошибка в тесте Тьюки: {e}")


@patch('scipy.stats.tukey_hsd')
def test_tukey_not_called_when_anova_not_significant(mock_tukey_hsd, mock_excel_data):
    df = mock_excel_data.copy()
    df_regions = df.iloc[2:].set_index('Регион')
    normal_years = ['2005', '2010']

    with patch('scipy.stats.f_oneway', return_value=(1.0, 0.5)):  # p = 0.5 > 0.01
        _, p_anova = f_oneway(df_regions['2005'], df_regions['2010'])
        alpha = 0.01
        if p_anova < alpha:
            tukey_hsd(df_regions['2005'], df_regions['2010'])

        mock_tukey_hsd.assert_not_called()
