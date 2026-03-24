def moyenne(a, b, c):
    moyenne_etudiant = (a + b + c) / 3

    if moyenne_etudiant >= 15:
        print("Très bon élève")
    elif 11 >= moyenne_etudiant <= 15:
        print("Bon élève")
    elif 8 >= moyenne_etudiant <= 11:
        print("Élève moyen")
    elif 0 >= moyenne_etudiant <= 7:
        print("Élève devant faire des efforts")
    else:
        print("L'élève est probablement décédé!") 

# Demande à l'utilisateur de rentrer les notes
a = int(input("Veuillez entrer une première note sur 20: "))
b = int(input("Veuillez entrer une deuxième note sur 20: "))
c = int(input("Veuillez entrer une troisième note sur 20: "))

# Appel de la fonction avec les notes saisies
moyenne(a, b, c)
