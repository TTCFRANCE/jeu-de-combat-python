# RPG - Jeu de Combat (Python - Console)

## Description
Ce projet est un mini RPG en console où le joueur combat des monstres aléatoires.  
Chaque personnage possède des points de vie, d'attaque et de défense, et le joueur peut choisir entre attaquer ou défendre.

## Objectif
J'ai réalisé ce projet pour apprendre :
- la programmation orientée objet (classes, héritage)
- la gestion des interactions entre objets (joueur vs monstre)
- la création d’un mini-jeu interactif en console
- la logique de combat et la prise de décision utilisateur

## Fonctionnalités
- Choix du joueur : attaquer ou défendre
- Combat contre des monstres aléatoires
- Gestion des points de vie, d’attaque et de défense
- Affichage dynamique des dégâts et de la vie restante
- Héritage : `Monstre` hérite de `Personnage`

## Architecture
- `main.py` : point d’entrée du jeu
- `personnage.py` : classe `Personnage` avec vie, attaque et défense
- `monstre.py` : classe `Monstre` héritée de `Personnage` et liste de monstres
- `combat.py` : fonction `lancer_combat` qui gère les tours de combat

## Technologies utilisées
- Python

## Lancer le projet
1. Installer Python
2. Exécuter le fichier principal :
```bash
python main.py
