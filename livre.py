# coding:utf-8

#class representant un livre de la bibliotheque
class Livre:
    #le constructeur
    def __init__(self, titre, auteur, annee, disponible=True):
        self.__titre = titre              
        self.__auteur = auteur            
        self.__annee = annee              
        self.__disponible = disponible 

    def emprunter(self):
        #si le livre est dispo, ça permet l'emprunt.
        #s'il n'est plus dispo, ça signale que le livre est déja emprnté
        
        if self.__disponible:
            self.__disponible = False
            print(f"Le livre '{self.__titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.__titre}' est déjà emprunté.")

    def rendre(self):
        if not self.__disponible:
            #si le livre était emprunté, ça permet de le rendre
            self.__disponible = True
            print(f"Le livre '{self.__titre}' a été rendu.")
        else:
            print(f"Le livre '{self.__titre}' était déjà disponible.")

    def afficher_infos(self):
        #Affiche toutes les informations du livre dans un format lisible.
        
        etat = "Disponible" if self.__disponible else "Emprunté"
        print(f"Le livre {self.__titre} est écrit par {self.__auteur} et a été publié en {self.__annee} | {etat}")

    def to_dict(self):
        #Convertit l'objet Livre en dictionnaire pour pouvoir le sauvegarder en JSON.

        return {
            "titre": self.__titre,
            "auteur": self.__auteur,
            "annee": self.__annee,
            "disponible": self.__disponible
        }
    
    # --- Getters (pour lire les attributs) ---
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur

    def get_annee(self):
        return self.__annee

    def est_disponible(self):
        return self.__disponible

    # --- Setters (pour modifier certains attributs) ---
    def set_disponible(self, etat):
        if isinstance(etat, bool):   # on vérifie que c’est bien un booléen
            self.__disponible = etat
        else:
            print("Erreur : la disponibilité doit être True ou False.")

    @staticmethod
    def from_dict(data):
        #Crée un objet Livre à partir d'un dictionnaire (utile pour charger JSON).
        
        return Livre(data["titre"], data["auteur"], data["annee"], data["disponible"])
