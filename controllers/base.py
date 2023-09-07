
from models.tournois import Tournoi
from models.tour import Tour
# from models.match import Match
from models.club import Club
from models.joueur import Joueur
from models.database import database_access, add_to_database, remove_from_database, update_database


# def reload_data(list_objects):
#     if isinstance(list_objects[0], Tournoi):
#         list_objects = database_access("tournois", Tournoi, "r")
#     elif isinstance(list_objects[0], Joueur):
#         list_objects = database_access("joueurs", Joueur, "r")
#     elif isinstance(list_objects[0], Club):
#         list_objects = database_access("clubs", Club, "r")
#     return list_objects


class Controller:
    '''Main controller'''

    def __init__(self, view, menu):

        self.view = view
        self.menu = menu

# créer un tournois

    def run(self):

        while True:
            self.menu.main_menu()

    # def test(self):
    #     '''teste appeler depuis main (en changeant le run par test)'''
    #     list_tournois = database_access("tournois", Tournoi, "r")
    #     tournoi = list_tournois[2]
    #     print(tournoi)
    #     tournoi.nom = "tata"
    #     print(tournoi)
    #     update_database(
    #         tournoi, list_tournois[2], list_tournois, "tournois", Tournoi)
