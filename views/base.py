from datetime import datetime


def validate_national_id(national_id):
    if national_id != 7 or (national_id[0:1].isalpha() is False) or (national_id[2:].isnumeric() is False):
        return False
    return True


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
        print("[\33[93m" "1" "\33[00m] Gérer les tournois en cours")
        print("[\33[93m" "2" "\33[00m] Gérer les tournois")
        print("[\33[93m" "3" "\33[00m] Gérer les joueur")
        print("[\33[93m" "4" "\33[00m] Gérer les club")
        print("[\33[93m" "5" "\33[00m] Quitter")

        while choice not in ("1", "2", "3", "4", "5"):
            if choice != "":
                print("\33[93m" "Mauvais choice !" "\33[00m")
            choice = input("\nChoix N° :")
        return choice

    def actual_tournaments(self, tournament, participants, games):
        '''gestion des tournois actif'''

        choice = ""
        while choice not in ("1", "4"):

            print(f"\n--- Bienvenu au tournoi {tournament.name} ---\n")
            print(
                f"- Le tournois en est au tour N°{tournament.actual_turn_number}\n")
            print("[\33[93m" "1" "\33[00m] Commencer le tour actuel")
            print("[\33[93m" "2" "\33[00m] Liste des participants")
            print("[\33[93m" "3" "\33[00m] Liste des match")
            print("[\33[93m" "4" "\33[00m] Retour au menu principal")

            while choice not in ("1", "2", "3", "4"):
                if choice != "":
                    print("\33[93m" "Mauvais choice !" "\33[00m")
                choice = input("\nChoix N° :")
            if choice == "2":
                for game in games:
                    for player in game:
                        print("\33[94m", player[0].full_name(),
                              player[0].score, "\33[00m")

                choice = input("\nChoix N° :")
            if choice == "3":
                for game in games:
                    print("\33[94m"
                          f'{game[0][0].full_name()} : {game[0][0].score}'
                          "\33[00m"
                          "\33[93m" " vs " "\33[00m"
                          "\33[94m"
                          f'{game[1][0].full_name()} : {game[1][0].score}'
                          "\33[00m"
                          )
                choice = input("\nChoix N° :")
        return choice

# gestion des tournaments
    def menu_tournaments(self):
        '''menu de gestion des tournois'''

        choice = ""
        print("\n--- Menu de gestion des tournois ---")
        print("[\33[93m" "1" "\33[00m] Lister les tournois actuel")
        print("[\33[93m" "2" "\33[00m] Créer un nouveau tournoi")
        print("[\33[93m" "3" "\33[00m] Retour au menu principal")
        while choice not in ("1", "2", "3"):
            if choice != "":
                print("\33[93m" "Mauvais choix !" "\33[00m")
            choice = input("\nChoix N° :")
        return choice

    def list_tournaments(self, list_tournaments):
        '''liste des tournois existant'''

        choice = 0
        print("\n--- Liste des tournois actuel ---\n")

        for id_tournament, tournament in enumerate(list_tournaments, start=1):
            if tournament.started is False:
                print(
                    f"[\33[93m{id_tournament}\33[00m] [\33[93mEn attente\33[00m]{tournament}")
            elif tournament.ended:
                print(
                    f"[\33[93m{id_tournament}\33[00m] [\33[91mTerminé\33[00m]{tournament}")
            else:
                print(
                    f"[\33[93m{id_tournament}\33[00m] [\33[94mEn cours\33[00m] {tournament}")
        while choice not in range(1, len(list_tournaments)+1):
            if choice != 0:
                print("\33[93m" "Mauvais choix !" "\33[00m")
            choice = int(input("Tournoi N° :"))
        return (choice - 1)

    def creer_tournament(self):
        '''formulaire de creation de tournoi'''
        cls = "Tournament"
        name = input("Nom du tournois :")
        place = input("Lieu du déroulement :")
        while True:
            try:
                start_date = datetime.strptime(
                    input("Date de début au format JJ/MM/AAAA :"), "%d/%m/%Y").strftime("%d/%m/%Y")
                break
            except ValueError:
                print("Format invalide, exemple de format valide : 31/08/2023")
        while True:
            try:
                end_date = datetime.strptime(
                    input("Date de fin au format JJ/MM/AAAA :"), "%d/%m/%Y").strftime("%d/%m/%Y")
                break
            except ValueError:
                print("Format invalide, exemple de format valide : 31/08/2023")

        nb_round = int(input("Nombre de tour :") or 4)
        tournament = (cls, name, place, start_date, end_date, nb_round)

        return tournament

    def manage_tournament(self, tournaments_data):
        '''menu de gestion d'un tournoi'''

        choice = ""
        print("\n--- Menu de gestion du tournoi ---")
        print(tournaments_data)
        print("[\33[93m" "1" "\33[00m] Modifier le tournoi")
        print("[\33[93m" "2" "\33[00m] Suprimer le tournoi")
        print("[\33[93m" "3" "\33[00m] Retour a la liste des tournois")
        print("[\33[93m" "4" "\33[00m] Retour au menu principal")

        while choice not in ("1", "2", "3", "4"):
            if choice != "":
                print("\33[93m" "Mauvais choix !" "\33[00m")
            choice = input("\nChoix N° :")
        if choice == "2":
            print("\33[91m"
                  f"/!\\ Voulez vous vraiment supprimer le tournoi {tournaments_data.name} ?"
                  "\33[00m"
                  )
            print("\33[93m" "/!\\ Cette action est irréversible." "\33[00m")
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
        print("[\33[93m" "1" "\33[00m] Nom : " + tournament.name)
        print("[\33[93m" "2" "\33[00m] Lieu : " + tournament.place)
        print("[\33[93m" "3" "\33[00m] Date de debut : " + tournament.start_date)
        print("[\33[93m" "4" "\33[00m] Date de fin : " + tournament.end_date)
        print("[\33[93m" "5" "\33[00m] Nombre de tour : ", tournament.nb_round)
        print("[\33[93m" "6" "\33[00m] Ajouter un joueur")
        print("[\33[93m" "7" "\33[00m] Retirer un joueur")
        print("[\33[93m" "8" "\33[00m] Commencer le tournoi")
        print("[\33[93m" "9" "\33[00m] Retour")
        while choice not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            if choice != "":
                print("\33[93m" "Mauvais choix !" "\33[00m")
            choice = input("\nChoix N° :")
        while choice == "8":
            if tournament.started:
                print("\33[93m" "tournoi déjà commencer !" "\33[00m")
                choice = input("\nChoix N° :")
            if len(tournament.list_players) % 2 != 0:
                print("\33[91m"
                      f"nombre de joueur invalide !({len(tournament.list_players)}) "
                      f"(le nombre de joueurs doit être pair.)"
                      "\33[00m"
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
        new_start_date = input("Nouvelle date de debut : ")
        return new_start_date

    def update_end_date_tournament(self, tournament):
        print("Date de fin actuel : " + tournament.end_date)
        new_end_date = input("Nouvelle date de fin : ")
        return new_end_date

    def update_nb_round_tournament(self, tournament):
        print("Nombre de tour actuel : " + str(tournament.nb_round))
        new_nb_round = input("Nouveau nombre de tour : ")
        return new_nb_round

# gestion des players
    def menu_players(self):
        '''menu de gestion des joueurs'''

        choice = ""
        print("\n--- Menu de gestion des joueurs ---\n")
        print("[\33[93m" "1" "\33[00m] Lister les joueurs actuel")
        print("[\33[93m" "2" "\33[00m] Créer un nouveau joueur")
        print("[\33[93m" "3" "\33[00m] Retour au menu principal")
        while choice not in ("1", "2", "3", "4"):
            if choice != "":
                print("\33[93m" "Mauvais choix !" "\33[00m")
            choice = input("\nChoix N° :")
        return choice

    def list_players(self, list_players):
        '''liste des joueurs existant'''
        choice = 0
        print("--- Liste des joueurs actuel ---\n")
        for id_player, player in enumerate(list_players, start=1):
            print(f"[{id_player}] {player}")

        while choice not in range(1, len(list_players)+1):
            if choice != 0:
                print("\33[93m" "Mauvais choix !" "\33[00m")
            choice = int(input("Joueur N° :"))
        return (choice - 1)

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
        print("[\33[93m" "1" "\33[00m] Modifier le joueur")
        print("[\33[93m" "2" "\33[00m] Suprimer le joueur")
        print("[\33[93m" "3" "\33[00m] Retour a la liste des joueurs")
        print("[\33[93m" "4" "\33[00m] Retour au menu principal")
        while choice not in ("1", "2", "3", "4"):
            if choice != "":
                print("\33[93m" "Mauvais choice !" "\33[00m")
            choice = input("\nChoix N° :")
        if choice == "2":
            print(
                f"\33[91m/!\\ Voulez vous vraiment supprimer le joueur {players_data.name} ?\33[00m")
            print("\33[93m" "/!\\ Cette action est irréversible." "\33[00m")
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
        print("[\33[93m" "1" "\33[00m] Nom : " + player.name)
        print("[\33[93m" "2" "\33[00m] Prenom : " + player.first_name)
        print("[\33[93m" "3" "\33[00m] Date de naissance : " +
              player.birthday)
        print("[\33[93m" "4" "\33[00m] Club : " + player.club)

        print("[\33[93m" "5" "\33[00m] Retour")
        while choice not in ("1", "2", "3", "4", "5"):
            if choice != "":
                print("\33[93m" "Mauvais choix !" "\33[00m")
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
        print("[\33[93m" "1" "\33[00m] Lister les clubs actuel")
        print("[\33[93m" "2" "\33[00m] Ajouter un nouveau club")
        print("[\33[93m" "3" "\33[00m] Retour au menu principal")
        while choice not in ("1", "2", "3"):
            if choice != "":
                print("\33[93m" "Mauvais choix !" "\33[00m")
            choice = input("\nChoix N° :")
        return choice

    def list_clubs(self, list_clubs):
        '''liste des clubs existant'''

        choice = 0
        print("\n--- Liste des clubs actuel ---\n")
        for id_club, club in enumerate(list_clubs, start=1):
            print(f"[{id_club}] {club}")

        while choice not in range(1, len(list_clubs) + 1):
            if choice != 0:
                print("\33[93m" "Mauvais choix !" "\33[00m")
            choice = int(input("Club N° :"))
        return (choice - 1)

    def creer_club(self):
        '''formulaire de creation de club'''

        cls = "Club"
        name = input("Nom du club :")
        national_id = input("Numéro d'identification national :").upper()
        while validate_national_id(national_id) is False:
            print("\33[93m" "Identifiant national invalide" "\33[00m")
            national_id = input("Numéro d'identification national :")

        club = (cls, name, national_id)
        return club

    def manage_club(self, clubs_data):
        '''menu de de modification d'un club'''

        choice = ""
        print("\n--- Menu de gestion des clubs ---\n")
        print(clubs_data)
        print("[\33[93m" "1" "\33[00m] Modifier le club")
        print("[\33[93m" "2" "\33[00m] Suprimer le club")
        print("[\33[93m" "3" "\33[00m] Retour a la liste des clubs")
        print("[\33[93m" "4" "\33[00m] Retour au menu principal")

        while choice not in ("1", "2", "3", "4"):
            if choice != "":
                print("\33[93m" "Mauvais choix !" "\33[00m")
            choice = input("\nChoix N° :")
        if choice == "2":
            print(
                f"\33[91m/!\\ Voulez vous vraiment supprimer le club {clubs_data.name} ?\33[00m")
            print("\33[93m" "/!\\ Cette action est irréversible." "\33[00m")
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
        print("[\33[93m" "1" "\33[00m] Nom : " + club.name)
        print("[\33[93m" "2" "\33[00m] Identification national : " +
              club.national_id)
        print("[\33[93m" "3" "\33[00m] Retour")
        while choice not in ("1", "2", "3"):
            if choice != "":
                print("\33[93m" "Mauvais choice !" "\33[00m")
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
