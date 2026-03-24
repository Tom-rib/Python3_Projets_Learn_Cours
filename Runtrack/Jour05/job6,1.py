def manipuler_liste():
    L = [ 1, 2, 3, 4, 5,]
    
    # Afficher l'élément à l'index 1
    print("Élément à l'index 1 :", L[1])
    
    # Modifier l'élément à l'index 2 en ajoutant les éléments à l'index 1 et 3
    L[2] = L[1] + L[3]
    
    # Afficher la liste modifiée
    print("Liste après modification :", L)

# Appel de la fonction
manipuler_liste()
