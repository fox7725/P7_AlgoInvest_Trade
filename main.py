import sys

import bruteforce.bruteforce
import optimized.optimized_par_classement
import optimized.optimized_sac_a_dos


def principal():
    """Menu principal"""
    print("Bienvenue dans le programme de découverte des Algorithmes de "
          "AlgoInvest réalisé par Christophe RENARD")
    print("Nous vous recommandons de commencer par le choix 1 pour découvrir la "
          "Bruteforce et le comparatif avec un algorithme optimisé puis le choix 2 pour découvrir un algorithme "
          "opérant un choix par classement des résultats et enfin le choix 3 pour utiliser la méthode dynamique du "
          "sac à dos proposée par ChatGPT.")
    choix = "0"
    while choix != "1" and choix != "2" and choix != "3" and choix != "Q" and choix != "q":
        print("")
        print("1 Bruteforce")
        print("2 Algorithme de classement et de tri")
        print("3 Algorithme dynamique du sac à dos proposé par ChatGPT")
        print("Q Quitter")
        choix = input("Que voulez vous faire ?")
        if choix == "1":
            print("")
            print("Veuillez patienter ...")
            resultat = bruteforce.bruteforce.resultat()
            print("")
            print(f"Le temps de traitement de la bruteforce a été de {resultat} "
                  f"secondes")
            print("")
            input("Pressez ENTER pour démarrer l'algorithme optimisé (par classement)")
            resultat_20_actions = optimized.optimized_par_classement.resultat_20_actions()
            print(f"Le temps de traitement de la bruteforce a été de {resultat_20_actions} "
                  f"secondes")
            input("Pressez ENTER pour retourner au menu")
            choix = "0"

        elif choix == "2":
            resultat = optimized.optimized_par_classement.resultat()
            print("")
            print(f"Temps mis pour traiter les deux fichiers : {resultat} "
                  f"secondes")
            print("")
            input("Pressez ENTER pour retourner au menu")
            choix = "0"

        elif choix == "3":
            print("")
            print("Veuillez patienter ...")
            resultat = optimized.optimized_sac_a_dos.resultat()
            print("")
            print(f"qui ont été traitées en {resultat} secondes")
            print("")
            input("Pressez ENTER pour retourner au menu")
            choix = "0"

        elif choix == "Q" or choix == "q":
            sys.exit("Merci et à bientôt !")


if __name__ == "__main__":
    principal()
