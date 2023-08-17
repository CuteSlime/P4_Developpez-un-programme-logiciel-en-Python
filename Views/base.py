
def menu_principal():
    print("Bonjour, /nBienvenu dans l'outils de gestion de tournois./nQue souhaiter vous faire ?")
    print("[1] gérer les tournois")
    print("[2] gérer les joueur")
    print("[3] gérer les club")
    print("[4] quitter")

    choix = input("choix N° :")
    return choix


def menu_tournois():
    print("Menu de gestion des tournois")
    print("[1] créer un tournoi")
    print("[2] modifier un tournoi")
    print("[3] suprimer un tournoi")
    print("[4] retour au menu principal")

    choix = input("choix N° :")
    return choix


def menu_club():
    print("Menu de gestion des clubs")
    print("[1] créer un club")
    print("[2] modifier un club")
    print("[3] suprimer un club")
    print("[4] retour au menu principal")

    choix = input("choix N° :")
    return choix


def menu_joueur():
    print("Menu de gestion des joueurs")
    print("[1] créer un joueur")
    print("[2] modifier un joueur")
    print("[3] suprimer un joueur")
    print("[4] retour au menu principal")

    choix = input("choix N° :")
    return choix
