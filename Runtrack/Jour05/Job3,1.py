def panier():
    # Créer une liste de fruits
    fruits = ["pomme", "cerise", "orange",]
    
    # Ajouter "Melon" à la fin de la liste
    fruits.append("Melon")
    
    # Retourner la liste mise à jour
    return fruits

# Appeler la fonction et afficher le résultat
liste_de_fruits = panier()
print(liste_de_fruits)
