class Tournoi:
    def __init__(self, lieu, date_debut, date_fin, numero_tour, tour, joueur, remarque, nb_tour=4):
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nb_tour = nb_tour
        self.numero_tour = numero_tour
        self.tour = tour
        self.joueur = joueur
        self.remarque = remarque


class Tour:
    def __init__(self, nom, match, date_debut, date_fin):
        self.nom = nom
        self.match = match
        self.date_debut = date_debut
        self.date_fin = date_fin


class Club:
    def __init__(self, nom, identifiant_national):
        self.nom = nom
        self.identifiant_national = identifiant_national


class Joueur:
    def __init__(self, nom, prenom, date_naissance, club):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.club = club


# class Match:
#     def __init__(self,):
#         match = ([joueur1.nom, score], [joueur2.nom, score])
