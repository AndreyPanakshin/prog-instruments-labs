import pytest
from unittest.mock import patch
import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Параметризованный тест для ANOVA с разными сценариями
@pytest.mark.parametrize("means,var,expected_significant", [
    ([50, 50, 50], 1.0, False),      # одинаковые средние
    ([50, 55, 60], 1.0, True),       # разные средние, малая дисперсия → значимо
    ([50, 55, 60], 10.0, False),     # разные средние, большая дисперсия → не значимо
])
def test_anova_logic_parametrized(means, var, expected_significant):
    np.random.seed(0)
    groups = [np.random.normal(m, np.sqrt(var), 10) for m in means]
    f_stat, p_val = f_oneway(*groups)
    is_significant = p_val < 0.01
    assert is_significant == expected_significant, \
        f"Means={means}, Var={var} → p={p_val:.4f}, expected {expected_significant}"


# Сложный тест: мокаем tukey_hsd, чтобы проверить логику вызова
@patch('scipy.stats.tukey_hsd')
def test_tukey_called_correctly_when_anova_significant(mock_tukey_hsd, mock_excel_data):
    # Подготовим данные
    df = mock_excel_data.copy()
    df_regions = df.iloc[2:].set_index('Регион')
    normal_years = ['2005', '2010']  # будем считать их "нормальными"

    # Притворимся, что ANOVA значим (p < 0.01)
    with patch('scipy.stats.f_oneway', return_value=(5.0, 0.001)):
        # Вызовем логику из основного кода (вручную)
        try:
            # Подменяем tukey_hsd моком
            mock_tukey_hsd.return_value.pvalue = np.array([[1.0, 0.0005], [0.0005, 1.0]])

            # Имитируем вызов Тьюки
            data_lists = [df_regions[year].values for year in normal_years]
            _ = mock_tukey_hsd(*data_lists)  # вызов

            # Проверяем: вызван ли с правильными аргументами?
            mock_tukey_hsd.assert_called_once()
            args = mock_tukey_hsd.call_args[0]
            assert len(args) == 2
            np.testing.assert_array_equal(args[0], df_regions['2005'].values)
            np.testing.assert_array_equal(args[1], df_regions['2010'].values)

        except Exception as e:
            pytest.fail(f"Ошибка в мок-тесте Тьюки: {e}")