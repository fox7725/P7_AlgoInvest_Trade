import csv
import time


def lecture_fichier(fichier):
    """Extraction des données du fichier et classement de celles ci par
    ordre croissant le la valeur de profit après deux ans"""
    with open(fichier, 'r') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            try:
                # Convertir price en float et vérifier s'il est supérieur à 0
                price = float(row['price'])
                profit_percentage = float(row['profit'])
                if price > 0:
                    # Convertir price en centimes
                    row['price'] = int(price * 100)
                    row['profit'] = row['price']*profit_percentage/100
                    data.append(row)
            except ValueError:
                # Gestion des erreurs de conversion (par exemple, si price n'est pas un nombre)
                continue
    # Trier la liste data par la valeur de profit en ordre décroissant
    data.sort(key=lambda x: x['profit'], reverse=True)
    return data


def lecture_fichier_20actions(fichier):
    """Extraction des données du fichier et classement de celles ci par
        ordre croissant le la valeur de profit après deux ans"""
    with open(fichier, 'r') as f:
        reader = csv.DictReader(f, delimiter=";")
        data = []
        for row in reader:
            try:
                # Convertir price en float et vérifier s'il est supérieur à 0
                price = float(row['cout'])
                profit_percentage = float(row['profit'])
                if price > 0:
                    # Convertir price en centimes
                    row['cout'] = int(price * 100)
                    row['profit'] = row['cout'] * profit_percentage / 100
                    data.append(row)
            except ValueError:
                # Gestion des erreurs de conversion (par exemple, si price n'est pas un nombre)
                continue
    # Trier la liste data par la valeur de profit en ordre décroissant
    data.sort(key=lambda x: x['profit'], reverse=True)
    return data


def construire_new_dataset(data, budget_max_centimes):
    """Construction du jeu d'actions sélectionnées et récupérations des
    totaux"""
    total_price = 0
    total_profit = 0
    new_dataset = []
    for row in data:
        if total_price + row['price'] <= budget_max_centimes:
            new_dataset.append(row)
            total_price += row['price']
            total_profit += row['profit']
        else:
            # Si l'ajout de cette action dépasse le budget, arrêter d'ajouter des actions
            continue
    retour = [new_dataset, total_price, total_profit]
    return retour


def traitement(fichier, budget_max_centimes):
    """Traitement du fichier et affichage des résultats"""
    print(" ")
    print(f"Valeurs sélectionnées pour le fichier '{fichier}' :")
    start_time = time.time()
    fichier_lu = lecture_fichier(fichier)
    fichier_traite = construire_new_dataset(fichier_lu, budget_max_centimes)
    liste_actions = fichier_traite[0]
    cout_max = fichier_traite[1]
    profit_max = fichier_traite[2]
    for action in liste_actions:
        print(f"Nom: {action['name']}, Coût: {action['price'] / 100}€, Valeur après 2 ans: "
              f"{round(action['profit'] / 100, 2)}€")
    print(f"totaux : achat {cout_max / 100} - profit "
          f"{round(profit_max / 100, 2)}")
    end_time = time.time()
    print(f"Le fichier initial contenait {len(fichier_lu)} actions, nous avons sélectionné {len(liste_actions)} "
          f"actions dans le fichier.")
    return end_time - start_time


def resultat():
    # Chemins des fichiers
    fichier1 = 'optimized/dataset1_Python+P7.csv'
    fichier2 = 'optimized/dataset2_Python+P7.csv'

    # Définir le budget maximum en centimes
    budget_max = 500
    budget_max_centimes = budget_max * 100

    # traitement du premier fichier
    fichier1_traite = traitement(fichier1, budget_max_centimes)
    print(f"Temps mis pour traiter le premier fichier : {fichier1_traite} "
          f"secondes")
    input("Tapez ENTER !")

    # traitement du second fichier
    fichier2_traite = traitement(fichier2, budget_max_centimes)
    print(f"Temps mis pour traiter le second fichier : {fichier2_traite} "
          f"secondes")
    input("Tapez ENTER !")

    print(" ")
    print("Valeurs sélectionnées sur l'ensemble des deux fichiers :")
    start_time = time.time()
    fichiers_ensembles = lecture_fichier(fichier1) + lecture_fichier(fichier2)
    fichiers_ensembles.sort(key=lambda x: x['profit'], reverse=True)
    fichiers_ensembles_traites = construire_new_dataset(fichiers_ensembles, budget_max_centimes)
    liste_actions = fichiers_ensembles_traites[0]
    cout_max = fichiers_ensembles_traites[1]
    profit_max = fichiers_ensembles_traites[2]
    for action in liste_actions:
        print(f"Nom: {action['name']}, Coût: {action['price'] / 100}€, Valeur après 2 ans: "
              f"{round(action['profit'] / 100, 2)}€")
    print(f"totaux : achat {cout_max/100} - profit "
          f"{round(profit_max/100, 2)}")
    end_time = time.time()
    print(f"Les deux fichiers ensemble contenaient {len(fichiers_ensembles)} actions, nous avons sélectionné"
          f" {len(liste_actions)} actions dans cet ensemble")
    duree = end_time - start_time
    return duree


def resultat_20_actions():
    # On indique le chemin du fichier
    fichier = "bruteforce/Actions.csv"

    # Pour le calcul de la durée, on indique le moment du début
    start_time = time.time()

    # Lecture et classement du fichier
    fichier_lu = lecture_fichier_20actions(fichier)

    # On modifie les entêtes pour utiliser le fichier avec le script optimisé
    fichier_modifie = [
        {'name': action['nom'], 'price': action['cout'], 'profit': action['profit']}
        for action in fichier_lu
    ]
    # Définir le budget maximum en centimes
    budget_max = 500
    budget_max_centimes = budget_max * 100

    # Traitement
    fichier_traite = construire_new_dataset(fichier_modifie, budget_max_centimes)
    liste_actions = fichier_traite[0]
    cout_max = fichier_traite[1]
    profit_max = fichier_traite[2]
    for action in liste_actions:
        print(f"Nom: {action['name']}, Coût: {action['price'] / 100}€, Valeur après 2 ans: "
              f"{round(action['profit'] / 100, 2)}€")
    print(f"totaux : achat {cout_max / 100} - profit "
          f"{round(profit_max / 100, 2)}")
    end_time = time.time()
    print(f"Le fichier contenait {len(fichier_lu)} actions, nous avons sélectionné"
          f" {len(liste_actions)} actions dans cet ensemble")
    duree = end_time - start_time
    return duree


if __name__ == "__main__":
    print("Merci de commencer par lancer main.py")
