
from models.tournois import Tournoi
from models.tour import Tour
# from models.match import Match
# from models.club import Club
from models.joueur import Joueur
from models.database import database_access, add_to_database, remove_from_database, update_database
list_tournois = [database_access("joueurs", Joueur, "r")]
list_tours = []
list_matchs = []
list_joueurs = database_access("joueurs", Joueur, "r")
list_clubs = []


class Controller:
    '''Main controller'''

    def __init__(self, view):
        # self.tournois = Tournoi.list_tournois()
        # self.matchs = Match.list_matchs()
        # self.clubs = Club.list_clubs()
        self.joueurs = list_joueurs
        self.view = view
    # def test(self):
    #     tour = Tour("round01")
    #     print(tour.list_matchs)

# créer un tournois

    def add_tournoi():
        '''ajoute le tournoi rentrer depuis la vue'''
        tournois = Tournoi(tournois_data)
        add_to_database(tournois, list_tournois, "tournois", Tournoi)

    def add_joueur():
        '''ajoute le joueur rentrer depuis la vue'''
        joueur = Joueur(joueur_data)
        add_to_database(joueur, list_joueurs, "joueurs", Joueur)

    def add_tour():
        '''ajoute un tour au tournoi rentrer depuis la vue'''
        pass

    def run(self):
        choix = ""

        self.view.menu_principal()
        match choix:
            case "1":
                return self.view.menu_tournois()
            case "2":
                return self.view.menu_joueur()
            case "3":
                return self.view.menu_club()
            case "4":
                exit()

    # """start_match reçois un match, et retourne le gagnant toute en distribuant les point"""

    # def start_match(self):

    #     for match in self.matchs:
    #         Match.play_match()

    def test(self):
        print("\33[93m", list_joueurs, "\33[00m")
        joueur2 = Joueur("Tite", "Phillipe", "14 Mars 2001",
                         club="not an actor")
        joueur4 = Joueur("Touite", "Phillipe",
                         "14 Mars 2001", club="not an actor")
        joueur3 = Joueur("Touuite", "Phillipe",
                         "14 Mars 2001", club="not an actor")
        joueur1 = Joueur("Toucuite", "Phillipe",
                         "14 Mars 2001", club="not an actor")

        add_to_database(joueur1, list_joueurs, "joueurs", Joueur)
        # remove_from_database(joueur1, list_joueurs, "joueurs", Joueur)
        update_database(joueur2, joueur1, list_joueurs, "joueurs", Joueur)
        print("\33[93m", list_joueurs, "\33[00m")
