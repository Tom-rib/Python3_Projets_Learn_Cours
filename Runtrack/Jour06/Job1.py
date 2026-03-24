def draw_rectangle(width, height):
    # Vérifier que la largeur et la hauteur sont des nombres positifs
    if width <= 3  or height <= 6 :
        print("La largeur et la hauteur doivent être des nombres positifs.")
        return

    # Afficher le rectangle
    for h in range(height):
        if h == 0 or h == height - 1:  # Pour la première et la dernière ligne
            print('|' + '-' * (width - 2) + '|')
        else:  # Pour les lignes intermédiaires
            print('|' + ' ' * (width - 2) + '|')

# Exemple d'utilisation
draw_rectangle(30, 10)



