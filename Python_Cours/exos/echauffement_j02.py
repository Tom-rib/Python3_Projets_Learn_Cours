"""
La Plateforme - Runtrack Renfo J02 - 17/03/26

╔═════════════════════════════════════════════════════════════════╗
║                                                                 ║
║              MISSION 0 — L'ÉCHAUFFEMENT PYTHON                  ║
║                                                                 ║
║  10 micro-exercices pour vérifier les bases                     ║
║  Durée cible : 30 minutes (~3 min par exo)                      ║
║  Écris ton code dans ce fichier, sous chaque énoncé.            ║
║                                                                 ║
║  Règles :                                                       ║
║  - Pas de Google, pas de ChatGPT, pas de StackOverflow          ║
║  - Si tu bloques plus de 3 min, passe au suivant.               ║
║  - Les 6 premiers sont obligatoires, les 4 derniers sont plus   ║
║    plus durs                                                    ║
║                                                                 ║
╚═════════════════════════════════════════════════════════════════╝
"""


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCICE 1 — Types et conversions
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Sans exécuter le code, prédis ce que chaque ligne affiche.
# Ensuite, vérifie en exécutant.
#
# print(type(42))
# print(type(3.14))
# print(type("42"))
# print(type(True))
# print(type(None))
# print(42 == "42")
# print(int("42") == 42)
# print(bool(""))
# print(bool("0"))
# print(bool(0))
#
# Écris tes prédictions en commentaire, puis exécute :

# Tes prédictions :
# type(42)      → int
# type(3.14)    → float
# type("42")    → string
# type(True)    → booléen
# type(None)    → ??
# 42 == "42"    →  string
# int("42")==42 → 
# bool("")      → ???
# bool("0")     → ???
# bool(0)       → ???


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCICE 2 — Variables et opérations
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# a) Crée deux variables `prix_ht` (100) et `taux_tva` (0.20).
#    Calcule et affiche le prix TTC.
#
# b) Tu as une durée en secondes : `duree = 3672`.
#    Affiche le résultat en heures, minutes, secondes.
#    Format attendu : "1h 1min 12s"
#    (Indice : // et %)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCICE 3 — Conditions
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Écris une fonction `categorie_age(age)` qui retourne :
#   - "mineur"    si age < 18
#   - "jeune"     si 18 <= age < 25
#   - "adulte"    si 25 <= age < 65
#   - "senior"    si age >= 65
#   - "invalide"  si age est négatif
#
# Teste-la avec : 15, 18, 24, 25, 64, 65, -3

def categorie_age(age):
    if age < 18:
        return 'mineur'
    elif age <= 18 and age < 25:
        return 'jeune'
    elif age <=25 and age < 65:
        return 'adulte'
    elif age => 65:
        return 'senior'
    return 'invalide'


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCICE 4 — Boucle for
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# a) Affiche les nombres de 1 à 20, mais :
#    - remplace les multiples de 3 par "Fizz"
#    - remplace les multiples de 5 par "Buzz"
#    - remplace les multiples de 3 ET 5 par "FizzBuzz"
#
#    Résultat attendu :
#    1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14,
#    FizzBuzz, 16, 17, Fizz, 19, Buzz
#
# b) Calcule la somme de tous les nombres pairs de 1 à 100.
#    (Résultat attendu : 2550)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCICE 5 — Boucle while
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Écris une fonction `devine_nombre()` :
#   - Elle choisit un nombre secret entre 1 et 50 (utilise random.randint)
#   - L'utilisateur tape des essais avec input()
#   - À chaque essai, la fonction dit "Plus grand", "Plus petit" ou "Bravo !"
#   - Elle affiche le nombre d'essais à la fin
#
# (Pour tester sans input, tu peux d'abord coder une version où
#  le "joueur" est une liste d'essais prédéfinis)

import random

def devine_nombre():
    pass  # ← remplace par ton code


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCICE 6 — Listes
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Tu as cette liste :
#   notes = [12, 17, 8, 15, 9, 14, 18, 6, 11, 16]
#
# SANS utiliser les fonctions built-in min(), max(), sum(), sorted() :
#
# a) Trouve et affiche la note la plus haute
# b) Trouve et affiche la note la plus basse
# c) Calcule et affiche la moyenne
# d) Compte combien de notes sont au-dessus de la moyenne

notes = [12, 17, 8, 15, 9, 14, 18, 6, 11, 16]


"""
Ces exos sont plus costauds, pas de panique si vous n'y arrivez pas !
"""

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCICE 7 — Dictionnaires                            [COSTAUD]
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Tu as ce dictionnaire :
#   inventaire = {
#       "pommes": 5,
#       "bananes": 2,
#       "oranges": 8,
#       "kiwis": 0,
#       "mangues": 3
#   }
#
# a) Affiche chaque fruit et sa quantité, un par ligne
# b) Affiche uniquement les fruits dont le stock est vide (0)
# c) Calcule le nombre total de fruits en stock
# d) Écris une fonction `acheter(inventaire, fruit, quantite)` qui :
#    - augmente le stock si le fruit existe
#    - ajoute le fruit au dict s'il n'existe pas
#    - refuse si la quantité est négative (affiche une erreur)

inventaire = {
    "pommes": 5,
    "bananes": 2,
    "oranges": 8,
    "kiwis": 0,
    "mangues": 3,
}


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCICE 8 — Strings                                  [COSTAUD]
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Écris une fonction `est_palindrome(mot)` qui retourne True si le mot
# est un palindrome (se lit pareil à l'endroit et à l'envers).
#
# Contraintes :
# - Ignore la casse ("Kayak" → True)
# - Ignore les espaces ("e s s e" → True)
# - N'utilise PAS [::-1] (fais-le avec une boucle)
#
# Tests :
#   est_palindrome("kayak")     → True
#   est_palindrome("Kayak")     → True
#   est_palindrome("python")    → False
#   est_palindrome("e s s e")   → True
#   est_palindrome("")          → True

def est_palindrome(mot):
    pass  # ← remplace par ton code


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCICE 9 — Fonctions et décomposition               [COSTAUD]
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Écris un programme qui vérifie la solidité d'un mot de passe.
#
# Un mot de passe est "fort" s'il respecte TOUTES ces règles :
#   - Au moins 8 caractères
#   - Contient au moins une majuscule
#   - Contient au moins une minuscule
#   - Contient au moins un chiffre
#   - Contient au moins un caractère spécial parmi : !@#$%^&*
#
# Écris UNE fonction par règle, puis une fonction principale
# `verifier_mdp(mdp)` qui les utilise toutes et retourne une liste
# des règles non respectées.
#
# Exemple :
#   verifier_mdp("abc")
#   → ["trop court", "pas de majuscule", "pas de chiffre", "pas de caractère spécial"]
#
#   verifier_mdp("Str0ng!Pass")
#   → []    (liste vide = tout est bon)
#
# Indice : str.isupper(), str.islower(), str.isdigit() existent.

def verifier_mdp(mdp):
    pass  # ← remplace par ton code


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# EXERCICE 10 — Tuples et retours multiples              [COSTAUD]
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#
# Tu as une liste de tuples représentant des élèves et leurs notes :
#
#   eleves = [
#       ("Alice", [15, 12, 18]),
#       ("Bob", [8, 9, 11]),
#       ("Charlie", [14, 16, 13]),
#       ("Diana", [7, 5, 9]),
#       ("Eve", [19, 17, 20]),
#   ]
#
# a) Écris une fonction `moyenne(notes)` qui calcule la moyenne d'une
#    liste de notes.
#
# b) Écris une fonction `bulletin(eleves)` qui affiche :
#      Alice    : 15.00 (mention Bien)
#      Bob      :  9.33 (mention Insuffisant)
#      ...
#
#    Mentions :
#      >= 16 : "Très bien"
#      >= 14 : "Bien"
#      >= 12 : "Assez bien"
#      >= 10 : "Passable"
#      < 10  : "Insuffisant"
#
# c) Écris une fonction `premier_de_classe(eleves)` qui retourne
#    un tuple (nom, moyenne) de l'élève avec la meilleure moyenne.

eleves = [
    ("Alice", [15, 12, 18]),
    ("Bob", [8, 9, 11]),
    ("Charlie", [14, 16, 13]),
    ("Diana", [7, 5, 9]),
    ("Eve", [19, 17, 20]),
]
