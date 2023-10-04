from models.tournaments import Tournament
from models.round import Round
from models.club import Club
from models.player import Player
from datetime import datetime
from models.database import database_access, add_to_database, remove_from_database, update_database


def convert_sub_objects(list_tournaments):
    for obj in list_tournaments:
        if obj.list_players:
            list_player = []
            for player in obj.list_players:
                player = Player(**player)
                list_player.append(player)

            obj.list_players = list_player

        if obj.list_rounds:
            list_round = []
            for round in obj.list_rounds:
                if isinstance(round, dict):
                    round = Round(**round)
                list_round.append(round)
            obj.list_rounds = list_round
    return list_tournaments


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

            case "5":
                return exit()

    def active_tournament(self, view_name, list_tournaments):
        '''gestion des round'''
        list_tournaments = convert_sub_objects(
            database_access("tournaments", Tournament, "r"))
        tournament = self.menu_list(
            "list_tournaments", list_tournaments, list_only=True)[1]
        id = tournament
        tournament = list_tournaments[id]
        while tournament.started is False:
            while list_tournaments[id].started is False:
                print("\33[93m" "Ce tournoi n'as pas encore commencé." "\33[00m")
                tournament = self.menu_list(
                    "list_tournaments", list_tournaments, list_only=True)[1]
                id = tournament
                tournament = list_tournaments[id]
        while tournament.ended is True:
            while list_tournaments[id].ended is True:
                print("\33[93m" "Ce tournoi est terminé" "\33[00m")
                tournament = self.menu_list(
                    "list_tournaments", list_tournaments, list_only=True)[1]
                id = tournament
                tournament = list_tournaments[id]

        round = tournament.list_rounds[int(tournament.actual_turn_number) - 1]
        # if tournament.actual_turn_number == 1:
        if round.participants == []:
            list_previous_match = []
            if int(tournament.actual_turn_number) > 1:
                for round in tournament.list_rounds:
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
                    print("\33[94m" f"Tournament {tournament.name} terminé !\33[00m")
                    print(
                        "\33[94m" f"Félicitation à {winner.full_name()} !\33[00m")

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
            case "4":
                pass

    def sub_main_menu(self, view_name, menu_name_list, list_objects, menu_name_create):
        '''gestion des sous menu (gestion des tournaments, players, clubs)'''

        choice = getattr(self.view, view_name)()
        match choice:
            case "1":
                return self.menu_list(menu_name_list, list_objects)
            case "2":
                return self.menu_create(menu_name_create, list_objects)
            case "3":
                pass

    def menu_list(self, view_name, list_objects, **kwargs):
        '''menu de selection des tournois, joueur ou clubs'''

        choice = getattr(self.view, view_name)(list_objects)
        obj = list_objects[int(choice)]
        id = choice

        manage_view = view_name.split("_")[1][:-1]
        manage_view = "manage_" + manage_view
        if kwargs:
            return [obj, id]
        return self.menu_manage(manage_view, id, obj, list_objects, view_name)

    def menu_manage(self, view_name, id, obj, list_objects, menu_name_list):
        '''gestion des menu de gestion pour les tournaments, players, clubs de façon individuel'''

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

            case "4":
                pass

    def menu_create(self, view_name, list_objects, ):
        '''gestion du menu de création d'un tournament, player, club'''

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

    def menu_edit(self, view_name, id, obj, list_objects):
        '''gestion de l'edition d'un tournament, player, club'''

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

    def edit_tournament(self, choice, view_name, id, obj, list_objects, manage_view):
        '''gestion dédier a l'edition d'un tournoi'''

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
                player = self.menu_list(
                    "list_players", list_players, list_only=True)[0]
                obj.add_player(player)
                update_database(
                    obj, list_objects[id], list_objects, "tournaments", Tournament)
                return self.edit_tournament(choice, view_name, id, obj,
                                            list_objects, manage_view)
            case "7":
                player = self.menu_list(
                    "list_players", obj.list_players, list_only=True)[0]
                obj.remove_player(player)
                update_database(
                    obj, list_objects[id], list_objects, "tournaments", Tournament)
            case "8":
                obj.start()
                update_database(
                    obj, list_objects[id], list_objects, "tournaments", Tournament)
                return self.menu_manage(manage_view, id, obj, list_objects, view_name)
            case "9":
                return self.menu_manage(manage_view, id, obj, list_objects, view_name)

    def edit_player(self, choice, view_name, id, obj, list_objects, manage_view):
        '''gestion dédier a l'edition d'un player'''

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
            case "5":
                return self.menu_manage(manage_view, id, obj, list_objects, view_name)

    def edit_club(self, choice, view_name, id, obj, list_objects, manage_view):
        '''gestion dédier a l'edition d'un club'''

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
            case "3":
                return self.menu_manage(manage_view, id, obj, list_objects, view_name)
