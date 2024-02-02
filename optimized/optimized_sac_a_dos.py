import pandas as pd
import time


# Lecture et nettoyage des données des fichiers CSV
def lire_et_nettoyer_csv(fichier):
    data = pd.read_csv(fichier)
    # Supprimer les lignes avec des valeurs négatives ou nulles dans 'price'
    data = data[data['price'] > 0]
    # Convertir 'price' en centimes et 'profit' en valeur absolue
    data['price'] = (data['price'] * 100).astype(int)
    data['profit'] = data['price'] * data['profit'] / 100
    return data


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
            solution.append({'name': action['name'], 'cost': action[
                'price'], 'value_after_2_years': action['profit']})
            w -= action['price']

    return solution

def resultat():
    # Chemins des fichiers
    fichier1 = 'optimized/dataset1_Python+P7.csv'
    fichier2 = 'optimized/dataset2_Python+P7.csv'

    # Définir le budget maximum en centimes
    budget_max = 500
    budget_max_centimes = budget_max * 100

    # Traiter le premier dataset
    start_time = time.time()
    actions1 = lire_et_nettoyer_csv(fichier1)
    afficher_resultats_individuels(actions1, budget_max_centimes, "Dataset 1")
    end_time = time.time()
    print(f"Le fichier contenait {len(actions1)} actions et a été traité en {end_time - start_time} secondes")
    print("")
    input("Tapez ENTER pour continuer")
    print("")
    print("Veuillez patienter ...")

    # Traiter le second dataset
    start_time = time.time()
    actions2 = lire_et_nettoyer_csv(fichier2)
    afficher_resultats_individuels(actions2, budget_max_centimes, "Dataset 2")
    end_time = time.time()
    print(f"Le fichier contenait {len(actions2)} actions et a été traité en {end_time - start_time} secondes")
    print("")
    input("Tapez ENTER pour continuer")
    print("")
    print("Veuillez patienter ...")

    # Traiter la combinaison des deux datasets
    start_time = time.time()
    actions_combinees = pd.concat([actions1, actions2], ignore_index=True)
    afficher_resultats_individuels(actions_combinees, budget_max_centimes, "Combinaison des Datasets 1 et 2")
    end_time = time.time()
    print(f"L'ensemble des deux fichiers contenaient {len(actions1)} actions")

    return end_time - start_time


def afficher_resultats_individuels(actions, budget_max_centimes, description):
    meilleur_ensemble = meilleur_investissement_sac_a_dos(actions, budget_max_centimes)
    total_cost = sum(action['cost'] for action in meilleur_ensemble)
    total_value_after_2_years = sum(action['value_after_2_years'] for action in meilleur_ensemble)

    print("")
    print(f"Résultats pour {description}:")
    for action in meilleur_ensemble:
        print(
            f"Nom: {action['name']}, Coût: {action['cost'] / 100:.2f}€, Valeur après 2 ans: {action['value_after_2_years'] / 100:.2f}€")
    print(f"Total d'achat: {total_cost / 100:.2f}€, Valeur totale après 2 ans: {total_value_after_2_years / 100:.2f}€")
    print(f"Nombre d'actions sélectionnées: {len(meilleur_ensemble)}\n")


if __name__ == "__main__":
    print("Merci de commencer par lancer main.py")
