class Controller:
    '''Main controller'''

    def __init__(self, view, menu):

        self.view = view
        self.menu = menu

# créer un tournois

    def run(self):

        while True:
            self.menu.main_menu()

    # def test(self):
    #     '''teste appeler depuis main (en changeant le run par test)'''
    #     list_tournois = database_access("tournois", Tournoi, "r")
    #     tournoi = list_tournois[2]
    #     print(tournoi)
    #     tournoi.nom = "tata"
    #     print(tournoi)
    #     update_database(
    #         tournoi, list_tournois[2], list_tournois, "tournois", Tournoi)
