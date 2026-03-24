def parites(nombres):
    if nombres %2==0 :
        print("Le nombre est pair.")
    else:
        print("Le nombre est impair.")

# Demande à l'utilisateur d'entrer un nombre
nombres_input = int(input("Veuillez entrer un nombre : "))
parites(nombres_input)  # Appel de la fonction avec nombres_input comme argument
