class Tournoi():
    def __init__(self, lieu, date_debut, date_fin, nb_tour=4):
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

    def add_tour(self, tour_name):
        self.list_tours.append(tour_name)