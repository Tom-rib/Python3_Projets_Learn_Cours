################################################################################
#                                                                              #
#   100 EXERCICES PYTHON — À COMPLÉTER                                         #
#                                                                              #
#   Cours : Data Science with Python (Chap. 10-12)                             #
#   © Félix Déage - 2026                                                       #
#                                                                              #
#   CONSIGNES :                                                                #
#   - Remplacez chaque _____ par la bonne valeur ou expression.                #
#   - Lancez le fichier avec : python exos_10-12.py                            #
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
#  CHAPITRE 10 — Variables                                                     #
################################################################################
 
print("\n=== Chapitre 10 : Variables ===\n")
 
# Exercice 81 : Affectation simple
x = 10
check(81, x, 10)
 
# Exercice 82 : Réaffectation — la nouvelle valeur écrase l'ancienne
x = 10
x = 25
check(82, x, 25)
 
# Exercice 83 : Incrémentation avec +=
x = 10
x += 5
check(83, x, 15)
 
# Exercice 84 : Décrémentation avec -=
x = 20
x -= 7
check(84, x, 13)
 
# Exercice 85 : Multiplication avec *=
x = 3
x *= 4
check(85, x, 12)
 
# Exercice 86 : x = x + 1 trois fois de suite
x = 0
x = x + 1
x = x + 1
x = x + 1
check(86, x, 3)
 
# Exercice 87 : type() sur un booléen
check(87, type(True), bool)
 
# Exercice 88 : type() sur une string
check(88, type("hello"), str)
 
# Exercice 89 : str() pour convertir un entier en string
check(89, str(123),"123")
 
# Exercice 90 : Affectation multiple
a, b, c = 10, 20, 30
check(90, a + b + c, 60)
 
 
################################################################################
#  CHAPITRE 12 — Structures de contrôle : if, elif, else                       #
################################################################################
 
print("\n=== Chapitre 12 : if / elif / else ===\n")
 
# Exercice 91 : if simple — la condition est-elle remplie ?
x = 15
if x > 10:
    resultat_91 = "grand"
else:
    resultat_91 = "petit"
check(91, resultat_91, "grand")
 
# Exercice 92 : if simple — et ici ?
x = 3
if x > 10:
    resultat_92 = "grand"
else:
    resultat_92 = "petit"
check(92, resultat_92, "petit")
 
# Exercice 93 : elif — trois cas possibles
x = 5
if x > 10:
    resultat_93 = "grand"
elif x > 0:
    resultat_93 = "moyen"
else:
    resultat_93 = "négatif"
check(93, resultat_93, "moyen")
 
# Exercice 94 : elif — cas négatif
x = -3
if x > 10:
    resultat_94 = "grand"
elif x > 0:
    resultat_94 = "moyen"
else:
    resultat_94 = "négatif"
check(94, resultat_94,"négatif")
 
# Exercice 95 : Condition avec and dans le if
x = 15
if x > 10 and x < 20:
    resultat_95 = "entre 10 et 20"
else:
    resultat_95 = "ailleurs"
check(95, resultat_95, "entre 10 et 20")
 
# Exercice 96 : Condition avec or dans le if
x = 100
if x < 0 or x > 50:
    resultat_96 = "extrême"
else:
    resultat_96 = "normal"
check(96, resultat_96, "extrême")
 
# Exercice 97 : Fonction par morceaux (vue dans le cours !)
#          / 2x + 3   si x < 0
# f(x) = -  3 − x     si 0 ≤ x < 2
#          \ x² − 3   si x ≥ 2
def f(x):
    if x < 0:
        return 2 * x + 3
    elif x < 2:
        return 3 - x
    else:
        return x ** 2 - 3
check(97, f(-1), 1)
 
# Exercice 98 : Même fonction, autre valeur
check(98, f(1),2)

 
# Exercice 99 : Même fonction, encore une autre valeur
check(99, f(5), 22)
 
# Exercice 100 : if imbriqués
x, y = 10, 5
if x > y:
    if x > 2 * y:
        resultat_100 = "bien plus grand"
    else:
        resultat_100 = "un peu plus grand"
else:
    resultat_100 = "plus petit ou égal"
check(100, resultat_100, "un peu plus grand")
