# coding:utf-8

from bibliotheque import Bibliotheque
from livre import Livre

def menu():
    
    biblio = Bibliotheque()  # Création de l'objet Bibliothèque (charge les livres JSON)

    while True:  # Boucle infinie jusqu'à ce que l'utilisateur choisisse de quitter
        print("\n===== MENU BIBLIOTHÈQUE =====")
        print("1. Ajouter un livre")
        print("2. Afficher tous les livres")
        print("3. Emprunter un livre")
        print("4. Rendre un livre")
        print("5. Chercher un livre")
        print("6. Sauvegarder et quitter")

        choix = input("Votre choix : ").strip()  # On supprime les espaces superflus

        match choix:  
            case "1":  
                # Ajouter un livre
                titre = input("Titre : ").strip()
                auteur = input("Auteur : ").strip()
                annee = input("Année : ").strip()
                livre = Livre(titre, auteur, annee)
                biblio.ajouter_livre(livre)

            case "2":  
                # Afficher tous les livres
                biblio.afficher_tous()

            case "3":  
                # Emprunter un livre
                titre = input("Titre du livre à emprunter : ").strip()
                livre = biblio.chercher_livre(titre)
                if livre:
                    livre.emprunter()
                else:
                    print("Livre non trouvé.")

            case "4":  
                # Rendre un livre
                titre = input("Titre du livre à rendre : ").strip()
                livre = biblio.chercher_livre(titre)
                if livre:
                    livre.rendre()
                else:
                    print("Livre non trouvé.")

            case "5":  
                # Chercher un livre
                titre = input("Titre du livre à chercher : ").strip()
                livre = biblio.chercher_livre(titre)
                if livre:
                    livre.afficher_infos()
                else:
                    print("Livre non trouvé.")

            case "6":  
                # Sauvegarder et quitter
                biblio.sauvegarder_fichier()
                print("Au revoir !")
                break  # Sortie de la boucle while

            case _:  
                print("Option invalide, veuillez réessayer.")

# Point d'entrée du programme
if __name__ == "__main__":
    menu()
