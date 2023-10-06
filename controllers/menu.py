from models.tournaments import Tournament
from models.club import Club
from models.player import Player
from datetime import datetime
from utils.database import convert_sub_objects, database_access, add_to_database, remove_from_database, update_database
from utils.text_color import (
    text_orange,
    text_blue,
    text_white
)


class Menu:
    def __init__(self, view):
        self.view = view

    def main_menu(self):
        '''gestion du  Menu principale'''

        list_tournaments = convert_sub_objects(
            database_access("tournaments", Tournament, "r"))
        list_players = database_access("players", Player, "r")
        list_clubs = database_access("clubs", Club, "r")
        choice = self.view.menu_principal()
        match choice:
            case "1":
                return self.active_tournament("actual_tournaments", list_tournaments)

            case "2":
                return self.sub_main_menu('menu_tournaments',
                                          'list_tournaments', list_tournaments, 'creer_tournament')

            case "3":
                return self.sub_main_menu('menu_players',
                                          'list_players', list_players, 'creer_player')

            case "4":
                return self.sub_main_menu('menu_clubs',
                                          'list_clubs', list_clubs, 'creer_club')

            case "0":
                return exit()

    def active_tournament(self, view_name, list_tournaments):
        '''gestion des tours

        Args:
            view_name : nom de la vue
            list_tournaments : liste des tournois
        '''

        list_tournaments = convert_sub_objects(
            database_access("tournaments", Tournament, "r"))
        tournament = self.menu_list(
            "list_tournaments", list_tournaments, list_only=True)[1]
        id = tournament
        tournament = list_tournaments[id]

        while tournament.started is False:
            while list_tournaments[id].started is False:
                print(text_orange, "Ce tournoi n'as pas encore commencé.", text_white)
                tournament = self.menu_list(
                    "list_tournaments", list_tournaments, list_only=True)[1]
                id = tournament
                tournament = list_tournaments[id]

        while tournament.ended is True:
            while list_tournaments[id].ended is True:
                print(text_orange, "Ce tournoi est terminé", text_white)
                tournament = self.menu_list(
                    "list_tournaments", list_tournaments, list_only=True)[1]
                id = tournament
                tournament = list_tournaments[id]

        round = tournament.list_rounds[int(tournament.actual_turn_number) - 1]

        if round.participants == []:
            list_previous_match = []
            if int(tournament.actual_turn_number) > 1:
                for round in tournament.list_rounds[0:int(tournament.actual_turn_number)]:
                    list_previous_match += round.list_matchs
            round.participants = tournament.list_players
            round.add_match(round.participants, list_previous_match)

        choice = getattr(self.view, view_name)(
            tournament, round.participants, round.list_matchs)

        match choice:
            case "1":
                round.play_match()
                if tournament.actual_turn_number == len(tournament.list_rounds):
                    tournament.ended = True
                    best_score = 0
                    winner = round.participants[0]
                    for participant in round.participants:
                        if participant.score > best_score:
                            best_score = participant.score
                            winner = participant
                    tournament.end_date = datetime.now().strftime('%d/%m/%Y %H:%M')
                    print(text_blue, f"Tournament {tournament.name} terminé !{text_white}")
                    print(
                        text_blue, f"Félicitation à {winner.full_name()} {text_white}")

                if tournament.actual_turn_number < len(tournament.list_rounds):
                    tournament.actual_turn_number += 1

                for game in round.list_matchs:
                    for player in game:
                        player[0] = player[0].__dict__
                list_participants = []

                for participant in round.participants:
                    participant = participant.__dict__
                    list_participants.append(participant)

                round.participants = list_participants

                update_database(tournament, list_tournaments[id],
                                list_tournaments, "tournaments", Tournament)
                list_tournaments = convert_sub_objects(
                    database_access("tournaments", Tournament, "r"))
                return self.active_tournament("actual_tournaments", list_tournaments)

            case "0":
                pass

    def sub_main_menu(self, view_name, menu_name_list, list_objects, menu_name_create):
        '''gestion des sous menu (gestion des tournois, joueurs, clubs)

        Args:
            view_name (_str_) : nom de la vue principale a utiliser
            menu_name_list (_str_) : nom de la vue a renvoyer au menu de listing
            menu_name_create (_str_) : nom de la vue a renvoyer au menu de création
            list_objects (_list_) : liste de tournois, joueurs, clubs
        '''

        choice = getattr(self.view, view_name)()
        match choice:
            case "1":
                return self.menu_list(menu_name_list, list_objects)

            case "2":
                return self.menu_create(menu_name_create, list_objects)

            case "0":
                pass

    def menu_list(self, view_name, list_objects, **kwargs):
        '''menu de selection des tournois, joueur ou clubs

        Args:
            view_name (_str_) : nom de la vue principale a utiliser
            list_objects (_list_) : liste de tournois, joueurs, clubs
            kwargs (_bool_) : option pour choisir le return

        return:
            **_list_ : un objet et sont id
             _def_ : le menu_manage correspondant a la vue
        '''

        choice = getattr(self.view, view_name)(list_objects)
        print(choice)
        if choice == -1:
            match view_name:
                case "list_tournaments":
                    return self.main_menu()

                case "menu_tournaments":
                    return self.sub_main_menu('menu_tournaments',
                                              'list_tournaments', list_objects, 'creer_tournament')
                case "list_players":
                    return ["return"]

                case "menu_players":
                    return self.sub_main_menu('menu_players',
                                              'list_players', list_objects, 'creer_player')

                case "menu_clubs":
                    return self.sub_main_menu('menu_clubs',
                                              'list_clubs', list_objects, 'creer_club')
        else:
            obj = list_objects[int(choice)]
            id = choice

            manage_view = view_name.split("_")[1][:-1]
            manage_view = "manage_" + manage_view
            if kwargs:
                return [obj, id]
            return self.menu_manage(manage_view, id, obj, list_objects, view_name)

    def menu_manage(self, view_name, id, obj, list_objects, menu_name_list):
        '''Menu de gestion pour les tournois, joueurs et clubs, de façon individuel

        Args:
            view_name (_str_) : nom de la vue principale a utiliser
            id (_int_) : numéro identifiant de l'objet dans ça liste
            obj (_object_) : objet individuel tirer de ça liste
            list_objects (_list_) : liste d'ou l'objet et originaire
            menu_name_list (_str_) : nom de la vue a renvoyer au menu de listing
        '''

        choice = getattr(self.view, view_name)(obj)
        edit_view = view_name.split("_")[1]
        edit_view = "menu_modification_" + edit_view
        match choice:
            case "1":
                return self.menu_edit(edit_view, id, obj, list_objects)

            case "2":
                if isinstance(obj, Tournament):
                    remove_from_database(
                        obj, list_objects, "tournaments", Tournament)

                elif isinstance(obj, Player):
                    remove_from_database(obj, list_objects, "players", Player)

                elif isinstance(obj, Club):
                    remove_from_database(obj, list_objects, "clubs", Club)

                return self.menu_list(menu_name_list, list_objects)

            case "3":
                return self.menu_list(menu_name_list, list_objects)

            case "0":
                pass

    def menu_create(self, view_name, list_objects, ):
        '''menu de création d'un tournoi, joueur, club

        Args:
            view_name (_str_) : nom de la vue principale a utiliser
            list_objects (_list_) : liste de tournois, joueurs, clubs
        '''

        obj = getattr(self.view, view_name)()
        match obj[0]:
            case "Tournament":
                obj = Tournament(obj[1], obj[2], obj[3], obj[4], nb_round=obj[5])
                add_to_database(obj, list_objects, "tournaments", Tournament)
                return self.sub_main_menu("menu_tournaments", 'list_tournaments', list_objects, 'creer_tournament')

            case "Player":
                obj = Player(obj[1], obj[2], obj[3], club=obj[4])
                add_to_database(
                    obj, list_objects, "players", Player)
                return self.sub_main_menu("menu_players", 'list_players', list_objects, 'creer_player')

            case "Club":
                obj = Club(obj[1], obj[2])
                add_to_database(obj, list_objects, "clubs", Club)
                return self.sub_main_menu("menu_clubs", 'list_clubs', list_objects, 'creer_club')

    def menu_edit(self, view_name: str, id: int, obj: object, list_objects: list):
        '''menu de selection d'un tournoi, joueur, club à editer

        Args:
            view_name (_str_) : nom de la vue principale a utiliser
            id (_int_) : numéro identifiant de l'objet dans ça liste
            obj (_object_) : objet individuel tirer de ça liste
            list_objects (_list_) : liste d'ou l'objet et originaire
        '''

        choice = getattr(self.view, view_name)(obj)
        manage_view = view_name.split("_")[2]
        manage_view = "manage_" + manage_view
        match manage_view:
            case "manage_tournament":
                self.edit_tournament(choice, view_name, id, obj,
                                     list_objects, manage_view)

            case "manage_player":
                self.edit_player(choice, view_name, id, obj,
                                 list_objects, manage_view)

            case "manage_club":
                self.edit_club(choice, view_name, id, obj,
                               list_objects, manage_view)

    def edit_tournament(self, choice: int, view_name: str, id: int, obj: object, list_objects: list, manage_view: str):
        '''gestion dédier a l'edition d'un tournoi

        Args:
            view_name (_str_) : nom de la vue principale a utiliser
            id (_int_) : numéro identifiant de l'objet dans ça liste
            obj (_object_) : objet individuel tirer de ça liste
            list_objects (_list_) : liste d'ou l'objet et originaire
            manage_view (_str_) : vue de gestion du tournoi

            '''

        list_players = database_access("players", Player, "r")
        match choice:
            case "1":
                obj.name = self.view.update_name_tournament(obj)
                update_database(
                    obj, list_objects[id], list_objects, "tournaments", Tournament)
                return self.menu_edit(view_name, id, obj, list_objects)

            case "2":
                obj.place = self.view.update_place_tournament(obj)
                update_database(
                    obj, list_objects[id], list_objects, "tournaments", Tournament)
                return self.menu_edit(view_name, id, obj, list_objects)

            case "3":
                obj.start_date = self.view.update_start_date_tournament(obj)
                update_database(
                    obj, list_objects[id], list_objects, "tournaments", Tournament)
                return self.menu_edit(view_name, id, obj, list_objects)

            case "4":
                obj.end_date = self.view.update_end_date_tournament(obj)
                update_database(
                    obj, list_objects[id], list_objects, "tournaments", Tournament)
                return self.menu_edit(view_name, id, obj, list_objects)

            case "5":
                obj.nb_round = int(self.view.update_nb_round_tournament(obj))

                while obj.nb_round != len(obj.list_rounds):
                    if obj.nb_round > len(obj.list_rounds):
                        obj.add_tour("Round" + str(len(obj.list_rounds) + 1))
                    if obj.nb_round < len(obj.list_rounds):
                        obj.remove_tour(obj.list_rounds[len(obj.list_rounds)])
                update_database(
                    obj, list_objects[id], list_objects, "tournaments", Tournament)

                return self.menu_edit(view_name, id, obj, list_objects)

            case "6":
                if self.menu_list(
                        "list_players", list_players, list_only=True)[0] != "return":
                    player = self.menu_list(
                        "list_players", list_players, list_only=True)[0]
                    obj.add_player(player)
                else:
                    return self.menu_edit("menu_modification_tournament", id, obj, list_objects)

                update_database(
                    obj, list_objects[id], list_objects, "tournaments", Tournament)
                return self.edit_tournament(choice, view_name, id, obj,
                                            list_objects, manage_view)
            case "7":
                if self.menu_list(
                        "list_players", list_players, list_only=True)[0] != "return":
                    player = self.menu_list(
                        "list_players", list_players, list_only=True)[0]
                    obj.remove_player(player)
                else:
                    return self.menu_edit("menu_modification_tournament", id, obj, list_objects)
                update_database(
                    obj, list_objects[id], list_objects, "tournaments", Tournament)

            case "8":
                obj.start()
                update_database(
                    obj, list_objects[id], list_objects, "tournaments", Tournament)
                return self.menu_manage(manage_view, id, obj, list_objects, view_name)

            case "0":
                return self.menu_manage(manage_view, id, obj, list_objects, view_name)

    def edit_player(self, choice, view_name, id, obj, list_objects, manage_view):
        '''gestion dédier a l'edition d'un joueur

        Args:
            view_name (_str_) : nom de la vue principale a utiliser
            id (_int_) : numéro identifiant de l'objet dans ça liste
            obj (_object_) : objet individuel tirer de ça liste
            list_objects (_list_) : liste d'ou l'objet et originaire
            manage_view (_str_) : vue de gestion du joueur

        '''

        match choice:
            case "1":
                obj.name = self.view.update_name_player(obj)
                update_database(
                    obj, list_objects[id], list_objects, "players", Player)
                return self.menu_edit(view_name, id, obj, list_objects)

            case "2":
                obj.first_name = self.view.update_prenom_player(obj)
                update_database(
                    obj, list_objects[id], list_objects, "players", Player)
                return self.menu_edit(view_name, id, obj, list_objects)

            case "3":
                obj.birthday = self.view.update_birthday_player(
                    obj)
                update_database(
                    obj, list_objects[id], list_objects, "players", Player)
                return self.menu_edit(view_name, id, obj, list_objects)

            case "4":
                obj.club = self.view.update_club_player(obj)
                update_database(
                    obj, list_objects[id], list_objects, "players", Player)
                return self.menu_edit(view_name, id, obj, list_objects)

            case "0":
                return self.menu_manage(manage_view, id, obj, list_objects, view_name)

    def edit_club(self, choice, view_name, id, obj, list_objects, manage_view):
        '''gestion dédier a l'edition d'un club

        Args:
            view_name (_str_) : nom de la vue principale a utiliser
            id (_int_) : numéro identifiant de l'objet dans ça liste
            obj (_object_) : objet individuel tirer de ça liste
            list_objects (_list_) : liste d'ou l'objet et originaire
            manage_view (_str_) : vue de gestion du club
        '''

        match choice:
            case "1":
                obj.name = self.view.update_name_club(obj)
                update_database(
                    obj, list_objects[id], list_objects, "clubs", Club)
                return self.menu_edit(view_name, id, obj, list_objects)

            case "2":
                obj.national_id = self.view.update_national_id_club(
                    obj)
                update_database(
                    obj, list_objects[id], list_objects, "clubs", Club)
                return self.menu_edit(view_name, id, obj, list_objects)

            case "0":
                return self.menu_manage(manage_view, id, obj, list_objects, view_name)
