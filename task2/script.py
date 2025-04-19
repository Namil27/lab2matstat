import numpy as np
from scipy.stats import norm


def simulate_ci_coverage(sample_size, true_median=np.log(2), n_trials=1000, alpha=0.05):
    covered = 0
    ci_bounds = []

    for _ in range(n_trials):
        sample = np.random.exponential(scale=1, size=sample_size)
        sample_median = np.median(sample)

        # Стандартная ошибка медианы
        se = 1 / np.sqrt(sample_size)

        # z-значение для доверительного интервала
        z = norm.ppf(1 - alpha / 2)

        lower = sample_median - z * se
        upper = sample_median + z * se

        ci_bounds.append((lower, upper))

        if lower <= true_median <= upper:
            covered += 1

    coverage_rate = covered / n_trials
    print(f"Доля интервалов, покрывших настоящую медиану ({true_median:.3f}): {coverage_rate:.3f}")
    return ci_bounds


# Пример запуска:
simulate_ci_coverage(sample_size=25)
# Пример запуска:
simulate_ci_coverage(sample_size=10000)


