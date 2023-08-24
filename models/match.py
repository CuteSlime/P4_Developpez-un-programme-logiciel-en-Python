import random
# from .joueur import Joueur
# from .tour import Tour


class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.match_print()

    def match_print(self):
        x = [self.joueur1.full_name(), self.joueur1.score]
        y = [self.joueur2.full_name(), self.joueur2.score]
        return (x, y)

    def play_match(self):
        winner = random()
        if winner > 0.5:
            print(self.joueur1.full_name(), "gagne !")
            self.joueur1.score += 1

        elif winner < 0.5:
            print(self.joueur2.full_name(), "gagne !")
            self.joueur2.score += 1
        else:
            print('c\'est une égalité !')
            self.joueur1.score += 0.5
            self.joueur2.score += 0.5
        print(self.match_print(), "teste")
        return self.match_print()

    def __repr__(self) -> str:
        self.match
