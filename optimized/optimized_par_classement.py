import csv


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


print("Pour le fichier 1 :")
fichier1_traite = lecture_fichier(fichier1)
print(fichier1_traite)
print("max500 :")
print(construire_new_dataset(fichier1_traite, budget_max_centimes)[0])
print(f"totaux : achat {construire_new_dataset(fichier1_traite, budget_max_centimes)[1]/100} - profit "
        f"{round(construire_new_dataset(fichier1_traite, budget_max_centimes)[2]/100, 2)}")
input("Tapez ENTER !")
print(" ")
print("Pour le fichier 2 :")
fichier2_traite = lecture_fichier(fichier2)
print(fichier2_traite)
print("max500 :")
print(construire_new_dataset(fichier2_traite, budget_max_centimes))
print(f"totaux : achat {construire_new_dataset(fichier2_traite, budget_max_centimes)[1]/100} - profit "
       f"{round(construire_new_dataset(fichier2_traite, budget_max_centimes)[2]/100, 2)}")
input("Tapez ENTER !")
print(" ")
print("pour les deux fichiers :")
fichiers_ensembles = lecture_fichier(fichier1) + lecture_fichier(fichier2)
fichiers_ensembles.sort(key=lambda x: x['profit'], reverse=True)
print(fichiers_ensembles)
print("max500 :")
print(construire_new_dataset(fichiers_ensembles, budget_max_centimes))
print(f"totaux : achat {construire_new_dataset(fichiers_ensembles, budget_max_centimes)[1]/100} - profit "
       f"{round(construire_new_dataset(fichiers_ensembles, budget_max_centimes)[2]/100, 2)}")
