from datetime import datetime


def validate_national_id(national_id):
    if national_id != 7 or (national_id[0:1].isalpha() is False) or (national_id[2:].isnumeric() is False):
        return False
    return True


class Views:
    '''vue principal appellant les autres'''

    def menu_principal(self):
        '''menu principal'''

        choix = ""
        print("Bonjour, /nBienvenu dans l'outils de gestion de tournois./nQue souhaiter vous faire ?")
        print("[1] Gérer les tournois en cours")
        print("[2] Gérer les tournois")
        print("[3] Gérer les joueur")
        print("[4] Gérer les club")
        print("[5] Quitter")

        while choix not in ("1", "2", "3", "4"):
            if choix != "":
                print("Mauvais choix !")
            choix = input("Choix N° :")
        return choix

    def tournois_actuel(self, tournoi, participants, matchs):
        '''gestion des tournois actif'''

        choix = ""
        print(f"Bienvenu au tournoi {tournoi.nom} ")
        print(f"Le tournois en est au tour N°{tournoi.numero_tour_actuel}")
        print("[1] Commencer le round actuel")
        print("[2] Liste des participants")
        print("[3] Liste des match")
        print("[4] Retour au menu principal")

        while choix not in ("1", "2", "3", "4"):
            if choix != "":
                print("Mauvais choix !")
            choix = input("Choix N° :")
        if choix == "2":
            print(participants)

            choix = input("Choix N° :")
        if choix == "3":
            print(matchs)
            choix = input("Choix N° :")
        return choix

# gestion des tournois
    def menu_tournois(self):
        '''menu de gestion des tournois'''

        choix = ""
        print("Menu de gestion des tournois")
        print("[1] Lister les tournois actuel")
        print("[2] Créer un nouveau tournoi")
        print("[3] Retour au menu principal")
        while choix not in ("1", "2", "3"):
            if choix != "":
                print("Mauvais choix !")
            choix = input("Choix N° :")
        return choix

    def list_tournois(self, liste_tournois):
        '''liste des tournois existant'''

        choix = 0
        print("Liste des tournois actuel")
        for id_tournoi, tournoi in enumerate(liste_tournois, start=1):
            print(f"[{id_tournoi}] {tournoi}")

        while choix not in range(1, len(liste_tournois)+1):
            if choix != 0:
                print("Mauvais choix !")
            choix = int(input("Tournoi N° :"))
        return (choix - 1)

    def creer_tournoi(self):
        '''formulaire de creation de tournoi'''
        cls = "Tournoi"
        nom = input("Nom du tournois :")
        lieu = input("Lieu du déroulement :")
        while True:
            try:
                date_debut = datetime.strptime(
                    input("Date de début au format JJ/MM/AAAA :"), "%d/%m/%Y").strftime("%d/%m/%Y")
                break
            except ValueError:
                print("Format invalide, exemple de format valide : 31/08/2023")
        while True:
            try:
                date_fin = datetime.strptime(
                    input("Date de fin au format JJ/MM/AAAA :"), "%d/%m/%Y").strftime("%d/%m/%Y")
                break
            except ValueError:
                print("Format invalide, exemple de format valide : 31/08/2023")

        nb_tour = int(input("Nombre de tour :") or 4)
        tournoi = (cls, nom, lieu, date_debut, date_fin, nb_tour)

        return tournoi

    def gestion_tournoi(self, tournois_data):
        '''menu de gestion d'un tournoi'''

        choix = ""
        print("Menu de gestion du tournoi")
        print(tournois_data)
        print("[1] Modifier le tournoi")
        print("[2] Suprimer le tournoi")
        print("[3] Retour a la liste des tournois")
        print("[4] Retour au menu principal")

        while choix not in ("1", "2", "3", "4"):
            if choix != "":
                print("Mauvais choix !")
            choix = input("Choix N° :")
        if choix == "2":
            print(
                f"/!\\ Voulez vous vraiment supprimer le tournoi {tournois_data.nom} ?")
            print("/!\\ Cette action est irréversible.")
            while choix != "O" and choix != "n" and choix != "N":
                choix = input("[O/n] :")
            if choix == "O":
                return "2"

        return choix

    def menu_modification_tournoi(self, tournoi):
        '''formulaire d'édition d'un tournois'''
        choix = ""
        print("Modification du tournoi " + tournoi.nom)
        print("Que voulez vous modifier ?")
        print("[1] Nom : " + tournoi.nom)
        print("[2] Lieu : " + tournoi.lieu)
        print("[3] Date de debut : " + tournoi.date_debut)
        print("[4] Date de fin : " + tournoi.date_fin)
        print("[5] Nombre de tour : ", tournoi.nb_tour)
        print("[6] Ajouter un joueur")
        print("[7] Retirer un joueur")
        print("[8] Retour")
        while choix not in ("1", "2", "3", "4", "5", "6", "7", "8"):
            if choix != "":
                print("Mauvais choix !")
            choix = input("Choix N° :")
        return choix

    def update_nom_tournoi(self, tournoi):
        print("Nom actuel : " + tournoi.nom)
        nouveau_nom = input("Nouveau nom : ")
        return nouveau_nom

    def update_lieu_tournoi(self, tournoi):
        print("Lieu actuel : " + tournoi.lieu)
        nouveau_lieu = input("Nouveau lieu : ")
        return nouveau_lieu

    def update_date_debut_tournoi(self, tournoi):
        print("Date de debut actuel : " + tournoi.date_debut)
        nouvelle_date_debut = input("Nouvelle date de debut : ")
        return nouvelle_date_debut

    def update_date_fin_tournoi(self, tournoi):
        print("Date de fin actuel : " + tournoi.date_fin)
        nouvelle_date_fin = input("Nouvelle date de fin : ")
        return nouvelle_date_fin

    def update_nb_tour_tournoi(self, tournoi):
        print("Nombre de tour actuel : " + str(tournoi.nb_tour))
        nouveau_nb_tour = input("Nouveau nombre de tour : ")
        return nouveau_nb_tour

# gestion des joueurs
    def menu_joueurs(self):
        '''menu de gestion des joueurs'''

        choix = ""
        print("Menu de gestion des joueurs")
        print("[1] Lister les joueurs actuel")
        print("[2] Créer un nouveau joueur")
        print("[3] Retour au menu principal")
        while choix not in ("1", "2", "3", "4"):
            if choix != "":
                print("Mauvais choix !")
            choix = input("Choix N° :")
        return choix

    def list_joueurs(self, liste_joueurs):
        '''liste des joueurs existant'''
        choix = 0
        print("Liste des joueurs actuel")
        for id_joueur, joueur in enumerate(liste_joueurs, start=1):
            print(f"[{id_joueur}] {joueur}")

        while choix not in range(1, len(liste_joueurs)+1):
            if choix != 0:
                print("Mauvais choix !")
            choix = int(input("Joueur N° :"))
        return (choix - 1)

    def creer_joueur(self):
        '''formulaire de creation de joueur'''

        cls = "Joueur"
        nom = input("Nom du joueur :")
        prenom = input("Prenom du joueur :")
        date_naissance = input("Date de naissance au format JJ/MM/AAAA :")
        club = input("Club :")
        joueur = (cls, nom, prenom, date_naissance, club)
        # vérifier si la date et le club sont valide
        return joueur

    def gestion_joueur(self, joueurs_data):
        '''menu de de modification d'un joueur'''

        choix = ""
        print("Menu de gestion des joueurs")
        print(joueurs_data)
        print("[1] Modifier le joueur")
        print("[2] Suprimer le joueur")
        print("[3] Retour a la liste des joueurs")
        print("[4] Retour au menu principal")
        while choix not in ("1", "2", "3", "4"):
            if choix != "":
                print("Mauvais choix !")
            choix = input("Choix N° :")
        if choix == "2":
            print(
                f"/!\\ Voulez vous vraiment supprimer le joueur {joueurs_data.nom} ?")
            print("/!\\ Cette action est irréversible.")
            while choix != "O" and choix != "n" and choix != "N":
                choix = input("[O/n] :")
            if choix == "O":
                return "2"

        return choix

    def menu_modification_joueur(self, joueur):
        '''formulaire d'édition d'un joueur'''
        choix = ""
        print("Modification du joueur " + joueur.nom)
        print("Que voulez vous modifier ?")
        print("[1] Nom : " + joueur.nom)
        print("[2] Prenom : " + joueur.prenom)
        print("[3] Date de naissance : " + joueur.date_naissance)
        print("[4] Club : " + joueur.club)

        print("[5] Retour")
        while choix not in ("1", "2", "3", "4", "5"):
            if choix != "":
                print("Mauvais choix !")
            choix = input("Choix N° :")
        return choix

    def update_nom_joueur(self, joueur):
        print("Nom actuel : " + joueur.nom)
        nouveau_nom = input("Nouveau nom : ")
        return nouveau_nom

    def update_prenom_joueur(self, joueur):
        print("Prenom actuel : " + joueur.prenom)
        nouveau_lieu = input("Nouveau prenom : ")
        return nouveau_lieu

    def update_date_naissance_joueur(self, joueur):
        print("Date de naissance actuel : " + joueur.date_naissance)
        nouvelle_date_debut = input("Nouvelle date de naissance : ")
        return nouvelle_date_debut

    def update_club_joueur(self, joueur):
        print("Club actuel : " + joueur.club)
        nouvelle_date_fin = input("Nouveau club : ")
        return nouvelle_date_fin

# gestion des club

    def menu_clubs(self):
        '''menu de gestion des club'''

        choix = ""
        print("Menu de gestion des clubs")
        print("[1] Lister les clubs actuel")
        print("[2] Ajouter un nouveau club")
        print("[3] Retour au menu principal")
        while choix not in ("1", "2", "3"):
            if choix != "":
                print("Mauvais choix !")
            choix = input("Choix N° :")
        return choix

    def list_clubs(self, liste_clubs):
        '''liste des clubs existant'''

        choix = 0
        print("Liste des clubs actuel")
        for id_club, club in enumerate(liste_clubs, start=1):
            print(f"[{id_club}] {club}")

        while choix not in range(1, len(liste_clubs) + 1):
            if choix != 0:
                print("Mauvais choix !")
            choix = int(input("Club N° :"))
        return (choix - 1)

    def creer_club(self):
        '''formulaire de creation de club'''

        cls = "Club"
        nom = input("Nom du club :")
        national_id = input("Numéro d'identification national :").upper()
        while validate_national_id(national_id) is False:
            print("Identifiant national invalide")
            national_id = input("Numéro d'identification national :")

        club = (cls, nom, national_id)
        return club

    def gestion_club(self, clubs_data):
        '''menu de de modification d'un club'''

        choix = ""
        print("Menu de gestion des clubs")
        print(clubs_data)
        print("[1] Modifier le club")
        print("[2] Suprimer le club")
        print("[3] Retour a la liste des clubs")
        print("[4] Retour au menu principal")

        while choix not in ("1", "2", "3", "4"):
            if choix != "":
                print("Mauvais choix !")
            choix = input("Choix N° :")
        if choix == "2":
            print(
                f"/!\\ Voulez vous vraiment supprimer le club {clubs_data.nom} ?")
            print("/!\\ Cette action est irréversible.")
            while choix != "O" and choix != "n" and choix != "N":
                choix = input("[O/n] :")
            if choix == "O":
                return "2"
        return choix

    def menu_modification_club(self, club):
        '''formulaire d'édition d'un club'''
        choix = ""
        print("Modification du club " + club.nom)
        print("Que voulez vous modifier ?")
        print("[1] Nom : " + club.nom)
        print("[2] Identification national : " + club.identifiant_national)
        print("[3] Retour")
        while choix not in ("1", "2", "3"):
            if choix != "":
                print("Mauvais choix !")
            choix = input("Choix N° :")
        return choix

    def update_nom_club(self, club):
        print("Nom actuel : " + club.nom)
        nouveau_nom = input("Nouveau nom : ")
        return nouveau_nom

    def update_identifiant_national_club(self, club):
        print("Identification national actuel : " + club.identifiant_national)
        nouvelle_id = input("Nouvelle identification national : ")
        return nouvelle_id
