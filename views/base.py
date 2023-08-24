class Views:
    '''vue principal appellant les autres'''

    def menu_principal():
        choix = 0
        print("Bonjour, /nBienvenu dans l'outils de gestion de tournois./nQue souhaiter vous faire ?")
        print("[1] gérer les tournois")
        print("[2] gérer les joueur")
        print("[3] gérer les club")
        print("[4] quitter")

        while choix != "1" and choix != "2" and choix != "3" and choix != "4":
            choix = input("choix N° :")
        return choix

    # gestion des tournois
    def gestion_tournois():
        choix = 0
        print("Menu de gestion des tournois")
        print("[1] lister les tournois actuel")
        print("[2] créer un nouveau tournoi")
        print("[3] retour au menu principal")
        while choix != "1" and choix != "2" and choix != "3":
            choix = input("choix N° :")
        return choix

    def list_tournois(liste_tournois):
        print("liste des tournois actuel")
        print(liste_tournois)

        choix = input("tournois N° :")
        return choix

    def creer_tournoi():
        nom = input("Nom du tournois :")
        lieu = input("Lieu du déroulement :")
        date_debut = input("date de début au format JJ/MM/AAAA :")
        date_fin = input("date de fin au format JJ/MM/AAAA :")
        nb_tour = input("choix N° :")
        tournoi = (nom, lieu, date_debut, date_fin, nb_tour)
        return tournoi

    def modifier_tournoi():
        choix = 0
        print("Menu de gestion des tournois")
        print("[2] modifier un tournoi")
        print("[3] suprimer un tournoi")
        print("[3] retour au menu principal")

        while choix != "1" and choix != "2" and choix != "3":
            choix = input("choix N° :")
        return choix

    def menu_club():
        choix = 0
        print("Menu de gestion des clubs")
        print("[1] créer un club")
        print("[2] modifier un club")
        print("[3] suprimer un club")
        print("[4] retour au menu principal")

        while choix != "1" and choix != "2" and choix != "3":
            choix = input("choix N° :")
        return choix

    def menu_joueur():
        choix = 0
        print("Menu de gestion des joueurs")
        print("[1] créer un joueur")
        print("[2] modifier un joueur")
        print("[3] suprimer un joueur")
        print("[4] retour au menu principal")

        while choix != "1" and choix != "2" and choix != "3":
            choix = input("choix N° :")
        return choix
