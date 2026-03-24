################################################################################
#                                                                              #
#   100 EXERCICES PYTHON — À COMPLÉTER                                         #
#                                                                              #
#   Cours : Data Science with Python (Chap. 3-6)                               #
#   © Félix Déage - 2026                                                       #
#                                                                              #
#   CONSIGNES :                                                                #
#   - Remplacez chaque _____ par la bonne valeur ou expression.                #
#   - Lancez le fichier avec : python exercices_python.py                      #
#   - Si tout est correct, chaque exercice affichera "OK".                     #
#   - Si une réponse est fausse, vous verrez "ERREUR à l'exercice X".          #
#                                                                              #
################################################################################

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
#  CHAPITRE 4 — Nombres, opérateurs et arithmétique                            #
################################################################################

print("\n=== Chapitre 4 : Nombres et arithmétique ===\n")

# Exercice 1 : Addition simple
check(1, 7 + 5, 12)

# Exercice 2 : Soustraction
check(2, 20 - 13, 7)

# Exercice 3 : Multiplication
check(3, 6 * 7, 42)

# Exercice 4 : Division (attention au type du résultat !)
check(4, 10 / 2, 5.0)

# Exercice 5 : Division entière
check(5, 17 // 3, 5)

# Exercice 6 : Modulo (reste de la division euclidienne)
check(6, 17 % 3, 2)

# Exercice 7 : Exponentiation (puissance)
check(7, 2 ** 10, 1024 )

# Exercice 8 : Valeur absolue
check(8, abs(-42), 42)

# Exercice 9 : Division entière avec un nombre négatif (arrondi vers le bas !)
check(9, -7 // 2, -4)

# Exercice 10 : Quel est le type du résultat de 8 / 4 ?
check(10, type(8 / 4), float)

# Exercice 11 : Quel est le type du résultat de 8 // 4 ?
check(11, type(8 // 4), int)

# Exercice 12 : Modulo pour tester la parité (0 si pair, 1 si impair)
check(12, 44 % 2, 0)

# Exercice 13 : Modulo pour tester la parité
check(13, 77 % 2, 1)

# Exercice 14 : pow() est équivalent à **
check(14, pow(3, 4), 81)

# Exercice 15 : Mélange d'opérations — attention à la précédence !
check(15, 2 + 3 * 4, 14)


################################################################################
#  CHAPITRE 5 — Précédence des opérateurs                                      #
################################################################################

print("\n=== Chapitre 5 : Précédence des opérateurs ===\n")

# Exercice 16 : Les parenthèses changent l'ordre
check(16, (2 + 3) * 4, 20)

# Exercice 17 : ** est prioritaire sur *
check(17, 2 * 3 ** 2, 18)

# Exercice 18 : Précédence mixte
check(18, 10 - 2 * 3 + 1, 5)

# Exercice 19 : Division et addition
check(19, 1 + 9 / 3, 4.0)

# Exercice 20 : Parenthèses imbriquées
check(20, (5 - 1) * ((7 + 1) / (3 - 1)), 16 )


################################################################################
#  CHAPITRE 6 — Conversions : binaire, décimal, hexadécimal                    #
################################################################################

print("\n=== Chapitre 6 : Conversions ===\n")

# Exercice 21 : Quel est le type de 3 ?
check(21, type(3), int)

# Exercice 22 : Quel est le type de 3.0 ?
check(22, type(3.0), float)

# Exercice 23 : Quel est le type de "3" ?
check(23, type("3"), str)

# Exercice 24 : Est-ce que 3 et 3.0 sont égaux ?
check(24, 3 == 3.0, True)

# Exercice 25 : Conversion binaire → décimal
check(25, 0b1010, 10)

# Exercice 26 : Conversion hexadécimal → décimal
check(26, 0xFF, 255)

# Exercice 27 : bin() retourne quel type ?
check(27, type(bin(42)), str)

# Exercice 28 : hex(255) donne quoi ?
check(28, hex(255), "0xff")

# Exercice 29 : int() avec base 2
check(29, int("101", 2), 5)

# Exercice 30 : int() en base 16
check(30, int("1A", 16), 26)