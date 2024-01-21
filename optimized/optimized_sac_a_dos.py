import pandas as pd
import time

# Chemins des fichiers
fichier1 = 'dataset1_Python+P7.csv'
fichier2 = 'dataset2_Python+P7.csv'

# Définir le budget maximum en centimes
budget_max = 500
budget_max_centimes = budget_max * 100

start_time = time.time()
# Lecture et nettoyage des données des fichiers CSV
def lire_et_nettoyer_csv(fichier):
    data = pd.read_csv(fichier)
    # Supprimer les lignes avec des valeurs négatives ou nulles dans 'price'
    data = data[data['price'] > 0]
    # Convertir 'price' en centimes et 'profit' en valeur absolue
    data['price'] = (data['price'] * 100).astype(int)
    data['profit'] = data['price'] * data['profit'] / 100
    return data


# Lire et nettoyer les données des deux fichiers
actions1 = lire_et_nettoyer_csv(fichier1)
actions2 = lire_et_nettoyer_csv(fichier2)

# Combiner les données des deux fichiers
actions_combinees = pd.concat([actions1, actions2], ignore_index=True)


# Fonction pour trouver le meilleur ensemble d'actions à acheter
def meilleur_investissement_sac_a_dos(actions, budget):
    n = len(actions)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        action_cost = actions.iloc[i-1]['price']
        action_profit = actions.iloc[i-1]['profit']
        for w in range(1, budget + 1):
            if action_cost <= w:
                dp[i][w] = max(dp[i-1][w], action_profit + dp[i-1][w-action_cost])
            else:
                dp[i][w] = dp[i-1][w]

    # Reconstitution de la solution
    w = budget
    solution = []
    for i in range(n, 0, -1):
        if w >= actions.iloc[i-1]['price'] and dp[i][w] != dp[i-1][w]:
            action = actions.iloc[i-1]
            solution.append({'name': action['name'], 'cost': action['price'], 'value_after_2_years': action['price'] + action['profit']})
            w -= action['price']

    return solution


# Trouver le meilleur ensemble d'actions
meilleur_ensemble = meilleur_investissement_sac_a_dos(actions_combinees, budget_max_centimes)

# Calculer et afficher les totaux
total_cost = sum(action['cost'] for action in meilleur_ensemble)
total_value_after_2_years = sum(action['value_after_2_years'] for action in meilleur_ensemble)

# Affichage des résultats
print("Actions sélectionnées :")
for action in meilleur_ensemble:
    print(f"Nom: {action['name']}, Coût: {action['cost']/100}€, Valeur après 2 ans: {action['value_after_2_years']/100}€")

print(" ")
print(f"Total d'achat: {total_cost/100}€, Valeur totale après 2 ans: {total_value_after_2_years/100}€")
print("Nombre d'actions sélectionnées : " + str(len(meilleur_ensemble)))
end_time = time.time()
print(f"Le temps de traitement avec la méthode du sac à dos est de "
      f"{end_time - start_time} secondes")