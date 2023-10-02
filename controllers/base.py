class Controller:
    '''Main controller'''

    def __init__(self, view, menu):

        self.view = view
        self.menu = menu

# créer un tournaments

    def run(self):

        while True:
            self.menu.main_menu()

    # def test(self):
    #     '''teste appeler depuis main (en changeant le run par test)'''
    #     list_tournaments = database_access("tournaments", Tournament, "r")
    #     tournament = list_tournaments[2]
    #     print(tournament)
    #     tournament.name = "tata"
    #     print(tournament)
    #     update_database(
    #         tournament, list_tournaments[2], list_tournaments, "tournaments", Tournament)
