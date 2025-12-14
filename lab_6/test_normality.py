from scipy.stats import shapiro
import numpy as np


def test_normality_shapiro_known_distribution():
    # Генерируем выборку из нормального распределения
    np.random.seed(42)
    normal_sample = np.random.normal(loc=50, scale=2, size=20)

    stat, p_val = shapiro(normal_sample)
    # При seed=42 и этих параметрах p-value > 0.05
    assert p_val > 0.05, f"Expected non-significant p-value, got {p_val:.4f}"