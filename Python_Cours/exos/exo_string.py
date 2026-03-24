################################################################################
#                                                                              #
#   100 EXERCICES PYTHON — À COMPLÉTER                                         #
#                                                                              #
#   Cours : Data Science with Python (Chap. 7-9)                               #
#   © Félix Déage - 2026                                                       #
#                                                                              #
#   CONSIGNES :                                                                #
#   - Remplacez chaque _____ par la bonne valeur ou expression.                #
#   - Lancez le fichier avec : python exos_7-9.py                              #
#   - Si tout est correct, chaque exercice affichera "OK".                     #
#   - Si une réponse est fausse, vous verrez "ERREUR à l'exercice X".          #
#                                                                              #

################################################
# Compteur pour suivre les résultats
total = 100
reussis = 0

def check(numero, obtenu, attendu):
    global reussis
    if obtenu == attendu:
        reussis += 1
        print(f"  Exercice {numero:>3} : OK")
    else:
        print(f"  Exercice {numero:>3} : ERREUR — attendu {repr(attendu)}, obtenu {repr(obtenu)}")
################################################################################

################################################################################
#  CHAPITRE 7 — Strings I                                                      #
################################################################################
 
print("\n=== Chapitre 7 : Strings I ===\n")
 
# Exercice 31 : Longueur d'une chaîne
check(31, len("Bonjour"), 7)
 
# Exercice 32 : Longueur de la chaîne vide
check(32, len(""), 0)
 
# Exercice 33 : Concaténation de chaînes
check(33, "Bon" + "jour", "Bonjour")
 
# Exercice 34 : Duplication de chaîne
check(34, "ha" * 3, "hahaha")
 
# Exercice 35 : Accéder au premier caractère (index 0 !)
check(35, "Python"[0], "P")
 
# Exercice 36 : Accéder au dernier caractère avec un index positif
check(36, "Python"[5], "n")
 
# Exercice 37 : .upper()
check(37, "bonjour".upper(), "BONJOUR")
 
# Exercice 38 : .lower()
check(38, "SALUT".lower(), "salut")
 
# Exercice 39 : .capitalize() met une majuscule au début, minuscules après
check(39, "bONJOUR tout le MONDE".capitalize(), "Bonjour tout le monde")
 
# Exercice 40 : .count() — compte les occurrences
check(40, "abracadabra".count("a"), 5)
 
# Exercice 41 : .find() — retourne la position de la sous-chaîne
check(41, "Bonjour le monde".find("monde"), 11)
 
# Exercice 42 : .find() quand la sous-chaîne n'existe pas
check(42, "Bonjour".find("xyz"), -1)
 
# Exercice 43 : .replace()
check(43, "chat".replace("ch", "r"), "rat")
 
# Exercice 44 : .strip() enlève les espaces aux extrémités
check(44, "   hello   ".strip(), "hello")
 
# Exercice 45 : Conversion en string avec str()
check(45, "Il y a " + str(42) + " réponses", "Il y a 42 réponses")
 
 
################################################################################
#  CHAPITRE 8 — Manipuler les strings                                          #
################################################################################
 
print("\n=== Chapitre 8 : Manipuler les strings ===\n")
 
# Exercice 46 : "in" pour tester la présence d'une sous-chaîne
check(46, "bon" in "bonjour", True )
 
# Exercice 47 : "not in"
check(47, "xyz" not in "abcdef", True)
 
# Exercice 48 : .split() par défaut (découpe sur les espaces)
check(48, "un deux trois".split(),['un','deux','trois'] )
 
# Exercice 49 : .split() avec un séparateur personnalisé
check(49, "a;b;c".split(";"), ['a','b','c'])
 
# Exercice 50 : .join() — le séparateur est AVANT .join()
check(50, "-".join(["x", "y", "z"]), 'x-y-z')
 
# Exercice 51 : .join() avec chaîne vide (colle tout ensemble)
check(51, "".join(["P", "y", "t", "h", "o", "n"]), "Python")
 
# Exercice 52 : .replace() pour supprimer un caractère (remplacer par "")
check(52, "J'aime les pommes".replace("e", ""),"J'aim ls pomms")
 
# Exercice 53 : .count() — attention, les majuscules comptent !
check(53, "Ananas ANANAS ananas".count("ananas"), 1)
 
# Exercice 54 : f-string (interpolation)
nom = "Alice"
age = 25
check(54, f"{nom} a {age} ans", "Alice a 25 ans")
 
# Exercice 55 : f-string avec un calcul à l'intérieur
check(55, f"2 + 3 = {2 + 3}", "2 + 3 = 5")
 
# Exercice 56 : .format() — méthode historique
check(56, "Je suis {}".format("content"), "")
 
# Exercice 57 : ord() — code Unicode de "A"
check(57, ord("A"), 65)
 
# Exercice 58 : chr() — caractère Unicode 97
check(58, chr(97), 'a')
 
# Exercice 59 : chr(ord(x)) redonne x
check(59, chr(ord("Z")), "Z")
 
# Exercice 60 : .rjust() — aligne à droite sur 6 caractères
check(60, "abc".rjust(6), "...abc")
 
 
################################################################################
#  CHAPITRE 9 — Booléens                                                       #
################################################################################
 
print("\n=== Chapitre 9 : Booléens ===\n")
 
# Exercice 61 : La valeur True
check(61, True, True)
 
# Exercice 62 : not True
check(62, not True, False)
 
# Exercice 63 : not False
check(63, not False, True)
 
# Exercice 64 : Test d'égalité
check(64, 5 == 5, True)
 
# Exercice 65 : Test d'inégalité
check(65, 5 != 3, True)
 
# Exercice 66 : Comparaison
check(66, 10 > 20, False)
 
# Exercice 67 : Inférieur ou égal
check(67, 5 <= 5, True)
 
# Exercice 68 : and — les deux doivent être vrais
check(68, True and False, False)
 
# Exercice 69 : and — les deux sont vrais
check(69, True and True, True)
 
# Exercice 70 : or — au moins un doit être vrai
check(70, False or True, True)
 
# Exercice 71 : or — les deux sont faux
check(71, False or False, False)
 
# Exercice 72 : Combinaison avec and
check(72, 10 > 5 and 10 < 20, True)
 
# Exercice 73 : not avec une expression entre parenthèses
check(73, not (3 > 5), True)
 
# Exercice 74 : Comparaison chaînée — toutes vraies
check(74, 1 < 2 < 3, True)
 
# Exercice 75 : Comparaison chaînée — au moins une fausse
check(75, 1 < 3 < 2, False)
 
# Exercice 76 : True (booléen) vs "True" (string) — ce n'est PAS pareil !
check(76, True == "True", False)
 
# Exercice 77 : Combinaison complexe
A = True
B = False
check(77, (A and B) or ((not B) and A), True)
 
# Exercice 78 : Précédence — not est évalué avant and
check(78, not False and True, True)
 
# Exercice 79 : Précédence — and est évalué avant or
check(79, True or False and False, True)
 
# Exercice 80 : "in" retourne un booléen
check(80, "ab" in "abcd", True)
