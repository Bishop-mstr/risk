import numpy as np

F = np.array([
    [3, 8, 7, 9],
    [5, 6, 3, 8],
    [4, 9, 9, 4],
    [6, 4, 5, 4]
])

probs = np.array([0.25, 0.15, 0.4, 0.2])
weights = np.array([1/3, 2/3])

def get_sigma(row):
    mean = np.sum(row * probs)
    var = np.sum(probs * (row - mean)**2)
    return np.sqrt(var)

def get_wald_max(row):
    return np.max(row)

sigmas = np.array([get_sigma(row) for row in F])
walds = np.array([get_wald_max(row) for row in F])

def normalize(arr):
    return (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

norm_sigmas = normalize(sigmas)
norm_walds = normalize(walds)

final_scores = (weights[0] * norm_sigmas) + (weights[1] * norm_walds)
best_idx = np.argmin(final_scores)

print(f"{'Рішення':<10}{'Сер. кв.':<10}{'Вальд':<10}{'N_С. кв.':<10}{'N_Вальд':<10}{'Оцінка':<10}")
for i in range(len(F)):
    print(f"x{i+1:<9}{sigmas[i]:<10.2f}{walds[i]:<10.2f}{norm_sigmas[i]:<10.2f}{norm_walds[i]:<10.2f}{final_scores[i]:.4f}")

print(f"Оптимальне рішення (Компроміс): x{best_idx+1}")