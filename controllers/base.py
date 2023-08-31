
from models.tournois import Tournoi
from models.tour import Tour
# from models.match import Match
from models.club import Club
from models.joueur import Joueur
from models.database import database_access, add_to_database, remove_from_database, update_database


class Controller:
    '''Main controller'''

    def __init__(self, view):
        # self.tournois = list_tournois
        # self.matchs = Match.list_matchs()
        # self.clubs = list_clubs
        # self.joueurs = list_joueurs
        self.view = view
    # def test(self):
    #     tour = Tour("round01")
    #     print(tour.list_matchs)

# créer un tournois

    def run(self):
        list_tournois = database_access("tournois", Tournoi, "r")
        list_tours = []
        list_matchs = []
        list_joueurs = database_access("joueurs", Joueur, "r")
        list_clubs = database_access("clubs", Club, "r")
        while True:
            menu_main = True

            tournoi_id = 0
            menu_tounois_main = menu_tournoi_create = menu_tournois_list = menu_tournoi_manage = menu_tournoi_edit = False
            joueur_id = 0
            menu_joueurs_main = menu_joueur_create = menu_joueurs_list = menu_joueur_manage = menu_joueur_edit = False
            club_id = 0
            menu_clubs_main = menu_club_create = menu_clubs_list = menu_club_manage = menu_club_edit = False

            # menu principal
            while menu_main:
                '''menu principal'''

                choix_main = self.view.menu_principal()
                match choix_main:
                    case "1":
                        menu_tounois_main = True
                        menu_main = False
                        break
                    case "2":
                        menu_joueurs_main = True
                        menu_main = False
                        break
                    case "3":
                        menu_clubs_main = True
                        menu_main = False
                        break
                    case "4":
                        menu_main = False
                        return exit()

            # menu principal des tournois
            while menu_tounois_main:
                choix = self.view.menu_tournois()
                match choix:
                    case "1":
                        menu_tournois_list = True
                        menu_tounois_main = False
                        break
                    case "2":
                        menu_tournoi_create = True
                        menu_tounois_main = False
                        break
                    case "3":
                        menu_main = True
                        menu_tounois_main = False
                        break

            # affichage de la list des tournois
            while menu_tournois_list:
                choix = self.view.list_tournois(list_tournois)
                menu_tournois_list = False
                menu_tournoi_manage = True
                tournoi = list_tournois[choix]
                break

            # menu de gestion de tournoi
            while menu_tournoi_manage:
                choix = self.view.gestion_tournoi(tournoi_id)

            # menu de création d'un tournoi
            while menu_tournoi_create:
                tournoi = self.view.creer_tournoi()
                tournoi = Tournoi(
                    tournoi[0], tournoi[1], tournoi[2], tournoi[3], nb_tour=tournoi[4])
                add_to_database(tournoi, list_tournois, "tournois", Tournoi)
                menu_tournoi_create = False
                menu_tounois_main = True

            # menu principal des joueurs
            while menu_joueurs_main:
                choix = self.view.menu_joueurs()
                match choix:
                    case "1":
                        menu_joueurs_list = True
                        menu_joueurs_main = False
                        break
                    case "2":
                        menu_joueur_create = True
                        menu_joueurs_main = False
                        break
                    case "3":
                        menu_main = True
                        menu_joueurs_main = False
                        break

            # affichage de la liste des joueurs
            while menu_joueurs_list:
                choix = self.view.list_joueurs(list_joueurs)
                menu_joueurs_list = False
                menu_joueur_manage = True

                break

            # menu de gestion de joueurs
            while menu_joueur_manage:
                choix = self.view.gestion_joueur()

            # menu de création d'un joueur
            while menu_joueur_create:
                joueur = self.view.creer_joueur()
                joueur = Joueur(
                    joueur[0], joueur[1], joueur[2], joueur[3], nb_tour=joueur[4])
                add_to_database(joueur, list_joueurs, "joueurs", Joueur)
                menu_joueur_create = False
                menu_joueurs_main = True

            # menu principal des clubs
            while menu_clubs_main:
                choix = self.view.menu_clubs()
                match choix:
                    case "1":
                        menu_clubs_list = True
                        menu_clubs_main = False
                        break
                    case "2":
                        menu_club_create = True
                        menu_clubs_main = False
                        break
                    case "3":
                        menu_main = True
                        menu_clubs_main = False
                        break

            # affichage de la list des clubs
            while menu_clubs_list:
                choix = self.view.list_clubs(list_clubs)
                menu_clubs_list = False
                menu_club_manage = True

                break

            # menu de gestion de club
            while menu_club_manage:
                choix = self.view.gestion_club()

            # menu de création d'un club
            while menu_club_create:
                club = self.view.creer_club()
                club = Club(
                    club[0], club[1], club[2], club[3], nb_tour=club[4])
                add_to_database(club, list_clubs, "clubs", Club)
                menu_club_create = False
                menu_clubs_main = True

    # """start_match reçois un match, et retourne le gagnant toute en distribuant les point"""

    # def start_match(self):

    #     for match in self.matchs:
    #         Match.play_match()

    def test(self):
        '''teste apeller depuis main (en changeant le run par test)'''

        tournoi = Tournoi("Biblo", "paris", "24/12/23", "25/12/23")
        # print("\33[93m", list_joueurs, "\33[00m")
        # joueur2 = Joueur("Tite", "Phillipe", "14 Mars 2001",
        #                  club="not an actor")
        # joueur4 = Joueur("Touite", "Phillipe",
        #                  "14 Mars 2001", club="not an actor")
        # joueur3 = Joueur("Touuite", "Phillipe",
        #                  "14 Mars 2001", club="not an actor")
        # joueur1 = Joueur("Toucuite", "Phillipe",
        #                  "14 Mars 2001", club="not an actor")
        add_to_database(tournoi, list_tournois, "tournois", Tournoi)
        # add_to_database(joueur1, list_joueurs, "joueurs", Joueur)
        # # remove_from_database(joueur1, list_joueurs, "joueurs", Joueur)
        # update_database(joueur2, joueur1, list_joueurs, "joueurs", Joueur)
        # print("\33[93m", list_joueurs, "\33[00m")
