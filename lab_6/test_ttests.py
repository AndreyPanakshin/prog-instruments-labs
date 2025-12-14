from scipy.stats import ttest_1samp, ttest_ind
import numpy as np

def test_one_sample_ttest():
    # Выборка: 10 значений вокруг 50
    sample = np.array([49, 50, 51, 48, 52, 50, 49, 51, 50, 50])
    pop_mean = 50.0
    t_stat, p_val = ttest_1samp(sample, pop_mean)
    assert np.isclose(t_stat, 0.0, atol=1e-6)  # симметрия → t ≈ 0
    assert p_val > 0.05

def test_two_sample_ttest_equal():
    np.random.seed(1)
    group1 = np.random.normal(50, 2, 15)
    group2 = np.random.normal(50, 2, 15)
    t_stat, p_val = ttest_ind(group1, group2, equal_var=True)
    assert p_val > 0.01  # не значимо при α=0.01