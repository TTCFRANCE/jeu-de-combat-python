class Personnage:
    def __init__(self, nom, vie, attaque, defense):
        self.nom = nom
        self.vie = vie
        self.attaque = attaque
        self.defense = defense

    def attaquer(self, cible):
        print(self.nom, "attaque", cible.nom)
        cible.vie = cible.vie - self.attaque
        print(cible.nom, "perd", self.attaque, "PV.")
        print("La vie de", cible.nom, "est à", cible.vie)

    def defendre(self, cible):
        print(self.nom, "défend l'attaque de", cible.nom)
        cible.attaque = cible.attaque - 5
        print("Défense de",  self.nom, "active : 5 PV")

    def est_vivant(self):
        return self.vie > 0