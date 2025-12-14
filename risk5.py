import numpy as np

matrix = np.array([
    [45, 32, 16],
    [15,  8, 10],
    [20, 18, 14],
    [30, 23,  7]
])

probs = np.array([1/3, 1/3, 1/3])

strategies = ["x1 (Обладнання)", "x2 (Ліцензії)", "x3 (Ноу-хау)", "x4 (Гроші)"]

def get_bayes(row):
    return np.sum(row * probs)

def get_wald(row):
    return np.min(row)

def get_risk(row):
    mean = get_bayes(row)
    variance = np.sum(probs * (row - mean)**2)
    return np.sqrt(variance)

print(f"{'Лямбда':<10}{'Критерій':<25}{'Найкраще рішення':<20}{'Значення':<10}")
print("-" * 65)

lambdas = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

for l in lambdas:
    hl_scores = []
    mod_scores = []

    for row in matrix:
        hl_val = (1 - l) * get_bayes(row) + l * get_wald(row)
        hl_scores.append(hl_val)

        mod_val = (1 - l) * get_bayes(row) - l * get_risk(row)
        mod_scores.append(mod_val)

    best_hl_idx = np.argmax(hl_scores)
    best_mod_idx = np.argmax(mod_scores)

    print(f"{l:<10.1f}{'Ходжеса-Лемана':<25}{strategies[best_hl_idx]:<20}{hl_scores[best_hl_idx]:.2f}")
    print(f"{l:<10.1f}{'Модифікований':<25}{strategies[best_mod_idx]:<20}{mod_scores[best_mod_idx]:.2f}")
    print("-" * 65)