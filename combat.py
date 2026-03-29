def lancer_combat(joueur, monstre):

    while joueur.est_vivant() and monstre.est_vivant():
        choix_joueur = int(input("" \
        "1. Attaquer (20 PV sur la cible)\n" \
        "2. Défendre (Réduit de 5 PV la la prochaine attaque de l'ennemi.)\n" \
        "Choix :"))

        if choix_joueur == 1:
            joueur.attaquer(monstre)

        elif choix_joueur == 2:
            joueur.defendre(monstre)

        if monstre.est_vivant():
            monstre.attaquer(joueur)

    if joueur.est_vivant():
        print(joueur.nom, "a gagné !")
    else:
        print(monstre.nom, "a gagné !")