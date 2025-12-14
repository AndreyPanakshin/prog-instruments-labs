import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, bartlett, levene, ttest_1samp, ttest_ind, f_oneway, tukey_hsd
import warnings

warnings.filterwarnings('ignore')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

print("ЛАБОРАТОРНАЯ РАБОТА №5")
print("Вариант 12 - Сибирский федеральный округ")
print("Уровень значимости α = 0.01\n")

# /////////////////////////////////////////////////////////////////////////////
# ЧАСТЬ 1
# /////////////////////////////////////////////////////////////////////////////

print("/" * 60)
print("ЧАСТЬ 1")
print("/" * 60)

# 1. Загрузка данных
print("\n1. ЗАГРУЗКА ДАННЫХ")
df = pd.read_excel('CHISLO_DOCTORS (2).xlsx', sheet_name='MyList')

df.reset_index(drop=True, inplace=True)

# Россия — строка 0
russia_data = df.iloc[0, 1:7].values           # [48.6, 50.1, 45.9, 48.7, 50.4, 51.0]

# Сибирский ФО — строка 1
sfo_data = df.iloc[1, 1:7].values             # [51.6, 52.4, 47.0, 48.8, 49.2, 49.4]

years = ['2005', '2010', '2015', '2019', '2020', '2021']

# Регионы Сибирского ФО — строки с 2 до конца
region_names = df.iloc[2:, 0].values.tolist()
regions_data = df.iloc[2:, 1:7].values

df_regions = pd.DataFrame(regions_data, columns=years, index=region_names)

print(f"Количество регионов СФО: {len(region_names)}")
print(f"Годы анализа: {', '.join(years)}")

print("\nТаблица для сравнения с Excel файлом:")
print("=" * 80)
print(f"{'Регион':<35}", end="")
for year in years:
    print(f"{year:>8}", end="")
print()
print("-" * 90)

print(f"{'Сибирский округ':<35}", end="")
for val in sfo_data:
    print(f"{val:>8.1f}", end="")
print()

for idx, region in enumerate(df_regions.index):
    print(f"{region:<35}", end="")
    for year in years:
        print(f"{df_regions.loc[region, year]:>8.1f}", end="")
    print()

print("-" * 90)

print(f"{'Россия':<35}", end="")
for val in russia_data:
    print(f"{val:>8.1f}", end="")
print()

print("-" * 90)

print(f"{'Среднее по СФО':<35}", end="")
for year in years:
    print(f"{df_regions[year].mean():>8.1f}", end="")
print()
print("=" * 80)

# 2. ВИЗУАЛИЗАЦИЯ ДАННЫХ
print("\n2. ВИЗУАЛИЗАЦИЯ ДАННЫХ")
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Анализ данных по Сибирскому федеральному округу', fontsize=16, fontweight='bold')

# Боксплот по годам
data_box = [df_regions[year] for year in years]
axes[0, 0].boxplot(data_box, labels=years)
axes[0, 0].set_title('Распределение показателя X по годам')
axes[0, 0].set_ylabel('Число врачей на 10 тыс. населения')
axes[0, 0].grid(True, alpha=0.3)

# Динамика по регионам (первые 8)
for region in df_regions.index[:8]:
    axes[0, 1].plot(years, df_regions.loc[region], marker='o', label=region)
axes[0, 1].set_title('Динамика показателя X по регионам СФО')
axes[0, 1].set_ylabel('Число врачей на 10 тыс. населения')
axes[0, 1].legend(bbox_to_anchor=(1.05, 1), loc='upper left')
axes[0, 1].grid(True, alpha=0.3)

# Среднее по СФО
sfo_mean = df_regions.mean()
axes[1, 0].plot(years, sfo_mean, marker='o', color='blue', label='Среднее по СФО', linewidth=2)
axes[1, 0].plot(years, russia_data, marker='o', color='red', label='Российская федерация')
axes[1, 0].set_title('Среднее значение показателя X по СФО')
axes[1, 0].set_ylabel('Число врачей на 10 тыс. населения')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# Убираем гистограмму — скрываем последнюю ячейку
axes[1, 1].axis('off')  # делает правый нижний график пустым

plt.tight_layout()
plt.show()

# 3. Описательная статистика
print("\n3. ОПИСАТЕЛЬНАЯ СТАТИСТИКА")
desc_stats = pd.DataFrame()
for year in years:
    desc_stats[year] = [
        df_regions[year].mean(),
        df_regions[year].std(),
        df_regions[year].quantile(0.25),
        df_regions[year].median(),
        df_regions[year].quantile(0.75),
        df_regions[year].min(),
        df_regions[year].max()
    ]
desc_stats.index = ['Среднее', 'Стд. отклонение', 'Q1', 'Медиана', 'Q3', 'Min', 'Max']
print(desc_stats.round(2))

# 4. Проверка на нормальность
print("\n4. ПРОВЕРКА НА НОРМАЛЬНОСТЬ (Тест Шапиро-Уилка)")
alpha = 0.01
normality_results = []
for year in years:
    stat, p_value = shapiro(df_regions[year])
    normality_results.append({
        'Год': year,
        'Статистика': stat,
        'p-value': p_value,
        'Нормальное': p_value > alpha
    })
normal_df = pd.DataFrame(normality_results)
print(normal_df.round(4))

normal_years = normal_df[normal_df['Нормальное']]['Год'].tolist()
print(f"\nГода, имеющие нормальное распределение: {normal_years}")

# 5. Проверка равенства дисперсий
if len(normal_years) < 2:
    print("\n5. ПРОВЕРКА РАВЕНСТВА ДИСПЕРСИЙ: недостаточно нормальных лет для сравнения")
    equal_var = False
else:
    print("\n5. ПРОВЕРКА РАВЕНСТВА ДИСПЕРСИЙ")
    try:
        bart_stat, bart_p = bartlett(*[df_regions[year] for year in normal_years])
    except Exception as e:
        bart_p = np.nan
        print(f"Ошибка в тесте Бартлетта: {e}")
    try:
        lev_stat, lev_p = levene(*[df_regions[year] for year in normal_years])
    except Exception as e:
        lev_p = np.nan
        print(f"Ошибка в тесте Левена: {e}")

    print(f"Тест Бартлетта: p-value = {bart_p:.4f}" if not np.isnan(bart_p) else "Тест Бартлетта: не выполнен")
    print(f"Тест Левена: p-value = {lev_p:.4f}" if not np.isnan(lev_p) else "Тест Левена: не выполнен")

    equal_var = (not np.isnan(bart_p) and bart_p > alpha) and (not np.isnan(lev_p) and lev_p > alpha)
    print(f"Дисперсии равны: {equal_var}")

# 6. Сравнение средних СФО с общероссийскими значениями
print("\n6. СРАВНЕНИЕ СРЕДНИХ СФО С РОССИЕЙ (t-тест для одной выборки)")
pair_results = []
for year in normal_years:
    russia_value = russia_data[years.index(year)]
    t_stat, p_value = ttest_1samp(df_regions[year], russia_value)
    is_significant = p_value < alpha
    difference = "Выше" if df_regions[year].mean() > russia_value else "Ниже"
    pair_results.append({
        'Год': year,
        'Среднее СФО': df_regions[year].mean(),
        'Среднее РФ': russia_value,
        'p-value': p_value,
        'Значимо': is_significant,
        'Различие': difference if is_significant else "Не значимо"
    })

if pair_results:
    comparison_df = pd.DataFrame(pair_results)
    print(comparison_df.round(4))
else:
    print("Нет нормальных лет для сравнения.")

# 7. Сравнение средних между нормальными годами (t-тест для независимых выборок)
if len(normal_years) >= 2 and equal_var:
    print("\n7. СРАВНЕНИЕ СРЕДНИХ МЕЖДУ НОРМАЛЬНЫМИ ГОДАМИ (равные дисперсии)")
    from itertools import combinations
    pair_results = []
    for year1, year2 in combinations(normal_years, 2):
        t_stat, p_value = ttest_ind(df_regions[year1], df_regions[year2], equal_var=True)
        pair_results.append({
            'Сравнение': f"{year1} vs {year2}",
            'p-value': p_value,
            'Значимо (p < α)': p_value < alpha,
            'Средние': f"{df_regions[year1].mean():.1f} vs {df_regions[year2].mean():.1f}"
        })
    if pair_results:
        pair_df = pd.DataFrame(pair_results)
        print(pair_df.round(4))
    else:
        print("Нет пар для сравнения.")
else:
    print("\n7. Недостаточно данных или дисперсии неравны — сравнение по п.7 пропущено.")

# 8. Множественное сравнение средних (ANOVA и Тьюки)
if len(normal_years) >= 2 and equal_var:
    print("\n8. МНОЖЕСТВЕННОЕ СРАВНЕНИЕ СРЕДНИХ (ANOVA + Тьюки)")
    try:
        f_stat, p_value_anova = f_oneway(*[df_regions[year] for year in normal_years])
        print(f"ANOVA тест: F = {f_stat:.4f}, p-value = {p_value_anova:.4f}")
        print(f"Есть значимые различия между годами: {p_value_anova < alpha}")
    except Exception as e:
        print(f"ANOVA не удалось выполнить: {e}")
        p_value_anova = None

    if p_value_anova and p_value_anova < 1.0:  # проверка, что ANOVA прошёл
        try:
            tukey = tukey_hsd(*[df_regions[year] for year in normal_years])
            print("\nЗначимые различия по тесту Тьюки (p < α = 0.01):")
            found = False
            for i in range(len(normal_years)):
                for j in range(i + 1, len(normal_years)):
                    p_val = tukey.pvalue[i][j]
                    if p_val < alpha:
                        print(f"  {normal_years[i]} vs {normal_years[j]}: p = {p_val:.4f}")
                        found = True
            if not found:
                print("  Значимых различий не обнаружено.")
        except Exception as e:
            print(f"Тест Тьюки не удалось выполнить: {e}")
else:
    print("\n8. ANOVA и Тьюки не применимы (недостаточно нормальных лет или дисперсии неравны).")