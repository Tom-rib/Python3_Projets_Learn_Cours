import random

# Fonction pour afficher le plateau
def afficher_plateau(plateau):
    print("\n")
    for row in plateau:
        print(" | ".join(row))
        print("-" * 9)

# Vérifier si un joueur a gagné
def verifier_gagnant(plateau, joueur):
    # Vérification des lignes, colonnes et diagonales
    for i in range(3):
        if all([case == joueur for case in plateau[i]]) or \
           all([plateau[j][i] == joueur for j in range(3)]):
            return True
    if all([plateau[i][i] == joueur for i in range(3)]) or \
       all([plateau[i][2 - i] == joueur for i in range(3)]):
        return True
    return False

# Vérifier si le plateau est plein
def plateau_plein(plateau):
    return all([case != ' ' for row in plateau for case in row])

# Choix d'un mouvement aléatoire pour le bot facile
def mouvement_facile(plateau):
    case_vide = [(i, j) for i in range(3) for j in range(3) if plateau[i][j] == ' ']
    return random.choice(case_vide)

# Vérifier si le bot peut gagner ou bloquer
def mouvement_moyen(plateau, joueur):
    adversaire = 'O' if joueur == 'X' else 'X'
    
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == ' ':
                plateau[i][j] = joueur
                if verifier_gagnant(plateau, joueur):
                    return (i, j)
                plateau[i][j] = adversaire
                if verifier_gagnant(plateau, adversaire):
                    return (i, j)
                plateau[i][j] = ' '
    return mouvement_facile
