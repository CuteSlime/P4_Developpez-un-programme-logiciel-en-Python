from utils.function import validate_national_id, date_input
from utils.text_color import (
    text_red,
    text_green,
    text_orange,
    text_blue,
    text_white
)


class Views:
    '''vue principal appellant les autres'''

    def menu_principal(self):
        '''menu principal

        Returns:
            _str_: input de l'utilisateur
        '''

        choice = ""
        print("\n"
              f"|{text_blue} Bonjour,{text_white}\n"
              f"|{text_blue} Bienvenu dans l'outils de gestion de tournaments. {text_white}\n"
              f"|{text_blue} Que souhaiter vous faire ?{text_white}"
              "\n"
              )
        print(f"[{text_orange}1{text_white}] Gérer les tournois en cours")
        print(f"[{text_orange}2{text_white}] Gérer les tournois")
        print(f"[{text_orange}3{text_white}] Gérer les joueur")
        print(f"[{text_orange}4{text_white}] Gérer les club")
        print(f"[{text_orange}0{text_white}] Quitter")

        while choice not in ("1", "2", "3", "4", "0"):
            if choice != "":
                print(f"{text_red} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        return choice

    def actual_tournaments(self, tournament: object, participants, matchs: list):
        '''gestion des tournois actif

        Args:
            tournament (_object_): tournois actuel
            matchs (_list_): list des matchs du tour

        Returns:
            _str_: input de l'utilisateur
        '''

        choice = ""
        while choice not in ("1", "0"):

            print(f"\n--- {text_blue}Bienvenu au tournoi {tournament.name} {text_white}---\n")
            print(
                f"- {text_blue}Le tournois en est au tour N°{tournament.actual_turn_number}{text_white}\n")
            print(f"[{text_orange}1{text_white}] Commencer le tour actuel")
            print(f"[{text_orange}2{text_white}] Liste des participants")
            print(f"[{text_orange}3{text_white}] Liste des match")
            print(f"[{text_orange}0{text_white}] Retour au menu principal")

            while choice not in ("1", "2", "3", "0"):
                if choice != "":
                    print(f"{text_red} Mauvais choix ! {text_white}")
                choice = input("\nChoix N° :")
            if choice == "2":
                for match in matchs:
                    for player in match:
                        print(text_blue, player[0].full_name(),
                              player[0].score, text_white)

                choice = input("\nChoix N° :")
            if choice == "3":
                for match in matchs:
                    print(text_blue,
                          f'{match[0][0].full_name()} : {match[0][0].score}',
                          text_white,
                          text_orange, " vs ", text_white,
                          text_blue,
                          f'{match[1][0].full_name()} : {match[1][0].score}',
                          text_white
                          )
                choice = input("\nChoix N° :")
        return choice

# gestion des tournaments
    def menu_tournaments(self):
        '''menu de gestion des tournois

        Returns:
            _str_: input de l'utilisateur
        '''

        choice = ""
        print(f"\n--- {text_blue}Menu de gestion des tournois {text_white}---")
        print(f"[{text_orange}1{text_white}] Lister les tournois actuel")
        print(f"[{text_orange}2{text_white}] Créer un nouveau tournoi")
        print(f"[{text_orange}0{text_white}] Retour au menu principal")
        while choice not in ("1", "2", "0"):
            if choice != "":
                print(f"{text_red} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        return choice

    def list_tournaments(self, list_tournaments: list):
        '''liste des tournois existant

        Args:
            list_tournaments (_list_): list des tournois

        Returns:
            _int_: input de l'utilisateur
        '''

        choice = ""
        print(f"\n--- {text_blue}Liste des tournois actuel{text_white} ---\n")

        for id_tournament, tournament in enumerate(list_tournaments, start=1):
            if tournament.started is False:
                print(
                    f"[{text_orange}{id_tournament}{text_white}]"
                    f"[{text_orange}En attente{text_white}]",
                    tournament)
            elif tournament.ended:
                print(
                    f"[{text_orange}{id_tournament}{text_white}]"
                    f"[{text_red}Terminé{text_white}]",
                    tournament)
            else:
                print(
                    f"[{text_orange}{id_tournament}{text_white}]"
                    f"[{text_blue}En cours{text_white}]",
                    tournament)

        while choice not in range(0, len(list_tournaments)+1):
            if choice != "":
                print(f"{text_red} Mauvais choix ! {text_white}")
            print(f"[{text_orange}0{text_white}] Pour retour")
            choice = input("Tournoi N° :")
            try:

                choice = int(choice)

            except ValueError:
                print(f"{text_red}rentrer un chiffre.{text_white}")
                choice = -1

        return choice - 1

    def creer_tournament(self):
        '''formulaire de creation de tournoi

        Returns:
            _list_: tulpe du tournoi
        '''

        cls = "Tournament"
        name = input("Nom du tournois :")
        place = input("Lieu du déroulement :")
        start_date = date_input("début")
        end_date = date_input("fin")
        nb_round = int(input("Nombre de tour :") or 4)
        while True:

            try:
                nb_round = int(nb_round)
                if nb_round >= 2:
                    break
                else:
                    print(f"{text_red}nombre de tour minimum : 2{text_white}")
                    nb_round = input("Nouveau nombre de tour : ")
            except ValueError:
                print(f"{text_red}rentrer un chiffre.{text_white}")
                nb_round = input("Nouveau nombre de tour : ")
        tournament = (cls, name, place, start_date, end_date, nb_round)

        return tournament

    def manage_tournament(self, tournament: object):
        '''menu de gestion d'un tournoi

        Args:
            tournament (_object_): le tournois selectionner depuis la list

        Returns:
            _str_: input de l'utilisateur
        '''

        choice = ""
        print(f"\n--- {text_blue}Menu de gestion du tournoi {text_white}---")
        print(tournament)
        print(f"[{text_orange}1{text_white}] Modifier le tournoi")
        print(f"[{text_orange}2{text_white}] Suprimer le tournoi")
        print(f"[{text_orange}3{text_white}] Retour a la liste des tournois")
        print(f"[{text_orange}0{text_white}] Retour au menu principal")

        while choice not in ("1", "2", "3", "0"):
            if choice != "":
                print(f"{text_red} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        if choice == "2":
            print(f"{text_red}/!\\ Voulez vous vraiment supprimer le tournoi {tournament.name} ?{text_white}")
            print(f"{text_red}/!\\ Cette action est irréversible.{text_white}")
            while choice != "O" and choice != "n" and choice != "N":
                choice = input("[O/n] :")
            if choice == "O":
                return "2"

        return choice

    def menu_modification_tournament(self, tournament: object):
        '''formulaire d'édition d'un tournois

        Args:
            tournament (_object_): le tournois selectionner depuis la list

        Returns:
            _str_: input de l'utilisateur
        '''

        choice = ""
        print(f"{text_blue}\n--- Modification du tournoi {tournament.name} {text_white}---")
        print("Que voulez vous modifier ?")
        print(f"[{text_orange}1{text_white}] Nom : {text_green}{tournament.name}{text_white}")
        print(f"[{text_orange}2{text_white}] Lieu : {text_green}{tournament.place}{text_white}")
        print(f"[{text_orange}3{text_white}] Date de debut : {text_green}{tournament.start_date}{text_white}")
        print(f"[{text_orange}4{text_white}] Date de fin : {text_green}{tournament.end_date}{text_white}")
        print(f"[{text_orange}5{text_white}] Nombre de tour : {text_green}{tournament.nb_round}{text_white}")
        print(f"[{text_orange}6{text_white}] Ajouter un joueur")
        print(f"[{text_orange}7{text_white}] Retirer un joueur")
        print(f"[{text_orange}8{text_white}] Commencer le tournoi")
        print(f"[{text_orange}0{text_white}] Retour")
        while choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "0"):
            if choice != "":
                print(f"{text_red} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        while choice == "8":
            if tournament.started:
                print(text_orange, "tournoi déjà commencer !", text_white)
                choice = input("\nChoix N° :")
            if len(tournament.list_players) % 2 != 0:
                print(text_red,
                      f"nombre de joueur invalide !({len(tournament.list_players)}) "
                      f"(le nombre de joueurs doit être pair.)",
                      text_white
                      )
                choice = input("\nChoix N° :")
            else:
                return choice
        return choice

    def update_name_tournament(self, tournament: object):
        '''mise à jour du nom du tournoi

        Args:
            tournament (_object_): le tournois selectionner depuis la list

        Returns:
            _str_: input de l'utilisateur
        '''

        print(f"Nom actuel : {text_green}{tournament.name}{text_white}")
        new_name = input("Nouveau nom: ")
        return new_name

    def update_place_tournament(self, tournament: object):
        '''mise à jour du lieu du tournoi

        Args:
            tournament (_object_): le tournois selectionner depuis la list

        Returns:
            _str_: input de l'utilisateur
        '''

        print(f"Lieu actuel : {text_green}{tournament.place}{text_white}")
        new_place = input("Nouveau lieu: ")
        return new_place

    def update_start_date_tournament(self, tournament: object):
        '''mise à jour de la date de début du tournoi

        Args:
            tournament (_object_): le tournois selectionner depuis la list

        Returns:
            _str_: input de l'utilisateur
        '''

        print(f"Date de debut actuel : {text_green}{tournament.start_date}{text_white}")
        new_start_date = date_input("début")
        return new_start_date

    def update_end_date_tournament(self, tournament: object):
        '''mise à jour de fin du tournoi

        Args:
            tournament (_object_): le tournois selectionner depuis la list

        Returns:
            _str_: input de l'utilisateur
        '''

        print(f"Date de fin actuel : {text_green}{tournament.end_date}{text_white}")
        new_end_date = date_input("fin")
        return new_end_date

    def update_nb_round_tournament(self, tournament: object):
        '''mise à jour du nombre de tour du tournoi

        Args:
            tournament (_object_): le tournois selectionner depuis la list

        Returns:
            _int_: input de l'utilisateur convertie
        '''

        print(f"Nombre de tour actuel : {text_green}{str(tournament.nb_round)}{text_white}")

        while True:
            new_nb_round = input("Nouveau nombre de tour : ")
            try:
                new_nb_round = int(new_nb_round)
                if new_nb_round > 2:
                    break
                else:
                    print(f"{text_red}nombre de tour minimum : 2{text_white}")
            except ValueError:
                print(f"{text_red}rentrer un chiffre.{text_white}")
        return new_nb_round

# gestion des players
    def menu_players(self):
        '''menu de gestion des joueurs

        Returns:
            _str_: input de l'utilisateur
        '''

        choice = ""
        print(f"\n--- {text_blue}Menu de gestion des joueurs {text_white}---\n")
        print(f"[{text_orange}1{text_white}] Lister les joueurs actuel")
        print(f"[{text_orange}2{text_white}] Créer un nouveau joueur")
        print(f"[{text_orange}0{text_white}] Retour au menu principal")
        while choice not in ("1", "2", "0"):
            if choice != "":
                print(f"{text_red} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        return choice

    def list_players(self, list_players: list):
        '''liste des joueurs existant

        Args:
            list_players (_list_): la list des joueurs

        Returns:
            _int_: input de l'utilisateur
        '''

        choice = ""
        print(f"---{text_blue} Liste des joueurs actuel {text_white}---\n")
        for id_player, player in enumerate(list_players, start=1):
            print(f"[{id_player}] {player}")

        while choice not in range(0, len(list_players)+1):
            if choice != "":
                print(f"{text_red} Mauvais choix ! {text_white}")
            print(f"[{text_orange}0{text_white}] Pour retour")
            choice = input("Joueur N° :")
            try:
                choice = int(choice)
            except ValueError:
                print(f"{text_red}rentrer un chiffre.{text_white}")
                choice = -1
        return choice - 1

    def creer_player(self):
        '''formulaire de creation de joueur

        Returns:
            _list_: un tulpe avec les donnée du joueur
        '''

        cls = "Player"
        name = input("Nom du joueur :")
        first_name = input("Prenom du joueur :")
        birthday = input("Date de naissance au format JJ/MM/AAAA :")
        club = input("Club :")
        player = (cls, name, first_name, birthday, club)
        # vérifier si la date et le club sont valide
        return player

    def manage_player(self, player: object):
        '''menu de de modification d'un joueur

        Args:
            player (_object_): le joueur selectionner depuis la list

        Returns:
            _str_: input de l'utilisateur
        '''

        choice = ""
        print(f"\n---{text_red} Menu de gestion des joueurs {text_white}---\n")
        print(player)
        print(f"[{text_orange}1{text_white}] Modifier le joueur")
        print(f"[{text_orange}2{text_white}] Suprimer le joueur")
        print(f"[{text_orange}3{text_white}] Retour a la liste des joueurs")
        print(f"[{text_orange}0{text_white}] Retour au menu principal")
        while choice not in ("1", "2", "3", "0"):
            if choice != "":
                print(f"{text_red} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        if choice == "2":
            print(
                f"{text_red}/!\\ Voulez vous vraiment supprimer le joueur {player.name} ?{text_white}")
            print(text_red, "/!\\ Cette action est irréversible.", text_white)
            while choice != "O" and choice != "n" and choice != "N":
                choice = input("[O/n] :")
            if choice == "O":
                return "2"

        return choice

    def menu_modification_player(self, player):
        '''formulaire d'édition d'un joueur

        Args:
            player (_object_): le joueur selectionner

        Returns:
            _str_: input de l'utilisateur
        '''

        choice = ""
        print(f"\n---{text_blue} Modification du joueur {player.name} {text_white}---")
        print("Que voulez vous modifier ?\n")
        print(f"[{text_orange}1{text_white}] Nom : {text_green}{player.name}{text_white}")
        print(f"[{text_orange}2{text_white}] Prenom : {text_green}{player.first_name}{text_white}")
        print(f"[{text_orange}3{text_white}] Date de naissance : {text_green}{player.birthday}{text_white}")
        print(f"[{text_orange}4{text_white}] Club : {text_green}{player.club}{text_white}")

        print(f"[{text_orange}0{text_white}] Retour")
        while choice not in ("1", "2", "3", "4", "0"):
            if choice != "":
                print(f"{text_red} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        return choice

    def update_name_player(self, player):
        '''mise à jour du nom d'un joueur

        Args:
            player (_object_): le joueur selectionner

        Returns:
            _str_: input de l'utilisateur
        '''

        print(f"Nom actuel : {text_green}{player.name}{text_white}")
        new_name = input("Nouveau nom: ")
        return new_name

    def update_prenom_player(self, player):
        '''mise à jour du prénom d'un joueur

        Args:
            player (_object_): le joueur selectionner

        Returns:
            _str_: input de l'utilisateur
        '''

        print(f"Prénom actuel : {text_green}{player.first_name}{text_white}")
        new_place = input("Nouveau prénom : ")
        return new_place

    def update_birthday_player(self, player):
        '''mise à jour de la date de naissance d'un joueur

        Args:
            player (_object_): le joueur selectionner

        Returns:
            _str_: input de l'utilisateur
        '''

        print(f"Date de naissance actuel : {text_green}{player.birthday}{text_white}")
        new_birthday = input("Nouvelle date de naissance : ")
        return new_birthday

    def update_club_player(self, player):
        '''mise à jour du club d'un joueur

        Args:
            player (_object_): le joueur selectionner

        Returns:
            _str_: input de l'utilisateur
        '''

        print(f"Club actuel : {text_green}{player.club}{text_white}")
        new_club = input("Nouveau club : ")
        return new_club

# gestion des club
    def menu_clubs(self):
        '''menu de gestion des club

        Returns:
            _str_: input de l'utilisateur
        '''

        choice = ""
        print(f"\n---{text_blue} Menu de gestion des clubs {text_white}---\n")
        print(f"[{text_orange}1{text_white}] Lister les clubs actuel")
        print(f"[{text_orange}2{text_white}] Ajouter un nouveau club")
        print(f"[{text_orange}0{text_white}] Retour au menu principal")
        while choice not in ("1", "2", "0"):
            if choice != "":
                print(f"{text_red} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        return choice

    def list_clubs(self, list_clubs):
        '''liste des clubs existant

        Args:
            list_clubs (_list_): la list des clubs

        Returns:
            _int_: input de l'utilisateur
        '''

        choice = ""
        print(f"\n---{text_blue} Liste des clubs actuel {text_white}---\n")
        for id_club, club in enumerate(list_clubs, start=1):
            print(f"[{id_club}] {club}")

        while choice not in range(0, len(list_clubs) + 1):
            if choice != "":
                print(f"{text_red} Mauvais choix ! {text_white}")
            print(f"[{text_orange}0{text_white}] Pour retour")

            choice = input("Club N° :")
            try:
                choice = int(choice)
            except ValueError:
                print(f"{text_red}rentrer un chiffre.{text_white}")
                choice = -1
        return choice - 1

    def creer_club(self):
        '''formulaire de creation de club

        Returns:
            _list_: un tulpe avec les donnée du club
        '''

        cls = "Club"
        name = input("Nom du club :")
        national_id = input("Numéro d'identification national :").upper()
        while validate_national_id(national_id) is False:
            print(text_orange, "Identifiant national invalide", text_white)
            national_id = input("Numéro d'identification national :")

        club = (cls, name, national_id)
        return club

    def manage_club(self, club):
        '''menu de de modification d'un club

        Args:
            club (_club_): le club selectionner dans la liste

        Returns:
            _str_: input de l'utilisateur
        '''

        choice = ""
        print("\n--- Menu de gestion des clubs ---\n")
        print(club)
        print(f"[{text_orange}1{text_white}] Modifier le club")
        print(f"[{text_orange}2{text_white}] Suprimer le club")
        print(f"[{text_orange}3{text_white}] Retour a la liste des clubs")
        print(f"[{text_orange}0{text_white}] Retour au menu principal")

        while choice not in ("1", "2", "3", "0"):
            if choice != "":
                print(f"{text_red} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        if choice == "2":
            print(
                f"{text_red}/!\\ Voulez vous vraiment supprimer le club {club.name} ?{text_white}")
            print(text_orange, "/!\\ Cette action est irréversible.", text_white)
            while choice != "O" and choice != "n" and choice != "N":
                choice = input("[O/n] :")
            if choice == "O":
                return "2"
        return choice

    def menu_modification_club(self, club):
        '''formulaire d'édition d'un club

        Args:
            club (_club_): le club selectionner

        Returns:
            _str_: input de l'utilisateur
        '''

        choice = ""
        print(f"\n--- Modification du club {text_green}{club.name}{text_white}---")
        print("Que voulez vous modifier ?\n")
        print(f"[{text_orange}1{text_white}] Nom : {text_green}{club.name}{text_white}")
        print(f"[{text_orange}2{text_white}] Identification national : {text_green}{club.national_id}{text_white}")
        print(f"[{text_orange}0{text_white}] Retour")
        while choice not in ("1", "2", "0"):
            if choice != "":
                print(f"{text_red} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        return choice

    def update_name_club(self, club):
        '''mise à jour du nom du club

        Args:
            player (_object_): le joueur selectionner

        Returns:
            _str_: input de l'utilisateur
        '''

        print(f"Nom actuel : {text_green}{club.name}{text_white}")
        new_name = input("Nouveau nom: ")
        return new_name

    def update_national_id_club(self, club):
        '''mise à jour de l'idendifiant national du club

        Args:
            player (_object_): le joueur selectionner

        Returns:
            _str_: input de l'utilisateur
        '''

        print(f"Identification national actuel : {text_green}{club.national_id}{text_white}")
        new_id = input("Nouvelle identification national : ")
        return new_id
