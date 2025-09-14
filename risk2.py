import math

firm1 = [(0.7, 9000), (0.3, 7000)]
firm2 = [(0.4, 13000), (0.6, 7500)]

def analyze_and_compare(firm1, firm2):
    def analyze(data):
        expected = sum(p * x for p, x in data)
        variance = sum(p * (x - expected) ** 2 for p, x in data)
        std_dev = math.sqrt(variance)
        cv = std_dev / expected
        return {"expected": expected, "variance": variance,
                "std_dev": std_dev, "cv": cv}
    
    f1 = analyze(firm1)
    f2 = analyze(firm2)
    
    safer = "Фірма 1" if f1["cv"] < f2["cv"] else "Фірма 2"
    more_profitable = "Фірма 1" if f1["expected"] > f2["expected"] else "Фірма 2"
    
    print(f"{'':<25}{'Фірма 1':<20}{'Фірма 2'}")
    print(f"{'Чиста поточна вартість':<25}{f1['expected']:<20.2f}{f2['expected']:.2f}")
    print(f"{'Дисперсія':<25}{f1['variance']:<20.2f}{f2['variance']:.2f}")
    print(f"{'Середньокв. відхилення':<25}{f1['std_dev']:<20.2f}{f2['std_dev']:.2f}")
    print(f"{'Коефіцієнт варіації':<25}{f1['cv']*100:<20.2f}{f2['cv']*100:.2f}")
    print()
    print(f"Менший ризик       : {safer}")
    print(f"Більше грошей      : {more_profitable}")

analyze_and_compare(firm1, firm2)
