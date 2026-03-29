from personnage import Personnage
import random

class Monstre(Personnage):
    pass

monstre_1 = Monstre("Squelette", 15, 5, 2)
monstre_2 = Monstre("Fantôme", 20, 10, 5)
monstre_3 = Monstre("Vampire", 25, 5, 10)
monstre_4 = Monstre("Gargouille", 45, 5, 5)
monstre_5 = Monstre("Sorcière", 40, 3, 20)

liste_monstres = [monstre_1, monstre_2, monstre_3, monstre_4, monstre_5]