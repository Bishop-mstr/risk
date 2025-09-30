import math

decisions = {
    "I": [10, -5, -5],
    "II": [-5, -5, 10],
    "III": [1.5, 1.5, 0],
    "IV": [0, 0, 0]
}

probabilities = [0.5, 0.1, 0.4]

def U(x):
    return (x + 5) ** 2 / 15

def analyze_decisions(decisions, probabilities):
    results = {}
    for name, profits in decisions.items():
        utilities = [U(x) for x in profits]
        expected_utility = sum(p*u for p,u in zip(probabilities, utilities))
        results[name] = expected_utility
    
    best = max(results, key=results.get)
    
    print(f"{'Рішення':<10}{'Очікувана корисність'}")
    for name, eu in results.items():
        print(f"{name:<10}{eu:.2f}")
    print(f"\nНайкраще рішення за очікуваною корисністю: {best}")

analyze_decisions(decisions, probabilities)
