from Models.Models import Joueur, Tour
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

joueur = Joueur("jean", "jean", 45, [12, 25])
round1 = Tour("round01", "match")
print(vars(joueur), round1.date_debut, round1.date_fin)
round1.tour_fini()
print(round1.date_debut, round1.date_fin)
# RAPPORT

#  liste de tous les joueurs par ordre alphabétique ;
# ● liste de tous les tournois ;
# ● nom et dates d’un tournoi donné ;
# ● liste des joueurs du tournoi par ordre alphabétique ;
# ● liste de tous les tours du tournoi et de tous les matchs du tour
