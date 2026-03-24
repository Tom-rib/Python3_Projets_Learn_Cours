def victoire(symbole):


    # Scénarios de victoire horizontale, verticale et diagonale
    combinaisons_gagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colonnes
        [0, 4, 8], [2, 4, 6] ]             # diagonales
    print("Vous avez gagner")
    
    if " " not in grille :
        print ("Match nul, vous pouvez reessayer .")
        fin = True 
    grille_jeu()



# La fonction victoire, donne tout les sénarios de victoire ainsi que les différents cas de match nul, en les mettants dans des conditions.

grille = [" "," "," "," "," "," "," "," "," ",]
input("Nous allons jouer au morpion.")
input("Les regles sont les suivantes : ")
input("Le premier a aligner 3 symboles identiques horizontalement, verticalement et en diagonale, GAGNE !!")
input("Appuyer sur entre pour demarrer la partie :")
def grille_jeu() :
    print(" +---+---+---+\n",
        "|",grille[0],"|" ,grille[1],"|" , grille[2],"|\n"
        " +---+---+---+\n",
        "|",grille[3],"|",grille[4],"|",grille[5],"|\n"
        " +---+---+---+\n",
        "|",grille[6],"|",grille[7],"|",grille[8],"|\n"
        " +---+---+---+")
    return grille_jeu
grille_jeu()

# La liste grille nous donne le nombre de case qui sera defini dans notre grille de jeu. 
# La fonction grille_jeu permet de styliser notre liste grille, pour lui implater des lignes represantant les case de notre, plateau de jeux.

symbole = "X"   
# La variable symbole représente le joueur 1 et le joueur 2. Afin de ne pas avoir a doubler 
# les condition de victoire, comme ils ont pour denominateur commun joueur.
fin = False

while fin == False :
    chiffre = int(input("Veuillez choisir une case pour jouer, entre 1 et 9 :")) -1
    if grille[chiffre] != " " :
        chiffre = int(input("Tu t'es trompe choisis une nouvelle case : "))
        grille[chiffre] = symbole
    else :
        grille[chiffre] = symbole
    grille_jeu()

# La boucle while est incrementer d'un int(input), afin de pouvoir demander a chaque tour où 
# on veut placer notre symoble a l'interieur de la grille.
# Le -1 ajouter derriere les parentheses permet de decaler de un la case qu'on veut remplir, 
# dans notre grille de jeu afin que ce soit plus intuitif. 

    victoire(symbole,)
    if symbole == "X" :
        symbole = "O"
    else :
        symbole = "X"

# La variable symbole permet de pouvoir englober nos deux joueur 
# en changeant leur valeur en les placants dans des conditions.

