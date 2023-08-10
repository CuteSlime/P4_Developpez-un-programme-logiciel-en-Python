

class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2

    def match_print(self):
        x = [self.joueur1.full_name(), self.joueur1.score]
        y = [self.joueur2.full_name(), self.joueur2.score]
        return (x, y)

    def __repr__(self) -> str:
        self.match
