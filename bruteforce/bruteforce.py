import csv
from itertools import combinations
import time


def lire_actions_csv(filename):
    """Lire les données des actions depuis un fichier CSV."""
    actions = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Saute l'en-tête du fichier CSV
        for row in reader:
            try:
                row = row[0].split(";")
                name = row[0]
                cost = int(row[1])
                profit = float(row[2])
                actions.append((name, cost, cost * profit / 100))
            except ValueError:
                continue  # Ignore les lignes mal formatées
    return actions


def calculer_profit(actions):
    """Calculer le profit total pour un ensemble d'actions."""
    return sum(profit for _, _, profit in actions)


def brute_force(actions, budget_max):
    """Trouver le meilleur ensemble d'actions à acheter par force brute."""
    n = len(actions)
    meilleure_combinaison = []
    meilleur_profit = 0

    for r in range(1, n + 1):
        for combination in combinations(actions, r):
            cout_total = sum(cost for _, cost, _ in combination)
            if cout_total <= budget_max:
                profit_total = calculer_profit(combination)
                if profit_total > meilleur_profit:
                    meilleur_profit = profit_total
                    meilleure_combinaison = combination

    return meilleure_combinaison


start_time = time.time()
# Exemple d'utilisation
actions = lire_actions_csv('Actions.csv')
budget_max = 500
meilleur_ensemble = brute_force(actions, budget_max)
print("Meilleur ensemble d'actions à acheter:", [action[0] for action in meilleur_ensemble])
end_time = time.time()
print(f"Le temps de traitement de la Brute Force a été de :"
      f" {end_time - start_time} secondes")
