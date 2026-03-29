from personnage import Personnage
from monstre import liste_monstres
from combat import lancer_combat
import random

joueur = Personnage("Player 1", 50, 15, 5)
monstre = random.choice(liste_monstres)

print("Un ennemi apparaît :", monstre.nom)

# Lancer le combat
lancer_combat(joueur, monstre)