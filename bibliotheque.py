# coding:utf-8

# Module pour lire et écrire des fichiers JSON
import json 

# On importe la classe Livre
from livre import Livre  

class Bibliotheque:

    def __init__(self, fichier="data/livres.json"):
        
        self.__livres = []       # Liste contenant tous les objets Livre
        self.__fichier = fichier # Fichier JSON pour persistance
        self.charger_fichier() # Charge automatiquement les livres existants

    def ajouter_livre(self, livre):
        
        self.__livres.append(livre)
        print(f"Livre '{livre.get_titre()}' ajouté avec succès.")
        self.sauvegarder_fichier()

    def afficher_tous(self):
        
        if not self.__livres:
            print("Aucun livre dans la bibliothèque.")
        else:
            print("\n===== LISTE DES LIVRES =====")
            for livre in self.__livres:
                livre.afficher_infos()

    def chercher_livre(self, titre):
        
        for livre in self.__livres:
            if livre.get_titre.lower() == titre.lower():
                return livre
        return None

    def sauvegarder_fichier(self):
        
        data = [livre.to_dict() for livre in self.__livres]  # Convertit chaque livre en dictionnaire
        with open(self.__fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)  # indent=4 pour un fichier JSON lisible
        print("Données sauvegardées avec succès !")

    def charger_fichier(self):
        
        try:
            with open(self.__fichier, "r", encoding="utf-8") as f:
                data = json.load(f)  # Charge les données JSON en liste de dictionnaires
                self.__livres = [Livre.from_dict(d) for d in data]  # Crée les objets Livre
        except FileNotFoundError:
            self.__livres = []  # Si fichier inexistant, on initialise une bibliothèque vide

    # ---------------- GETTERS / SETTERS ----------------

    def get_livres(self):
        #Retourne la liste complète des livres (lecture seule)
        return self.__livres.copy()  # copie pour éviter les modifications externes

    def get_fichier(self):
        #Retourne le chemin du fichier de sauvegarde
        return self.__fichier

    def set_fichier(self, nouveau_fichier):
        #Modifie le fichier de sauvegarde
        if isinstance(nouveau_fichier, str) and nouveau_fichier.endswith(".json"):
            self.__fichier = nouveau_fichier
        else:
            print("Erreur : le fichier doit être une chaîne terminant par '.json'.")