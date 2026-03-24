def afficher_triangle(hauteur):
    # Boucle pour chaque niveau de la hauteur
    for i in range(hauteur):
        # Imprimer les espaces pour centrer le triangle
        print(' ' * (hauteur - i - 1), end='')

        # Imprimer le côté gauche du triangle
        print('/', end='')

        # Imprimer les espaces entre les côtés gauche et droit
        if i == 0 :
            # Si c'est le premier niveau, il n'y a pas d'espace entre
            print('')
        else:
            print('_' * (2 * i - 1), end='')
            print('\\')

    # Imprimer la base du triangle
    print('_' * (2 * hauteur - 1))


# Demander à l'utilisateur la hauteur du triangle
try:
    hauteur_input = int(input("Entrez la hauteur du triangle : "))
    if hauteur_input < 1:
        print("Veuillez entrer un nombre entier positif.")
    else:
        afficher_triangle(hauteur_input)
except ValueError:
    print("Veuillez entrer un nombre entier.")
