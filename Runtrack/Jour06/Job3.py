def afficher_tapis(n):
    # Boucle pour chaque ligne
    for i in range(n + 1):
        # Initialisation de la ligne
        ligne = ''
        for j in range(n + 1):
            # Vérifie si la position est sur la diagonale
            if i == j:
                ligne += '\\'  # Caractère de la diagonale
            else:
                ligne += '#'  # Caractère du tapis
        print(ligne)

# Demander à l'utilisateur la taille du tapis
try:
    taille_input = int(input("Entrez la taille n du tapis (n >= ) : "))
    if taille_input < 3 :
        print("Veuillez entrer un nombre entier positif ou zéro.")
    else:
        afficher_tapis(taille_input)
except ValueError:
    print("Veuillez entrer un nombre entier.")
