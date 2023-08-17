
# from models.tournois import Tournoi
from models.tour import Tour
# from models.match import Match
# from models.club import Club
from models.joueur import list_joueurs


list_tournois = []
list_tours = []
list_matchs = []
list_joueurs = list_joueurs()
list_clubs = []


class Controller:
    '''Main controller'''

    def __init__(self, view):
        # self.tournois = Tournoi.list_tournois()
        # self.matchs = Match.list_matchs()
        # self.clubs = Club.list_clubs()
        self.joueurs = list_joueurs

        self.view = view

    # def lister_joueurs(joueurs_data):
    #     for joueur in joueurs_data:
    #         print(joueur)
    #         list_joueurs.append(Joueur(**joueur))
    #     return list_joueurs
    def test(self):
        tour = Tour("round01")
        print(tour.list_matchs)

    def run():
        choix = 0
        running = True
        menu_principal()
        while running:
            match choix:
                case "1":
                    return menu_tournois()
                case "2":
                    return menu_joueur()
                case "3":
                    return menu_club()
                case "4":
                    exit()
                case _:
                    print("Choix incorrect !")

    """start_match reçois un match, et retourne le gagnant toute en distribuant les point"""

    def start_match(self):

        for match in self.matchs:
            Match.play_match()
