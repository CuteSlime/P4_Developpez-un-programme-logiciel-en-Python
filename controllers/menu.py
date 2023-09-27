from models.tournois import Tournoi
from models.tour import Tour
from models.club import Club
from models.joueur import Joueur
from datetime import datetime
from models.database import database_access, add_to_database, remove_from_database, update_database


def convert_sub_objects(list_tournois):
    for obj in list_tournois:
        if obj.list_joueurs:
            list_joueur = []
            for joueur in obj.list_joueurs:
                joueur = Joueur(**joueur)
                list_joueur.append(joueur)

            obj.list_joueurs = list_joueur

        if obj.list_tours:
            list_tour = []
            for tour in obj.list_tours:
                if isinstance(tour, dict):
                    tour = Tour(**tour)
                list_tour.append(tour)
            obj.list_tours = list_tour
    return list_tournois


class Menu:
    def __init__(self, view):
        self.view = view

    def main_menu(self):
        '''gestion du  Menu principale'''

        list_tournois = convert_sub_objects(
            database_access("tournois", Tournoi, "r"))
        list_joueurs = database_access("joueurs", Joueur, "r")
        list_clubs = database_access("clubs", Club, "r")
        choix = self.view.menu_principal()
        match choix:
            case "1":
                return self.active_tournament("tournois_actuel", list_tournois)
            case "2":
                return self.sub_main_menu('menu_tournois',
                                          'list_tournois', list_tournois, 'creer_tournoi')
            case "3":
                return self.sub_main_menu('menu_joueurs',
                                          'list_joueurs', list_joueurs, 'creer_joueur')
            case "4":
                return self.sub_main_menu('menu_clubs',
                                          'list_clubs', list_clubs, 'creer_club')

            case "5":
                return exit()

    def active_tournament(self, view_name, list_tournois):
        '''gestion des tour'''
        list_tournois = convert_sub_objects(
            database_access("tournois", Tournoi, "r"))
        tournoi = self.menu_list(
            "list_tournois", list_tournois, list_only=True)[1]
        id = tournoi
        tournoi = list_tournois[id]
        while tournoi.started is False:
            while list_tournois[id].started is False:
                print("\33[93m" "Ce tournoi n'as pas encore commencé." "\33[00m")
                tournoi = self.menu_list(
                    "list_tournois", list_tournois, list_only=True)[1]
                id = tournoi
                tournoi = list_tournois[id]
        while tournoi.ended is True:
            while list_tournois[id].ended is True:
                print("\33[93m" "Ce tournoi est terminé" "\33[00m")
                tournoi = self.menu_list(
                    "list_tournois", list_tournois, list_only=True)[1]
                id = tournoi
                tournoi = list_tournois[id]

        tour = tournoi.list_tours[int(tournoi.numero_tour_actuel) - 1]
        # if tournoi.numero_tour_actuel == 1:
        if tour.participants == []:
            list_previous_match = []
            if int(tournoi.numero_tour_actuel) > 1:
                for round in tournoi.list_tours:
                    list_previous_match += round.list_matchs
                    print(list_previous_match)
            tour.participants = tournoi.list_joueurs
            tour.add_match(tour.participants, list_previous_match)

        choix = getattr(self.view, view_name)(
            tournoi, tour.participants, tour.list_matchs)

        match choix:
            case "1":
                tour.play_match()
                if tournoi.numero_tour_actuel == len(tournoi.list_tours):
                    tournoi.ended = True
                    best_score = 0
                    winner = tour.participants[0]
                    for participant in tour.participants:
                        if participant.score > best_score:
                            best_score = participant.score
                            winner = participant
                    tournoi.date_fin = datetime.now().strftime('%d/%m/%Y %H:%M')
                    print("\33[94m" f"Tournoi {tournoi.nom} terminé !\33[00m")
                    print(
                        "\33[94m" f"Félicitation à {winner.full_name()} !\33[00m")

                if tournoi.numero_tour_actuel < len(tournoi.list_tours):
                    tournoi.numero_tour_actuel += 1

                for match in tour.list_matchs:
                    for joueur in match:
                        joueur[0] = joueur[0].__dict__
                list_participants = []
                for participant in tour.participants:
                    participant = participant.__dict__
                    list_participants.append(participant)

                tour.participants = list_participants

                update_database(tournoi, list_tournois[id],
                                list_tournois, "tournois", Tournoi)
                list_tournois = convert_sub_objects(
                    database_access("tournois", Tournoi, "r"))
                return self.active_tournament("tournois_actuel", list_tournois)
            case "4":
                pass

    def sub_main_menu(self, view_name, menu_name_list, list_objects, menu_name_create):
        '''gestion des sous menu (gestion des tournois, joueurs, clubs)'''

        choix = getattr(self.view, view_name)()
        match choix:
            case "1":
                return self.menu_list(menu_name_list, list_objects)
            case "2":
                return self.menu_create(menu_name_create, list_objects)
            case "3":
                pass

    def menu_list(self, view_name, list_objects, **kwargs):
        '''menu de selection des tournois, joueurs ou clubs'''

        choix = getattr(self.view, view_name)(list_objects)
        obj = list_objects[int(choix)]
        id = choix

        manage_view = view_name.split("_")[1][:-1]
        manage_view = "gestion_" + manage_view
        if kwargs:
            return [obj, id]
        return self.menu_manage(manage_view, id, obj, list_objects, view_name)

    def menu_manage(self, view_name, id, obj, list_objects, menu_name_list):
        '''gestion des menu de gestion pour les tournois, joueurs, clubs de façon individuel'''

        choix = getattr(self.view, view_name)(obj)
        edit_view = view_name.split("_")[1]
        edit_view = "menu_modification_" + edit_view
        match choix:
            case "1":
                return self.menu_edit(edit_view, id, obj, list_objects)

            case "2":
                if isinstance(obj, Tournoi):
                    remove_from_database(
                        obj, list_objects, "tournois", Tournoi)

                elif isinstance(obj, Joueur):
                    remove_from_database(obj, list_objects, "joueurs", Joueur)

                elif isinstance(obj, Club):
                    remove_from_database(obj, list_objects, "clubs", Club)

                return self.menu_list(menu_name_list, list_objects)

            case "3":
                return self.menu_list(menu_name_list, list_objects)

            case "4":
                pass

    def menu_create(self, view_name, list_objects, ):
        '''gestion du menu de création d'un tournoi, joueur, club'''

        obj = getattr(self.view, view_name)()
        match obj[0]:
            case "Tournoi":
                obj = Tournoi(obj[1], obj[2], obj[3], obj[4], nb_tour=obj[5])
                add_to_database(obj, list_objects, "tournois", Tournoi)
                return self.sub_main_menu("menu_tournois", 'list_tournois', list_objects, 'creer_tournoi')

            case "Joueur":
                obj = Joueur(obj[1], obj[2], obj[3], club=obj[4])
                add_to_database(
                    obj, list_objects, "joueurs", Joueur)
                return self.sub_main_menu("menu_joueurs", 'list_joueurs', list_objects, 'creer_joueur')

            case "Club":
                obj = Club(obj[1], obj[2])
                add_to_database(obj, list_objects, "clubs", Club)
                return self.sub_main_menu("menu_clubs", 'list_clubs', list_objects, 'creer_club')

    def menu_edit(self, view_name, id, obj, list_objects):
        '''gestion de l'edition d'un tournoi, joueur, club'''

        choix = getattr(self.view, view_name)(obj)
        manage_view = view_name.split("_")[2]
        manage_view = "gestion_" + manage_view
        match manage_view:
            case "gestion_tournoi":
                self.edit_tournoi(choix, view_name, id, obj,
                                  list_objects, manage_view)

            case "gestion_joueur":
                self.edit_joueur(choix, view_name, id, obj,
                                 list_objects, manage_view)

            case "gestion_club":
                self.edit_club(choix, view_name, id, obj,
                               list_objects, manage_view)

    def edit_tournoi(self, choix, view_name, id, obj, list_objects, manage_view):
        '''gestion dédier a l'edition d'un tournoi'''

        list_joueurs = database_access("joueurs", Joueur, "r")
        match choix:
            case "1":
                obj.nom = self.view.update_nom_tournoi(obj)
                update_database(
                    obj, list_objects[id], list_objects, "tournois", Tournoi)
                return self.menu_edit(view_name, id, obj, list_objects)
            case "2":
                obj.lieu = self.view.update_lieu_tournoi(obj)
                update_database(
                    obj, list_objects[id], list_objects, "tournois", Tournoi)
                return self.menu_edit(view_name, id, obj, list_objects)
            case "3":
                obj.date_debut = self.view.update_date_debut_tournoi(obj)
                update_database(
                    obj, list_objects[id], list_objects, "tournois", Tournoi)
                return self.menu_edit(view_name, id, obj, list_objects)
            case "4":
                obj.date_fin = self.view.update_date_fin_tournoi(obj)
                update_database(
                    obj, list_objects[id], list_objects, "tournois", Tournoi)
                return self.menu_edit(view_name, id, obj, list_objects)
            case "5":
                obj.nb_tour = int(self.view.update_nb_tour_tournoi(obj))
                while obj.nb_tour != len(obj.list_tours):
                    if obj.nb_tour > len(obj.list_tours):
                        obj.add_tour("Round" + str(len(obj.list_tours) + 1))
                    if obj.nb_tour < len(obj.list_tours):
                        obj.remove_tour(obj.list_tours[len(obj.list_tours)])
                update_database(
                    obj, list_objects[id], list_objects, "tournois", Tournoi)

                return self.menu_edit(view_name, id, obj, list_objects)
            case "6":
                joueur = self.menu_list(
                    "list_joueurs", list_joueurs, list_only=True)[0]
                obj.add_joueur(joueur)
                update_database(
                    obj, list_objects[id], list_objects, "tournois", Tournoi)
            case "7":
                joueur = self.menu_list(
                    "list_joueurs", obj.list_joueurs, list_only=True)[0]
                obj.remove_joueur(joueur)
                update_database(
                    obj, list_objects[id], list_objects, "tournois", Tournoi)
            case "8":
                obj.start()
                update_database(
                    obj, list_objects[id], list_objects, "tournois", Tournoi)
                return self.menu_manage(manage_view, id, obj, list_objects, view_name)
            case "9":
                return self.menu_manage(manage_view, id, obj, list_objects, view_name)

    def edit_joueur(self, choix, view_name, id, obj, list_objects, manage_view):
        '''gestion dédier a l'edition d'un joueur'''

        match choix:
            case "1":
                obj.nom = self.view.update_nom_joueur(obj)
                update_database(
                    obj, list_objects[id], list_objects, "joueurs", Joueur)
                return self.menu_edit(view_name, id, obj, list_objects)
            case "2":
                obj.prenom = self.view.update_prenom_joueur(obj)
                update_database(
                    obj, list_objects[id], list_objects, "joueurs", Joueur)
                return self.menu_edit(view_name, id, obj, list_objects)
            case "3":
                obj.date_naissance = self.view.update_date_naissance_joueur(
                    obj)
                update_database(
                    obj, list_objects[id], list_objects, "joueurs", Joueur)
                return self.menu_edit(view_name, id, obj, list_objects)
            case "4":
                obj.club = self.view.update_club_joueur(obj)
                update_database(
                    obj, list_objects[id], list_objects, "joueurs", Joueur)
                return self.menu_edit(view_name, id, obj, list_objects)
            case "5":
                return self.menu_manage(manage_view, id, obj, list_objects, view_name)

    def edit_club(self, choix, view_name, id, obj, list_objects, manage_view):
        '''gestion dédier a l'edition d'un club'''

        match choix:
            case "1":
                obj.nom = self.view.update_nom_club(obj)
                update_database(
                    obj, list_objects[id], list_objects, "clubs", Club)
                return self.menu_edit(view_name, id, obj, list_objects)
            case "2":
                obj.identifiant_national = self.view.update_identifiant_national_club(
                    obj)
                update_database(
                    obj, list_objects[id], list_objects, "clubs", Club)
                return self.menu_edit(view_name, id, obj, list_objects)
            case "3":
                return self.menu_manage(manage_view, id, obj, list_objects, view_name)
