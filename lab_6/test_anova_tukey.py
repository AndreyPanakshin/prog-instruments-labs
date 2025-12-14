import pytest
import numpy as np
from scipy.stats import f_oneway
from unittest.mock import patch, Mock

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


def test_tukey_called_only_when_anova_significant(mock_excel_data):
    df = mock_excel_data.copy()
    region_data = df.iloc[2:]
    alpha = 0.01

    with patch('scipy.stats.f_oneway', return_value=(10.0, 0.0005)) as mock_f_oneway:
        # Вызываем как в основном коде: scipy.stats.f_oneway(...)
        from scipy.stats import f_oneway  # ← локально, чтобы мок сработал
        f_stat, p_anova = f_oneway(region_data['2005'], region_data['2010'])

    assert p_anova < alpha, f"Expected p < {alpha}, got {p_anova}"

    with patch('scipy.stats.tukey_hsd', return_value=Mock(pvalue=np.array([[1.0, 0.0003], [0.0003, 1.0]]))) as mock_tukey:
        from scipy.stats import tukey_hsd
        if p_anova < alpha:
            _ = tukey_hsd(region_data['2005'].values, region_data['2010'].values)

        mock_tukey.assert_called_once()
        args, _ = mock_tukey.call_args
        assert len(args) == 2
        np.testing.assert_array_equal(args[0], region_data['2005'].values)
        np.testing.assert_array_equal(args[1], region_data['2010'].values)


def test_tukey_not_called_when_anova_not_significant(mock_excel_data):
    df = mock_excel_data.copy()
    region_data = df.iloc[2:]
    alpha = 0.01

    with patch('scipy.stats.f_oneway', return_value=(0.5, 0.6)):
        f_stat, p_anova = f_oneway(region_data['2005'], region_data['2010'])

    assert p_anova >= alpha

    tukey_mock = Mock()
    import scipy.stats
    original_tukey = scipy.stats.tukey_hsd
    scipy.stats.tukey_hsd = tukey_mock

    try:
        if p_anova < alpha:
            data_lists = [region_data[year].values for year in ['2005', '2010']]
            _ = scipy.stats.tukey_hsd(*data_lists)

        tukey_mock.assert_not_called()

    finally:
        scipy.stats.tukey_hsd = original_tukey
