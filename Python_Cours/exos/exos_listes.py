################################################################################
#                                                                              #
# ██████  ███████           ██████     Data Science with Python - v.0.9        #
# ██   ██ ██                ██   ██    © Félix Déage - 2026                    #
# ██   ██ ███████ ██  █  ██ ██████     License CC BY-SA 4.0 FR                 #
# ██   ██      ██ ██ ███ ██ ██                                                 #
# ██████  ███████  ███ ███  ██         inspired by learnxinyminutes.com        #
#                                                                              #
################################################################################
#               #                                                              #
#  Chap. 16     #  Exercices : les listes (I)                                  #
#               #                                                              #
################################################################################
#
#  30 exercices de difficulté croissante
#
#  Niveaux :
#    ⭐          Fondamentaux (exos 1-10)
#    ⭐⭐        Intermédiaires (exos 11-20)
#    ⭐⭐⭐      Avancés (exos 21-30)
#
#  Consignes :
#    - Chaque exercice est indépendant sauf indication contraire
#    - Testez vos réponses dans un interpréteur Python
#    - Les réponses attendues sont indiquées en commentaire quand c'est utile
#
###########################################


# =============================================================================
#  ⭐ FONDAMENTAUX (1-10)
# =============================================================================

# -----------------------------------------------------------------------------
# Exercice 1 – Créer une liste
# -----------------------------------------------------------------------------
# Créez une liste `fruits` contenant les strings "pomme", "banane" et "cerise".
# Puis affichez-la avec print().


fruits = ["pomme", "banane", "cerise"]
print(fruits)

# -----------------------------------------------------------------------------
# Exercice 2 – Accéder à un élément
# -----------------------------------------------------------------------------
# À partir de la liste suivante :
animaux = ["chat", "chien", "perroquet", "hamster"]

# Affichez "perroquet" en utilisant son indice.
print(animaux[2])



# -----------------------------------------------------------------------------
# Exercice 3 – Indice négatif
# -----------------------------------------------------------------------------
# À partir de la même liste `animaux`, affichez le dernier élément en
# utilisant un indice négatif.

print(animaux[-1])

# -----------------------------------------------------------------------------
# Exercice 4 – Longueur d'une liste
# -----------------------------------------------------------------------------
# Affichez le nombre d'éléments dans la liste suivante :
couleurs = ["rouge", "vert", "bleu", "jaune", "violet"]
# Résultat attendu : 5

nombres= len(couleurs)  
print(nombres)


# -----------------------------------------------------------------------------
# Exercice 5 – Ajouter un élément
# -----------------------------------------------------------------------------
# Partez de la liste suivante :
planetes = ["Mercure", "Vénus", "Terre"]

# Ajoutez "Mars" à la fin de la liste, puis affichez-la.
# Résultat attendu : ["Mercure", "Vénus", "Terre", "Mars"]

planetes.append("Mars")
print(planetes)



# -----------------------------------------------------------------------------
# Exercice 6 – Retirer le dernier élément
# -----------------------------------------------------------------------------
# Partez de la liste suivante :
notes = [12, 15, 8, 17, 9]

# Retirez le dernier élément avec .pop() et stockez-le dans une variable
# `derniere_note`. Affichez `derniere_note` et la liste modifiée.
# Résultat attendu : derniere_note = 9, notes = [12, 15, 8, 17]

derniere_note = notes.pop()
print(derniere_note)    
print(notes)


# -----------------------------------------------------------------------------
# Exercice 7 – Supprimer par indice
# -----------------------------------------------------------------------------
# Partez de la liste suivante :
lettres = ["a", "b", "c", "d", "e"]

# Supprimez l'élément d'indice 2 avec `del`. Affichez la liste.
# Résultat attendu : ["a", "b", "d", "e"]

del lettres[2]
print(lettres)


# -----------------------------------------------------------------------------
# Exercice 8 – Concaténer deux listes
# -----------------------------------------------------------------------------
# Créez deux listes :
#   debut = [1, 2, 3]
#   fin   = [4, 5, 6]
#
# Créez une troisième liste `tout` qui est la concaténation des deux.
# Affichez `tout`.
# Résultat attendu : [1, 2, 3, 4, 5, 6]


debut = [1, 2, 3]
fin   = [4, 5, 6]

tout = debut + fin
print(tout)



# -----------------------------------------------------------------------------
# Exercice 9 – Tester l'appartenance
# -----------------------------------------------------------------------------
# Partez de la liste suivante :
villes = ["Marseille", "Lyon", "Paris", "Bordeaux"]

# En utilisant `in`, affichez :
#   a) si "Marseille" est dans la liste
#   b) si "Toulouse" est dans la liste
# Résultat attendu : True, False




# -----------------------------------------------------------------------------
# Exercice 10 – Modifier un élément
# -----------------------------------------------------------------------------
# Partez de la liste suivante :
scores = [10, 20, 30, 40]

# Remplacez la valeur d'indice 1 (qui vaut 20) par 25. Affichez la liste.
# Résultat attendu : [10, 25, 30, 40]



# =============================================================================
#  ⭐⭐ INTERMÉDIAIRES (11-20)
# =============================================================================

# -----------------------------------------------------------------------------
# Exercice 11 – Construire une liste par accumulation
# -----------------------------------------------------------------------------
# Créez une liste vide `carres`. À l'aide d'une boucle `for` allant de 1 à 5
# (inclus), ajoutez à `carres` le carré de chaque nombre.
# Résultat attendu : [1, 4, 9, 16, 25]



# -----------------------------------------------------------------------------
# Exercice 12 – Somme des éléments
# -----------------------------------------------------------------------------
# Sans utiliser la fonction sum(), calculez la somme de tous les éléments de
# la liste suivante à l'aide d'une boucle :
nombres = [3, 7, 2, 9, 4]
# Résultat attendu : 25




# -----------------------------------------------------------------------------
# Exercice 13 – Trouver le maximum (sans max())
# -----------------------------------------------------------------------------
# Sans utiliser la fonction max(), trouvez le plus grand élément de :
valeurs = [14, 7, 23, 3, 42, 18]
# Résultat attendu : 42
#
# Indice : partez du premier élément comme "champion provisoire", puis
# parcourez la liste en le remplaçant si vous trouvez mieux.



# -----------------------------------------------------------------------------
# Exercice 14 – Compter les occurrences
# -----------------------------------------------------------------------------
# Comptez combien de fois la valeur 3 apparaît dans la liste suivante,
# sans utiliser .count() :
donnees = [3, 1, 4, 3, 5, 3, 2, 3]
# Résultat attendu : 4



# -----------------------------------------------------------------------------
# Exercice 15 – Inverser une liste (sans .reverse())
# -----------------------------------------------------------------------------
# Créez une nouvelle liste `inversee` qui contient les éléments de la liste
# suivante dans l'ordre inverse, sans utiliser .reverse() ni [::-1] :
original = [10, 20, 30, 40, 50]
# Résultat attendu : [50, 40, 30, 20, 10]
#
# Indice : vous pouvez utiliser les indices négatifs et une boucle.



# -----------------------------------------------------------------------------
# Exercice 16 – Fusionner en alternance
# -----------------------------------------------------------------------------
# Étant donné deux listes de même longueur :
a = [1, 3, 5]
b = [2, 4, 6]

# Créez une liste `melange` qui alterne les éléments des deux listes.
# Résultat attendu : [1, 2, 3, 4, 5, 6]
#
# Indice : utilisez une boucle et les indices.



# -----------------------------------------------------------------------------
# Exercice 17 – Supprimer les doublons (en gardant l'ordre)
# -----------------------------------------------------------------------------
# À partir de la liste suivante :
avec_doublons = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Créez une nouvelle liste `sans_doublons` qui ne contient chaque valeur
# qu'une seule fois, dans l'ordre de première apparition.
# Résultat attendu : [3, 1, 4, 5, 9, 2, 6]
#
# Indice : parcourez la liste et n'ajoutez un élément que s'il n'est pas
# déjà dans votre nouvelle liste (utilisez `in`).



# -----------------------------------------------------------------------------
# Exercice 18 – Liste de listes : accès imbriqué
# -----------------------------------------------------------------------------
# Soit la liste suivante (une "matrice" 3×3) :
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# a) Affichez la valeur 6
# b) Affichez la valeur 7
# c) Remplacez la valeur 5 par 0, puis affichez `matrice`



# -----------------------------------------------------------------------------
# Exercice 19 – Aplatir une liste de listes
# -----------------------------------------------------------------------------
# Transformez la liste suivante :
imbriquee = [[1, 2], [3, 4], [5, 6]]

# En une seule liste "plate" :
# Résultat attendu : [1, 2, 3, 4, 5, 6]
#
# Indice : deux boucles imbriquées, ou une boucle + l'opérateur `+`.



# -----------------------------------------------------------------------------
# Exercice 20 – Rotation à gauche
# -----------------------------------------------------------------------------
# Écrivez un code qui effectue une "rotation à gauche" de la liste :
# le premier élément part à la fin, tous les autres avancent d'un cran.
data = [10, 20, 30, 40, 50]
# Résultat attendu : [20, 30, 40, 50, 10]
#
# Indice : pensez à .pop(), .append(), ou à la concaténation.



# =============================================================================
#  ⭐⭐⭐ AVANCÉS (21-30)
# =============================================================================

# -----------------------------------------------------------------------------
# Exercice 21 – Tri à bulles (Bubble Sort)
# -----------------------------------------------------------------------------
# Implémentez un tri à bulles pour trier la liste suivante dans l'ordre
# croissant. N'utilisez pas .sort() ni sorted().
a_trier = [64, 34, 25, 12, 22, 11, 90]
# Résultat attendu : [11, 12, 22, 25, 34, 64, 90]
#
# Principe : parcourez la liste et échangez deux éléments voisins s'ils sont
# dans le mauvais ordre. Recommencez jusqu'à ce qu'aucun échange ne soit
# nécessaire.



# -----------------------------------------------------------------------------
# Exercice 22 – Recherche binaire
# -----------------------------------------------------------------------------
# Écrivez une fonction `recherche_binaire(liste, cible)` qui cherche `cible`
# dans une liste triée et renvoie son indice (ou -1 si absente).
#
# Testez avec :
triee = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# recherche_binaire(triee, 23)  => 5
# recherche_binaire(triee, 10)  => -1
#
# Principe : comparez la cible au milieu de la liste. Si c'est plus petit,
# cherchez dans la moitié gauche ; sinon dans la moitié droite.



# -----------------------------------------------------------------------------
# Exercice 23 – Transposer une matrice
# -----------------------------------------------------------------------------
# Transposez la matrice suivante (les lignes deviennent des colonnes) :
mat = [
    [1, 2, 3],
    [4, 5, 6]
]
# Résultat attendu :
# [
#     [1, 4],
#     [2, 5],
#     [3, 6]
# ]
#
# Indice : la transposée a autant de lignes que la matrice originale a de
# colonnes.



# -----------------------------------------------------------------------------
# Exercice 24 – Produit scalaire
# -----------------------------------------------------------------------------
# Écrivez une fonction `produit_scalaire(v1, v2)` qui calcule le produit
# scalaire de deux vecteurs (listes de même longueur).
#
# Rappel : produit_scalaire([a, b, c], [x, y, z]) = a*x + b*y + c*z
#
# Testez avec :
# produit_scalaire([1, 2, 3], [4, 5, 6])  => 32  (car 1×4 + 2×5 + 3×6)



# -----------------------------------------------------------------------------
# Exercice 25 – Suite de Fibonacci
# -----------------------------------------------------------------------------
# Générez une liste contenant les 15 premiers termes de la suite de Fibonacci.
# Rappel : chaque terme est la somme des deux précédents.
# F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3, …
#
# Résultat attendu : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]



# -----------------------------------------------------------------------------
# Exercice 26 – Crible d'Ératosthène
# -----------------------------------------------------------------------------
# Implémentez le crible d'Ératosthène pour trouver tous les nombres premiers
# jusqu'à 50.
#
# Principe :
#   1. Créez une liste de booléens de taille 51 (indices 0 à 50), tous à True
#   2. Mettez 0 et 1 à False (pas premiers)
#   3. Pour chaque nombre i à partir de 2 : s'il est encore True, mettez tous
#      ses multiples (2i, 3i, 4i…) à False
#   4. Les indices encore à True sont les nombres premiers
#
# Résultat attendu : [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]



# -----------------------------------------------------------------------------
# Exercice 27 – Sous-liste de somme maximale (Kadane)
# -----------------------------------------------------------------------------
# Trouvez la somme maximale d'une sous-liste contiguë dans :
serie = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Résultat attendu : 6  (la sous-liste [4, -1, 2, 1] a la plus grande somme)
#
# Indice (algorithme de Kadane) : parcourez la liste en maintenant deux
# variables : la somme du "meilleur segment en cours" et la "meilleure somme
# globale".



# -----------------------------------------------------------------------------
# Exercice 28 – Rotation de matrice 90°
# -----------------------------------------------------------------------------
# Faites tourner la matrice suivante de 90° dans le sens horaire :
grille = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Résultat attendu :
# [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]
#
# Indice : une rotation 90° horaire = transposer, puis inverser chaque ligne.



# -----------------------------------------------------------------------------
# Exercice 29 – Pascal's triangle
# -----------------------------------------------------------------------------
# Générez les 7 premières lignes du triangle de Pascal sous forme d'une
# liste de listes.
#
# Résultat attendu :
# [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1]
# ]
#
# Principe : chaque valeur intérieure d'une ligne est la somme des deux
# valeurs au-dessus d'elle dans la ligne précédente.



# -----------------------------------------------------------------------------
# Exercice 30 – Simuler une pile et une file
# -----------------------------------------------------------------------------
# En utilisant uniquement une liste et les méthodes .append() et .pop() :
#
# a) Simulez une PILE (stack, Last In First Out) :
#    - Empilez les valeurs 10, 20, 30
#    - Dépilez deux valeurs et affichez-les
#    Résultat attendu : 30, puis 20
#
# b) Simulez une FILE (queue, First In First Out) :
#    - Enfilez les valeurs 10, 20, 30
#    - Défilez deux valeurs et affichez-les
#    Résultat attendu : 10, puis 20
#
# Indice pour la file : .pop() accepte un argument optionnel…
#   (cherchez ce que fait .pop(0))
