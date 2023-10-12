from models.tournaments import Tournament
from models.club import Club
from models.player import Player
from utils.database import convert_sub_objects, database_access, add_to_database, remove_from_database, update_database
from utils.controllers_menu import start_round, tournament_statue


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

    def active_tournament(self, view_name: str, list_tournaments: list):
        '''gestion des tours

        Args:
            view_name : nom de la vue
            list_tournaments : liste des tournois
        '''

        list_tournaments = convert_sub_objects(
            database_access("tournaments", Tournament, "r"))

        tournament_with_id = tournament_statue(self, list_tournaments)
        id = tournament_with_id[0]
        tournament = tournament_with_id[1]

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
                start_round(self, id, round, tournament, list_tournaments)
            case "0":
                return self.main_menu()

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
                return self.main_menu()

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
            manage_view = "manage_" + view_name.split("_")[1][:-1]
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
        edit_view = "menu_modification_" + view_name.split("_")[1]
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
                return self.main_menu()

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

    def edit_tournament(self, choice: int, view_name: str, id: int,
                        tournament: object, list_tournaments: list, manage_view: str):
        '''gestion dédier a l'edition d'un tournoi

        Args:
            view_name (_str_) : nom de la vue principale a utiliser
            id (_int_) : numéro identifiant de le tournoi dans ça liste
            tournament (_object_) : tournoi individuel tirer de ça liste
            list_tournaments (_list_) : liste d'ou le tournoi et originaire
            manage_view (_str_) : vue de gestion du tournoi

            '''

        list_players = database_access("players", Player, "r")
        tournament_players = convert_sub_objects(
            database_access("tournaments", Tournament, "r"))[id].list_players
        match choice:
            case "1":
                tournament.name = self.view.update_name_tournament(tournament)
                update_database(
                    tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)
                return self.menu_edit(view_name, id, tournament, list_tournaments)

            case "2":
                tournament.place = self.view.update_place_tournament(tournament)
                update_database(
                    tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)
                return self.menu_edit(view_name, id, tournament, list_tournaments)

            case "3":
                tournament.start_date = self.view.update_start_date_tournament(tournament)
                update_database(
                    tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)
                return self.menu_edit(view_name, id, tournament, list_tournaments)

            case "4":
                tournament.end_date = self.view.update_end_date_tournament(tournament)
                update_database(
                    tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)
                return self.menu_edit(view_name, id, tournament, list_tournaments)

            case "5":
                tournament.nb_round = int(self.view.update_nb_round_tournament(tournament))

                while tournament.nb_round != len(tournament.list_rounds):
                    if tournament.nb_round > len(tournament.list_rounds):
                        tournament.add_tour("Round" + str(len(tournament.list_rounds) + 1))
                    if tournament.nb_round < len(tournament.list_rounds):
                        tournament.remove_tour(tournament.list_rounds[len(tournament.list_rounds)])
                update_database(
                    tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)

                return self.menu_edit(view_name, id, tournament, list_tournaments)

            case "6":
                player = self.menu_list(
                    "list_players", list_players, list_only=True)[0]
                if player != "return":
                    tournament.add_player(player)
                else:
                    return self.menu_edit("menu_modification_tournament", id, tournament, list_tournaments)

                update_database(
                    tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)
                return self.edit_tournament(choice, view_name, id, tournament,
                                            list_tournaments, manage_view)
            case "7":
                player = self.menu_list(
                    "list_players", tournament_players, list_only=True)
                if player[0] != "return":
                    tournament.remove_player(tournament.list_players[player[1]])
                else:
                    return self.menu_edit("menu_modification_tournament", id, tournament, list_tournaments)
                update_database(
                    tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)

            case "8":
                tournament.start()
                update_database(
                    tournament, list_tournaments[id], list_tournaments, "tournaments", Tournament)
                return self.menu_manage(manage_view, id, tournament, list_tournaments, view_name)

            case "0":
                return self.menu_manage(manage_view, id, tournament, list_tournaments, view_name)

    def edit_player(self, choice, view_name, id, player, list_players, manage_view):
        '''gestion dédier a l'edition d'un joueur

        Args:
            view_name (_str_) : nom de la vue principale a utiliser
            id (_int_) : numéro identifiant du joueur dans ça liste
            player (_object_) : joueur individuel tirer de ça liste
            list_players (_list_) : liste d'ou le joueur et originaire
            manage_view (_str_) : vue de gestion du joueur

        '''

        match choice:
            case "1":
                player.name = self.view.update_name_player(player)
                update_database(
                    player, list_players[id], list_players, "players", Player)
                return self.menu_edit(view_name, id, player, list_players)

            case "2":
                player.first_name = self.view.update_prenom_player(player)
                update_database(
                    player, list_players[id], list_players, "players", Player)
                return self.menu_edit(view_name, id, player, list_players)

            case "3":
                player.birthday = self.view.update_birthday_player(
                    player)
                update_database(
                    player, list_players[id], list_players, "players", Player)
                return self.menu_edit(view_name, id, player, list_players)

            case "4":
                player.club = self.view.update_club_player(player)
                update_database(
                    player, list_players[id], list_players, "players", Player)
                return self.menu_edit(view_name, id, player, list_players)

            case "0":
                return self.menu_manage(manage_view, id, player, list_players, view_name)

    def edit_club(self, choice, view_name, id, obj, list_objects, manage_view):
        '''gestion dédier a l'edition d'un club

        Args:
            view_name (_str_) : nom de la vue principale a utiliser
            id (_int_) : numéro identifiant du club dans ça liste
            obj (_object_) : club individuel tirer de ça liste
            list_objects (_list_) : liste d'ou le club et originaire
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
