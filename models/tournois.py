import json
# from .tour import Tour
# from .joueur import Joueur
# from .tour import Tour


class Tournoi():
    def __init__(self, nom, lieu, date_debut, date_fin, nb_tour=4):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nb_tour = nb_tour
        self.numero_tour_actuel = 1
        self.list_tours = []
        self.list_joueurs = []
        self.remarque = ""

    def add_joueur(self, joueur):
        self.list_joueurs.append(joueur)
        print(self.list_joueurs)

    def add_tour(self, tour_name):
        self.list_tours.append(tour_name)

    def __str__(self):
        return f"\33[90m Nom : {self.nom} /n à : {self.lieu} /n Début du tournoi : {self.date_debut} Fin : {self.date_fin} /nDescription : {self.remarque}\33[0m"
