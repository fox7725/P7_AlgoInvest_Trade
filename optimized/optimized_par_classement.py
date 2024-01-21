import csv
import time


# Chemins des fichiers
fichier1 = 'dataset1_Python+P7.csv'
fichier2 = 'dataset2_Python+P7.csv'

# Définir le budget maximum en centimes
budget_max = 500
budget_max_centimes = budget_max * 100


def lecture_fichier(fichier):
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


def construire_new_dataset(data, budget_max_centimes):
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


print("Valeurs sélectionnées pour le fichier 1 :")
start_time = time.time()
fichier1_lu = lecture_fichier(fichier1)
fichier1_traite = construire_new_dataset(fichier1_lu, budget_max_centimes)
liste_actions = fichier1_traite[0]
cout_max = fichier1_traite[1]
profit_max = fichier1_traite[2]
for action in liste_actions:
    print(f"Nom: {action['name']}, Coût: {action['price'] / 100}€, Valeur après 2 ans: "
          f"{round(action['profit'] / 100, 2)}€")
print(f"totaux : achat {cout_max/100} - profit "
        f"{round(profit_max/100, 2)}")
end_time = time.time()
print(f"Le fichier initial contenait {len(fichier1_lu)} actions, nous avons sélectionné {len(liste_actions)} "
      f"actions dans le fichier")
print(f"Temps mis pour traiter le premier fichier : {end_time - start_time} secondes")
input("Tapez ENTER !")

print(" ")
print("Valeurs sélectionnées pour le fichier 2 :")
start_time = time.time()
fichier2_lu = lecture_fichier(fichier2)
fichier2_traite = construire_new_dataset(fichier2_lu, budget_max_centimes)
liste_actions = fichier2_traite[0]
cout_max = fichier2_traite[1]
profit_max = fichier2_traite[2]
for action in liste_actions:
    print(f"Nom: {action['name']}, Coût: {action['price'] / 100}€, Valeur après 2 ans: "
          f"{round(action['profit'] / 100, 2)}€")
print(f"totaux : achat {cout_max/100} - profit "
        f"{round(profit_max/100, 2)}")
end_time = time.time()
print(f"Le fichier initial contenait {len(fichier2_lu)} actions, nous avons sélectionné {len(liste_actions)} "
      f"actions dans le fichier")
print(f"Temps mis pour traiter le second fichier : {end_time - start_time} secondes")
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
print(f"Temps mis pour traiter les deux fichiers : {end_time - start_time} secondes")
