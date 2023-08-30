class Views:
    '''vue principal appellant les autres'''

    def menu_principal(self):
        '''menu principal'''

        choix = ""
        print("Bonjour, /nBienvenu dans l'outils de gestion de tournois./nQue souhaiter vous faire ?")
        print("[1] Gérer les tournois")
        print("[2] Gérer les joueur")
        print("[3] Gérer les club")
        print("[4] Quitter")

        while choix != "1" and choix != "2" and choix != "3" and choix != "4":
            choix = input("choix N° :")
        return str(choix)

# gestion des tournois
    def menu_tournois(self):
        '''menu de gestion des tournois'''

        choix = ""
        print("Menu de gestion des tournois")
        print("[1] Lister les tournois actuel")
        print("[2] Créer un nouveau tournoi")
        print("[3] Retour au menu principal")
        while choix != "1" and choix != "2" and choix != "3":
            choix = input("choix N° :")
        return choix

    def list_tournois(self, liste_tournois):
        '''liste des tournois existant'''

        print("Liste des tournois actuel")
        print(liste_tournois)
        id = 0
        for tournoi in liste_tournois:
            id += 1
            print(str(id) + " " + str(tournoi.nom))
        choix = input("Tournois N° :")
        return choix

    def creer_tournoi(self):
        '''formulaire de creation de tournoi'''

        nom = input("Nom du tournois :")
        lieu = input("Lieu du déroulement :")
        date_debut = input("Date de début au format JJ/MM/AAAA :")
        date_fin = input("Date de fin au format JJ/MM/AAAA :")
        nb_tour = input("Nombre de tour :")
        tournoi = (nom, lieu, date_debut, date_fin, nb_tour)
        # vérifier si les date sont valide
        return tournoi

    def gestion_tournoi(self):
        '''menu de de modification d'un tournoi'''

        choix = ""
        print("Menu de gestion des tournois")
        print(tournois_data)
        print("[1] modifier le tournoi")
        print("[2] suprimer le tournoi")
        print("[3] retour a la liste des tournois")
        print("[4] retour au menu principal")

        while choix != "1" and choix != "2" and choix != "3" and choix != "4":
            choix = input("choix N° :")
        return choix

    def menu_modification_tournoi(self, tournoi):
        print("Modification du tournoi " + tournoi.nom)
        print("que voulez vous modifier ?")
        print("[1] Nom : " + tournoi.nom)
        print("[2] Lieu : " + tournoi.lieu)
        print("[3] date de debut : " + tournoi.date_debut)
        print("[4] date de fin : " + tournoi.date_fin)
        print("[5] nombre de tour : " + tournoi.nb_tour)
        choix = input("choix N° :")
        return choix

    def update_nom_tournoi(self, tournoi):
        print("nom actuel : " + tournoi.nom)
        nouveau_nom = input("nouveau nom : ")
        return nouveau_nom

    def update_lieu_tournoi(self, tournoi):
        print("lieu actuel : " + tournoi.lieu)
        nouveau_lieu = input("nouveau lieu : ")
        return nouveau_lieu

    def update_date_debut_tournoi(self, tournoi):
        print("date de debut actuel : " + tournoi.date_debut)
        nouvelle_date_debut = input("nouvelle date de debut : ")
        return nouvelle_date_debut

    def update_date_fin_tournoi(self, tournoi):
        print("date de fin actuel : " + tournoi.date_fin)
        nouvelle_date_fin = input("nouvelle date de fin : ")
        return nouvelle_date_fin

    def update_date_fin_tournoi(self, tournoi):
        print("nombre de tour actuel : " + tournoi.date_fin)
        nouveau_nb_tour = input("nouveau nombre de tour : ")
        return nouveau_nb_tour

# gestion des club

    def menu_clubs(self):
        '''menu de gestion des club'''

        choix = ""
        print("Menu de gestion des clubs")
        print("[1] lister les clubs actuel")
        print("[2] ajouter un nouveau club")
        print("[3] retour au menu principal")
        while choix != "1" and choix != "2" and choix != "3":
            choix = input("choix N° :")
        return choix

    def list_clubs(self, liste_clubs):
        '''liste des clubs existant'''

        print("liste des clubs actuel")
        print(liste_clubs)

        choix = input("clubs N° :")
        return choix

    def creer_club(self):
        '''formulaire de creation de club'''

        nom = input("Nom du club :")
        national_id = input("Numéro d'identification national :")
        club = (nom, national_id)
        # vérifier si le numéro poséde le bon format
        # deux lettres suivies de cinq chiffres (par exemple, AB12345)
        return club

    def gestion_club(self):
        '''menu de de modification d'un club'''

        choix = ""
        print("Menu de gestion des clubs")
        print(clubs_data)
        print("[1] modifier le club")
        print("[2] suprimer le club")
        print("[3] retour a la liste des clubs")
        print("[4] retour au menu principal")

        while choix != "1" and choix != "2" and choix != "3" and choix != "4":
            choix = input("choix N° :")
        return choix

# gestion des joueurs
    def menu_joueurs(self):
        '''menu de gestion des joueurs'''

        choix = ""
        print("Menu de gestion des joueurs")
        print("[1] lister les joueurs actuel")
        print("[2] créer un nouveau joueur")
        print("[3] retour au menu principal")
        while choix != "1" and choix != "2" and choix != "3":
            choix = input("choix N° :")
        return choix

    def list_joueurs(self, liste_joueurs):
        '''liste des joueurs existant'''

        print("liste des joueurs actuel")
        print(liste_joueurs)

        choix = input("joueurs N° :")
        return choix

    def creer_joueur(self):
        '''formulaire de creation de joueur'''

        nom = input("Nom du joueur :")
        prenom = input("Prenom du joueur :")
        date_naissance = input("date de naissance au format JJ/MM/AAAA :")
        club = input("club :")
        joueur = (nom, prenom, date_naissance, club)
        # vérifier si la date et le club sont valide
        return joueur

    def gestion_joueur(self):
        '''menu de de modification d'un joueur'''

        choix = ""
        print("Menu de gestion des joueurs")
        print(joueurs_data)
        print("[1] modifier le joueur")
        print("[2] suprimer le joueur")
        print("[3] retour a la liste des joueurs")
        print("[4] retour au menu principal")

        while choix != "1" and choix != "2" and choix != "3" and choix != "4":
            choix = input("choix N° :")
        return choix
