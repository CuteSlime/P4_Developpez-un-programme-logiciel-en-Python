import json
# from .club import Club


with open('../data/joueurs.json', 'r', encoding='utf8') as joueurs_data:
    joueurs_data = json.load(joueurs_data)
# print(joueurs_data)

list_joueurs = []


def lister_joueurs(joueurs_data):
    for joueur in joueurs_data:
        print(joueur)
        list_joueurs.append(Joueur(**joueur))
    return list_joueurs


class Joueur:
    def __init__(self, nom, prenom, date_naissance, **kwargs):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.score = kwargs.get('score', 0)
        self.club = kwargs.get('club')
# import JSON pour Joueur, plus pour le club du joueur

    def full_name(self):
        return f"{self.prenom} {self.nom}"

    def add_to_joueurs(self):
        if not isinstance(self, Joueur):
            return ValueError("Ceci n'est pas un Joueur valide")
        joueurs_data.append(self.__dict__)
        joueur_json = json.dumps(joueurs_data, indent=4)
        with open('../data/joueurs.json', 'w', encoding='utf8') as jsonfile:
            jsonfile.write(joueur_json)

    def __str__(self):
        return f"{self.full_name()} {self.date_naissance} {self.score} {self.club}"


joueur = Joueur(**joueurs_data[0])


joueur2 = Joueur("Toucuit", "Phillipe", "14 Mars 2001", club="not an actor")
joueur2.add_to_joueurs()
