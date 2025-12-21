from scipy.stats import shapiro
import numpy as np


def test_normality_shapiro_known_distribution():
    """Test Shapiro-Wilk on a known normal sample (seeded).

    With seed=42, normal sample should not reject H₀ (p > 0.05).
    """
    np.random.seed(42)
    normal_sample = np.random.normal(loc=50, scale=2, size=20)

    stat, p_val = shapiro(normal_sample)
    assert p_val > 0.05, f"Expected non-significant p-value, got {p_val:.4f}"
