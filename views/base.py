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
        '''menu principal'''

        choice = ""
        print("\n"
              "| Bonjour,\n"
              "| Bienvenu dans l'outils de gestion de tournaments. \n"
              "| Que souhaiter vous faire ?"
              "\n"
              )
        print(f"[{text_orange}1{text_white}] Gérer les tournois en cours")
        print(f"[{text_orange}2{text_white}] Gérer les tournois")
        print(f"[{text_orange}3{text_white}] Gérer les joueur")
        print(f"[{text_orange}4{text_white}] Gérer les club")
        print(f"[{text_orange}0{text_white}] Quitter")

        while choice not in ("1", "2", "3", "4", "0"):
            if choice != "":
                print(f"{text_orange} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        return choice

    def actual_tournaments(self, tournament, participants, games):
        '''gestion des tournois actif'''

        choice = ""
        while choice not in ("1", "0"):

            print(f"\n--- Bienvenu au tournoi {tournament.name} ---\n")
            print(
                f"- Le tournois en est au tour N°{tournament.actual_turn_number}\n")
            print(f"[{text_orange}1{text_white}] Commencer le tour actuel")
            print(f"[{text_orange}2{text_white}] Liste des participants")
            print(f"[{text_orange}3{text_white}] Liste des match")
            print(f"[{text_orange}0{text_white}] Retour au menu principal")

            while choice not in ("1", "2", "3", "0"):
                if choice != "":
                    print(f"{text_orange} Mauvais choix ! {text_white}")
                choice = input("\nChoix N° :")
            if choice == "2":
                for game in games:
                    for player in game:
                        print(text_blue, player[0].full_name(),
                              player[0].score, text_white)

                choice = input("\nChoix N° :")
            if choice == "3":
                for game in games:
                    print(text_blue,
                          f'{game[0][0].full_name()} : {game[0][0].score}',
                          text_white,
                          text_orange, " vs ", text_white,
                          text_blue,
                          f'{game[1][0].full_name()} : {game[1][0].score}',
                          text_white
                          )
                choice = input("\nChoix N° :")
        return choice

# gestion des tournaments
    def menu_tournaments(self):
        '''menu de gestion des tournois'''

        choice = ""
        print("\n--- Menu de gestion des tournois ---")
        print(f"[{text_orange}1{text_white}] Lister les tournois actuel")
        print(f"[{text_orange}2{text_white}] Créer un nouveau tournoi")
        print(f"[{text_orange}0{text_white}] Retour au menu principal")
        while choice not in ("1", "2", "0"):
            if choice != "":
                print(f"{text_orange} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        return choice

    def list_tournaments(self, list_tournaments):
        '''liste des tournois existant'''

        choice = ""
        print("\n--- Liste des tournois actuel ---\n")

        for id_tournament, tournament in enumerate(list_tournaments, start=1):
            if tournament.started is False:
                print(
                    f"[{text_orange}{id_tournament}{text_white}]"
                    f"[{text_orange}En attente{text_white}]",
                    text_green, tournament, text_white)
            elif tournament.ended:
                print(
                    f"[{text_orange}{id_tournament}{text_white}]"
                    f"[{text_red}Terminé{text_white}]",
                    text_green, tournament, text_white)
            else:
                print(
                    f"[{text_orange}{id_tournament}{text_white}]"
                    f"[{text_blue}En cours{text_white}]",
                    text_green, tournament, text_white)

        while choice not in range(0, len(list_tournaments)+1):
            if choice != "":
                print(f"{text_orange} Mauvais choix ! {text_white}")
            print(f"[{text_orange}0{text_white}] Pour retour")
            choice = input("Tournoi N° :")
            try:

                choice = int(choice)

            except ValueError:
                print("rentrer un chiffre.")
                choice = -1

        return choice - 1

    def creer_tournament(self):
        '''formulaire de creation de tournoi'''

        cls = "Tournament"
        name = input("Nom du tournois :")
        place = input("Lieu du déroulement :")
        start_date = date_input("début")
        end_date = date_input("fin")
        nb_round = int(input("Nombre de tour :") or 4)
        while True:
            nb_round = input("Nouveau nombre de tour : ")
            try:
                nb_round = int(nb_round)
                if nb_round > 2:
                    break
                else:
                    print("nombre de tour minimum : 2")
            except ValueError:
                print("rentrer un chiffre.")
        tournament = (cls, name, place, start_date, end_date, nb_round)

        return tournament

    def manage_tournament(self, tournaments_data):
        '''menu de gestion d'un tournoi'''

        choice = ""
        print("\n--- Menu de gestion du tournoi ---")
        print(tournaments_data)
        print(f"[{text_orange}1{text_white}] Modifier le tournoi")
        print(f"[{text_orange}2{text_white}] Suprimer le tournoi")
        print(f"[{text_orange}3{text_white}] Retour a la liste des tournois")
        print(f"[{text_orange}0{text_white}] Retour au menu principal")

        while choice not in ("1", "2", "3", "0"):
            if choice != "":
                print(f"{text_orange} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        if choice == "2":
            print(text_red,
                  f"/!\\ Voulez vous vraiment supprimer le tournoi {tournaments_data.name} ?{text_white}"
                  )
            print(text_orange, "/!\\ Cette action est irréversible.", text_white)
            while choice != "O" and choice != "n" and choice != "N":
                choice = input("[O/n] :")
            if choice == "O":
                return "2"

        return choice

    def menu_modification_tournament(self, tournament):
        '''formulaire d'édition d'un tournois'''
        choice = ""
        print("\n--- Modification du tournoi " + tournament.name, "---")
        print("Que voulez vous modifier ?")
        print(f"[{text_orange}1{text_white}] Nom : " + tournament.name)
        print(f"[{text_orange}2{text_white}] Lieu : " + tournament.place)
        print(f"[{text_orange}3{text_white}] Date de debut : " + tournament.start_date)
        print(f"[{text_orange}4{text_white}] Date de fin : " + tournament.end_date)
        print(f"[{text_orange}5{text_white}] Nombre de tour : ", tournament.nb_round)
        print(f"[{text_orange}6{text_white}] Ajouter un joueur")
        print(f"[{text_orange}7{text_white}] Retirer un joueur")
        print(f"[{text_orange}8{text_white}] Commencer le tournoi")
        print(f"[{text_orange}0{text_white}] Retour")
        while choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "0"):
            if choice != "":
                print(f"{text_orange} Mauvais choix ! {text_white}")
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

    def update_name_tournament(self, tournament):
        print("Nom actuel : " + tournament.name)
        new_name = input("Nouveau nom: ")
        return new_name

    def update_place_tournament(self, tournament):
        print("Lieu actuel : " + tournament.place)
        new_place = input("Nouveau lieu: ")
        return new_place

    def update_start_date_tournament(self, tournament):
        print("Date de debut actuel : " + tournament.start_date)
        new_start_date = date_input("début")
        return new_start_date

    def update_end_date_tournament(self, tournament):
        print("Date de fin actuel : " + tournament.end_date)
        new_end_date = date_input("fin")
        return new_end_date

    def update_nb_round_tournament(self, tournament):
        print("Nombre de tour actuel : " + str(tournament.nb_round))

        while True:
            new_nb_round = input("Nouveau nombre de tour : ")
            try:
                new_nb_round = int(new_nb_round)
                if new_nb_round > 2:
                    break
                else:
                    print("nombre de tour minimum : 2")
            except ValueError:
                print("rentrer un chiffre.")
        return new_nb_round

# gestion des players
    def menu_players(self):
        '''menu de gestion des joueurs'''

        choice = ""
        print("\n--- Menu de gestion des joueurs ---\n")
        print(f"[{text_orange}1{text_white}] Lister les joueurs actuel")
        print(f"[{text_orange}2{text_white}] Créer un nouveau joueur")
        print(f"[{text_orange}0{text_white}] Retour au menu principal")
        while choice not in ("1", "2", "0"):
            if choice != "":
                print(f"{text_orange} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        return choice

    def list_players(self, list_players):
        '''liste des joueurs existant'''
        choice = ""
        print("--- Liste des joueurs actuel ---\n")
        for id_player, player in enumerate(list_players, start=1):
            print(f"[{id_player}] {player}")

        while choice not in range(0, len(list_players)+1):
            if choice != "":
                print(f"{text_orange} Mauvais choix ! {text_white}")
            print(f"[{text_orange}0{text_white}] Pour retour")
            choice = input("Joueur N° :")
            try:
                choice = int(choice)
            except ValueError:
                print("rentrer un chiffre.")
                choice = -1
        return choice - 1

    def creer_player(self):
        '''formulaire de creation de joueur'''

        cls = "Player"
        name = input("Nom du joueur :")
        first_name = input("Prenom du joueur :")
        birthday = input("Date de naissance au format JJ/MM/AAAA :")
        club = input("Club :")
        player = (cls, name, first_name, birthday, club)
        # vérifier si la date et le club sont valide
        return player

    def manage_player(self, players_data):
        '''menu de de modification d'un joueur'''

        choice = ""
        print("\n--- Menu de gestion des joueurs ---\n")
        print(players_data)
        print(f"[{text_orange}1{text_white}] Modifier le joueur")
        print(f"[{text_orange}2{text_white}] Suprimer le joueur")
        print(f"[{text_orange}3{text_white}] Retour a la liste des joueurs")
        print(f"[{text_orange}0{text_white}] Retour au menu principal")
        while choice not in ("1", "2", "3", "0"):
            if choice != "":
                print(f"{text_orange} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        if choice == "2":
            print(
                f"{text_red}/!\\ Voulez vous vraiment supprimer le joueur {players_data.name} ?{text_white}")
            print(text_orange, "/!\\ Cette action est irréversible.", text_white)
            while choice != "O" and choice != "n" and choice != "N":
                choice = input("[O/n] :")
            if choice == "O":
                return "2"

        return choice

    def menu_modification_player(self, player):
        '''formulaire d'édition d'un joueur'''
        choice = ""
        print("\n--- Modification du joueur " + player.name, "---")
        print("Que voulez vous modifier ?\n")
        print(f"[{text_orange}1{text_white}] Nom : " + player.name)
        print(f"[{text_orange}2{text_white}] Prenom : " + player.first_name)
        print(f"[{text_orange}3{text_white}] Date de naissance : " +
              player.birthday)
        print(f"[{text_orange}4{text_white}] Club : " + player.club)

        print(f"[{text_orange}0{text_white}] Retour")
        while choice not in ("1", "2", "3", "4", "0"):
            if choice != "":
                print(f"{text_orange} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        return choice

    def update_name_player(self, player):
        print("Nom actuel : " + player.name)
        new_name = input("Nouveau nom: ")
        return new_name

    def update_prenom_player(self, player):
        print("Prénom actuel : " + player.first_name)
        new_place = input("Nouveau prénom : ")
        return new_place

    def update_birthday_player(self, player):
        print("Date de naissance actuel : " + player.birthday)
        new_birthday = input("Nouvelle date de naissance : ")
        return new_birthday

    def update_club_player(self, player):
        print("Club actuel : " + player.club)
        new_club = input("Nouveau club : ")
        return new_club

# gestion des club

    def menu_clubs(self):
        '''menu de gestion des club'''

        choice = ""
        print("\n--- Menu de gestion des clubs ---\n")
        print(f"[{text_orange}1{text_white}] Lister les clubs actuel")
        print(f"[{text_orange}2{text_white}] Ajouter un nouveau club")
        print(f"[{text_orange}0{text_white}] Retour au menu principal")
        while choice not in ("1", "2", "0"):
            if choice != "":
                print(f"{text_orange} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        return choice

    def list_clubs(self, list_clubs):
        '''liste des clubs existant'''

        choice = ""
        print("\n--- Liste des clubs actuel ---\n")
        for id_club, club in enumerate(list_clubs, start=1):
            print(f"[{id_club}] {club}")

        while choice not in range(0, len(list_clubs) + 1):
            if choice != "":
                print(f"{text_orange} Mauvais choix ! {text_white}")
            print(f"[{text_orange}0{text_white}] Pour retour")

            choice = input("Club N° :")
            try:
                choice = int(choice)
            except ValueError:
                print("rentrer un chiffre.")
                choice = -1
        return choice - 1

    def creer_club(self):
        '''formulaire de creation de club'''

        cls = "Club"
        name = input("Nom du club :")
        national_id = input("Numéro d'identification national :").upper()
        while validate_national_id(national_id) is False:
            print(text_orange, "Identifiant national invalide", text_white)
            national_id = input("Numéro d'identification national :")

        club = (cls, name, national_id)
        return club

    def manage_club(self, clubs_data):
        '''menu de de modification d'un club'''

        choice = ""
        print("\n--- Menu de gestion des clubs ---\n")
        print(clubs_data)
        print(f"[{text_orange}1{text_white}] Modifier le club")
        print(f"[{text_orange}2{text_white}] Suprimer le club")
        print(f"[{text_orange}3{text_white}] Retour a la liste des clubs")
        print(f"[{text_orange}0{text_white}] Retour au menu principal")

        while choice not in ("1", "2", "3", "0"):
            if choice != "":
                print(f"{text_orange} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        if choice == "2":
            print(
                f"{text_red}/!\\ Voulez vous vraiment supprimer le club {clubs_data.name} ?{text_white}")
            print(text_orange, "/!\\ Cette action est irréversible.", text_white)
            while choice != "O" and choice != "n" and choice != "N":
                choice = input("[O/n] :")
            if choice == "O":
                return "2"
        return choice

    def menu_modification_club(self, club):
        '''formulaire d'édition d'un club'''
        choice = ""
        print("\n--- Modification du club " + club.name, '---')
        print("Que voulez vous modifier ?\n")
        print(f"[{text_orange}1{text_white}] Nom : " + club.name)
        print(f"[{text_orange}2{text_white}] Identification national : " +
              club.national_id)
        print(f"[{text_orange}0{text_white}] Retour")
        while choice not in ("1", "2", "0"):
            if choice != "":
                print(f"{text_orange} Mauvais choix ! {text_white}")
            choice = input("\nChoix N° :")
        return choice

    def update_name_club(self, club):
        print("Nom actuel : " + club.name)
        new_name = input("Nouveau nom: ")
        return new_name

    def update_national_id_club(self, club):
        print("Identification national actuel : " + club.national_id)
        new_id = input("Nouvelle identification national : ")
        return new_id
