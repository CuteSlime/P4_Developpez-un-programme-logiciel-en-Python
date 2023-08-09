from datetime import datetime


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


class Tour:
    def __init__(self, nom):
        self.nom = nom
        self.list_matchs = []
        self.date_debut = datetime.now().strftime('%d/%m/%Y %H:%M')
        self.date_fin = "en cours"

    def add_match(self, match):
        self.list_matchs.append(match.match_print())

    def tour_fini(self):
        self.date_fin = datetime.now().strftime('%d/%m/%Y %H:%M')
        return self.date_fin


class Club:
    def __init__(self, nom, identifiant_national):
        self.nom = nom
        self.identifiant_national = identifiant_national

    def __repr__(self) -> str:
        self.nom


class Joueur:
    def __init__(self, nom, prenom, date_naissance, club):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.score = 0
        self.club = club.nom
# import JSON pour Joueur, plus pour le club du joueur

    def full_name(self):
        return f"{self.prenom} {self.nom}"

    def __repr__(self) -> str:
        self.full_name()


class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2

    def match_print(self):
        x = [self.joueur1.full_name(), self.joueur1.score]
        y = [self.joueur2.full_name(), self.joueur2.score]
        return (x, y)

    def __repr__(self) -> str:
        self.match
