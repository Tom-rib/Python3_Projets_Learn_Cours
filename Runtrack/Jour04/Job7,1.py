def fonction(langage):
    langage = langage.lower()  # Normalise l'entrée en minuscules
    
    if langage == "javascript":
        print("Tu es un développeur web.")
    elif langage == "python":
        print("Tu es un développeur IA.")
    elif langage == "java":
        print("Tu es un développeur logiciel.")
    elif langage == "reactjs":
        print("Tu es un développeur mobile.")
    else:
        print("Langage non reconnu.")

# Exemple d'utilisation
langue_input = input("Entrez un langage de programmation : ")
fonction(langue_input)
