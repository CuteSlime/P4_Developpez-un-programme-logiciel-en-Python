
from Models.Models import Joueur, Tour, Match, Club

# from Views.Views import
# from Controllers.Controllers import

# Chaque tournoi doit contenir au moins les informations suivantes :
# ● nom ;
# ● lieu ;
# ● date de début et de fin ;
# ● nombre de tours – réglez la valeur par défaut sur 4 ;
# ● numéro correspondant au tour actuel ;
# ● une liste des tours ;
# ● une liste des joueurs enregistrés ;
# ● description pour les remarques générales du directeur du tournoi.
club1 = Club("inconnu", "AB12345")
club2 = Club("titou", "AB12345")
joueur1 = Joueur("jean", "jean", 45, club1)
joueur2 = Joueur("phillipe", "phillipe", 45, club2)
round1 = Tour("round01")

match1 = Match(joueur1, joueur2)
round1.add_match(match1)
print(joueur2.full_name(), round1.date_debut, round1.date_fin)
print(round1.match[0])
print(round1.date_debut, round1.date_fin)
# RAPPORT

#  liste de tous les joueurs par ordre alphabétique ;
# ● liste de tous les tournois ;
# ● nom et dates d’un tournoi donné ;
# ● liste des joueurs du tournoi par ordre alphabétique ;
# ● liste de tous les tours du tournoi et de tous les matchs du tour
